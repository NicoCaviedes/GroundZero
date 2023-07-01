from django.contrib import admin
from .models import Usuario,InfoEmpresa,CategoriaProducto,Producto,SesionesEmpleados,Profesiones

# Register your models here.
admin.site.register(Usuario)
admin.site.register(InfoEmpresa)
admin.site.register(CategoriaProducto)
admin.site.register(Producto)
admin.site.register(SesionesEmpleados)
admin.site.register(Profesiones)