from django import forms

from requests.models import SolicitudEmpleo


class SolicitudEmpleoForm(forms.ModelForm):
    class Meta:
        model = SolicitudEmpleo
        fields = ['rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'telefono', 'fecha_nacimiento', 'direccion', 'cv']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_cv(self):
        cv = self.cleaned_data.get('cv')
        if cv:
            # Verifica que el archivo sea un PDF
            if not cv.name.endswith('.pdf'):
                raise forms.ValidationError('Solo se permite subir archivos PDF.')
        return cv