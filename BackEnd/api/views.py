# Create your views here.

##Models
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated  # Permisos para JWT

from .models import Sub_Categories
from .models import Categories
from .models import Supplier_Categories
from .models import Suppliers
from .models import Products
from .models import Inventory
from .models import Clients
from .models import Sell_Type
from .models import Payment_Method
from .models import Sells
from .models import Sell_Detail
from .models import Record
from .models import Reviews
from .models import Area
from .models import Access
from .models import Employee_Clasification
from .models import Position
from .models import Employees

##Serializers
from .serializers import Sub_CategoriesSerializer
from .serializers import CategoriesSerializer
from .serializers import Supplier_CategoriesSerializer
from .serializers import SuppliersSerializer
from .serializers import ProductsSerializer
from .serializers import InventorySerializer
from .serializers import ClientsSerializer
from .serializers import Sell_TypeSerializer
from .serializers import Payment_MethodSerializer
from .serializers import SellsSerializer
from .serializers import Sell_DetailSerializer
from .serializers import RecordSerializer
from .serializers import ReviewsSerializer
from .serializers import AreaSerializer
from .serializers import AccessSerializer
from .serializers import Employee_ClasificationSerializer
from .serializers import PositionSerializer
from .serializers import EmployeesSerializer

# VIEWS #

##SubCategories
class Sub_CategoriesListCreate(generics.ListCreateAPIView):
    queryset = Sub_Categories.objects.all()
    serializer_class = Sub_CategoriesSerializer
    
class Sub_CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sub_Categories.objects.all()
    serializer_class = Sub_CategoriesSerializer
    
##Categories
class CategoriesListCreate(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    
class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


##Supplier_Categories
class Supplier_CategoriesListCreate(generics.ListCreateAPIView):
    queryset = Supplier_Categories.objects.all()
    serializer_class = Supplier_CategoriesSerializer
    
class Supplier_CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier_Categories.objects.all()
    serializer_class = Supplier_CategoriesSerializer

##Suppliers
class SuppliersListCreate(generics.ListCreateAPIView):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden gestionar proveedores

class SuppliersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden ver los detalles de proveedores

##Products
class ProductsListCreate(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

##Inventory 
class InventoryListCreate(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden gestionar el inventario

class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden ver los detalles del inventario

##Clients
class ClientsListCreate(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    
class ClientsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    
##Sell_Type
class Sell_TypeListCreate(generics.ListCreateAPIView):
    queryset = Sell_Type.objects.all()
    serializer_class = Sell_TypeSerializer
    
class Sell_TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sell_Type.objects.all()
    serializer_class = Sell_TypeSerializer

##Payment_Method
class Payment_MethodListCreate(generics.ListCreateAPIView):
    queryset = Payment_Method.objects.all()
    serializer_class = Payment_MethodSerializer
    
class Payment_MethodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment_Method.objects.all()
    serializer_class = Payment_MethodSerializer
    
##Sells
class SellsListCreate(generics.ListCreateAPIView):
    queryset = Sells.objects.all()
    serializer_class = SellsSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden gestionar las ventas

class SellsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sells.objects.all()
    serializer_class = SellsSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden ver los detalles de ventas

##Sell_Detail
class Sell_DetailListCreate(generics.ListCreateAPIView):
    queryset = Sell_Detail.objects.all()
    serializer_class = Sell_DetailSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden gestionar detalles de ventas

class Sell_DetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sell_Detail.objects.all()
    serializer_class = Sell_DetailSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden ver los detalles de ventas

##Records
class RecordListCreate(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden gestionar el historial de ventas

class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden ver los detalles del historial de ventas

##Reviews  
class ReviewsListCreate(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    
class ReviewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

##Area
class AreaListCreate(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    
class AreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

##Access
class AccessListCreate(generics.ListCreateAPIView):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden gestionar los accesos de empleados

class AccessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden ver los detalles de accesos

##Employee_Clasification
class Employee_ClasificationListCreate(generics.ListCreateAPIView):
    queryset = Employee_Clasification.objects.all()
    serializer_class = Employee_ClasificationSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden gestionar clasificaciones de empleados

class Employee_ClasificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee_Clasification.objects.all()
    serializer_class = Employee_ClasificationSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden ver los detalles de las clasificaciones

##Postion 
class PositionListCreate(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden gestionar los puestos de trabajo

class PositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden ver los detalles de los puestos

##Employees
class EmployeesListCreate(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden gestionar empleados

class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden ver los detalles de los empleados

