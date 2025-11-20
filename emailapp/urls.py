from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('detail/<int:id>',views.detail_email,name='detail_email'),
    path('search/',views.search_email,name='search_email'),
    path('delete/<int:id>',views.delete_email,name='delete_email'),
    path('add/', views.add_email, name='add_email')   
]