from django.db import models
from django.utils import timezone
import os

#Se crean las clases que van a definir las tablas para luego ser llamadas en el views.py

#region TablaPaciente
class Paciente(models.Model):

    estadoCivil_Choices = (
        ('S', 'Soltero'),
        ('C', 'Casado'),
        ('V', 'Viudo'),
        ('D', 'Divorciado'),
        ('N', 'No informado'),
    )

    sexo_Choices = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'No especifica')
    )

    cPacNombres         = models.CharField(max_length=200)
    nPacDni             = models.CharField(max_length=15, unique=True)          #CAMBIAR PRIMERA LETRA!!!!!
    dPacFechaRegistro   = models.DateTimeField(auto_now_add=True)
    cPacEstadoCivil     = models.CharField(max_length=1, choices=estadoCivil_Choices, default='N')
    cPacSexo            = models.CharField(max_length=1, choices=sexo_Choices, default='M')
    dPacFecNacimiento   = models.DateField()
    cPacCiudadNacimiento = models.CharField(max_length=200)
    cPacDireccion       = models.CharField(max_length=200)
    nPacCodPostal       = models.IntegerField(blank=True, null=True)
    nPacCelTlf          = models.CharField(max_length=15)
    cPacEmail           = models.EmailField(max_length=254, blank=True, null=True)
    cPacOcupacion       = models.CharField(max_length=200, blank=True, null=True)
    cPacAlergia         = models.CharField(max_length=200, blank=True, null=True)
    cNombresApoderado   = models.CharField(max_length=200, blank=True, null=True)
    iPacImg             = models.ImageField(upload_to='images', blank=True, null=True)
    nTelfApoderado      = models.CharField(max_length=15, blank=True, null=True)

    dUltFecActualizacion = models.DateTimeField(auto_now=True)
    bEstado             = models.BooleanField(default=True)

    def __str__(self):
        return self.cPacNombres
#endregion

#region TablaTratamiento
class Tratamiento(models.Model):
    cTratNombre = models.CharField(max_length=200)
    mTratPrecio = models.DecimalField(max_digits=6, decimal_places=2, help_text='Solo número')  #Ejemplo: 9999,99
    cTratDesc   = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.cTratNombre
#endregion

#region TablaPlanTratamiento
class PlanTratamiento(models.Model):
    fkPaciente      = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dPlnFechaTrat   = models.DateTimeField(default=timezone.now)
    fkTratamiento   = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    cPlnNomTrat     = models.CharField(max_length=200)
    cPlnObservacion = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.cPlnNomTrat
#endregion

#region TablaPagoPaciente
class PagoPaciente(models.Model):
    pagoModo_Choices = (
        ('T', 'Pago con tarjeta'),
        ('E', 'Pago en efectivo'),
    )
    
    fkPaciente      = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dPagoFecha      = models.DateTimeField(default=timezone.now)
    fkTratamiento   = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    #cPagoNomDoc     = models.CharField(max_length=200, blank=True, null=True)
    mPagoMontoTotal = models.DecimalField(max_digits=6, decimal_places=2, help_text='Solo número')
    cModoPago       = models.CharField(max_length=4, choices=pagoModo_Choices, default='E')

    def __str__(self):
        return self.fkPaciente.cPacNombres
#endregion

#region ImgRayosx
class ImgRayosx(models.Model):
    fkPaciente  = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    iRayosxImg  = models.ImageField(upload_to='images')
    tDescImg    = models.TextField(max_length=500, blank=True, null=True)
    dFechaImg   = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.fkPaciente.cPacNombres
#endregion

#region Receta
class Receta (models.Model):
    fkPaciente      = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dRctaFecha      = models.DateTimeField(default=timezone.now)
    fkTratamiento   = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    tDescripcion    = models.TextField(max_length=300, blank=True, null=True)
    tIndicacion     = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.fkPaciente.cPacNombres
#endregion

#region Especialidades

#region OdontoGeneral
class OdontoGeneral(models.Model):
    fkPaciente            = models.ForeignKey(Paciente, on_delete=models.CASCADE)     #ADDED!!
    dOdontGeneralFecha    = models.DateTimeField(default=timezone.now)
    tMotivoConsulta       = models.TextField(max_length=500)
    cEnfermedadActual     = models.CharField(max_length=250)
    tMedicaActual         = models.TextField(max_length=500, blank=True, null=True)
    cTiempoEnfermedad     = models.CharField(max_length=200, blank=True, null=True)
    cSignosSintomas       = models.CharField(max_length=250)
    tRelatoCrono          = models.TextField(max_length=400, blank=True, null=True)
    #Antecedentes Cronologicos
    tAnteceFamiliar       = models.TextField(max_length=300, blank=True, null=True)
    tAntecePersonal       = models.TextField(max_length=300, blank=True, null=True)
    #Examen Actual
    tExamenGeneral        = models.TextField(max_length=400)
    tExamenOdontEstoma    = models.TextField(max_length=450, blank=True, null=True)
    #Diagnostico
    tDiagPresuntivo       = models.TextField(max_length=400, blank=True, null=True)
    tDiagDefinitivo       = models.TextField(max_length=500, blank=True, null=True)
    tPlanTratamiento      = models.TextField(max_length=450, blank=True, null=True)
    tRecomendacion        = models.TextField(max_length=400, blank=True, null=True) #(Nombre generico del medicamento, dosis, via de administracion, tiempo de administracion, cuidados, medidas higenico-dieteticas, preventivas)
    tAlta                 = models.TextField(max_length=400)

    def __str__(self):
        return self.fkPaciente.cPacNombres
#endregion

#region Endodoncia

#region EndoCaracteristica
class EndoCaracteristica(models.Model):
    cNombre = models.CharField(max_length=200)
    bEstado = models.BooleanField(default=True) 

    def __str__(self):
        return self.cNombre
#endregion

#region EndoAnatoRadicular
class EndoAnatoRadicular(models.Model):
    cNombre = models.CharField(max_length=200)
    bEstado = models.BooleanField(default=True) 

    def __str__(self):
        return self.cNombre
#endregion

class Endodoncia(models.Model):
    #EXAMEN CLINICO
    frioCalor_Choices = (
        ('A', 'Alta'),
        ('B', 'Retardada'),
        ('C', 'Alivio')
    )

    fkPaciente    = models.ForeignKey(Paciente, on_delete=models.CASCADE)         #ADDED!!
    dEndoFecha    = models.DateTimeField(default = timezone.now)
    cEndoDolor    = models.BooleanField(default=False) #(DUELE SI O NO) # O USAR CHOICES
    cEndoFrio     = models.CharField(max_length=1, choices=frioCalor_Choices, default = 'A' )
    cEndoCalor    = models.CharField(max_length=1, choices=frioCalor_Choices, default = 'A' )

    #EXAMEN RADIOGRAFICO
    cAnatoRadOtros   = models.CharField(max_length=200, blank=True, null=True)
    #Imagen? 

    #Notas evolucion
    dEndoEvolFecha    = models.DateTimeField(default=timezone.now)
    tEndoEvolDescrip  = models.TextField(max_length=400, blank=True, null=True)
    tEndoControl      = models.TextField(max_length=400, blank=True, null=True)

    #ManyToMany
    fkEndoCaracteristica  = models.ManyToManyField(EndoCaracteristica, related_name="endoCaracteristica", blank=True) 
    fkEndoAnatoRadicular  = models.ManyToManyField(EndoAnatoRadicular, related_name="endoAnatoRadicular", blank=True)
    def __str__(self):
        return self.fkPaciente.cPacNombres

#region FichaEndodoncia
class FichaEndodoncia(models.Model):
    fkEndodoncia      = models.OneToOneField(Endodoncia, related_name="endoFicha", on_delete=models.CASCADE)       
    #DIAGNÓSTICO, PRONÓSTICO, PLAN DE TRATAMIENTOS
    dEndoDiagFecha    = models.DateTimeField(default = timezone.now)
    tEndoDiente       = models.TextField(max_length=50)
    tEndoDiagnostico  = models.TextField(max_length=400, blank=True, null=True)
    tEndoPronostico   = models.TextField(max_length=400, blank=True, null=True)
    tEndoPlan         = models.TextField(max_length=400, blank=True, null=True) 
    tRecomendPosTrat  = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.fkEndodoncia.fkPaciente.cPacNombres
#endregion

#region DetalleFichaEndodoncia
class DetalleFichaEndodoncia(models.Model):
    fkFichaEndodoncia   = models.ForeignKey(FichaEndodoncia, on_delete=models.CASCADE) 
    cConducto           = models.CharField(max_length=50, blank=True, null=True)
    cConducTent         = models.CharField(max_length=50, blank=True, null=True)
    cConducDef          = models.CharField(max_length=50, blank=True, null=True)
    cPuntReher          = models.CharField(max_length=50, blank=True, null=True)
    cLAP                = models.CharField(max_length=50, blank=True, null=True) 
    def __str__(self):
        return self.fkFichaEndodoncia
#endregion

#endregion

#region Ortodoncia 
class Ortodoncia(models.Model):
    fkPaciente          = models.ForeignKey(Paciente, on_delete=models.CASCADE)         #ADDED!!
    dOrtoFecha          = models.DateTimeField(default=timezone.now)
    #Analisis Facial
        #Patron Facial:
    cMesoFacial         = models.CharField(max_length=50, blank=True, null=True)
    cDolicoFacial       = models.CharField(max_length=50, blank=True, null=True)
    cBraquiFacial       = models.CharField(max_length=50, blank=True, null=True)
     #Perfil:
    cRectoPerfil        = models.CharField(max_length=50, blank=True, null=True)
    cConcavoPerfil      = models.CharField(max_length=50, blank=True, null=True)
    cConvexoPerfil      = models.CharField(max_length=50, blank=True, null=True)
    #Asimetria:
    cMandDerecha        = models.CharField(max_length=50, blank=True, null=True)
    cMandIzquierda      = models.CharField(max_length=50, blank=True, null=True)
    cOtras              = models.CharField(max_length=50, blank=True, null=True)
    #Altura Facial:
    cEquilibradaAltura  = models.CharField(max_length=50, blank=True, null=True)
    cLargaAltura        = models.CharField(max_length=50, blank=True, null=True)
    cCortaAltura        = models.CharField(max_length=50, blank=True, null=True)
    #Ancho Facial:
    cEquilibradaAncho  = models.CharField(max_length=50, blank=True, null=True)
    cEstrechoAncho     = models.CharField(max_length=50, blank=True, null=True)
    cAmplioAncho       = models.CharField(max_length=50, blank=True, null=True)
    #Perfil Maxilar:
    cOrtognaticoMaxi   = models.CharField(max_length=50, blank=True, null=True)
    cPrognaticoMaxi    = models.CharField(max_length=50, blank=True, null=True)
    cRetrognaticoMaxi  = models.CharField(max_length=50, blank=True, null=True)
    #Perfil Madibular:
    OrtognaticoMandi   = models.CharField(max_length=50, blank=True, null=True)
    PrognaticoMandi    = models.CharField(max_length=50, blank=True, null=True)
    RetrognaticoMandi  = models.CharField(max_length=50, blank=True, null=True)
    #Surco Labio-Menton:
    cNormalSurco       = models.CharField(max_length=50, blank=True, null=True)
    #cNormalSurco       = models.CharField(max_length=50, blank=True, null=True)    #Se repite?????????
    cBorradoSurco      = models.CharField(max_length=50, blank=True, null=True)
    #Labios en Reposo:
    cCompetentReposo   = models.CharField(max_length=50, blank=True, null=True)
    cIncompetentReposo = models.CharField(max_length=50, blank=True, null=True)
    #Perfil Labial:
    cProtusivoLabial   = models.CharField(max_length=50, blank=True, null=True)
    cSupLabialprot     = models.CharField(max_length=50, blank=True, null=True)
    cInfLabialprot     = models.CharField(max_length=50, blank=True, null=True)
    cRetrusivosLabial  = models.CharField(max_length=50, blank=True, null=True)
    cSupLabialrtr      = models.CharField(max_length=50, blank=True, null=True)
    cInfLabialrtr      = models.CharField(max_length=50, blank=True, null=True)
    cNormalLabial      = models.CharField(max_length=50, blank=True, null=True)
    #Analisis funcional 
    #Respiración:
    cBucalRespi        = models.CharField(max_length=50, blank=True, null=True)
    cNasalRespi        = models.CharField(max_length=50, blank=True, null=True)
    cMixtaRespi        = models.CharField(max_length=50, blank=True, null=True)
    cDeglucionN        = models.CharField(max_length=50, blank=True, null=True)
    cDeglucionA        = models.CharField(max_length=50, blank=True, null=True)
    #Actividad Comisural:
    cNormalComisural   = models.CharField(max_length=50, blank=True, null=True)
    cContraccComisural = models.CharField(max_length=50, blank=True, null=True)
    #Actividad Lingual:
    cNormalAct = models.CharField(max_length=50)
    cInterpAnterior    = models.CharField(max_length=50, blank=True, null=True)
    cInterpLateral     = models.CharField(max_length=50, blank=True, null=True)
    #Labio Superior:
    cNormalLabioSup    = models.CharField(max_length=50, blank=True, null=True)
    cHipoactivLabioSup = models.CharField(max_length=50, blank=True, null=True)
    cHiperactivLavioSup= models.CharField(max_length=50, blank=True, null=True)
    #Labio Inferior:
    cNormalLabioInfe   = models.CharField(max_length=50, blank=True, null=True)
    cHipoactivLabioInf = models.CharField(max_length=50, blank=True, null=True)
    cHiperactivLabioInf= models.CharField(max_length=50, blank=True, null=True)
    #Masetero:
    cNormalMaset       = models.CharField(max_length=50, blank=True, null=True)
    cHipoactivo        = models.CharField(max_length=50, blank=True, null=True)
    cHiperactivo       = models.CharField(max_length=50, blank=True, null=True)
    #Mentoniano:
    cNormalMenton      = models.CharField(max_length=50, blank=True, null=True)
    cHipoactivoMenton  = models.CharField(max_length=50, blank=True, null=True)
    cHiperactivoMenton = models.CharField(max_length=50, blank=True, null=True)
    cDedosMenton       = models.CharField(max_length=50, blank=True, null=True)
    cLenguaMenton      = models.CharField(max_length=50, blank=True, null=True)
    cLabiosMenton      = models.CharField(max_length=50, blank=True, null=True)
    cOnicofagiaMenton  = models.CharField(max_length=50, blank=True, null=True)

    #TABLAAAAAAA CEFALOGRAMA DE RICKETTS :D?
        #MAX. INFERIOR, NORMA, INICIAL
    cEjeFacial         = models.CharField(max_length=50, blank=True, null=True) #(90º +- 3,0º)
    cProFacial         = models.CharField(max_length=50, blank=True, null=True) #(87º +- 3,0º)
    cAnglPlMandib      = models.CharField(max_length=50, blank=True, null=True) #(26º +- 4,0º)
    cAlturaFacInf      = models.CharField(max_length=50, blank=True, null=True) #(47º +- 4,0º)
    cArcoMandib        = models.CharField(max_length=50, blank=True, null=True) #(26º +- 4,0º)
    cMaxSuperior       = models.CharField(max_length=50, blank=True, null=True)
    cConvexFacial      = models.CharField(max_length=50, blank=True, null=True) #(+2)
    cProfMaxilar       = models.CharField(max_length=50, blank=True, null=True) #(90º+-3,0º)
    cDientes           = models.CharField(max_length=50, blank=True, null=True)
    cIncisivoInfAPO    = models.CharField(max_length=50, blank=True, null=True) #(+1º)
    cInclinaIncisInf   = models.CharField(max_length=50, blank=True, null=True) #(22º+-4,0º)
    c1erMolarSupPTV    = models.CharField(max_length=50, blank=True, null=True) #(edad +3)
    cIncisInfAPLO      = models.CharField(max_length=50, blank=True, null=True) #(+1,25)
    cAnguloInterInc    = models.CharField(max_length=50, blank=True, null=True) #(130º+-10º)
    cPerfBlando        = models.CharField(max_length=50, blank=True, null=True)
    cProtLabioInf      = models.CharField(max_length=50, blank=True, null=True) #(-2+-2mm)

    #TABLAAAAAAA CEFALOGRAMA MC NAMARA
        #Medida, Norma, Paciente
    cVertA             = models.CharField(max_length=50, blank=True, null=True) #(0 mm +- 1 mm)
    cVertPO            = models.CharField(max_length=50, blank=True, null=True) #(-8 a 6/ -4 a 0)
    cNormasCompstNorma = models.CharField(max_length=50, blank=True, null=True) 
    cNormasCompstPac   = models.CharField(max_length=50, blank=True, null=True) 
    cLongMaxilarNorma  = models.CharField(max_length=50, blank=True, null=True) 
    cLongMaxilarPac    = models.CharField(max_length=50, blank=True, null=True) 
    cLongMandibNorma   = models.CharField(max_length=50, blank=True, null=True) 
    cLongMandibPac     = models.CharField(max_length=50, blank=True, null=True) 
    cAlturaNorma       = models.CharField(max_length=50, blank=True, null=True) 
    cAlturaPac         = models.CharField(max_length=50, blank=True, null=True) 

    #TABLAAAAAA ANALISIS ESQUELETAL
    cAnalisis          = models.CharField(max_length=500, blank=True, null=True)

    #DETERMINACION DEL TIPO FACIAL
        #VERT
        #MESOFACIAL 0 BRAQUI + 0,5 BRAQUI SEVERO + 1
        #DOLICO SUAVE - 0,5 DOLICO - 1 DOLICO SEVERO - 2
        #TABLAAAAAAAA 
        #ANALISIS DE ARCOS DENTARIOS, DESCRIPCION DE MALOCLUSION
    cDiscreDentariamm  = models.CharField(max_length=50, blank=True, null=True) 
    cEspcLibreNancemm  = models.CharField(max_length=50, blank=True, null=True) 
    cDiscreTFCefalomm  = models.CharField(max_length=50, blank=True, null=True) 
    cTotalTFmm         = models.CharField(max_length=50, blank=True, null=True) 

    #PLANIFICACION DEL V.T.O.
        #V.T.O, 1. APO
        #       +, -
    cVTOEjeFacial     = models.CharField(max_length=50, blank=True, null=True)
    cEjefacialmas     = models.CharField(max_length=50, blank=True, null=True)
    cEjefacialmenos   = models.CharField(max_length=50, blank=True, null=True)
    cEsoacioLibreMas  = models.CharField(max_length=50, blank=True, null=True)
    cEsoacioLibreMenos= models.CharField(max_length=50, blank=True, null=True)
    cConvexidadmas    = models.CharField(max_length=50, blank=True, null=True)
    cConvexidadmenos  = models.CharField(max_length=50, blank=True, null=True)
    cConvexidad       = models.CharField(max_length=50, blank=True, null=True)
    cVertMoralMas     = models.CharField(max_length=50, blank=True, null=True)
    cVertMoralMenos   = models.CharField(max_length=50, blank=True, null=True)
    c1aAPOMas         = models.CharField(max_length=50, blank=True, null=True)
    c1aAPOMenos       = models.CharField(max_length=50, blank=True, null=True)  
    c1aAPO            = models.CharField(max_length=50, blank=True, null=True)
    cExpacionMas      = models.CharField(max_length=50, blank=True, null=True)
    cExpacionMenos    = models.CharField(max_length=50, blank=True, null=True)
    cAglInterMas      = models.CharField(max_length=50, blank=True, null=True)
    cAglInterMenos    = models.CharField(max_length=50, blank=True, null=True) 
    cAnguloInterincis = models.CharField(max_length=50, blank=True, null=True)
    cDesgInterMas     = models.CharField(max_length=50, blank=True, null=True)
    cDesgInterMenos   = models.CharField(max_length=50, blank=True, null=True)
    cLInfMas          = models.CharField(max_length=50, blank=True, null=True)
    cLinfMenos        = models.CharField(max_length=50, blank=True, null=True)
    cLabioInferPlanoE = models.CharField(max_length=50, blank=True, null=True)
    cReloc1Mas        = models.CharField(max_length=50, blank=True, null=True)
    cReloc1Menos      = models.CharField(max_length=50, blank=True, null=True)
    cTotalApoMas      = models.CharField(max_length=50, blank=True, null=True)
    cTotalApoMenos    = models.CharField(max_length=50, blank=True, null=True)
    cNetoApoMas       = models.CharField(max_length=50, blank=True, null=True)
    cNetoApoMenos     = models.CharField(max_length=50, blank=True, null=True)
    cPorHemiMas       = models.CharField(max_length=50, blank=True, null=True)
    cPorHemiMenos      = models.CharField(max_length=50, blank=True, null=True)

    #PLAN DE TRATAMIENTO Y OBJETIVOS:
    tOrtoPlanTrat     = models.TextField(max_length=500, blank=True, null=True)
    #TECNICA Y APARATOLOGIA A EMPLEAR:
    tOrtoTecnicApar   = models.TextField(max_length=500, blank=True, null=True)
    #TIEMPO ESTIMADO DE TRATAMIENTO:
    cOrtoTiempoTrat   = models.CharField(max_length=100, blank=True, null=True)

    #FichaEvolucion NISE COMO PONERO XD 
    #TABLAAAAAAAAA (Fecha, Tratamiento Realizado, Tratamiento por Realizar, Pago, Saldo, Prox. Cita)
    def __str__(self):
        return self.fkPaciente.cPacNombres
#endregion

#region RehabilitaciónOral
class RehabilitacionOral(models.Model):
    fkPaciente           = models.ForeignKey(Paciente, on_delete=models.CASCADE)         #ADDED!!
    dRehabFecha          = models.DateTimeField(default=timezone.now)
    tRehabMotivo         = models.TextField(max_length=500, blank=True, null=True)
    #ANTECEDENTES
    #ANTECEDENTES PERSONALES
        #Fisiológicos
    cNacimiento          = models.CharField(max_length=100, blank=True, null=True)
    cLactancia           = models.CharField(max_length=100, blank=True, null=True)
    cDesarrollo          = models.CharField(max_length=100, blank=True, null=True)
    cHabitos             = models.CharField(max_length=100, blank=True, null=True)
    cTabaco              = models.CharField(max_length=100, blank=True, null=True)
    cAlcohol             = models.CharField(max_length=100, blank=True, null=True)
        #Patológicos
    cRehabEnferEruptivas = models.CharField(max_length=100, blank=True, null=True)
    cRehabEnferSistemica = models.CharField(max_length=100, blank=True, null=True)
    cRehabTransfus       = models.CharField(max_length=100, blank=True, null=True)
    cRehabAlergias       = models.CharField(max_length=100, blank=True, null=True)
    cRehabIntervuirurgi  = models.CharField(max_length=100, blank=True, null=True)
    cRehabInfeccion      = models.CharField(max_length=100, blank=True, null=True)
    cRehabHospitalizac   = models.CharField(max_length=100, blank=True, null=True)
    cRehabPatoOtros      = models.CharField(max_length=100, blank=True, null=True)

    #ANTECEDENTES FAMILIARES
    cAnFaPadre           = models.CharField(max_length=100, blank=True, null=True)
    cAnFaMadre           = models.CharField(max_length=100, blank=True, null=True)
    cAnFaHermanos        = models.CharField(max_length=100, blank=True, null=True)
    cAnFaConyuge         = models.CharField(max_length=100, blank=True, null=True)
    cAnFaHijos           = models.CharField(max_length=100, blank=True, null=True)

    #Socioeconomicos
    cVivienda           = models.CharField(max_length=100, blank=True, null=True)
    cAgua               = models.CharField(max_length=100, blank=True, null=True)
    cLuz                = models.CharField(max_length=100, blank=True, null=True)
    cAnimales           = models.CharField(max_length=100, blank=True, null=True)

    #EVALUACIÓN SISTÉMICA
    cEvaSistPiel        = models.CharField(max_length=100, blank=True, null=True)
    cEvaSistSistLinfa   = models.CharField(max_length=100, blank=True, null=True)
    cEvaSistSistMotor   = models.CharField(max_length=100, blank=True, null=True)
    cEvaSistSistOseoArt = models.CharField(max_length=100, blank=True, null=True)
    cEvaSistSistNervio  = models.CharField(max_length=100, blank=True, null=True)
    cEvaSistAparCircula = models.CharField(max_length=100, blank=True, null=True) 
    cEvaSistAparRespira = models.CharField(max_length=100, blank=True, null=True)
    cEvaSistAparDigesti = models.CharField(max_length=100, blank=True, null=True)
    cEvaSistAparUri     = models.CharField(max_length=100, blank=True, null=True)
    cEvaSistOrgSentidos = models.CharField(max_length=100, blank=True, null=True)

    #EXAMEN FÍSICO GENERAL
    cExaFisGPosicioActi = models.CharField(max_length=100, blank=True, null=True)
    cExaFisGDeambulacion= models.CharField(max_length=100, blank=True, null=True)
    cExaFisGFascies     = models.CharField(max_length=100, blank=True, null=True)
    cExaFisGPsiquis     = models.CharField(max_length=100, blank=True, null=True)
    cExaFisGConstNutri  = models.CharField(max_length=100, blank=True, null=True)
    cExaFisGPiel        = models.CharField(max_length=100, blank=True, null=True)
    cExaFisGPulso       = models.CharField(max_length=100, blank=True, null=True)
    cExaFisGRespira     = models.CharField(max_length=100, blank=True, null=True)
    cExaFisGTemperatura = models.CharField(max_length=100, blank=True, null=True)
    cExaFisGPresArterial= models.CharField(max_length=100, blank=True, null=True)
    cExaFisGPeso        = models.CharField(max_length=100, blank=True, null=True)
    cExaFisGTalla       = models.CharField(max_length=100, blank=True, null=True)

    #EXAMEN FÍSICO REGIONAL
        #Extraoral
    cExaFisRegCabeza    = models.CharField(max_length=100, blank=True, null=True)
    cExaFisRegCara      = models.CharField(max_length=100, blank=True, null=True)
    cExaFisRegCuello    = models.CharField(max_length=100, blank=True, null=True)
    cExaFisRegLabios    = models.CharField(max_length=100, blank=True, null=True)

        #Articulación Temporo Mandibular (ATM):
    cATMovimienApertura = models.CharField(max_length=100, blank=True, null=True)
    cATMovimienCierre   = models.CharField(max_length=100, blank=True, null=True)
    cATHipertroMuscular = models.CharField(max_length=100, blank=True, null=True)
    cATMovimienLatDer   = models.CharField(max_length=100, blank=True, null=True)
    cATMovimienLatIzq   = models.CharField(max_length=100, blank=True, null=True)
    cATRuidosArtiChasq  = models.CharField(max_length=100, blank=True, null=True)

        #Dolor a la Palpación:
    cDolPalMasete       = models.CharField(max_length=100, blank=True, null=True)
    cDolPalTemporales   = models.CharField(max_length=100, blank=True, null=True)
    cDolPalPterioExt    = models.CharField(max_length=100, blank=True, null=True)
    cDolPalPteriodeosInt= models.CharField(max_length=100, blank=True, null=True)
    cDolPalDigastricos  = models.CharField(max_length=100, blank=True, null=True)
    cDolPalSuprahioides = models.CharField(max_length=100, blank=True, null=True)
    cDolPalEstern       = models.CharField(max_length=100, blank=True, null=True)
    cDolPalMuscPostCuell= models.CharField(max_length=100, blank=True, null=True)

        #Intraoral:
    cIntraLabios        = models.CharField(max_length=100, blank=True, null=True)
    cIntraVestibSurco   = models.CharField(max_length=100, blank=True, null=True)

    #DIAGNOSTICO PRESUNTIVO
    tRehabDiagClinico   = models.TextField(max_length=400, blank=True, null=True)
    tRehabRadiografico  = models.TextField(max_length=400, blank=True, null=True)
    tRehabFotografico   = models.TextField(max_length=400, blank=True, null=True)

    #DIAGNOSTICO DEFINITIVO
    tRehabDiagDef       = models.TextField(max_length=500, blank=True, null=True)

    #PLAN DE TRATAMIENTO
    tPlanTrat           = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.fkPaciente.cPacNombres
#endregion

#region OdonPediatria

#region OdonPediatriaPlan
class OdonPediatriaPlan (models.Model):
    cNombre         = models.CharField(max_length=100)
    bEstado         = models.BooleanField(default=True)

    def __str__(self):
        return self.cNombre
#endregion

class OdonPediatria(models.Model):
    fkPaciente             = models.ForeignKey(Paciente, on_delete=models.CASCADE)         #ADDED!!
    dOPedFecha             = models.DateTimeField(default=timezone.now)
    tOpedMotivo            = models.TextField(max_length=500, blank=True, null=True)
    tHistEnfermeAct        = models.TextField(max_length=400, blank=True, null=True)
    bOPedTratMedico        = models.BooleanField(default=True) #(Tratameinto si o no? Cual?)
    cOpedUltima            = models.CharField(max_length=400, blank=True, null=True)
    bOPedMedica            = models.BooleanField(default=True) #(Tomando medicamento si o no? Cual?)
    tAnteFam               = models.TextField(max_length=500, blank=True, null=True)

    #ANTECEDENTES ODONTOLOGICOS:
    tTratAnt              = models.TextField(max_length=400, blank=True, null=True)
    tHigieneOral          = models.TextField(max_length=400, blank=True, null=True) #(como, cuando, donde, quien, con que)
    tHabitosDeletereos    = models.TextField(max_length=300, blank=True, null=True) #(frecuencia, duracion, intesidad)
    
    #TABLAAAAAAAA Comportamiento General
    #(Extrovertido, Introvertido, Sobreprotegido, Independiente, Timido, Temeroso, Agresivo)
    #Rendim Escolar (Bueno,Malo)
    #Reaccion TTO, Bueno, Malo (Medico, Odontologico)

    cOpedConViveNino      = models.CharField(max_length=100, blank=True, null=True)
    cOpedQuienCuidaNino   = models.CharField(max_length=100, blank=True, null=True)
    cOpedNivelEducPadres  = models.CharField(max_length=100, blank=True, null=True)
    cOpedActitudPadresTto = models.CharField(max_length=200, blank=True, null=True)
    tOpedObservaciones    = models.TextField(max_length=500, blank=True, null=True)
    
    #cPlan                = models.CharField(max_length=30, choices= Plan_Choises, blank=True, null=True )
    tOPedRemisiones       = models.TextField(max_length=400, blank=True, null=True)

    #ManyToMany
    fkOdonPediatriaPlan = models.ManyToManyField(OdonPediatriaPlan, related_name="odonPedPlan", blank=True)

    def __str__(self):
        return self.fkPaciente.cPacNombres

#region OdonPedExamenExtraOral
class OdonPedExamenExtraOral (models.Model):
    fkOdonPediatria = models.OneToOneField(OdonPediatria, related_name="odonPedExtraOral", on_delete=models.CASCADE)
    #Examen Extraoral
    cFrente      = models.CharField(max_length=100, blank=True, null=True)
    cPerfil      = models.CharField(max_length=100, blank=True, null=True)
    cNariz       = models.CharField(max_length=100, blank=True, null=True)
    cLabios      = models.CharField(max_length=100, blank=True, null=True)
    cATM         = models.CharField(max_length=100, blank=True, null=True)
    cAdenopatias = models.CharField(max_length=100, blank=True, null=True)
    cOtros       = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.fkOdonPediatria.fkPaciente.cPacNombres
#endregion

#region OdonPedExamenIntraOral
class OdonPedExamenIntraOral (models.Model):
    fkOdonPediatria       = models.OneToOneField(OdonPediatria, related_name="odonPedIntraOral", on_delete=models.CASCADE)
    #Examen Intraoral
    cOrofaringe= models.CharField(max_length=100, blank=True, null=True)
    cPaladar   = models.CharField(max_length=100, blank=True, null=True)
    cEncias    = models.CharField(max_length=100, blank=True, null=True)
    cLengua    = models.CharField(max_length=100, blank=True, null=True)
    cMucosas   = models.CharField(max_length=100, blank=True, null=True)
    cBoca      = models.CharField(max_length=100, blank=True, null=True)
    cFrenillos = models.CharField(max_length=100, blank=True, null=True)
    cOtros     = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.fkOdonPediatria
#endregion

#region OdonPedExamenOclusion
class OdonPedExamenOclusion (models.Model):
    fkOdonPediatria       = models.OneToOneField(OdonPediatria, related_name="odonPedOclusion", on_delete=models.CASCADE)
    #Examen de Oclusión
    cRelaciMolar  = models.CharField(max_length=100, blank=True, null=True)
    cRelaciCanina = models.CharField(max_length=100, blank=True, null=True)
    cApinamiento  = models.CharField(max_length=100, blank=True, null=True)
    cSobremordida = models.CharField(max_length=100, blank=True, null=True)
    cRelacitrans  = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.fkOdonPediatria
#endregion

#region OdonPedOtrosExamen
class OdonPedOtrosExamen (models.Model):
    fkOdonPediatria       = models.OneToOneField(OdonPediatria, related_name="odonPedOtroExamen", on_delete=models.CASCADE)
    #EXAMENES COMPLEMENTARIOS
    tExaCompLab         = models.TextField(max_length=300, blank=True, null=True)
    tExaCompRadiografico= models.TextField(max_length=300, blank=True, null=True)
    bMedioDiagPac       = models.BooleanField(default=True) #(Se entregan medios diagnosticos al paciente? Si o No)
    tOPedDiagDef        = models.TextField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.fkOdonPediatria
#endregion

#endregion

#endregion

#region Odontograma

class Odontograma(models.Model):
    fkPaciente     = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dFechaRegistro = models.DateTimeField(auto_now_add=True, editable=False)
    cT11 = models.CharField(max_length=90, default='sano')
    cT12 = models.CharField(max_length=90, default='sano')
    cT13 = models.CharField(max_length=90, default='sano')
    cT14 = models.CharField(max_length=90, default='sano')
    cT15 = models.CharField(max_length=90, default='sano')
    cT16 = models.CharField(max_length=90, default='sano')
    cT17 = models.CharField(max_length=90, default='sano')
    cT18 = models.CharField(max_length=90, default='sano')
    cT21 = models.CharField(max_length=90, default='sano')
    cT22 = models.CharField(max_length=90, default='sano')
    cT23 = models.CharField(max_length=90, default='sano')
    cT24 = models.CharField(max_length=90, default='sano')
    cT25 = models.CharField(max_length=90, default='sano')
    cT26 = models.CharField(max_length=90, default='sano')
    cT27 = models.CharField(max_length=90, default='sano')
    cT28 = models.CharField(max_length=90, default='sano')
    cT31 = models.CharField(max_length=90, default='sano')
    cT32 = models.CharField(max_length=90, default='sano')
    cT33 = models.CharField(max_length=90, default='sano')
    cT34 = models.CharField(max_length=90, default='sano')
    cT35 = models.CharField(max_length=90, default='sano')
    cT36 = models.CharField(max_length=90, default='sano')
    cT37 = models.CharField(max_length=90, default='sano')
    cT38 = models.CharField(max_length=90, default='sano')
    cT41 = models.CharField(max_length=90, default='sano')
    cT42 = models.CharField(max_length=90, default='sano')
    cT43 = models.CharField(max_length=90, default='sano')
    cT44 = models.CharField(max_length=90, default='sano')
    cT45 = models.CharField(max_length=90, default='sano')
    cT46 = models.CharField(max_length=90, default='sano')
    cT47 = models.CharField(max_length=90, default='sano')
    cT48 = models.CharField(max_length=90, default='sano')
    cT51 = models.CharField(max_length=90, default='sano')
    cT52 = models.CharField(max_length=90, default='sano')
    cT53 = models.CharField(max_length=90, default='sano')
    cT54 = models.CharField(max_length=90, default='sano')
    cT55 = models.CharField(max_length=90, default='sano')
    cT61 = models.CharField(max_length=90, default='sano')
    cT62 = models.CharField(max_length=90, default='sano')
    cT63 = models.CharField(max_length=90, default='sano')
    cT64 = models.CharField(max_length=90, default='sano')
    cT65 = models.CharField(max_length=90, default='sano')
    cT71 = models.CharField(max_length=90, default='sano')
    cT72 = models.CharField(max_length=90, default='sano')
    cT73 = models.CharField(max_length=90, default='sano')
    cT74 = models.CharField(max_length=90, default='sano')
    cT75 = models.CharField(max_length=90, default='sano')
    cT81 = models.CharField(max_length=90, default='sano')
    cT82 = models.CharField(max_length=90, default='sano')
    cT83 = models.CharField(max_length=90, default='sano')
    cT84 = models.CharField(max_length=90, default='sano')
    cT85 = models.CharField(max_length=90, default='sano')
    dUltFecActualizacion = models.DateTimeField(auto_now=True)

#endregion

##########################################################################################

#region DiccionarioDeDatos
"""
FALTA! - Aquí irá una descripción básica por cada tabla!!!!

Tabla : Paciente
Desc  : Detalles del paciente

"""
#endregion