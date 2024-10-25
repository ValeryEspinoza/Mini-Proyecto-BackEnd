# Mini-Proyecto-BackEnd
Proyecto Grupal de Foward Costa Rica


py manage.py makemigrations
py manage.py migrate
py manage.py runserver




# BYRON 



# SEBAS

JSON Web Tokens (JWT) para proteger las rutas privadas.Utilizamos el paquete djangorestframework-simplejwt para implementar la autenticación JWT en Django.

1. Instalar las dependencias:
Asegúrate de tener instalados los siguientes paquetes en tu entorno:


pip install djangorestframework
pip install djangorestframework-simplejwt

2. Configuración básica del JWT en Django:
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

python
Copiar código
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