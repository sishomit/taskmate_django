from django.urls import path
from users_app import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from users_app.forms import EmailValidationOnForgotPassword

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('reset', PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword,
                                            email_template_name='registration/password_reset_email.html'),
         {'post_reset_redirect': 'password_reset_done'}, name='reset'),
    path('password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         {'post_reset_redirect': 'reset/done'}, name='password_reset_confirm', ),
    path('password_reset_complete',
         PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete')

]
