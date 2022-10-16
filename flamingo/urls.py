from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('flamingo_store.urls')),
    path('api/', include('flamingo_api.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
