from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    #     path('api-auth/', include('rest_framework.urls')),
    #     path('admin/', admin.site.urls),
    #     path('api/', include('UserProfile.api.urls')),
]

urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name='index.html'))]
