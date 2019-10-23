from django.contrib import admin
from django.urls import path, include

from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'Houses API'
API_DESCRIPTION = 'A Web API for houses'
schema_view = get_swagger_view(title=API_TITLE)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('docs/', include_docs_urls(title=API_TITLE,description=API_DESCRIPTION)),
    path('swagger-docs/', schema_view),
]
