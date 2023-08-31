from.import views
from django.urls import path
app_name='Cstoreapp'
urlpatterns = [
    path('',views.dept,name='dept'),
    path('login/',views.Login,name='login'),
    path('register',views.register,name='register'),
    path('shop',views.shop,name='shop',),
    path('order/',views.order,name='order',),
    path('status/',views.status,name='status')
    ]
