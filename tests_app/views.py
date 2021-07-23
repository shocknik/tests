from django.http import HttpResponse
from django.shortcuts import render
from .models import Test, TestType

def test_list(request):
    test_type = TestType.objects.all()
    tests = Test.objects.all()

    return render(request, 'tests_app/tests/list.html',
                  {'tests': tests,})


# Create your views here.
