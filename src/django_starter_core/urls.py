from django.urls import path, include

urlpatterns = [
    path('', include('django_starter_core.contrib.guide.urls')),
    path('about/', include('django_starter_core.contrib.about.urls')),
    path('docs/', include('django_starter_core.contrib.docs.urls')),
    path('notifications/', include('django_starter_core.contrib.notifications.urls')),
    path('admin/', include('django_starter_core.contrib.admin.urls')),
]
