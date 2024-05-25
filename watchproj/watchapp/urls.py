from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('',views.Home,name='home'),
    path('bicycle/',views.product,name='product'),
    path('<slug:c_slug>/',views.product,name='product_by_category'),
    path('<slug:c_slug>/',views.Home,name='product_by_category'),
    path('details/<int:id>',views.Details,name='details'),

]


