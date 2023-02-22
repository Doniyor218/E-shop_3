from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('my basket', views.mybasket, name='my basket'),
    path('new product', views.newproduct, name='new product')
]

from .views import upload_resume
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('upload_resume/',upload_resume, name = "files" )
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('files.urls'))
]

from django.urls import path
from .views import upload_resume


urlpatterns = [
    path('upload_resume/',upload_resume, name = "files" )
]