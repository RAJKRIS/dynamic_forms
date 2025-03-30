from django.urls import path
from .views import create_form_template, list_form_templates, form_detail

urlpatterns = [
    path('create/', create_form_template, name='create_form'),
    path('', list_form_templates, name='list_forms'),
    path('<int:form_id>/', form_detail, name='form_detail'),
]
