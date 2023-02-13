from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('footer/', footer),
    path('about_us/', about_us),
    path('add_subscription/', add_subscription),
    path('service/', service_page),
    path('contact/', contact_us),
    path('send/', send_email),
    path('visitors/', statistics)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header  =  "BengalTroops Administration"  
admin.site.site_title  =  "Bengaltroops Admin"
admin.site.index_title  =  "Bengaltroops Admin"