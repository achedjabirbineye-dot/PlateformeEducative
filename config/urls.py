from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views # <--- Nouvel import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    
    # Routes pour le login et le logout
    path('connexion/', auth_views.LoginView.as_view(template_name='core/connexion.html'), name='login'),
    path('deconnexion/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)