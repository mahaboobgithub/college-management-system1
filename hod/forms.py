
from django import forms
from hod.models import HodModel
import re
from hod.mixins import RegistrationMixin




class HODForm(RegistrationMixin,forms.ModelForm):

    name = forms.CharField(validators=[RegistrationMixin.check_name])
    gender = RegistrationMixin.gender
    class Meta:
        model = HodModel
        fields = "__all__"


