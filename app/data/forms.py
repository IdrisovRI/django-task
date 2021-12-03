from django import forms
from data.models import Data


class DataForm(forms.ModelForm):
    a = forms.IntegerField()
    b = forms.IntegerField()

    class Meta:
        model = Data
        fields = ('a', 'b')
