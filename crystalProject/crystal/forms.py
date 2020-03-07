from django.forms import ModelForm
from .models import incidente


class incidenteForm(ModelForm):
    class Meta:
        model = incidente
        fields = ['document', 'date', 'user', 'hour', 'zone', 'address', 'brand', 'model', 'registrationNumber']