from django.contrib import messages
from django.shortcuts import redirect, render

from requests.forms import SolicitudEmpleoForm

def job_request(request):
    if request.method == 'POST':
        form = SolicitudEmpleoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu solicitud de empleo ha sido enviada con éxito!')
            return redirect('job_request')
        else:
            messages.error(request, 'Hubo un error al enviar tu solicitud. Verifica los campos e intenta nuevamente.')
    else:
        form = SolicitudEmpleoForm()

    return render(request, 'job_request.html', {'form': form})
