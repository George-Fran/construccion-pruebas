from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar/', views.register, name='register'),
    path('ingresar/', LoginView.as_view(template_name='bindev/login.html'), name='login'),
    path('salir/', LogoutView.as_view(), name='logout'),
    path('eliminar/<int:post_id>', views.delete, name='delete'),
    path('perfil/<str:username>', views.profile, name='profile'),
    path('editar/', views.editar, name='editar'),
    path('seguir/<str:username>/', views.seguir, name='seguir'),
    path('dejardeseguir/<str:username>/', views.dejardeseguir, name='dejardeseguir'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)