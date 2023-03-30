from django.db import models

# Create your models here.

class Nutrition(models.Model):    
    name = models.CharField(max_length=500, blank=False)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='nutritions/', default='nutritions/default.png', blank=True)
    calories = models.FloatField(blank=True, null=True)
    total_fat = models.FloatField(blank=True, null=True)
    saturated_fat = models.FloatField(blank=True, null=True)
    sodium = models.FloatField(blank=True, null=True) # mg
    total_carbohydrate = models.FloatField(blank=True, null=True)
    dietary_fiber = models.FloatField(blank=True, null=True)
    sugar = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    vitamin_D = models.FloatField(blank=True, null=True) # mcg
    calcium = models.FloatField(blank=True, null=True) # mg
    iron = models.FloatField(blank=True, null=True) # mg
    potassium = models.FloatField(blank=True, null=True) # mg
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name
    

 