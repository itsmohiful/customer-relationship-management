from django.urls import path
from . import views


urlpatterns = [

    path('',views.home,name='home'),
    path('products/',views.products,name='product'),
    path('customers/<str:pk_test>',views.customers,name='customer'),
    path('create_order_inline/<str:pk>',views.createorderinlineset,name='create_order_inline'),
    path('create_order/',views.createorder,name='create_order'),
    path('update_order/<str:pk>',views.updateorder,name='update_order'),
    path('delete_order/<str:pk>',views.deleteorder,name='delete_order'),

    #register & login
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

]
