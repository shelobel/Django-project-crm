from django.urls import path
from . import views

from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', views.registerPage,name = "register"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),

    path('',views.home, name = "home"),

    path('user/',views.userPage, name = "user-page"),

    path('account/', views.accountSettings, name = "account"),
    path('products/',views.products, name = "products"),
    path('customer/<str:primaryKey>/',views.customer, name = "customer"),
    path('create_order/<str:primaryKey>/', views.createOrder, name ="create_order" ),
    path('update_order/<str:primaryKey>/', views.updateOrder, name ="update_order" ),
    path('delete_order/<str:primaryKey>/', views.deleteOrder, name ="delete_order" ),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "accounts/password_reset.html"), name = "reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "accounts/password_reset_sent.html"), name = "password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_confirm.html"), name = "password_reset_confirm"),
    # check out documentation for kwargs
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_done.html"), name = "password_reset_complete"),
]




# password recovery system for nonstaff
# 1. submit email form                          //PasswordResetView.as_view()
# 2. email sent success msg                     //PasswordResetDoneView.as_view()
# 3. link to password reset in email            //PasswordResetConfirmView.as_view()
# 4. password changed message                   //PasswordResetCompleteView.as_view()