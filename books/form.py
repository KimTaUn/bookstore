from django import forms
from django.forms import widgets
from django.forms.widgets import Textarea

from books.models import Review


class ReviewForm(forms.ModelForm):

    body = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class': "form-control text-break text-start lh-sm",
                'placeholder': "write your review here...",
                'style': "height: 100px"
            }))
    image = forms.ImageField(
        label='Review Image Upload:',
        required=False)

    class Meta:
        model = Review
        fields = ['body', 'image']
        # add att to form
