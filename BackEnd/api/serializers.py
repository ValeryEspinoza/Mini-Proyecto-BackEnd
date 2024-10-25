from rest_framework import serializers
from .models import (
    Sub_Categories, Categories, Supplier_Categories, Suppliers, Products,
    Inventory, Clients, Sell_Type, Sells, Sell_Detail, Record, Reviews,
    Area, Access, Employee_Clasification, Position, Employees, Payment_Method
)


class ProductsSerializer(serializers.ModelSerializer):
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


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

    def validate_category_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre de la categoría no puede estar vacío.")
        if len(value) > 100:
            raise serializers.ValidationError("El nombre de la categoría no puede exceder 100 caracteres.")
        if Categories.objects.filter(category_name=value).exists():
            raise serializers.ValidationError("Ya existe una categoría con este nombre.")
        return value

    def validate_category_description(self, value):
        if not value:
            raise serializers.ValidationError("La descripción de la categoría no puede estar vacía.")
        return value

    def validate_id_sub_category(self, value):
        if not Sub_Categories.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La subcategoría seleccionada no es válida.")
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


class Supplier_CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier_Categories
        fields = '__all__'


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'

    def validate_supplier_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre del proveedor no puede estar vacío.")
        return value


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("La cantidad no puede ser negativa.")
        return value

    def validate_id_product(self, value):
        if not Products.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El producto seleccionado no es válido.")
        return value


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

    def validate_client_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre del cliente no puede estar vacío.")
        return value


class Sell_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell_Type
        fields = '__all__'


class Payment_MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Method
        fields = '__all__'


class SellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sells
        fields = '__all__'

    def validate_id_client(self, value):
        if not Clients.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El cliente seleccionado no es válido.")
        return value

    def validate_id_sell_type(self, value):
        if not Sell_Type.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El tipo de venta seleccionado no es válido.")
        return value


class Sell_DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell_Detail
        fields = '__all__'

    def validate_id_sell(self, value):
        if not Sells.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La venta seleccionada no es válida.")
        return value

    def validate_id_product(self, value):
        if not Products.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El producto seleccionado no es válido.")
        return value

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("La cantidad debe ser mayor que cero.")
        return value


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


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


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'


class Employee_ClasificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Clasification
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

    def validate_employee_name(self, value):
        if not value:
            raise serializers.ValidationError("El nombre del empleado no puede estar vacío.")
        return value

    def validate_id_position(self, value):
        if not Position.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La posición seleccionada no es válida.")
        return value

    def validate_id_employee_classification(self, value):
        if not Employee_Clasification.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("La clasificación de empleado seleccionada no es válida.")
        return value
