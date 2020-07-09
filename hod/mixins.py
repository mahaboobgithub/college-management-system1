
from django import forms
import re

class RegistrationMixin:

    gen = (('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'))
    gender = forms.ChoiceField(choices=gen, widget=forms.RadioSelect)

    def check_name(name):
        # name = self.cleaned_data["name"]
        res = re.findall(r"^[A-Z a-z]*$", name)
        if res:
            return name
        else:
            raise forms.ValidationError("Invalid Name")











# class RegistrationMixin:
#     gen = (('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others'))
#
#     gender = forms.ChoiceField(choices=gen, widget=forms.RadioSelect)
#
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     def clean_name(self):
#         name = self.cleaned_data["name"]
#         res = re.findall(r"^[A-Z a-z]*$", name)
#         if res:
#             return name
#         else:
#             raise forms.ValidationError("Invalid Name")