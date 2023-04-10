from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView

from app.authentications.api.v1.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, \
    PasswordResetConfirmView, PasswordResetTokenVerifyView

app_name = 'authentications'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('password/change/', PasswordChangeView.as_view(), name='password_change'),
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # verify user token
    path('token/user/verify/', PasswordResetTokenVerifyView.as_view(), name='password_reset_token_verify'),

    # jwt token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
