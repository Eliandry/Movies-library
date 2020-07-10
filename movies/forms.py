from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Rating, RatingStar, Reviews


class ReviewForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Reviews
        fields = ("name", "email", "text", "captcha")
        widgets = {
            "name": forms.TextInput(attrs={'placeholder':'Имя'}),
            "email": forms.EmailInput(attrs={'placeholder':'Email'}),
            "text": forms.Textarea(attrs={'required':True, 'cols':47, 'rows':5,'placeholder':'Содержание'})
        }


class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)
