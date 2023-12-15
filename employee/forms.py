from django import forms
from .models import Employee, Vacation


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ["birth_date"]


class VacationForm(forms.ModelForm):
    class Meta:
        model = Vacation
        exclude = ["start_date", "end_date", "employee"]
