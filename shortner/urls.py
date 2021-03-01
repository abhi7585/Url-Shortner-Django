from django.urls import path
from . views import home, final

app_name = 'shortner'

urlpatterns = [
    path('', home, name='home'),
    path('<str:pk>', final, name='final')
]