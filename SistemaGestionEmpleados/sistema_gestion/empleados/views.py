from django.shortcuts import render, redirect, get_object_or_404

from empleados.models import Empleado, Departamento


# Create your views here.
def listar_empleados(request):
    busqueda = request.GET.get('buscar','')
    departamento_id = request.GET.get('departamento','')

    empleados = Empleado.objects.all()
    departamentos = Departamento.objects.all()

    if busqueda:
        empleados = empleados.filter(nombre__icontains=busqueda)

    if departamento_id:
        empleados = empleados.filter(departamento_id=departamento_id)

    context = {
        'empleados': empleados,
        'departamentos': departamentos,
        'busqueda': busqueda,
        'departamento_id': departamento_id
    }

    return render(request, 'empleados/listar.html', context)

def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        departamento_id = request.POST.get('departamento', None)
        departamento_id = int(departamento_id) if departamento_id else None

        departamento = Departamento.objects.get(id=departamento_id) if departamento_id else None

        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            departamento=departamento
        )
        return redirect('listar_empleados')
    departamentos = Departamento.objects.all()
    return render(request, 'empleados/agregar.html', {'departamentos':departamentos})

def editar_empleado(request,id):
    empleado = get_object_or_404(Empleado, id=id)
    departamentos = Departamento.objects.all()

    if request.method =='POST':
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.email = request.POST['email']
        departamento_id = request.POST.get('departamento',None)
        departamento_id = int(departamento_id) if departamento_id else None
        empleado.departamento = Departamento.objects.get(id=departamento_id) if departamento_id else None

        empleado.save()
        return redirect('listar_empleados')
    return render(request,'empleados/editar.html', {'empleado': empleado,'departamentos':departamentos})


def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado,id=id)
    empleado.delete()
    return redirect('listar_empleados')