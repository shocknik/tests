from django.shortcuts import render, get_object_or_404
from .models import Cable, Category


def cab_list(request):
    category = None
    categories = Category.objects.all().order_by('pk')
    cables = Cable.objects.all()
    mark = Cable.objects.filter(category=category)

    return render(request, 'cables/cables_t/list.html',
                  {'cables': cables,
                   'category': category,
                   'categories': categories,
                   'mark': mark,

                   })
