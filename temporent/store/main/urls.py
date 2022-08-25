from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('contact/', Message.as_view(), name='Contact'),
    path('dashboard_1/', Dashboardconfirm.as_view(), name='dashboard1'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', Login.as_view(), name='Login'),
    path('about/', About.as_view(), name='about'),
    path('borrow/', Borrow.as_view(), name='borrow'),
    path('search/', search, name='search'),
    path('product_details/<id>', ProductDetailView.as_view(), name="product"),
    
]
