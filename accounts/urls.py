from django.urls import path
from .import views
# from bus.models import 'view'

urlpatterns = [
    path('register/', views.register, name='register'), #register_url
    path('login/', views.login, name='login'),#login_url
    path('logout/', views.logout, name='logout'), #logout_url
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),  #registration activate
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'), #forgot password
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),#resetpassword activate
    path('resetpassword/', views.resetpassword, name='resetpassword'),
    # path('dashboard/', views.dashboard, name='dashboard'),#dashboard link
    # path('')
    # path('',views.dashboard, name='dashboard'),
]