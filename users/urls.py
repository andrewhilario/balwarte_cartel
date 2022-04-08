
from django.urls import path, reverse_lazy
from django.conf import settings
from . import views 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



app_name = 'users'
urlpatterns = [

    path('register/', views.register, name='register'),
    path('login', views.login_form, name='login'),
    path('logout', views.logout_user, name='logout'),

    path('forgot-password', views.forgot_password, name='forgot_password'),
    path('change-password/<token>', views.change_password, name='change_password'),


    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout , name='checkout'),
    path('update-item', views.updateItem , name='update_item'),
    path('process-order', views.processOrder, name='process-order')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)