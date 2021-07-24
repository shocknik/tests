from django.http import HttpResponse
from django.shortcuts import render
from .models import Test, TestType

def test_list(request):
    type_test = TestType.objects.all().order_by('pk')
    tests = Test.objects.all()

    return render(request, 'tests_app/tests/list.html',
                  {'tests': tests,
                   'type_test': type_test,

                   })


# Create your views here.
