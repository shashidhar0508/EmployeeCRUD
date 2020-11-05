from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showallemployees, name="showallemployees"),
    path('Insert', views.Insertemp, name="Insertemp"),
    path('delete/<str:id>', views.delete, name="delete"),
    path('edit/<str:id>', views.edit, name="edit"),
    path('edit/update/<str:id>', views.update, name="update"),
]
