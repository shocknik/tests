from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Test, TestType
from cart.forms import CartAddProductForm

def f_list(request):
    type_test = None
    type_tests = TestType.objects.all().order_by('pk')
    tests = Test.objects.all()

    return render(request, 'tests_app/tests/list.html',
                  {'tests': tests,
                   'type_test': type_test,
                   'type_tests': type_tests,

                   })


def test_detail(request, pk):
    test = get_object_or_404(Test,
                             pk=pk)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'tests_app/tests/test_detail.html',
                  {'test': test, 'cart_product_form': cart_product_form})
