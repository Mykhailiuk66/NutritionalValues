from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.nutritions, name="nutritions"),
    path('nutrition/<int:pk>', views.nutrition, name="nutrition"),
    path('meal', views.meal, name="meal"),
    
    
    path('create-nutrition/', views.create_nutrition, name="create-nutrition"),
    path('update-nutrition/<int:pk>', views.update_nutrition, name="update-nutrition"),
    path('delete-nutrition/<int:pk>', views.delete_nutrition, name="delete-nutrition"),
    
    path('add-nutrition/<int:pk>', views.add_nutrition_to_total, name="add-nutrition"),
    path('remove-nutrition/<int:pk>', views.remove_nutrition_from_total, name="remove-nutrition"),

]
