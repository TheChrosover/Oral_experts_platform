# Generated by Django 3.2.8 on 2021-10-15 05:15

from django.db import models,migrations

def OnCargarEndoCaracteristicas(apps, schema_editor):
    tbCaracteristica = apps.get_model("PacientesApp", "EndoCaracteristica")

    listaEndoCaracteristica = [
        tbCaracteristica(cNombre = "Inflacion Intraoral"),
        tbCaracteristica(cNombre = "Inflacion Extraoral"),
        tbCaracteristica(cNombre = "Fistula"),
        tbCaracteristica(cNombre = "Movilidad"),
        tbCaracteristica(cNombre = "Caries Profunda"),
        tbCaracteristica(cNombre = "Signos de Trauma"),
        tbCaracteristica(cNombre = "Cemento Temporal"),
        tbCaracteristica(cNombre = "Cambio de color coronal")
    ]
    for row in listaEndoCaracteristica:
        row.save()

def OnCargarEndoAnatoRadicular(apps, schema_editor):
    tbEndoAnatoRad = apps.get_model("PacientesApp", "EndoAnatoRadicular")

    listaAnatoRad = [
        tbEndoAnatoRad(cNombre = "Normal"),
        tbEndoAnatoRad(cNombre = "Dilacerada"),
        tbEndoAnatoRad(cNombre = "Curva"),
        tbEndoAnatoRad(cNombre = "Formación Incompleta"),
        tbEndoAnatoRad(cNombre = "Perforación Cameral"),
        tbEndoAnatoRad(cNombre = "Perforación Rad"),
        tbEndoAnatoRad(cNombre = "Espacio del Ligamento Periodontal Ensanchado"),
        tbEndoAnatoRad(cNombre = "Rarefacción Apical"),
        tbEndoAnatoRad(cNombre = "Cuerpo Extrano Intrarrad"),
        tbEndoAnatoRad(cNombre = "Fractura Rad"),
        tbEndoAnatoRad(cNombre = "Reabsorción INT"),
        tbEndoAnatoRad(cNombre = "Reabsorcion EXT"),
        tbEndoAnatoRad(cNombre = "Disminución del Lumen del Conducto"),
        tbEndoAnatoRad(cNombre = "Obturación Endodontica Parcial"),
        tbEndoAnatoRad(cNombre = "Sobreobturacion")
    ]

    for row in listaAnatoRad:
        row.save()

def OnCargarOdonPediatriaPlan(apps, schema_editor):
    tbPlan = apps.get_model("PacientesApp", "OdonPediatriaPlan")

    listaPlan = [
        tbPlan(cNombre = "Prevencion"),
        tbPlan(cNombre = "Cirugia Oral"),
        tbPlan(cNombre = "Operatoria"),
        tbPlan(cNombre = "Ortodoncia"),
        tbPlan(cNombre = "Ortopediamaxilar"),
        tbPlan(cNombre = "Endodoncia"),
        tbPlan(cNombre = "Periodoncia"),
        tbPlan(cNombre = "Restauracion"),
        tbPlan(cNombre = "Mantenimiento"),
        tbPlan(cNombre = "Odontologia Integral")
    ]
    
    for row in listaPlan:
        row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('PacientesApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(OnCargarEndoCaracteristicas),
        migrations.RunPython(OnCargarEndoAnatoRadicular),
        migrations.RunPython(OnCargarOdonPediatriaPlan),
    ]
