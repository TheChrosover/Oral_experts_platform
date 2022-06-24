from django import forms
# from django.forms import ModelForm, widgets
# from django.utils.translation import gettext_lazy as _
from .models import *


class FrmPaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        exclude = ['dPacFechaRegistro', 'dUltFecActualizacion', 'bEstado']
        # labels = {
        #     'cPacNombres': _('Nombres y apellidos'),
        #     'nPacDni': _('DNI'),
        #     'cPacEstadoCivil': _('Estado civil'),
        #     'cPacSexo': _('Sexo'),
        #     'dPacFecNacimiento': _('Fecha de nacimiento'),
        #     'cPacCiudadNacimiento': _('Ciudad de nacimiento'),
        #     'cPacDireccion': _('Dirección'),
        #     'nPacCodPostal': _('Código postal'),
        #     'nPacCelTlf': _('Telefono/Celular'),
        #     'cPacEmail': _('Correo'),
        #     'cPacOcupacion': _('Ocupación'),
        #     'cPacAlergia': _('Alergia'),
        #     'cNombresApoderado': _('Apoderado'),
        #     'iPacImg': _('Imagen'),
        #     'nTelfApoderado': _('Tel/Cel de apoderado'),
        # }
        widgets = {
            'cPacNombres': forms.TextInput(attrs={'class': 'form-control'}),
            'nPacDni': forms.TextInput(attrs={'class': 'form-control'}),
            'dPacFechaRegistro': forms.TextInput(attrs={'class': 'form-control'}),
            'cPacEstadoCivil': forms.Select(attrs={'class': 'form-control'}),
            'cPacSexo': forms.Select(attrs={'class': 'form-control'}),
            'cPacCiudadNacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'cPacDireccion': forms.TextInput(attrs={'class': 'form-control'}),
            'nPacCodPostal': forms.TextInput(attrs={'class': 'form-control'}),
            'nPacCelTlf': forms.TextInput(attrs={'class': 'form-control'}),
            'cPacEmail': forms.EmailInput(attrs={'class': 'form-control'}),
            'cPacOcupacion': forms.TextInput(attrs={'class': 'form-control'}),
            'cPacAlergia': forms.TextInput(attrs={'class': 'form-control'}),
            'cNombresApoderado': forms.TextInput(attrs={'class': 'form-control'}),
            'iPacImg': forms.FileInput(
                attrs={'class': 'custom-file-input', 'id': 'inputGroupFile01', 'onchange': 'readURL(this);'}),
            'nTelfApoderado': forms.TextInput(attrs={'class': 'form-control'}),

            'dPacFecNacimiento': forms.TextInput(attrs={
                'class': 'form-control flatpickr flatpickr-input',
                'id': 'basicFlatpickr',
                'type': 'text',
                'placeholder': '01/01/2021',
            }),
        }
        # help_texts = {
        #     'cPacNombres': _('EsteEsUnHelpText'),
        #     'nPacDni': _('EsteEsUnHelpText'),
        #     'cPacEstadoCivil': _('EsteEsUnHelpText'),
        #     'cPacSexo': _('EsteEsUnHelpText'),
        #     'dPacFecNacimiento': _('EsteEsUnHelpText'),
        #     'cPacCiudadNacimiento': _('EsteEsUnHelpText'),
        #     'cPacDireccion': _('EsteEsUnHelpText'),
        #     'nPacCodPostal': _('EsteEsUnHelpText'),
        #     'nPacCelTlf': _('EsteEsUnHelpText'),
        #     'cPacEmail': _('EsteEsUnHelpText'),
        #     'cPacOcupacion': _('EsteEsUnHelpText'),
        #     'cPacAlergia': _('EsteEsUnHelpText'),
        #     'cNombresApoderado': _('EsteEsUnHelpText'),
        #     'iPacImg': _('EsteEsUnHelpText'),
        #     'nTelfApoderado': _('EsteEsUnHelpText'),
        # }


class FrmTratamiento(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = '__all__'
        widgets = {
            'cTratNombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'mTratPrecio': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }),
            'cTratDesc': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmPlanTratamiento(forms.ModelForm):
    class Meta:
        model = PlanTratamiento
        fields = '__all__'
        exclude = ['fkPaciente']
        widgets = {
            'dPlnFechaTrat': forms.DateTimeInput(
                attrs={
                    'class': 'form-control'
                }),
            'fkTratamiento': forms.Select(
                attrs={
                    'class': 'form-control'
                }),
            'cPlnNomTrat': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cPlnObservacion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmPagoPaciente(forms.ModelForm):
    class Meta:
        model = PagoPaciente
        fields = '__all__'
        exclude = ['fkPaciente']
        widgets = {
            'dPagoFecha': forms.DateTimeInput(
                attrs={
                    'class': 'form-control'
                }),
            'fkTratamiento': forms.Select(
                attrs={
                    'class': 'form-control'
                }),
            'mPagoMontoTotal': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }),
            'cModoPago': forms.Select(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmImgRayosx(forms.ModelForm):
    class Meta:
        model = ImgRayosx
        fields = '__all__'
        exclude = ['fkPaciente']
        widgets = {
            'iRayosxImg': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }),
            'tDescImg': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'dFechaImg': forms.DateTimeInput(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmReceta(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'
        exclude = ['fkPaciente']
        widgets = {
            'dRctaFecha': forms.DateTimeInput(
                attrs={
                    'class': 'form-control'
                }),
            'fkTratamiento': forms.Select(
                attrs={
                    'class': 'form-control'
                }),
            'tDescripcion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmOdontoGeneral(forms.ModelForm):
    class Meta:
        model = OdontoGeneral
        fields = '__all__'
        exclude = ['fkPaciente']
        widgets = {
            'dOdontGeneralFecha': forms.DateTimeInput(
                attrs={
                    'class': 'form-control'
                }),
            'tMotivoConsulta': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'cEnfermedadActual': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tMedicaActual': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'cTiempoEnfermedad': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cSignosSintomas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tRelatoCrono': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tAnteceFamiliar': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tAntecePersonal': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tExamenGeneral': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tExamenOdontEstoma': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tDiagPresuntivo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tDiagDefinitivo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tPlanTratamiento': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tRecomendacion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tAlta': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmEndoCaracteristica(forms.ModelForm):
    class Meta:
        model = EndoCaracteristica
        fields = '__all__'
        exclude = ['bCaractEstado']
        widgets = {
            'cCaractNombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmEndoAnatoRadicular(forms.ModelForm):
    class Meta:
        model = EndoAnatoRadicular
        fields = '__all__'
        exclude = ['bEstado']
        widgets = {
            'cAnatRadNombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmEndodoncia(forms.ModelForm):
    class Meta:
        model = Endodoncia
        fields = '__all__'
        exclude = ['fkPaciente']
        widgets = {
            'dEndoFecha': forms.DateTimeInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEndoDolor': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEndoFrio': forms.Select(
                attrs={
                    'class': 'form-control'
                }),
            'cEndoCalor': forms.Select(
                attrs={
                    'class': 'form-control'
                }),
            'cAnatoRadOtros': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'dEndoEvolFecha': forms.DateTimeInput(
                attrs={
                    'class': 'form-control'
                }),
            'tEndoEvolDescrip': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tEndoControl': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
        }

    fkEndoCaracteristica = forms.ModelMultipleChoiceField(queryset=EndoCaracteristica.objects.all(),
                                                          widget=forms.CheckboxSelectMultiple)
    fkEndoAnatoRadicular = forms.ModelMultipleChoiceField(queryset=EndoAnatoRadicular.objects.all(),
                                                          widget=forms.CheckboxSelectMultiple)


class FrmFichaEndodoncia(forms.ModelForm):
    class Meta:
        model = FichaEndodoncia
        fields = '__all__'
        exclude = ['fkEndodoncia']
        widgets = {
            'dEndoDiagFecha': forms.DateTimeInput(
                attrs={
                    'class': 'form-control'
                }),
            'tEndoDiente': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tEndoDiagnostico': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tEndoPronostico': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tEndoPlan': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tRecomendPosTrat': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmDetalleFichaEndodoncia(forms.ModelForm):
    class Meta:
        model = DetalleFichaEndodoncia
        fields = '__all__'
        exclude = ['fkFichaEndodoncia']
        widgets = {
            'cConducto': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cConducTent': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cConducDef': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cPuntReher': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLAP': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmOrtodoncia(forms.ModelForm):
    class Meta:
        model = Ortodoncia
        fields = '__all__'
        exclude = ['fkPaciente']
        widgets = {
            'dOrtoFecha': forms.DateTimeInput(
                attrs={
                    'class': 'form-control'
                }),
            'cMesoFacial': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDolicoFacial': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cBraquiFacial': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cRectoPerfil': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cConcavoPerfil': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cConvexoPerfil': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cMandDerecha': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cMandIzquierda': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cOtras': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEquilibradaAltura': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLargaAltura': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cCortaAltura': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEquilibradaAncho': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEstrechoAncho': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAmplioAncho': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cOrtognaticoMaxi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cPrognaticoMaxi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cRetrognaticoMaxi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'OrtognaticoMandi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'PrognaticoMandi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'RetrognaticoMandi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cNormalSurco': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cBorradoSurco': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cCompetentReposo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cIncompetentReposo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cProtusivoLabial': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cSupLabialprot': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cInfLabialprot': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cRetrusivosLabial': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cSupLabialrtr': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cInfLabialrtr': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cNormalLabial': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cBucalRespi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cNasalRespi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cMixtaRespi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDeglucionN': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDeglucionA': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cNormalComisural': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cContraccComisural': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cNormalAct': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cInterpAnterior': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cInterpLateral': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cNormalLabioSup': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cHipoactivLabioSup': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cHiperactivLavioSup': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cNormalLabioInfe': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cHipoactivLabioInf': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cHiperactivLabioInf': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cNormalMaset': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cHipoactivo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cHiperactivo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cNormalMenton': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cHipoactivoMenton': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cHiperactivoMenton': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDedosMenton': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLenguaMenton': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLabiosMenton': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cOnicofagiaMenton': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEjeFacial': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cProFacial': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAnglPlMandib': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAlturaFacInf': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cArcoMandib': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cMaxSuperior': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cConvexFacial': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cProfMaxilar': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDientes': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cIncisivoInfAPO': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cInclinaIncisInf': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'c1erMolarSupPTV': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cIncisInfAPLO': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAnguloInterInc': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cPerfBlando': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cProtLabioInf': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cVertA': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cVertPO': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cNormasCompstNorma': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cNormasCompstPac': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLongMaxilarNorma': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLongMaxilarPac': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLongMandibNorma': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLongMandibPac': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAlturaNorma': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAlturaPac': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAnalisis': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDiscreDentariamm': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEspcLibreNancemm': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDiscreTFCefalomm': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cTotalTFmm': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cVTOEjeFacial': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEjefacialmas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEjefacialmenos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEsoacioLibreMas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEsoacioLibreMenos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cConvexidadmas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cConvexidadmenos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cConvexidad': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cVertMoralMas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cVertMoralMenos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'c1aAPOMas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'c1aAPOMenos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'c1aAPO': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExpacionMas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExpacionMenos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAglInterMas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAglInterMenos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAnguloInterincis': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDesgInterMas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDesgInterMenos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLInfMas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLinfMenos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLabioInferPlanoE': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cReloc1Mas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cReloc1Menos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cTotalApoMas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cTotalApoMenos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cNetoApoMas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cNetoApoMenos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cPorHemiMas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cPorHemiMenos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tOrtoPlanTrat': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tOrtoTecnicApar': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'cOrtoTiempoTrat': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmRehabilitacionOral(forms.ModelForm):
    class Meta:
        model = RehabilitacionOral
        fields = '__all__'
        exclude = ['fkPaciente']
        widgets = {
            'dRehabFecha': forms.DateTimeInput(
                attrs={
                    'class': 'form-control'
                }),
            'tRehabMotivo': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'cNacimiento': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLactancia': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDesarrollo': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cHabitos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cTabaco': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAlcohol': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cRehabEnferEruptivas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cRehabEnferSistemica': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cRehabTransfus': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cRehabAlergias': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cRehabIntervuirurgi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cRehabInfeccion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cRehabHospitalizac': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cRehabPatoOtros': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAnFaPadre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAnFaMadre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAnFaHermanos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAnFaConyuge': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAnFaHijos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cVivienda': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAgua': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLuz': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAnimales': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEvaSistPiel': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEvaSistSistLinfa': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEvaSistSistMotor': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEvaSistSistOseoArt': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEvaSistSistNervio': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEvaSistAparCircula': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEvaSistAparRespira': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEvaSistAparDigesti': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEvaSistAparUri': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEvaSistOrgSentidos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisGPosicioActi': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisGDeambulacion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisGFascies': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisGPsiquis': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisGConstNutri': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisGPiel': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisGPulso': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisGRespira': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisGTemperatura': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisGPresArterial': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisGPeso': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisGTalla': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisRegCabeza': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisRegCara': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisRegCuello': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cExaFisRegLabios': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cATMovimienApertura': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cATMovimienCierre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cATHipertroMuscular': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cATMovimienLatDer': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cATMovimienLatIzq': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cATRuidosArtiChasq': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDolPalMasete': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDolPalTemporales': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDolPalPterioExt': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDolPalPteriodeosInt': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDolPalDigastricos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDolPalSuprahioides': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDolPalEstern': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cDolPalMuscPostCuell': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cIntraLabios': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cIntraVestibSurco': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tRehabDiagClinico': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tRehabRadiografico': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tRehabFotografico': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tRehabDiagDef': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tPlanTrat': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmOdonPediatriaPlan(forms.ModelForm):
    class Meta:
        model = OdonPediatriaPlan
        fields = '__all__'
        exclude = ['bEstado']
        widgets = {
            'cNombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmOdonPediatria(forms.ModelForm):
    class Meta:
        model = OdonPediatria
        fields = '__all__'
        exclude = ['fkPaciente']
        widgets = {
            'dOPedFecha': forms.DateTimeInput(
                attrs={
                    'class': 'form-control'
                }),
            'tOpedMotivo': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tHistEnfermeAct': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'bOPedTratMedico': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }),
            'cOpedUltima': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'bOPedMedica': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }),
            'tAnteFam': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tTratAnt': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tHigieneOral': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tHabitosDeletereos': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'cOpedConViveNino': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cOpedQuienCuidaNino': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cOpedNivelEducPadres': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cOpedActitudPadresTto': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'tOpedObservaciones': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tOPedRemisiones': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
        }

    fkOdonPediatriaPlan = forms.ModelMultipleChoiceField(queryset=OdonPediatriaPlan.objects.all(),
                                                         widget=forms.CheckboxSelectMultiple)


class FrmOdonPedExamenExtraOral(forms.ModelForm):
    class Meta:
        model = OdonPedExamenExtraOral
        fields = '__all__'
        exclude = ['fkOdonPediatria']
        widgets = {
            'cFrente': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cPerfil': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cNariz': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLabios': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cATM': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cAdenopatias': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cOtros': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmOdonPedExamenIntraOral(forms.ModelForm):
    class Meta:
        model = OdonPedExamenIntraOral
        fields = '__all__'
        exclude = ['fkOdonPediatria']
        widgets = {
            'cOrofaringe': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cPaladar': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cEncias': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cLengua': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cMucosas': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cBoca': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cFrenillos': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cOtros': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmOdonPedExamenOclusion(forms.ModelForm):
    class Meta:
        model = OdonPedExamenOclusion
        fields = '__all__'
        exclude = ['fkOdonPediatria']
        widgets = {
            'cRelaciMolar': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cRelaciCanina': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cApinamiento': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cSobremordida': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'cRelacitrans': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
        }


class FrmOdonPedOtrosExamen(forms.ModelForm):
    class Meta:
        model = OdonPedOtrosExamen
        fields = '__all__'
        exclude = ['fkOdonPediatria']
        widgets = {
            'tExaCompLab': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'tExaCompRadiografico': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }),
            'bMedioDiagPac': forms.CheckboxInput(
                attrs={
                    'class': 'form-control'
                }),
            'tOPedDiagDef': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
        }

    # region Odontograma


dientes_Choices = (
    ('caries', 'Caries'),
    ('coronatemp', 'Corona Temporal'),
    ('dentausente', 'Pieza dentaria ausente'),
    ('dentsuper', 'Pieza Dental Supernumeraria'),
    ('diastema', 'Diastema'),
    ('edentotal', 'Edentutlo total'),
    ('erupcion', 'Erupción'),
    ('fractura', 'Fractura'),
    ('muñon', 'Espigo-Muñon'),
    ('ortoremov1', 'Ortoremov'),
    ('ortoremovbuen', 'Aparato Ortodóntico Removible (Buen estado)'),
    ('ortoremovmal', 'Aparato Ortodóntico Removible (Mal estado)'),
    ('protesisfijabuen', 'Prótesis Fija (Buen Estado)'),
    ('protesisfijamal', 'Prótesis Fija (Mal Estado)'),
    ('protremovbuen', 'Protremovbuen'),
    ('protremovmal', 'Protremovmal'),
    ('resbuenestado', 'Restauración (Buen estado)'),
    ('resmalestado', 'Restauración (Mal estado)'),
    ('restemp', 'Restauración (Temporal)'),
    ('sellantebueno', 'Sellante (Buen estado)'),
    ('sellantemalo', 'Sellante (Mal estado)'),
)


class T11Form(forms.ModelForm):
    cT11 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT11', ]


class T12Form(forms.ModelForm):
    cT12 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT12', ]


class T13Form(forms.ModelForm):
    cT13 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT13', ]


class T14Form(forms.ModelForm):
    cT14 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT14', ]


class T15Form(forms.ModelForm):
    cT15 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT15', ]


class T16Form(forms.ModelForm):
    cT16 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT16', ]


class T17Form(forms.ModelForm):
    cT17 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT17', ]


class T18Form(forms.ModelForm):
    cT18 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT18', ]


class T21Form(forms.ModelForm):
    cT21 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT21', ]


class T22Form(forms.ModelForm):
    cT22 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT22', ]


class T23Form(forms.ModelForm):
    cT23 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT23', ]


class T24Form(forms.ModelForm):
    cT24 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT24', ]


class T25Form(forms.ModelForm):
    cT25 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT25', ]


class T26Form(forms.ModelForm):
    cT26 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT26', ]


class T27Form(forms.ModelForm):
    cT27 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT27', ]


class T28Form(forms.ModelForm):
    cT28 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT28', ]


class T31Form(forms.ModelForm):
    cT31 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT31', ]


class T32Form(forms.ModelForm):
    cT32 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT32', ]


class T33Form(forms.ModelForm):
    cT33 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT33', ]


class T34Form(forms.ModelForm):
    cT34 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT34', ]


class T35Form(forms.ModelForm):
    cT35 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT35', ]


class T36Form(forms.ModelForm):
    cT36 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT36', ]


class T37Form(forms.ModelForm):
    cT37 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT37', ]


class T38Form(forms.ModelForm):
    cT38 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT38', ]


class T41Form(forms.ModelForm):
    cT41 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT41', ]


class T42Form(forms.ModelForm):
    cT42 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT42', ]


class T43Form(forms.ModelForm):
    cT43 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT43', ]


class T44Form(forms.ModelForm):
    cT44 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT44', ]


class T45Form(forms.ModelForm):
    cT45 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT45', ]


class T46Form(forms.ModelForm):
    cT46 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT46', ]


class T47Form(forms.ModelForm):
    cT47 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT47', ]


class T48Form(forms.ModelForm):
    cT48 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT48', ]


class T51Form(forms.ModelForm):
    cT51 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT51', ]


class T52Form(forms.ModelForm):
    cT52 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT52', ]


class T53Form(forms.ModelForm):
    cT53 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT53', ]


class T54Form(forms.ModelForm):
    cT54 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT54', ]


class T55Form(forms.ModelForm):
    cT55 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT55', ]


class T61Form(forms.ModelForm):
    cT61 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT61', ]


class T62Form(forms.ModelForm):
    cT62 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT62', ]


class T63Form(forms.ModelForm):
    cT63 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT63', ]


class T64Form(forms.ModelForm):
    cT64 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT64', ]


class T65Form(forms.ModelForm):
    cT65 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT65', ]


class T71Form(forms.ModelForm):
    cT71 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT71', ]


class T72Form(forms.ModelForm):
    cT72 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT72', ]


class T73Form(forms.ModelForm):
    cT73 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT73', ]


class T74Form(forms.ModelForm):
    cT74 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT74', ]


class T75Form(forms.ModelForm):
    cT75 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT75', ]


class T81Form(forms.ModelForm):
    cT81 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT81', ]


class T82Form(forms.ModelForm):
    cT82 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT82', ]


class T83Form(forms.ModelForm):
    cT83 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT83', ]


class T84Form(forms.ModelForm):
    cT84 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT84', ]


class T85Form(forms.ModelForm):
    cT85 = forms.MultipleChoiceField(
        choices=dientes_Choices,

        widget=forms.CheckboxSelectMultiple,
        # label='',
    )

    class Meta:
        model = Odontograma
        fields = ['cT85', ]

# endregion
