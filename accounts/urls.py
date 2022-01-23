from atexit import register
from django.urls import path
from .views import register, login, logout, activate, dashboard, forgotPassword, resetPassword_validate, resetPassword
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', dashboard, name='dashboard'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('forgotPassword/', forgotPassword, name='forgotPassword'),
    path('resetPassword_validate/<uidb64>/<token>/',
         resetPassword_validate, name='resetPassword_validate'),
    path('resetPassword/',
         resetPassword, name='resetPassword'),

]
