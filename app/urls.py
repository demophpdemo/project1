from django.urls import path
from . import views
app_name = 'app'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
