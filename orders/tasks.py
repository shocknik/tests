from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr.{}'.format(order_id)
    message = 'Уважаемый {}, \n\nВаш заказ успешно создан.\ ID Вашего заказа {}'.format(order.first_name, order.id)

    mail_sent = send_mail(subject,
                          message,
                          'monievg@yandex.ru',
                          [order.email])
    return mail_sent
