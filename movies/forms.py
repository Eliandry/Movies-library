from django import forms
from .models import Rating,RatingStar

class RatingForm(forms.ModelForm):
    star=forms.ModelChoiceField(
        queryset=RatingStar.objects.all(),widget=forms.RadioSelect(),empty_label=None
    )
    class Meta:
        model=Rating
        fields=("star",)