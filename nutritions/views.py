from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Nutrition
# Create your views here.

def nutritions(request):
    page_num = request.GET.get('page', 1)

    nutritions = Nutrition.objects.all()
    paginator = Paginator(nutritions, 5)


    queryset = paginator.get_page(page_num)


    context = {
        'queryset': queryset,
    }
    return render(request, 'nutritions/nutritions.html', context=context)