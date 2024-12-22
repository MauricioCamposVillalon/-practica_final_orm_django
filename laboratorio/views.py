from django.shortcuts import render, get_object_or_404, redirect
from .models import Laboratorio
from .forms import LaboratorioForm

def laboratorio_lista(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio/lista.html', {'laboratorios': laboratorios})

def laboratorio_formulario(request, id=None):
    if id:
        laboratorio = get_object_or_404(Laboratorio, id=id)
    else:
        laboratorio = None
    form = LaboratorioForm(request.POST or None, instance=laboratorio)
    if form.is_valid():
        form.save()
        return redirect('laboratorio_lista')
    return render(request, 'laboratorio/formulario.html', {'form': form})

def laboratorio_eliminar(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio_lista')
    return render(request, 'laboratorio/eliminar.html', {'laboratorio': laboratorio})

