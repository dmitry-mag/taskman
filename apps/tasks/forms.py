from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Task


class TaskForm(ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Добавить', css_class='btn-primary'))
    class Meta:
        model = Task
        fields = ['name', 'signed', 'status']


class TaskUpdateForm(ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Сохранить изменения', css_class='btn-primary'))
    class Meta:
        model = Task
        fields = '__all__'
