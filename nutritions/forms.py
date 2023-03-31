from django.forms import ModelForm
from .models import Nutrition


class NutritionForm(ModelForm):
    class Meta:
        model = Nutrition
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'w-full rounded-lg border-gray-200 p-4 text-sm shadow-sm', 'placeholder': field.label})


