from decimal import Decimal
from django.conf import settings
from tests_app.models import Test, TestType


class Cart(object):

    def __init__(self, request):
        self.session = request.session  # инициализация корзины
        cart = self.session.get(settings.CART_SESSION_ID)  # пытаемся получить корзину из текущей сессии
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, test, quantity=1, update_quantity=False):

        test_id = str(test.id)
        if test_id not in self.cart:
            self.cart[test_id] = {'quantity': 0,
                                  'price': str(test.price)}
        if update_quantity:
            self.cart[test_id]['quantity'] = quantity
        else:
            self.cart[test_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        #  Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, test):

        test_id = str(test.id)
        if test_id in self.cart:
            del self.cart[test_id]
            self.save()

    def __iter__(self):  # извлекаем экземпляры испытания, присутствующие в корзине

        """
        Перебор заказов в корзине
        """

        test_ids = self.cart.keys()

        tests = Test.objects.filter(id__in=test_ids)
        for test in tests:
            self.cart[str(test.id)]['test'] = test

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):  # подсчет всех испытаний в корзине
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Удаление сессии из корзины (очистка сеанса)
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
