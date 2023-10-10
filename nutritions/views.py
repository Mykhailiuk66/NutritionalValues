from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib import messages

from .models import Nutrition
from .forms import NutritionForm
from .utils import is_ajax
# Create your views here.

def nutritions(request):
    search = request.GET.get('search', '')

    nutritions = Nutrition.objects.filter(
        Q(name__icontains=search) | Q(description__icontains=search)
    )

    paginator = Paginator(nutritions, 8)
    try:
        page_num = int(request.GET.get('page', 1))
        if page_num > paginator.num_pages: page_num = paginator.num_pages
        if page_num < 1: page_num = 1
    except:
        page_num = 1

    queryset = paginator.get_page(page_num)
    page_range = paginator.get_elided_page_range(page_num, on_each_side=1, on_ends=1)

    context = {
        'queryset': queryset,
        'page_range': page_range,
        'search': search,
    }
    return render(request, 'nutritions/nutritions.html', context=context)


def nutrition(request, pk):
    nutrition = get_object_or_404(Nutrition, id=pk)


    context = {
        'nutrition': nutrition,
    }
    return render(request, 'nutritions/single-nutrition.html', context=context)


def create_nutrition(request):

    if request.method == 'POST':
        form = NutritionForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('nutritions')
        else:
            messages.error(request, "Something went wrong")
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
            print("Something went wrong")
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


def add_nutrition_to_total(request, pk):
    if request.method == "GET":
        if not isinstance(request.session.get('meal'), list):
            request.session['meal'] = list()

        request.session['meal'].append(pk)
        request.session.modified = True

        

    return redirect('nutritions')


def remove_nutrition_from_total(request, pk):
    if request.method == "GET":
        if not isinstance(request.session.get('meal'), list):
            request.session['meal'] = list()

        if pk in request.session['meal']: 
            request.session['meal'].remove(pk)
            request.session.modified = True
        

    return redirect('meal')


@login_required(login_url='/account/login')
def meal(request):
    nutritions = [Nutrition.objects.get(id=nutrition_id) for nutrition_id in request.session.get('meal', []) ]

    field_totals = {
        'calories': 0,
        'total_fat': 0,
        'saturated_fat': 0,
        'sodium': 0,
        'total_carbohydrate': 0,
        'dietary_fiber': 0,
        'sugar': 0,
        'protein': 0,
        'vitamin_D': 0,
        'calcium': 0,
        'iron': 0,
        'potassium': 0,
    }

    for nutrition in nutritions:
        for field in field_totals.keys():
            field_totals[field] += getattr(nutrition, field) or 0


    context = {
        'nutritions': nutritions,
        'field_totals': field_totals,
    }
    return render(request, 'nutritions/meal.html', context=context)