from django import forms


class ContactUs(forms.Form):
    email = forms.EmailField(required=True)
    phone_no = forms.IntegerField()
    query = forms.CharField(max_length=10, required=True, widget=forms.Textarea)