from django.urls import path
from . import views

urlpatterns=[
    path('',views.addshow,name='addshow'),
    path('display',views.display,name='display'),
    path('delete/<int:id>/',views.delete_data,name='delete'),
    path('updatedata/<int:id>/',views.update_data,name='updatedata')
]