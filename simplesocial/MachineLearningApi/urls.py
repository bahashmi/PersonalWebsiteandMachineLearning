from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'MachineLearningApi'

urlpatterns = [
path('ImportData/', views.DataImportFile.as_view(), name="importDatafile"),
path(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
path('MachineLearningApi/preprocess/', views.PreprocessPage, name='preprocess'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)