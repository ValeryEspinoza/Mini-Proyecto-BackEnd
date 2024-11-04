from django.db import models

# Create your models here.
"""class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return str(self.nombre)
"""

#Sub_Categoria de productos
class Sub_Categories(models.Model):
    id_sub_category = models.AutoField(primary_key=True)
    sub_category_name = models.CharField(max_length=100, null= False)
    def __str__(self):
        return str(self.sub_category_name)


#Categoria de productos
class Categories(models.Model):
    id_category = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, null= False)
    category_description = models.TextField(null=False)
    id_sub_category = models.ForeignKey(Sub_Categories, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.category_name)
    

#Listo
class Supplier_Categories(models.Model):
    id_supplier_category = models.AutoField(primary_key=True)
    supplier_category_name = models.CharField(max_length=100, null=False)
    supplier_category_description = models.TextField(null= False)
    def __str__(self):
        return str(self.supplier_category_name)


class Suppliers(models.Model):
    id_supplier = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=100)
    supplier_description =  models.TextField(null=False)
    id_supplier_category =  models.ForeignKey(Supplier_Categories, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.supplier_name)


class Products(models.Model):
    id_product =  models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=7,  decimal_places=2, null= False)
    product_description =  models.TextField( null= False)
    id_category =  models.ForeignKey(Categories, on_delete=models.CASCADE)
    id_suplier =   models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.product_name)

class Inventory(models.Model):
    id_inventory = models.AutoField(primary_key=True)
    inventory_description = models.TextField(null=False)
    stock = models.IntegerField(null=False)
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.inventory_description)
   
class Clients(models.Model):
    id_client = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=100, null=False)
    client_lastname = models.CharField(max_length=100, null=False)
    client_email = models.CharField(max_length=200, unique=True, null=False)
    register_Date = models.DateField()
    def __str__(self):
        return str(self.client_name)
    
class Sell_Type(models.Model):
    id_sell_type = models.AutoField(primary_key=True)
    type_name =  models.CharField(max_length=100, null=False)
    type_description = models.TextField(null= False)
    def __str__(self):
        return str(self.type_name)
    
class Payment_Method(models.Model):
    id_payment_method = models.AutoField(primary_key=True)
    payment_method = models.CharField(max_length=100)
    payment_method_description = models.TextField(null= False)
    id_sell_type = models.ForeignKey(Sell_Type,  on_delete=models.CASCADE)
    def __str__(self):
        return str(self.payment_method)
    
class Sells(models.Model):
    id_sell = models.AutoField(primary_key=True)
    id_client= models.ForeignKey(Clients,  on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_sell)
    
class Sell_Detail(models.Model):
    id_sell_detail = models.AutoField(primary_key=True)
    sell_date = models.DateField()
    sub_total = models.DecimalField(max_digits=8, decimal_places=2)
    taxes = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    id_sell =  models.ForeignKey(Sells, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Products,  on_delete=models.CASCADE)
    id_paymenth_method = models.ForeignKey(Payment_Method,   on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_sell) 
    
class Record(models.Model):
    id_record = models.AutoField(primary_key=True)
    id_sell_detail =  models.ForeignKey(Sell_Detail, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_record)   
    
class Reviews(models.Model):
    id_review = models.AutoField(primary_key=True)
    review = models.TextField(null= False)
    calification = models.DecimalField(max_digits=2, decimal_places=1, null=False)
    id_product = models.ForeignKey(Products,  on_delete=models.CASCADE)
    id_client = models.ForeignKey(Clients,   on_delete=models.CASCADE)
    def __str__(self):
        return str(self.review)
    
class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=100, null=False)
    area_description = models.TextField(null=False)
    def __str__(self):
        return str(self.area_name)
   
class Access(models.Model):
    id_access = models.AutoField(primary_key=True)
    access_name = models.CharField(max_length=100,  null= False)
    permissions = models.TextField(null=False)
    def __str__(self):
        return str(self.access_name)

class Employee_Clasification(models.Model):
    id_employee_classification = models.AutoField(primary_key=True)
    employee_clasifiaction_name = models.CharField(max_length=100, null=False)
    id_access =  models.ForeignKey(Access,  on_delete=models.CASCADE)
    id_area = models.ForeignKey(Area,   on_delete=models.CASCADE)
    def __str__(self):
        return str(self.employee_clasifiaction_name)

class Position(models.Model):
    id_position = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=100, null=False)
    position_description = models.TextField(null=False)
    id_employee_clasification = models.ForeignKey(Employee_Clasification,   on_delete=models.CASCADE)
    def __str__(self):
        return str(self.position_name)
    
# arreglado
class Employees(models.Model):
    id_employee = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)

    class AgeChoices(models.IntegerChoices):
        UNDER_18 = 0, "Under 18"
        BETWEEN_18_25 = 1, "18-25"
        BETWEEN_26_35 = 2, "26-35"
        OVER_35 = 3, "Over 35"

    age = models.IntegerField(choices=AgeChoices.choices, null=False)  # Aqui asignamos las opciones de edad

    email = models.CharField(max_length=100, unique=True, null=False)
    iniciation_date = models.DateField(null=False)
    id_position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

