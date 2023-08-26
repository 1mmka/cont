from msilib.schema import ListView
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import ImgCreate
from main.views import ImgList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ImgCreate.as_view(),name='create_view'),
    path('list/',ImgList.as_view(),name='list_view')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
