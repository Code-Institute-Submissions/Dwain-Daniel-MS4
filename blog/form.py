from django import forms


class CommentForm(forms.Form):
    """Form for creating comments"""
    comment = forms.CharField(required=True, widget=forms.Textarea)
