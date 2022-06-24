from django.contrib import admin
from .models import *

# Añadiendo los modelos (tablas) al admin page

admin.site.register(Paciente)
admin.site.register(Tratamiento)
admin.site.register(PlanTratamiento)
admin.site.register(PagoPaciente)
admin.site.register(ImgRayosx)
admin.site.register(Receta)

admin.site.register(OdontoGeneral)
admin.site.register(Endodoncia)
admin.site.register(EndoCaracteristica)
admin.site.register(EndoAnatoRadicular)
admin.site.register(FichaEndodoncia)
admin.site.register(DetalleFichaEndodoncia)
admin.site.register(Ortodoncia)
admin.site.register(RehabilitacionOral)
admin.site.register(OdonPediatria)
admin.site.register(OdonPediatriaPlan)
admin.site.register(OdonPedExamenExtraOral)
admin.site.register(OdonPedExamenIntraOral)
admin.site.register(OdonPedExamenOclusion)
admin.site.register(OdonPedOtrosExamen)
admin.site.register(Odontograma)