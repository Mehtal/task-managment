from django.contrib import admin
from django.urls import path, include
from taskmanagment import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/doc', include('django.contrib.admindocs.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('taskmanagment.api.urls')),
    #path('', views.dashboard),
    path('', include('taskmanagment.urls', namespace="task")),
    path('stock/', include('stock.urls', namespace="stock")),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
