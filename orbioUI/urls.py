from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('developer/', views.developer, name='developer'),

    path('move_element/', views.move_element, name='move_element'),
    path('home_elements/', views.home_elements, name='home_elements'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)