from django.urls import path
from . import views

urlpatterns = [
    path('fun/',views.fun,name='fun'),
    path('delete/<id>',views.delete,name='delete'),
    path('edit/<id>',views.edit,name='edit'),
    path('',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('veg/',views.veg,name='veg'),
    path('nonveg/',views.nonveg,name='nonveg'),
    path('item/',views.item,name='item'),
    path('tiffen/',views.tiffen,name='tiffen'),
    path('chai/',views.chai,name='chai'),
    path('signout',views.signout,name='signout'),
    path('teaorder',views.teaorder,name='teaorder'),
    path("sample/",views.sample),
]
