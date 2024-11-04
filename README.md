# Mini-Proyecto-BackEnd
Proyecto Grupal de Foward Costa Rica

py manage.py makemigrations
py manage.py migrate
py manage.py runserver



# Django Models

Este documento describe los modelos utilizados en la aplicación que gestionan categorías, proveedores, productos, inventarios, clientes y ventas  de una tienda deportiva.

## Modelos

### 1. Categories

 ```python

class Products(models.Model):
    id_product = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar de forma única cada producto
    product_name = models.CharField(max_length=100)  # Almacena el nombre del producto, con un límite de 100 caracteres
    product_price = models.DecimalField(max_digits=7, decimal_places=2)  # Precio del producto, con hasta 7 dígitos en total y 2 decimales
    product_description = models.TextField()  # Descripción detallada del producto, permitiendo suficiente espacio para información extensa
    id_category = models.ForeignKey(Categories, on_delete=models.CASCADE)  # Relación con la categoría del producto, lo que permite clasificar los productos
    id_suplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)  # Relación con el proveedor del producto, esencial para gestionar la cadena de suministro

    def __str__(self):
        return str(self.product_name)  # Representación del producto como cadena, facilitando la identificación en listas y formularios

# Este modelo representa los productos disponibles en el inventario del sistema. 
# Cada producto tiene un nombre, un precio y una descripción, así como relaciones con una categoría y un proveedor.
# La gestión adecuada de estos productos es fundamental para el funcionamiento de un negocio, ya que permite organizar, clasificar y mantener un seguimiento sobre el stock disponible.
# El método __str__ permite mostrar el nombre del producto al instanciarlo, facilitando su identificación en el sistema.

///////////////////////////////////////////////////////////////////////////////////////////////////////////

class Supplier_Categories(models.Model):
    id_supplier_category = models.AutoField(primary_key=True)  # Clave primaria autoincremental para la categoría del proveedor
    supplier_category_name = models.CharField(max_length=100)  # Nombre de la categoría del proveedor, con un límite de 100 caracteres
    supplier_category_description = models.TextField()  # Descripción de la categoría del proveedor, permitiendo mayor detalle

    def __str__(self):
        return str(self.supplier_category_name)  # Representación de la categoría del proveedor como cadena

# Este modelo define las categorías a las que pertenecen los proveedores. Cada categoría tiene un nombre y una descripción, lo que facilita la organización y gestión de los proveedores.
# La categorización de proveedores es esencial para identificar y agrupar a los proveedores según el tipo de productos o servicios que ofrecen, lo que mejora la eficiencia en la toma de decisiones de compra.
# El método __str__ devuelve el nombre de la categoría cuando el objeto se representa como una cadena, facilitando su identificación en listas.

///////////////////////////////////////////////////////////////////////////////////////////////////////////

class Suppliers(models.Model):
    id_supplier = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar de forma única cada proveedor
    supplier_name = models.CharField(max_length=100)  # Almacena el nombre del proveedor, con un límite de 100 caracteres
    supplier_description = models.TextField()  # Guarda una descripción detallada del proveedor, permitiendo una comprensión más clara de su oferta
    id_supplier_category = models.ForeignKey(Supplier_Categories, on_delete=models.CASCADE)  # Relación con la categoría del proveedor

    def __str__(self):
        return str(self.supplier_name)  # Representación del proveedor como cadena

# Este modelo define a los proveedores que suministran productos al sistema. Cada proveedor tiene un nombre y una descripción, así como una relación con una categoría específica.
# La gestión de proveedores es crucial para asegurar una buena cadena de suministro, permitiendo realizar un seguimiento de las condiciones de venta, calidad de productos y plazos de entrega.
# El método __str__ devuelve el nombre del proveedor para facilitar su identificación en diferentes contextos del sistema.

/////////////////////////////////////////////////////////////////////////////////////////////////////////

class Inventory(models.Model):
    id_inventory = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar de forma única cada entrada en el inventario
    inventory_description = models.TextField()  # Guarda una descripción detallada del inventario, permitiendo notas adicionales o detalles importantes
    stock = models.IntegerField()  # Cantidad de stock disponible para el producto, fundamental para la gestión de inventario
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE)  # Relación con el producto asociado, facilitando el seguimiento del stock por producto

    def __str__(self):
        return str(self.inventory_description)  # Representación del inventario como cadena

# Este modelo gestiona el inventario de productos, incluyendo la cantidad disponible para cada uno. 
# Se vincula a productos específicos para un mejor control del stock, permitiendo gestionar entradas y salidas de inventario de manera efectiva.
# Una gestión adecuada del inventario es crucial para prevenir sobrestock o faltantes, asegurando que la empresa pueda satisfacer la demanda de los clientes.
# El método __str__ muestra una descripción del inventario al instanciarlo, facilitando su identificación en informes y listados.

/////////////////////////////////////////////////////////////////////////////////////////////////////////

class Clients(models.Model):
    id_client = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar de forma única cada cliente
    client_name = models.CharField(max_length=100)  # Almacena el nombre del cliente, con un límite de 100 caracteres
    client_lastname = models.CharField(max_length=100)  # Almacena el apellido del cliente, con un límite de 100 caracteres
    client_email = models.CharField(max_length=200)  # Guarda el correo electrónico del cliente, con un límite de 200 caracteres
    register_Date = models.DateField()  # Fecha de registro del cliente, importante para el seguimiento de la relación con el cliente

    def __str__(self):
        return str(self.client_name)  # Representación del cliente como cadena

# Este modelo representa a los clientes en el sistema, almacenando su nombre, apellido y correo electrónico, así como la fecha en que se registraron.
# La información de los clientes es esencial para el marketing, el servicio al cliente y el seguimiento de las ventas, permitiendo personalizar las ofertas y mejorar la atención.
# El método __str__ devuelve el nombre del cliente para facilitar su identificación en la interfaz de usuario y en la gestión de datos.

/////////////////////////////////////////////////////////////////////////////////////////////////////////

class Sell_Type(models.Model):
    id_sell_type = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar de forma única cada tipo de venta
    type_name = models.CharField(max_length=100)  # Almacena el nombre del tipo de venta, con un límite de 100 caracteres
    type_description = models.TextField()  # Guarda una descripción detallada del tipo de venta, permitiendo aclarar su propósito y características

    def __str__(self):
        return str(self.type_name)  # Representación del tipo de venta como cadena

# Este modelo define los diferentes tipos de venta que pueden existir en el sistema, como ventas al por menor, ventas al por mayor, etc.
# Cada tipo tiene un nombre y una descripción, lo que ayuda a clasificar y organizar las transacciones en el sistema.
# Comprender las diferentes categorías de venta es crucial para el análisis de las estrategias comerciales y la optimización de los procesos de venta.
# El método __str__ devuelve el nombre del tipo de venta para facilitar su identificación y uso en la interfaz del sistema.

/////////////////////////////////////////////////////////////////////////////////////////////////////////

class Payment_Method(models.Model):
    id_payment_method = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar de forma única cada método de pago
    payment_method = models.CharField(max_length=100)  # Almacena el nombre del método de pago, con un límite de 100 caracteres
    payment_method_description = models.TextField()  # Guarda una descripción detallada del método de pago, informando sobre su uso y condiciones
    id_sell_type = models.ForeignKey(Sell_Type, on_delete=models.CASCADE)  # Relación con el tipo de venta asociado

    def __str__(self):
        return str(self.payment_method)  # Representación del método de pago como cadena

# Este modelo almacena los diferentes métodos de pago disponibles en el sistema, como efectivo, tarjeta de crédito, transferencia bancaria, etc.
# Facilita su gestión en el proceso de ventas y proporciona claridad sobre las opciones que los clientes pueden utilizar al realizar una compra.
# Entender los métodos de pago es esencial para garantizar una experiencia de compra fluida y para la gestión financiera del negocio.
# El método __str__ muestra el nombre del método de pago para facilitar su identificación en informes y registros.

/////////////////////////////////////////////////////////////////////////////////////////////////////////

class Sells(models.Model):
    id_sell = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar de forma única cada venta
    id_client = models.ForeignKey(Clients, on_delete=models.CASCADE)  # Relación con el cliente que realiza la venta

    def __str__(self):
        return str(self.id_sell)  # Representación de la venta como cadena

# Este modelo gestiona las ventas, asociando cada venta a un cliente específico. 
# Facilita el seguimiento de transacciones realizadas y permite llevar un control sobre las ventas en el sistema, proporcionando información vital para la gestión del negocio.
# La identificación clara de las ventas es fundamental para el análisis de rendimiento y la planificación estratégica.
# El método __str__ permite identificar fácilmente la venta mediante su ID, facilitando su uso en informes y consultas.

/////////////////////////////////////////////////////////////////////////////////////////////////////////

class sell_detail(models.Model):
    id_sell_detail = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar de forma única cada detalle de la venta
    sell_date = models.DateField()  # Fecha en la que se realizó la venta, importante para el historial de transacciones
    sub_total = models.DecimalField(max_digits=8, decimal_places=2)  # Subtotal de la venta, con hasta 8 dígitos y 2 decimales
    taxes = models.DecimalField(max_digits=8, decimal_places=2)  # Impuestos aplicados a la venta, con hasta 8 dígitos y 2 decimales
    total = models.DecimalField(max_digits=8, decimal_places=2)  # Total de la venta, con hasta 8 dígitos y 2 decimales
    id_sell = models.ForeignKey(Sells, on_delete=models.CASCADE)  # Relación con la venta correspondiente
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE)  # Relación con el producto vendido
    id_paymenth_method = models.ForeignKey(Payment_Method, on_delete=models.CASCADE)  # Relación con el método de pago utilizado

# Este modelo detalla cada venta, incluyendo información como la fecha de la venta, subtotal, impuestos y total.
# Se relaciona con la venta principal, el producto vendido y el método de pago utilizado, permitiendo un seguimiento exhaustivo de las transacciones.
# Los detalles de venta son cruciales para el análisis financiero, permitiendo comprender mejor el rendimiento de productos y métodos de pago.
# Este modelo contribuye a la transparencia y claridad en la contabilidad y gestión de ingresos.

/////////////////////////////////////////////////////////////////////////////////////////////////////////

class Record(models.Model):
    id_record = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar de forma única cada registro
    id_sell_detail = models.ForeignKey(sell_detail, on_delete=models.CASCADE)  # Relación con el detalle de la venta correspondiente

# Este modelo representa registros de ventas, permitiendo asociar cada registro con un detalle de venta específico.
# Facilita el seguimiento de cada transacción y ayuda a mantener un historial claro de las operaciones realizadas.
# La gestión de registros es fundamental para auditorías y para la generación de informes financieros precisos.

/////////////////////////////////////////////////////////////////////////////////////////////////////////

class Reviews(models.Model):
    id_review = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar de forma única cada revisión
    review = models.TextField()  # Texto de la revisión del producto, permitiendo comentarios extensos
    calification = models.DecimalField(max_digits=2, decimal_places=1)  # Calificación de la revisión, con hasta 2 dígitos y 1 decimal
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE)  # Relación con el producto revisado
    id_client = models.ForeignKey(Clients, on_delete=models.CASCADE)  # Relación con el cliente que realiza la revisión

# Este modelo representa las reseñas o valoraciones de los productos por parte de los clientes. 
# Permite recoger opiniones y calificaciones, lo que puede ser útil para mejorar la calidad del producto y la satisfacción del cliente.
# Cada revisión está relacionada con un producto específico y con el cliente que la realiza, facilitando el seguimiento de las opiniones y la gestión de la reputación de los productos.

/////////////////////////////////////////////////////////////////////////////////////////////////////////

class Area(models.Model):
    id_area = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar de forma única cada área
    area_name = models.CharField(max_length=100)  # Almacena el nombre del área, con un límite de 100 caracteres
    area_description = models.TextField()  # Guarda una descripción detallada del área, permitiendo mayor claridad en su propósito

    def __str__(self):
        return str(self.area_name)  # Representación del área como cadena

# Este modelo define las diferentes áreas dentro de la organización. 
# Cada área tiene un nombre y una descripción, facilitando la identificación y gestión de las distintas secciones del negocio.
# La organización por áreas es esencial para mejorar la eficiencia operativa y para establecer responsabilidades claras dentro de la empresa.
# El método __str__ permite mostrar el nombre del área al instanciarlo, facilitando su uso en diferentes contextos.

/////////////////////////////////////////////////////////////////////////////////////////////////////////

class Access(models.Model):
    id_access = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar de forma única cada acceso
    access_name = models.CharField(max_length=100)  # Almacena el nombre del acceso, con un límite de 100 caracteres
    permissions = models.TextField()  # Guarda los permisos asociados al acceso, permitiendo detallar las capacidades de los usuarios

    def __str__(self):
        return str(self.access_name)  # Representación del acceso como cadena

# Este modelo define los accesos dentro del sistema, permitiendo gestionar los permisos de los usuarios. 
# Cada acceso tiene un nombre y una descripción de los permisos asociados, facilitando la administración de la seguridad y la funcionalidad del sistema.
# La correcta gestión de accesos es crucial para proteger la información y asegurar que los usuarios tengan los permisos adecuados para realizar sus tareas.
# El método __str__ devuelve el nombre del acceso para facilitar su identificación en el sistema.

/////////////////////////////////////////////////////////////////////////////////////////////////////////

class Employee_Clasification(models.Model):
    id_employee_classification = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar de forma única cada clasificación de empleados
    employee_clasifiaction_name = models.CharField(max_length=100)  # Almacena el nombre de la clasificación de empleados, con un límite de 100 caracteres
    id_access = models.ForeignKey(Access, on_delete=models.CASCADE)  # Relación con el modelo Access
    id_area = models.ForeignKey(Area, on_delete=models.CASCADE)  # Relación con el modelo Area

    def __str__(self):
        return str(self.employee_clasifiaction_name)  # Representación de la clasificación como cadena

# Este modelo define las clasificaciones de empleados en la organización, asociando cada clasificación a un área y a sus permisos de acceso. 
# Esto facilita la gestión de recursos humanos y el control de acceso a diferentes secciones del sistema.
# Comprender las clasificaciones de empleados es esencial para la organización interna y la correcta asignación de responsabilidades y permisos dentro de la empresa.
# El método __str__ permite identificar fácilmente cada clasificación, facilitando su uso en la administración de personal.

/////////////////////////////////////////////////////////////////////////////////////////////////////////

class Employees(models.Model):
    id_employee = models.AutoField(primary_key=True)  # Clave primaria autoincremental para identificar de forma única cada empleado
    name = models.CharField(max_length=100)  # Almacena el nombre del empleado, con un límite de 100 caracteres
    last_name = models.CharField(max_length=100)  # Almacena el apellido del empleado, con un límite de 100 caracteres

    class AgeChoices(models.IntegerChoices):
        UNDER_18 = 0, "Under 18"  # Opción para empleados menores de 18 años
        BETWEEN_18_25 = 1, "18-25"  # Opción para empleados entre 18 y 25 años
        BETWEEN_26_35 = 2, "26-35"  # Opción para empleados entre 26 y 35 años
        OVER_35 = 3, "Over 35"  # Opción para empleados mayores de 35 años

    age = models.IntegerField(choices=AgeChoices.choices)  # Campo para seleccionar la edad del empleado según las opciones definidas
    email = models.CharField(max_length=100)  # Guarda el correo electrónico del empleado, con un límite de 100 caracteres

# Este modelo representa a los empleados de la organización, almacenando su nombre, apellido, edad y correo electrónico. 
# Facilita la gestión de recursos humanos al mantener un registro de cada empleado.
# La categorización de la edad de los empleados puede ser útil para análisis demográficos y para planificar políticas de empleo.
# La información de contacto es esencial para la comunicación interna y la gestión de recursos humanos.


///////////////////////////////////////JSON WEB TOKEN/////////////////////////////////////////////////////

JSON Web Tokens (JWT) para proteger las rutas privadas. Utilizamos el paquete djangorestframework-simplejwt para implementar la autenticación JWT en Django.

1. Instalar las dependencias:
Asegúrate de tener instalados los siguientes paquetes en tu entorno:


pip install djangorestframework
pip install djangorestframework-simplejwt

2. Configuración básica de JWT en Django:
En el archivo settings.py, agrega el siguiente código para configurar el JWT:


INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Opcional: Configurar tiempos de expiración de los tokens
            from datetime import timedelta
..........................
            SIMPLE_JWT = {
                'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
                'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
                'ROTATE_REFRESH_TOKENS': False,
                'BLACKLIST_AFTER_ROTATION': True,
                'ALGORITHM': 'HS256',
                'SIGNING_KEY': SECRET_KEY,  # Usa tu propia clave secreta
            }

4. Rutas para obtener y refrescar los tokens
En el proyecto hay dos archivos urls.py:
     uno en la carpeta principal del proyecto y otro en la aplicación api. Aquí es donde gestionaremos las rutas JWT.

# a. Archivo BackEnd/urls.py (archivo principal del proyecto) -->
Este archivo solo debe incluir las rutas para las aplicaciones que definas, en este caso, la aplicación api. Si no lo tienes, agrega lo siguiente:


        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('api/', include('api.urls')),  # Incluimos las rutas de la aplicación API
        ]



# b. Archivo api/urls.py (archivo específico de la aplicación)
Aquí es donde definimos las rutas específicas para obtener y refrescar los tokens JWT.

Añade las siguientes importaciones y rutas para gestionar los tokens:


        from django.urls import path
        from rest_framework_simplejwt.views import (
            TokenObtainPairView,
            TokenRefreshView,
        )

        urlpatterns = [
            # Rutas para obtener y refrescar tokens JWT
            path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtener token de acceso y refresco
            path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refrescar el token de acceso
        ]


Estas rutas permiten a los usuarios autenticarse y recibir los tokens de acceso y refresco.

5. Proteger las vistas con JWT

Ahora que hemos configurado las rutas para JWT, vamos a proteger algunas de las rutas de tu API usando el sistema de autenticación JWT.
 ejemplo:

        from rest_framework.permissions import IsAuthenticated  # Permisos para JWT
        ...
        ..
        .
        ##Suppliers
        class SuppliersListCreate(generics.ListCreateAPIView):
            queryset = Suppliers.objects.all()
            serializer_class = SuppliersSerializer
            permission_classes = [IsAuthenticated] # Solo usuarios autenticados pueden gestionar


#Acceder a una ruta protegida
En Postman, crea una nueva solicitud GET a la URL http://localhost:8000/api/productos/ (o cualquier otra ruta protegida que hayas configurado).

Ve a la pestaña Headers y añade el encabezado:

Key: Authorization
Value: Bearer <access_token>

Si el token de acceso es válido, recibirás la respuesta de la ruta protegida. Si el token no es válido o ha expirado, recibirás un error 401 Unauthorized.

# Refrescar el token de acceso
En Postman, crea una nueva solicitud POST a la URL http://localhost:8000/api/token/refresh/.

En el cuerpo de la solicitud, selecciona x-www-form-urlencoded y añade el siguiente parámetro:

refresh: El token de refresco que recibiste al autenticarte.
El servidor te devolverá un nuevo token de acceso que puedes usar para seguir accediendo a las rutas protegidas.


SUPER USUARIO:
Para administrar la aplicación y tener acceso completo al panel de administración de Django, necesitamos crear un superusuario. El superusuario tiene permisos completos para realizar cualquier operación dentro de la aplicación y es esencial para la configuración inicial.

Pasos para Crear un Superusuario
Asegúrate de que el servidor de desarrollo está detenido (si está corriendo) y abre una terminal en el directorio raíz del proyecto, donde se encuentra el archivo manage.py.

Ejecuta el Comando de Creación de Superusuario:

En la terminal, escribe el siguiente comando:


#     python manage.py createsuperuser


Completa la Información Solicitada:

Django te pedirá que ingreses la información del superusuario. Completa los campos con la siguiente información:

Username: Nombre de usuario del superusuario (esto es lo que usarás para iniciar sesión en el panel de administración).
Email: Dirección de correo electrónico del superusuario (opcional, pero recomendado).
Password: Contraseña segura para el superusuario.
Django solicitará que confirmes la contraseña para asegurar que esté correctamente ingresada.

Confirmación de Creación:

Si todos los datos se ingresaron correctamente, verás un mensaje en la terminal indicando que el superusuario se ha creado exitosamente. Esto permite al superusuario iniciar sesión en el panel de administración de Django.

Acceso al Panel de Administración
Inicia el servidor de desarrollo:

#     python manage.py runserver

Accede al Panel de Administración:

Abre tu navegador y ve a http://127.0.0.1:8000/admin. Allí verás la pantalla de inicio de sesión del panel de administración de Django.

Inicia Sesión:

Ingresa el nombre de usuario y la contraseña del superusuario que acabas de crear. Al iniciar sesión, tendrás acceso completo a todas las secciones del panel de administración, desde donde podrás gestionar usuarios, modelos y otros datos de la aplicación.



//////////////////// Prevención de ataques comunes/////////////////////////////////////////////////////

SQL injection: Por lo general, ocurre cuando le pide a un usuario una entrada, como su nombre de usuario/ID de usuario, y en lugar de un nombre/ID, el usuario le da una instrucción SQL, qu8e se ejecutará en tu base de datos. Con este tipo de ataques se busca acceder a la base de datos y obtener permisos de administrador, lo que se busca generalmente es causar daño a la empresa/organizacion y/o el robo de datos sensibles.

Usando lo que se conoce como OR payload, que es una sentencia sql con el siguiente formato: 
SELECT * FROM Users WHERE UserId = 105 OR 1=1;  ya que 1 = 1 es siempre verdadero, nos retornará toda la informacion dentro de la tabla Users, obteniendo acceso a nuestro sistema. 

Aplicación de medidas de seguridad en nuestro proyecto: 
1. El ORM de Django utiliza automáticamente consultas parametrizadas, lo que ayuda a prevenir la inyección de SQL. Utilizamos siempre los métodos ORM para las operaciones de base de datos en lugar de escribir consultas SQL sin procesar.

2. Validación de entradas: Nos aseguramos de validar todas las entradas de usuario, en los modelos, los serializers y en cualquier punto donde se procesan los datos de usuario.

3. Sanitización de datos: Utiliza funciones de sanitización para limpiar cualquier dato de entrada antes de procesarlo.

4. Con la implementación de roles, nos aseguramos de otorgar privilegios mínimos, otorgando al usuario unicamente los permisos necesarios para realizar sus tareas de acuerdo a su rol.

5. Django proporciona varias funciones de seguridad integradas, como la protección CSRF, que ayuda a prevenir ciertos tipos de ataques. Asegúrese de que estas funciones estén habilitadas y configuradas correctamente.


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Cross-Site Scripting (XSS): es un tipo de vulnerabilidad de seguridad que se encuentra en las aplicaciones web. Permite a los atacantes inyectar scripts maliciosos del lado del cliente en páginas web vistas por otros usuarios. Esto puede dar lugar a acciones no autorizadas, robo de datos y otras actividades maliciosas.

1.Para sanitizar las entradas de usuarios podemos implementar la biblioteca bleach en Python para sanitizar HTML y asi eliminar cualquier código potencialmente peligroso.

a: pip install bleach django-bleach
b: Vamos al archivo de settings.py y agregamos el django_bleach app.
 INSTALLED_APPS = [
    # ...
    'django_bleach',
    # ...
]

c: tambien en el archivo de settings.py

BLEACH_ALLOWED_TAGS = ['p', 'b', 'i', 'u', 'em', 'strong', 'a']
BLEACH_ALLOWED_ATTRIBUTES = ['href', 'title', 'style']
BLEACH_ALLOWED_STYLES = ['font-family', 'font-weight', 'text-decoration', 'font-variant']
BLEACH_STRIP_TAGS = True
BLEACH_STRIP_COMMENTS = False

d: Creamos nuestros modelos utilizando los BleachField en lugar de los textfield
from django_bleach.models import BleachField

class Producto(models.Model):
    safe_name = BleachField(max_length=255)
    safe_description = BleachField()


2. Codificación de HTML: Antes de mostrar datos en la interfaz, codifica los caracteres especiales en HTML. Esto evita que el navegador interprete las entradas del usuario como código ejecutable.

3. Uso de una Biblioteca Segura: Utiliza bibliotecas de plantillas del lado del cliente que manejen la codificación de manera segura, como React o Angular, que tienen mecanismos integrados para prevenir XSS.



//////////////////////////////////Cross-Site Request Forgery/////////////////////////////////////////////////
Los ataques de falsificación de solicitudes entre sitios (CSRF) son vulnerabilidades comunes de aplicaciones web que se aprovechan de la confianza que un sitio web ya ha otorgado a un usuario y su navegador. En un ataque CSRF, un atacante suele utilizar técnicas de ingeniería social para manipular a un usuario autenticado para que ejecute acciones maliciosas sin su conocimiento o consentimiento. CSRF también se conoce por varios otros nombres, incluidos XSRF, «surf en el mar», sesión de equitación, falsificación de referencias entre sitios y enlaces hostiles. 

Para la prevención de estos ataques podemos utilizar los tokens CSRF:

Un token CSRF es un valor secreto único e impredecible generado por una aplicación del lado del servidor y enviado al cliente para su inclusión en las solicitudes HTTP posteriores emitidas por el cliente. Después de que se emite el token, cuando el cliente realiza una solicitud, el servidor comprueba si la solicitud contiene el token esperado y lo rechaza si el token falta o no es válido.

Asegurarnos de que el middleware CSRF este activo en tu archivo settings.py.
Activar el Middleware CSRF: Django tiene el middleware CSRF activado por defecto. Asegúrate de que ...

MIDDLEWARE = [
    ...................
    'django.middleware.csrf.CsrfViewMiddleware' 
    ...................
]

Las demás configuraciones se realizan en el front-end. Se le debe añadir la etiqueta  <CSRFToken /> a los forms para que se adjunte el token en el form y este se refresca cada vez que realiza la acción. 

m m

### Grupos y Permisos en Django

Django cuenta con un robusto sistema de gestión de usuarios que incluye la capacidad de crear grupos y definir permisos. Esto permite controlar qué acciones puede realizar cada usuario en la aplicación.

**Pasos para gestionar grupos y permisos:**

1. **Crear grupos:** Se pueden crear grupos desde el panel de administración de Django o mediante código. Cada grupo puede tener varios permisos asociados.

2. **Asignar permisos a grupos:** Una vez creado un grupo, puedes asignarle permisos específicos que controlan el acceso a diversas funcionalidades de la aplicación.

3. **Asignar usuarios a grupos:** Se le creo un espacion donde se digitará el role y que a su vez realiza la insercion de los datos en la tabla intermedia entre usuario y grupo con su permiso que es propia de Django. 

4. **Verificación de permisos en vistas:** Al desarrollar las vistas, puedes usar clases de permisos para asegurarte de que solo los usuarios con los permisos adecuados puedan acceder a determinadas funcionalidades.


