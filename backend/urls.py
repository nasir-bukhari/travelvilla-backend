from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('routes/', include('routes.urls')),
    path('admin', admin.site.urls),

    #     path('api-auth/', include('rest_framework.urls')),
     
    #     path('api/', include('UserProfile.api.urls')),
]

urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name='index.html'))]
