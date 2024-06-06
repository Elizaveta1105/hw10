from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy
from . import views
from .forms import LoginForm

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


app_name = 'authenticate'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='authenticate/login.html', form_class=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(template_name='authenticate/logout.html'), name='logout'),
    path('password-reset/', PasswordResetView.as_view(template_name='authenticate/password_reset.html', email_template_name='authenticate/password_reset_email.html', success_url=reverse_lazy('authenticate:password_reset_done')), name='password-reset'),
    path('password-reset/done', PasswordResetDoneView.as_view(template_name='authenticate/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='authenticate/password_reset_confirm.html', success_url=reverse_lazy('authenticate:password_reset_complete')), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='authenticate/password_reset_complete.html'), name='password_reset_complete')
]
