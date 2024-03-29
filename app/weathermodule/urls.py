from django.urls import path,include
from app.weathermodule import views

urlpatterns = [

    path('',views.index,name='index'),
    path ("api/trigger/",views.trigger,name ="app-trigger"),
]