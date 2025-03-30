from django.db import models

class FormTemplate(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class FormField(models.Model):
    FIELD_TYPES = [
        ('text', 'Text'),
        ('email', 'Email'),
        ('number', 'Number'),
    ]
    
    form_template = models.ForeignKey(FormTemplate, on_delete=models.CASCADE, related_name="fields")
    label = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20, choices=FIELD_TYPES)

    def __str__(self):
        return f"{self.label} ({self.field_type})"

class FormResponse(models.Model):
    form_template = models.ForeignKey(FormTemplate, on_delete=models.CASCADE, related_name="responses")
    response_data = models.JSONField()

    def __str__(self):
        return f"Response to {self.form_template.name}"
