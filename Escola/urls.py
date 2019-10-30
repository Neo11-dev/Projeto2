from django.contrib import admin
from django.urls import path
from cursos.views import home
from professor.views import home
from turma.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cursos/',home),
    path('professor/',home),
    path('turma/', home),
]
