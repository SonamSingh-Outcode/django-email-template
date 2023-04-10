"""
v1 API url for swagger view
"""
from django.urls import include, path

app_name = 'v1-apis'

urlpatterns = [
    path('', include('core.urls')),
    path('auth/', include('app.authentications.api.v1.urls', namespace='authentications')),
    path('users/', include('app.users.api.v1.urls', namespace='users'))
]
