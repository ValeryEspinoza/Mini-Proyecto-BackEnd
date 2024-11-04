from rest_framework import serializers
from datetime import datetime

from django.contrib.auth.models import User, Group
from rest_framework import serializers



from .models import (
    Sub_Categories, Categories, Supplier_Categories, Suppliers, Products,
    Inventory, Clients, Sell_Type, Sells, Sell_Detail, Record, Reviews,
    Area, Access, Employee_Clasification, Position, Employees, Payment_Method
)



class UserSerializer(serializers.ModelSerializer):
    role=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'role', 'password', 'username', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        # Extrae la contraseña del validated_data
       
        # Extrae el campo adicional 'group' que se usará para el grupo
        role = validated_data.pop('role')  # Asegúrate de que el nombre sea correcto
        # Crea el usuario sin guardar la contraseña aún
        user = User(**validated_data)
        # Establece la contraseña usando el método set_password
        user.set_password(validated_data['password'])
        # Guarda el usuario en la base de datos
        user.save()



        # Asigna el usuario al grupo si 'roll' es proporcionado
        if role:
            try:
                group = Group.objects.get(name=role)
                user.groups.add(group)  # Aquí se usa add(), que es correcto                                
            except Group.DoesNotExist:
                raise serializers.ValidationError(f"El grupo '{role}' no existe. ")
                    
        return user
    


    
    def validate_password (self, values):
        if len(values) <= 6:
           raise serializers.ValidationError(
               "Error: The name must contain at least 5 characters"
           )
        return values  
        
    def validate_email (self, values):
        if len(values) <= 5:
           raise serializers.ValidationError(
               "Error: The name must contain at least 5 characters"
           )
        return values  


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

    def validate_category_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre de la categoría no puede estar vacío.")
        if len(value) > 100:
            raise serializers.ValidationError("El nombre de la categoría no puede exceder 100 caracteres.")


    def validate_category_description(self, value):
        if not value:
            raise serializers.ValidationError("La descripción de la categoría no puede estar vacía.")
        return value


class Sub_CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Categories
        fields = '__all__'

    def validate_sub_category_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre de la subcategoría no puede estar vacío.")
        if len(value) > 100:
            raise serializers.ValidationError("El nombre de la subcategoría no puede exceder 100 caracteres.")
        return value

    def validate_id_category(self, value):
        if not Categories.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La categoría seleccionada no es válida.")
        return value


class ProductsSerializer(serializers.ModelSerializer):
    category= CategoriesSerializer(source='id_category')
    class Meta:
        model = Products
        fields = '__all__'

    def validate_product_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre del producto no puede estar vacío.")
        if len(value) > 100:
            raise serializers.ValidationError("El nombre del producto no puede exceder 100 caracteres.")
        return value

    def validate_product_price(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio del producto no puede ser negativo.")
        return value

    def validate_product_description(self, value):
        if not value:
            raise serializers.ValidationError("La descripción del producto no puede estar vacía.")
        return value

    def validate_id_category(self, value):
        if not Categories.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La categoría seleccionada no es válida.")
        return value

    def validate_id_supplier(self, value):
        if not Suppliers.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El proveedor seleccionado no es válido.")
        return value


class Supplier_CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier_Categories
        fields = '__all__'

    def validate_supplier_category_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre de la Categoría del producto no puede estar vacío.")
        if len(value) > 100:
            raise serializers.ValidationError("El nombre de la Categoría no puede exceder 100 caracteres.")
        return value
    
    def validate_supplier_category_description(self, value):
        if not value:
            raise serializers.ValidationError("La descripción de la categoría no puede estar vacía.")
        return value


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'

    def validate_supplier_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre del proveedor no puede estar vacío.")
        return value
    
    def validate_supplier_description(self, value):
        if not value:
            raise serializers.ValidationError("La descripción del proveedor no puede estar vacía.")
        return value
    
    def validate_id_supplier_category(self, value):
        if not Supplier_Categories.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La categoría seleccionada no es válida.")
        return value


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("La cantidad no puede ser negativa.")
        return value

    def validate_id_product(self, value):
        if not Products.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El producto seleccionado no es válido.")
        return value
    
    def validate_inventory_description(self, value):
        if not value:
            raise serializers.ValidationError("La descripción del proveedor no puede estar vacía.")
        return value


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

    def validate_client_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre del cliente no puede estar vacío.")
        return value
    
    def validate_client_lastname(self, value):
        if not value:
            raise serializers.ValidationError("El apellido del cliente no puede estar vacío.")
        return value
    
    def validate_client_email(self, value):
        if '@' not in value:
            raise serializers.ValidationError("El correo electrónico debe contener el símbolo '@'.")
        return value
    

class Sell_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell_Type
        fields = '__all__'

    def validate_type_name(self, value):
        if not value:
            raise serializers.ValidationError("El tipo de venta no puede estar vacío.")
        return value
    
    def validate_type_description(self, value):
        if not value:
            raise serializers.ValidationError("La descripción del tipo de venta no puede estar vacía.")
        return value

class Payment_MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Method
        fields = '__all__'
    
    def validate_payment_method(self, value):
        if not value:
            raise serializers.ValidationError("El método de pago no puede estar vacío.")
        return value

    def validate_payment_method_description(self, value):
        if not value:
            raise serializers.ValidationError("La descripción del tipo de pago no puede estar vacía.")
        return value


class SellsSerializer(serializers.ModelSerializer):
   # sell_detail_set = SellDetailSerializer(many=True, read_only=True)  # Incluye los detalles de la venta
    class Meta:
        model = Sells
        fields = '__all__'

    def validate_id_client(self, value):
        if not Clients.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El cliente seleccionado no es válido.")
        return value

class Sell_DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell_Detail
        fields = '__all__'

    def validate_sub_total(self, value):
        if value <= 0:
            raise serializers.ValidationError("El subtotal debe ser mayor a cero.")
        return value
    
    def validate_sell_date(self, value):
        if value > datetime.now().date():
            raise serializers.ValidationError("La fecha de venta no puede ser en el futuro.")
        return value
    
    def validate_total(self, value):
        if value <= 0:
            raise serializers.ValidationError("El subtotal debe ser mayor a cero.")
        return value
    
    def validate_id_product(self, value):
        if not Products.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El producto seleccionado no es válido.")
        return value
    
    def validate_id_paymenth_method(self, value):
        if not Payment_Method.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El método de pago seleccionado no es válido.")
        return value
    
    def validate_id_sell(self, value):
        if not Sells.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La venta seleccionada no es válido.")
        return value


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

    def validate_id_sell_detail(self, value):
        if not Sell_Detail.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La venta seleccionada no es válida.")
        return value
    

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

    def validate_review_text(self, value):
        if not value:
            raise serializers.ValidationError("El texto de la reseña no puede estar vacío.")
        return value

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("La calificación debe estar entre 1 y 5.")
        return value
    
    def validate_id_product(self, value):
        if not Products.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El producto seleccionado no es válido.")
        return value
    
    def validate_id_client(self, value):
        if not Clients.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El cliente seleccionado no es válido.")
        return value
    

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

    def validate_area_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre de la área no puede estar vacío.")
        return value
    
    def validate_area_description(self, value):
        if not value:
            raise serializers.ValidationError("La descripción no puede estar vacío.")
        return value
    

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'

    def validate_access_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre del acceso debe estar definido.")
        return value
    
    def validate_permissions(self, value):
        if not value:
            raise serializers.ValidationError("La descripción de los permisos no puede estar vacío.")
        return value


class Employee_ClasificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Clasification
        fields = '__all__'

    def validate_employee_clasifiaction_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre no puede estar vacío.")
        return value
    
    def validate_id_access(self, value):
        if not Access.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El Acceso seleccionado no es válido.")
        return value
    
    def validate_id_area(self, value):
        if not Area.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El area seleccionada no es válida.")
        return value
    

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

    def validate_position_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre de la posición no puede estar vacío.")
        return value
    
    def validate_position_description(self, value):
        if not value:
            raise serializers.ValidationError("La descripción de la posicion no puede estar vacía.")
        return value   

    def validate_id_employee_clasification(self, value):
        if not Employee_Clasification.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La clasificacion del empleado no es válida.")
        return value 


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre del empleado no puede estar vacío.")
        return value
    
    def validate_last_name(self, value):
        if not value:
            raise serializers.ValidationError("El apellipdo del empleado no puede estar vacío.")
        return value
    
    def validate_email(self, value):
        if '@' not in value:
            raise serializers.ValidationError("El correo electrónico debe contener el símbolo '@'.")
        return value

    def validate_id_position(self, value):
        if not Position.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La posición no es válida.")
        return value 
