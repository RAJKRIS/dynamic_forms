from django.shortcuts import render, get_object_or_404, redirect
from .models import FormTemplate, FormField, FormResponse
from .forms import FormTemplateForm, FormFieldFormSet

def create_form_template(request):
    if request.method == "POST":
        form = FormTemplateForm(request.POST)
        formset = FormFieldFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            form_template = form.save()
            formset.instance = form_template
            formset.save()
            return redirect('list_forms')
    else:
        form = FormTemplateForm()
        formset = FormFieldFormSet()

    return render(request, 'formsapp/create_form.html', {'form': form, 'formset': formset})

def list_form_templates(request):
    forms = FormTemplate.objects.all()
    return render(request, 'formsapp/list_forms.html', {'forms': forms})

def form_detail(request, form_id):
    form_template = get_object_or_404(FormTemplate, id=form_id)
    fields = form_template.fields.all()
    responses = FormResponse.objects.filter(form_template=form_template)

    if request.method == "POST":
        response_data = {field.name: request.POST.get(field.name, '') for field in fields}
        FormResponse.objects.create(form_template=form_template, response_data=response_data)
        return redirect('form_detail', form_id=form_id)

    return render(request, 'formsapp/form_detail.html', {
        'form_template': form_template,
        'fields': fields,
        'responses': responses
    })
