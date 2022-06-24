from django.forms.fields import NullBooleanField
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from .forms import *
import logging


def nuevoPaciente(request):
    if request.method == "POST":
        frmPaciente = FrmPaciente(request.POST or None, request.FILES or None)
        if frmPaciente.is_valid():
            frmPaciente.save()
            return redirect('pacientes:listaPaciente')
    else:
        frmPaciente = FrmPaciente()
        context = {
            'frmPaciente': frmPaciente,
            # 'tipo_titulo' : 'Nuevo Producto!',
            # 'tipo_boton' : 'Guardar Producto',
        }
        return render(request, 'pacientes/NewPaciente.html', context)


def perfilPaciente(request, item_id):
    try:
        # itemPaciente = get_object_or_404(Paciente, pk=item_id)
        itemPaciente = Paciente.objects.get(pk=item_id)
        formEditarPaciente = FrmPaciente(request.POST or None, instance=itemPaciente)

        if formEditarPaciente.is_valid():
            tempform = formEditarPaciente.save(commit=False)  # Don't save it yet
            tempform.save()  # Now save it
            return redirect('pacientes:perfilPaciente', item_id=item_id)
        context = {
            'itemPaciente': itemPaciente,
            # 'header' : 'Perfil de Usuario: ',
            'formEditarPaciente': formEditarPaciente
        }
    except Paciente.DoesNotExist:
        raise Http404("Paciente no existe")
    return render(request, 'pacientes/Perfilpaciente.html', context)


def listaPaciente(request):
    allPacientes = Paciente.objects.all()

    context = {
        'allPacientes': allPacientes,
    }
    return render(request, 'pacientes/ListPacientes.html', context)


# Especialidades

def nuevoOdontogeneral(request, item_id):
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    frmOdGeneral = FrmOdontoGeneral(request.POST or None)

    if frmOdGeneral.is_valid():
        tempform = frmOdGeneral.save(commit=False)
        tempform.fkPaciente = itemPaciente
        tempform.save()
        return redirect('pacientes:listaOdontogeneral', item_id=item_id)
    context = {
        'frmOdGeneral': frmOdGeneral,
        'itemPaciente': itemPaciente
    }
    return render(request, 'pacientes/NewOdontGeneral.html', context)


def listaOdontogeneral(request, item_id):
    itemsOdontoGeneral = OdontoGeneral.objects.filter(fkPaciente=item_id)
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    context = {
        'itemsOdontoGeneral': itemsOdontoGeneral,
        'itemPaciente': itemPaciente,
    }
    return render(request, 'pacientes/ListOdontGeneral.html', context)


def nuevoOdontopediatria(request, item_id):
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    frmOdPediatria = FrmOdonPediatria(request.POST or None)

    if frmOdPediatria.is_valid():
        tempform = frmOdPediatria.save(commit=False)
        tempform.fkPaciente = itemPaciente
        tempform.save()
        return redirect('pacientes:listaOdontopedriatria', item_id=item_id)
    context = {
        'frmOdPediatria': frmOdPediatria,
        'itemPaciente': itemPaciente,
    }
    return render(request, 'pacientes/NewOdontopedriatria.html', context)


def listaOdontopediatria(request, item_id):
    itemsOdontoPediatria = OdonPediatria.objects.filter(fkPaciente=item_id)
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    context = {
        'itemsOdontoPediatria': itemsOdontoPediatria,
        'itemPaciente': itemPaciente
    }
    return render(request, 'pacientes/ListOdontopedriatria.html', context)


def nuevoEndodoncia(request, item_id):
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    frmEndodoncia = FrmEndodoncia(request.POST or None)

    if frmEndodoncia.is_valid():
        tempform = frmEndodoncia.save(commit=False)
        tempform.fkPaciente = itemPaciente
        tempform.save()
        return redirect('pacientes:listaEndodoncia', item_id=item_id)
    context = {
        'frmEndodoncia': frmEndodoncia,
        'itemPaciente': itemPaciente,
    }
    return render(request, 'pacientes/NewEndodoncia.html', context)


def listaEndodoncia(request, item_id):
    itemsOdontoPediatria = OdonPediatria.objects.filter(fkPaciente=item_id)
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    context = {
        'itemsOdontoPediatria': itemsOdontoPediatria,
        'itemPaciente': itemPaciente
    }
    return render(request, 'pacientes/ListEndodoncia.html', context)


def nuevoOrtodoncia(request, item_id):
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    frmOrtodoncia = FrmOrtodoncia(request.POST or None)

    if frmOrtodoncia.is_valid():
        tempform = frmOrtodoncia.save(commit=False)
        tempform.fkPaciente = itemPaciente
        tempform.save()
        return redirect('pacientes:listaOrtodoncia', item_id=item_id)
    context = {
        'frmOrtodoncia': frmOrtodoncia,
        'itemPaciente': itemPaciente
    }
    return render(request, 'pacientes/NewOrtodoncia.html', context)


def listaOrtodoncia(request, item_id):
    itemsOrtodoncia = Ortodoncia.objects.filter(fkPaciente=item_id)
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    context = {
        'itemsOrtodoncia': itemsOrtodoncia,
        'itemPaciente': itemPaciente
    }
    return render(request, 'pacientes/ListOrtodoncia.html', context)


def nuevoRehaboral(request, item_id):
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    frmRehabilitacionOral = FrmRehabilitacionOral(request.POST or None)

    if frmRehabilitacionOral.is_valid():
        tempform = frmRehabilitacionOral.save(commit=False)
        tempform.fkPaciente = itemPaciente
        tempform.save()
        return redirect('pacientes:listaRehaboral', item_id=item_id)
    context = {
        'frmRehabilitacionOral': frmRehabilitacionOral,
        'itemPaciente': itemPaciente
    }
    return render(request, 'pacientes/NewRehabOral.html', context)


def listaRehaboral(request, item_id):
    itemsRehaboral = RehabilitacionOral.objects.filter(fkPaciente=item_id)
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    context = {
        'itemsRehaboral': itemsRehaboral,
        'itemPaciente': itemPaciente
    }
    return render(request, 'pacientes/ListRehabOral.html', context)


# PlanDeTratamiento
def planTratamiento(request, item_id):
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    frmPlan = FrmPlanTratamiento(request.POST or None)

    if frmPlan.is_valid():
        tempform = frmPlan.save(commit=False)
        tempform.fkPaciente = itemPaciente
        tempform.save()

    context = {
        'itemPaciente': itemPaciente,
        'frmPlan': frmPlan
    }
    return render(request, 'pacientes/NewPlanTrat.html', context)


# pagos
def nuevoPago(request, item_id):
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    frmPago = FrmPagoPaciente(request.POST or None)

    if frmPago.is_valid():
        tempform = frmPago.save(commit=False)
        tempform.fkPaciente = itemPaciente
        tempform.save()
        return redirect('pacientes:listaPagos', item_id=item_id)
    context = {
        'frmPago': frmPago,
        'itemPaciente': itemPaciente
    }
    return render(request, 'pacientes/NewPagos.html', context)


def listaPagos(request, item_id):
    itemsPagos = PagoPaciente.objects.filter(fkPaciente=item_id)
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    context = {
        'itemsPagos': itemsPagos,
        'itemPaciente': itemPaciente
    }
    return render(request, 'pacientes/ListPagos.html', context)


# recetas

def listaRecetas(request, item_id):
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    frmReceta = FrmReceta(request.POST or None)

    if frmReceta.is_valid():
        tempform = frmReceta.save(commit=False)
        tempform.fkPaciente = itemPaciente
        tempform.save()
        return redirect('pacientes:listaRecetas', item_id=item_id)
    context = {
        'itemPaciente': itemPaciente,
        'frmReceta': frmReceta
    }
    return render(request, 'pacientes/ListReceta.html', context)


# imagenes
def imagenes(request, item_id):
    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    frmImg = FrmImgRayosx(request.POST or None)

    if frmImg.is_valid():
        tempform = frmImg.save(commit=False)
        tempform.fkPaciente = itemPaciente
        tempform.save()
        return redirect('pacientes:imagenes', item_id=item_id)
    context = {
        'itemPaciente': itemPaciente,
        'frmImg': frmImg
    }
    return render(request, 'pacientes/imagenes.html', context)


# odontograma
def odontograma(request, item_id):
    # logger = logging.getLogger('app_api')
    # logger.error('Something went wrong!')
    #
    # logger.info('asdasdasdasdasd')

    itemPaciente = get_object_or_404(Paciente, pk=item_id)
    if Odontograma.objects.filter(fkPaciente=itemPaciente).count() <= 0:
        odontograma = Odontograma.objects.create(fkPaciente=itemPaciente)
    else:
        odontograma = Odontograma.objects.filter(fkPaciente=itemPaciente).first()

    listaEstado = [
        'caries', 'coronatemp',
        'dentausente',
        'dentsuper', 'diastema',
        'edentotal', 'erupcion',
        'fractura', 'muñon',
        'ortoremov1', 'ortoremovbuen',
        'ortoremovmal', 'protesisfijabuen',
        'protesisfijamal', 'protremovbuen',
        'protremovmal', 'resbuenestado',
        'resmalestado', 'restemp',
        'sellantebueno',
        'sellantemalo'
    ]

    listaForms = (
        T12Form(request.POST or None, instance=odontograma), T11Form(request.POST or None, instance=odontograma),
        T13Form(request.POST or None, instance=odontograma), T14Form(request.POST or None, instance=odontograma),
        T15Form(request.POST or None, instance=odontograma), T16Form(request.POST or None, instance=odontograma),
        T17Form(request.POST or None, instance=odontograma), T18Form(request.POST or None, instance=odontograma),
        T21Form(request.POST or None, instance=odontograma), T22Form(request.POST or None, instance=odontograma),
        T23Form(request.POST or None, instance=odontograma), T24Form(request.POST or None, instance=odontograma),
        T25Form(request.POST or None, instance=odontograma), T26Form(request.POST or None, instance=odontograma),
        T27Form(request.POST or None, instance=odontograma), T28Form(request.POST or None, instance=odontograma),
        T31Form(request.POST or None, instance=odontograma), T32Form(request.POST or None, instance=odontograma),
        T33Form(request.POST or None, instance=odontograma), T34Form(request.POST or None, instance=odontograma),
        T35Form(request.POST or None, instance=odontograma), T36Form(request.POST or None, instance=odontograma),
        T37Form(request.POST or None, instance=odontograma), T38Form(request.POST or None, instance=odontograma),
        T41Form(request.POST or None, instance=odontograma), T42Form(request.POST or None, instance=odontograma),
        T43Form(request.POST or None, instance=odontograma), T44Form(request.POST or None, instance=odontograma),
        T45Form(request.POST or None, instance=odontograma), T46Form(request.POST or None, instance=odontograma),
        T47Form(request.POST or None, instance=odontograma), T48Form(request.POST or None, instance=odontograma),
        T51Form(request.POST or None, instance=odontograma), T52Form(request.POST or None, instance=odontograma),
        T53Form(request.POST or None, instance=odontograma), T54Form(request.POST or None, instance=odontograma),
        T55Form(request.POST or None, instance=odontograma), T61Form(request.POST or None, instance=odontograma),
        T62Form(request.POST or None, instance=odontograma), T63Form(request.POST or None, instance=odontograma),
        T64Form(request.POST or None, instance=odontograma), T65Form(request.POST or None, instance=odontograma),
        T71Form(request.POST or None, instance=odontograma), T72Form(request.POST or None, instance=odontograma),
        T73Form(request.POST or None, instance=odontograma), T74Form(request.POST or None, instance=odontograma),
        T75Form(request.POST or None, instance=odontograma), T81Form(request.POST or None, instance=odontograma),
        T82Form(request.POST or None, instance=odontograma), T83Form(request.POST or None, instance=odontograma),
        T84Form(request.POST or None, instance=odontograma), T85Form(request.POST or None, instance=odontograma),
    )

    for item in listaForms:
        form = item
        # if request.method == 'POST':
        if form.is_valid() and form.is_bound:
            form.save()

    context = {
        'itemPaciente': itemPaciente,
        'odontograma': odontograma,
        'listaEstado': listaEstado,
        # 'tooth_form' : tooth_form,
        'listaForms': listaForms
    }
    return render(request, 'pacientes/odontograma.html', context)


def actualizaOdontograma(request, item_id):
    paciente = Paciente.objects.get(pk=item_id)
    odontograma = Odontograma.objects.get(fkPaciente=paciente.id)
    if request.method == 'POST':
        return redirect('pacientes:odontograma', item_id=item_id)

    return render(request, 'odontogram.html', {
        'odontograma': odontograma,
        'item_pk': item_id,
    }
                  )
