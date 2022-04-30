from django import forms
from .models import Cats
class CatsForm(forms.ModelForm):
    class Meta:
        model = Cats
        fields = ['name_c', 'age_c', 'breed_c', 'type_of_wool_c']

