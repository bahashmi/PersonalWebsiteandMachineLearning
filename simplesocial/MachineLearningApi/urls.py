from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'MachineLearningApi'

urlpatterns = [
path('display/', views.userDetails),
path('ImportData/', views.DataImportFile.as_view(), name="importDatafile"),
path(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
path('MachineLearningApi/preprocess/', views.PreprocessPage, name='preprocess'),
path('MachineLearningApi/preprocess/display/', views.userDetails,name='display'),
path('MachineLearningApi/preprocess/partitiondata/',views.partitiondata,name='partitiondata'),
path('MachineLearningApi/preprocess/partitiondata/CreateModel/',views.CreateModel,name='CreateModel'),
path('MachineLearningApi/preprocess/partitiondata/CreateModel/display/', views.userDetails,name='userDetails'),
path('MachineLearningApi/preprocess/partitiondata/CreateModel/display/userdetails/', views.userDetails,name='display'),
path('MachineLearningApi/preprocess/partitiondata/CreateModel/display/userdetails/datacleaning', views.Datacleaning,name='datacleaning'),
path('MachineLearningApi/preprocess/partitiondata/CreateModel/display/userdetails/datacleaning/datacleaninglatest', views.Datacleaning,name='datacleaned'),
path('MachineLearningApi/preprocess/partitiondata/CreateModel/display/userdetails/datacleaning/datacleaninglatest/replaceValues', views.replaceValues,name='replaceValues'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)