from django.db import models

def upload_location(instance, filename):
    filebase, extension = filename.split('.')
    nameFile = 'perfil_'+str(instance.id_usuario)
    return 'usuarios/%s.%s' % (nameFile, extension)

def upload_location_prod(instance, filename):
    filebase, extension = filename.split('.')
    nameFile = 'producto_'+str(instance.id_prod)
    return 'productos/%s.%s' % (nameFile, extension)


# Create your models here.
class Profesiones(models.Model):
    id_prof         = models.AutoField(primary_key=True)
    nombre          = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)

class Usuario(models.Model):
    id_usuario      = models.IntegerField(primary_key=True, default=0)
    rut             = models.CharField(max_length=12, null=False)
    nombre          = models.CharField(max_length=20, blank=False, null=False)
    ape_paterno     = models.CharField(max_length=20, blank=False, null=False)
    ape_materno     = models.CharField(max_length=20, blank=False, null=True)
    fecha_nac       = models.DateField(blank=False, null=False)
    telefono        = models.CharField(max_length=9, null=True)
    email           = models.EmailField(unique=True, max_length=30, blank=False, null=False)
    direccion       = models.CharField(max_length=100, blank=False, null=True)
    img_perfil      = models.ImageField(upload_to=upload_location, null=True)
    calificacion    = models.IntegerField(null=False, default=0)
    id_prof         = models.ForeignKey(Profesiones, on_delete=models.CASCADE, db_column='id_prof')

    def __str__(self):
        return str(self.nombre)+" "+str(self.ape_paterno)
    
    @property
    def getProfesionName(self):
        return self.id_prof.nombre
    
class InfoEmpresa(models.Model):
    id_inf_emp  = models.AutoField(primary_key=True)
    rut         = models.CharField(max_length=12, null=False)
    nombreRubro = models.CharField(max_length=30, blank=False, null=False)

class CategoriaProducto(models.Model):
    id_categ_prod   = models.AutoField(primary_key=True)
    nombre          = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    id_prod         = models.IntegerField(primary_key=True, default=0)
    nombre          = models.CharField(max_length=20, blank=False, null=False)
    precio          = models.IntegerField(null=False, default=0)
    stock           = models.PositiveIntegerField(null=False, default=0)
    img_producto    = models.ImageField(upload_to=upload_location_prod, null=True)
    id_categ_prod   = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE, db_column='id_categ_prod')
    id_usuario      = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')

    def __str__(self):
        return str(self.nombre)

class SesionesEmpleados(models.Model):
    id_sesion_emp   = models.AutoField(primary_key=True)

class CompraUsuario(models.Model):
    id_compra_user  = models.IntegerField(primary_key=True, default=0)
    total_compra    = models.IntegerField(null=False, default=0)
    cont_prods      = models.IntegerField(null=False, default=0)
    id_user         = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')