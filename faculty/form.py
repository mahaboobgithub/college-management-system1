
from django import forms
from faculty.models import FacultyModel
from hod.mixins import RegistrationMixin

class FacultyForm(RegistrationMixin,forms.ModelForm):

    gender = RegistrationMixin.gender
    name = forms.CharField(validators=[RegistrationMixin.check_name])

    class Meta:
        model = FacultyModel
        fields = "__all__"