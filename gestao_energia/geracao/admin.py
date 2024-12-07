from django.contrib import admin
from geracao.models import Faturamento
from geracao.models import Cliente

# Register your models here.
admin.site.register([Faturamento, Cliente])