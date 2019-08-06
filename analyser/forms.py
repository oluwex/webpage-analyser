from django import forms


class SearchForm(forms.Form):
    url = forms.URLField(widget=forms.URLInput(attrs={'placeholder': "Enter URL"}))