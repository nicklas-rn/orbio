from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('developer/', views.developer, name='developer'),
    path('developer_moveSteppers/', views.developer_moveSteppers, name='developer_moveSteppers'),
    path('developer_setHeaters/', views.developer_setHeaters, name='developer_setHeaters'),

    path('move_element/', views.move_element, name='move_element'),
    path('home_elements/', views.home_elements, name='home_elements'),

    path('read_temps/', views.read_temps, name='read_temps'),
    path('set_temps/', views.set_temps, name='set_temps'),


    path('production/', views.production, name='production'),
    path('pcr_run/', views.pcr_run, name='pcr_run'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)