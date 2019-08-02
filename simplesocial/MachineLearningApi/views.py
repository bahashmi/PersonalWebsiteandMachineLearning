from django.shortcuts import render
from django.views.generic import View
from MachineLearningApi.models import CSVFile
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EventsForm
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
import pandas as pd
import numpy as np
# Create your views here.

def partition(Xparam,Tparam,nfraction,shuffle):
	nRows = Xparam.shape[0]
	rows = np.arange(nRows)
	if shuffle == True:
		np.random.shuffle(rows)

	nTrain = int(nRows* nfraction )
	trainRows = rows[:nTrain]
	testRows = rows[nTrain:]
	Xtrain, Ttrain = Xparam[trainRows,:], Tparam[trainRows, :]
	Xtest, Ttest  = Xparam[testRows, :], Tparam[testRows,:]
	return Xtrain,Ttrain, Xtest, Ttest

def PreprocessPage(request):
	data = pd.read_csv('media/4cols.csv')
	print(data.shape)
	data_html = data.to_html()
	f = open('media/4cols.csv',"r")
	header = f.readline()
	print(header)
	names = header.strip().split(',')
	names = [i.replace('"','') for i in names]
	filedata = np.loadtxt(f,delimiter=",")
	print(names)
	print(filedata)
	# df = pd.DataFrame(data=filedata.flatten())
	# filedataht =pd.DataFrame(data=filedata,index=pd.RangeIndex(range(1, 4)),columns=pd.RangeIndex(range(1, 3)))
	# filedatahtml = filedataht
	# filedata_html = filedata.to_html()
	df = pd.read_csv('media/4cols.csv',skiprows=1)
	dfcolumnvalues = pd.read_csv('media/4cols.csv')
	print('dfcolumnvalues[[lights]] ',dfcolumnvalues[['lights']])
	filedf = dfcolumnvalues[['lights']].to_html
	# print("df latest ",df.to_html)
	# print(dfcolumnvalues.loc[:,'lights']) # column values
	# dfcolumnvalues.loc[:,'lights'].to_html 
	# print(filedf[:,0:1]) need to learn dataframe indexing
    #splitting data into test and train 
	
	targetvalues = dfcolumnvalues[['lights']].values
	inputvalues = dfcolumnvalues[['Appliances','T1','RH_1']].values
	print("T: ", targetvalues[:1])
	print("X: ",inputvalues[1:])
	Xtrain,Ttrain, Xtest, Ttest = partition(inputvalues,targetvalues,0.8,True)
	print("Xtrain: ",Xtrain)
	dfXtrain = pd.DataFrame(Xtrain) 
	print("Ttrain: ",Ttrain)
	dfTtrain = pd.DataFrame(Ttrain)
	print("Xtest: ",Xtest)
	dfXtest = pd.DataFrame(Xtest)
	print("Ttest: ",Ttest)
	dfTtest = pd.DataFrame(Ttest)
	return render(request, 'preprocess.html', {'loaded_data': data_html,'filedatahtml':filedf,'Xtrain':dfXtrain.to_html,'Ttrain':dfTtrain.to_html,'Xtest':dfXtest.to_html,'Ttest':dfTtest.to_html})
	# return render(request,"preprocess.html")
	# data_html = data.to_html()
# 	context = {'loaded_data': data_html}
    # return render(request, 'preprocess.html',{'loaded_data': data_html})
# return render(request, "dataflow/table.html", context)

def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "thanks.html", data)
    # if not GET, then proceed

	csv_file = request.FILES["csv_file"]
	fs = FileSystemStorage(location='media')
	filename = fs.save(csv_file.name,csv_file)
	print("uploaded file in upload_csv ",csv_file.name)

	if not csv_file.name.endswith('.csv'):
		messages.error(request,'File is not CSV type')
		return HttpResponseRedirect(reverse("thanks.html"))
    #if file is too large, return
	# if csv_file.multiple_chunks():
	# 	# messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
	# 	return HttpResponseRedirect(reverse("MachineLearningApi:upload_csv"))
    
	
	file_data = csv_file.read().decode("utf-8")

	lines = file_data.split("\n")
	#loop over the lines and save them in db. If error , store as string and then display

	for line in lines:
		print("line: ", line)
		if len(line) == 0:
			break
		if line != lines[0]:
			fields = line.split(",")
			print(" 0",fields[0])
			b = CSVFile(Appliances=fields[0])
			print(" 1",fields[1])
			b = CSVFile(lights=fields[1])
			print(" 2",fields[2])
			b = CSVFile(T1=fields[2])
			print(" 3",fields[3])
			b = CSVFile(RH_1=fields[3])
			b = CSVFile(name='Beatles Blog')
			b.save()
	return HttpResponseRedirect(reverse("MachineLearningApi:upload_csv"))


def upload(request):
	if request.method == 'POST':
		uploaded_file = request.FILES['myfile']
		print( " the uploaded file ",uploaded_file.name)
	return render(request,"thanks.html")


class DataImportFile(View):

    def get(self, request, *args, **kwargs):
        print("dhgdey")
        return render(request,"thanks.html")

    def get_redirect_url(self, *args, **kwargs):
        return reverse("simplesocial:home")
    
    def PreprocessData(request):
        print("helli")
        data = {}
        if "GET" == request.method:
            print('here')
        return render(request, "thanks.html", "hrgeu")
        print(" preprocessing")
        # all_entries= CSVFile.objects.filter(Appliances='60')
        # Entry.objects.all().delete()
        enteries =CSVFile.objects.values_list('RH_1', flat=True)
        CSVFile.objects.all().delete()
        all_entries1 = CSVFile.objects.all()
        print("all enteries ",enteries)
        return HttpResponseRedirect(reverse("MachineLearningApi:PreprocessData"))
