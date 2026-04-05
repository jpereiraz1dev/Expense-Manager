from django.contrib import admin
from .models import Gasto,MetaInvestimento,Fixo,Parcela,Planejamento

# Register your models here.

admin.site.register(Gasto)
admin.site.register(MetaInvestimento)
admin.site.register(Fixo)
admin.site.register(Parcela)
admin.site.register(Planejamento)