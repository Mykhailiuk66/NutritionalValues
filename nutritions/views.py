from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import Nutrition
from .forms import NutritionForm
# Create your views here.

def nutritions(request):
    nutritions = Nutrition.objects.all()
    paginator = Paginator(nutritions, 8)

    try:
        page_num = int(request.GET.get('page', 1))
        if page_num > paginator.num_pages: page_num = paginator.num_pages
        if page_num < 1: page_num = 1
    except:
        page_num = 1


    queryset = paginator.get_page(page_num)
    page_range = paginator.get_elided_page_range(page_num, on_each_side=2, on_ends=1)

    context = {
        'queryset': queryset,
        'page_range': page_range,
    }
    return render(request, 'nutritions/nutritions.html', context=context)


def create_nutrition(request):

    if request.method == 'POST':
        form = NutritionForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('nutritions')
        else:
            print("Form is not valid")
    else:
        form = NutritionForm()


    context = {
        'form': form
    }
    return render(request, 'form_template.html', context=context)


def update_nutrition(request, pk):
    nutrition = get_object_or_404(Nutrition, id=pk)

    if request.method == 'POST':
        form = NutritionForm(request.POST, request.FILES, instance=nutrition)

        if form.is_valid():
            form.save()

            return redirect('nutritions')
        else:
            print("Form is not valid")
    else:
        form = NutritionForm(instance=nutrition)


    context = {
        'form': form
    }
    return render(request, 'form_template.html', context=context)


def delete_nutrition(request, pk):
    nutrition = get_object_or_404(Nutrition, id=pk)

    if request.method == 'POST':
        nutrition.delete()
        return redirect('nutritions')

    context = {
        'object': nutrition
    }
    return render(request, 'delete_template.html', context=context)