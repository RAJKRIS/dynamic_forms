from django import forms
from django.forms import inlineformset_factory
from .models import FormTemplate, FormField

class FormTemplateForm(forms.ModelForm):
    class Meta:
        model = FormTemplate
        fields = ['name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class FormFieldForm(forms.ModelForm):
    class Meta:
        model = FormField
        fields = ['label', 'name', 'field_type']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'DELETE' in self.fields:
            self.fields['DELETE'].widget = forms.HiddenInput()  # Hide delete checkbox
        
        for field_name, field in self.fields.items():
            if field_name == "field_type":
                field.widget.attrs.update({'class': 'form-select'})  # Dropdown
            else:
                field.widget.attrs.update({'class': 'form-control'})



# Allow unlimited fields using `extra=3` (users can add more)
FormFieldFormSet = inlineformset_factory(
    FormTemplate, 
    FormField, 
    form=FormFieldForm, 
    extra=1,   # Start with 3 empty field forms
    can_delete=True  # Allow deleting fields
)