from django.urls import path
from . import views


app_name = 'MachineLearningApi'

urlpatterns = [
path('ImportData/', views.DataImportFile.as_view(), name="importDatafile"),
path(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
]
