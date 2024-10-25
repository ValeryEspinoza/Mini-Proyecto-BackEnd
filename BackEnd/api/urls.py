from django.urls import path
from . import views
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns = [
    # Rutas de Sub_Categories
    path('subcategories/', views.Sub_CategoriesListCreate.as_view(), name='sub_categories-list'),
    path('subcategories/<int:pk>/', views.Sub_CategoriesDetail.as_view(), name='sub_categories-detail'),
    
    # Rutas de productos
    path('categories/', views.CategoriesListCreate.as_view(), name='categories-list'),
    path('categories/<int:pk>/', views.CategoriesDetail.as_view(), name='categories-detail'),
    
    #Supplier_Categories
    path('suppliercategories/', views.Supplier_CategoriesListCreate.as_view(), name='supplier_categories-list'),
    path('suppliercategories/<int:pk>/', views.Supplier_CategoriesDetail.as_view(), name='supplier_categories-detail'),
    
    #Suppliers
    path('suppliers/', views.SuppliersListCreate.as_view(), name='suppliers-list'),
    path('suppliers/<int:pk>/', views.SuppliersDetail.as_view(), name='suppliers-detail'),
    
    #Products
    path('products/', views.ProductsListCreate.as_view(), name='products-list'),
    path('Products/<int:pk>/', views.ProductsDetail.as_view(), name='products-detail'),  
    
    #Inventory
    path('inventory/', views.InventoryListCreate.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', views.InventoryDetail.as_view(), name='inventory-detail'),
    
    #Clients
    path('clients/', views.ClientsListCreate.as_view(), name='clients-list'),
    path('clients/<int:pk>/', views.ClientsDetail.as_view(), name='clients-detail'),
    
    #Sell_Type
    path('selltype/', views.Sell_TypeListCreate.as_view(), name='Sell_Type-list'),
    path('selltype/<int:pk>/', views.Sell_TypeDetail.as_view(), name='Sell_Type-detail'),  
    
    #Payment_Method
    path('paymentmethod/', views. Payment_MethodListCreate.as_view(), name='payment_method-list'),
    path('paymentmethod/<int:pk>/', views. Payment_MethodDetail.as_view(), name='payment_method-detail'),
    
    #Sells
    path('sells/', views. SellsListCreate.as_view(), name='sells-list'),
    path('sells/<int:pk>/', views.SellsDetail.as_view(), name='sells-detail'),
    
    #Sells_Detail
    path(' selldetail/', views. Sell_DetailListCreate.as_view(), name='sell_Detail-list'),
    path(' selldetail/<int:pk>/', views.Sell_DetailDetail.as_view(), name='sell_Detail-detail'),
    
    #Record
    path('record/', views.RecordListCreate.as_view(), name='record-list'),
    path('record/<int:pk>/', views.RecordDetail.as_view(), name='record-detail'),
   
    #Review
    path('review/', views.ReviewsListCreate.as_view(), name='review-list'),
    path('review/<int:pk>/', views.ReviewsDetail.as_view(), name='review-detail'), 
    
    #Area
    path('area/', views.AreaListCreate.as_view(), name='area-list'),
    path('area/<int:pk>/', views.AreaDetail.as_view(), name='area-detail'), 
    
    #Access
    path('access/', views.AccessListCreate.as_view(), name='access-list'),
    path('access/<int:pk>/', views.AccessDetail.as_view(), name='access-detail'),
    
    #Employee_Clasification
    path('employeeclasification/', views.Employee_ClasificationListCreate.as_view(), name='Employee_Clasification-list'),
    path('employeeclasification/<int:pk>/', views.Employee_ClasificationDetail.as_view(), name='Employee_Clasification-detail'),  
    
    #Position
    path('position/', views.PositionListCreate.as_view(), name='Position-list'),
    path('position/<int:pk>/', views.PositionDetail.as_view(), name='Position-detail'),  
    
    #Employees
    path('employees/', views.EmployeesListCreate.as_view(), name='employees-list'),
    path('employees/<int:pk>/', views.EmployeesDetail.as_view(), name='employees-detail'),  




]