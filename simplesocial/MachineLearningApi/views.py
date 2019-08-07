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
from matplotlib import pylab
import matplotlib.pyplot as plt
import mpld3 as mpld3
import jinja2 as jinja2
import json
import codecs
from bokeh.plotting import figure,output_file,show
from bokeh.embed import components,file_html
from bokeh.resources import CDN
from collections import Iterable
from django.contrib import messages


# from pylab import *
# import PIL, PIL.Image, StringIO
# Create your views here.

# def get_name(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('thanks.html')
#     else:
#         form = PostForm()
#     return render(request, 'thanks.html', {'form': form})


from .forms import UserModelForm

def userDetails(request):

    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():

            u = form.save()
            users = UserDetails.objects.all()

            return render(request, 'display.html', {'users': users})

            

    else:
        form_class = UserModelForm

    return render(request, 'display.html', {
        'form': form_class,
    })


def flatten(lis):
	returnlist = []
	for item in lis:
		returnlist.append(item)
	return returnlist
		


def train(Xparam,T):
	d = {}
	means = np.mean(Xparam,axis=0)
	stds = np.stack(Xparam,axis=0)
	Xs = (Xparam - means)/stds
	Xs1 = np.hstack((np.ones((Xs.shape[0],1)),Xs))
	w = np.linalg.lstsq(np.dot(Xs1.T,Xs1), np.dot(Xs1.T,T))[0]
	d.update({'means':means})
	d.update({'stds':stds})
	d.update({'w':w})
	return d

def use(model,X):
	modelmeans = model.get('means')
	modelstds = model.get('stds')
	w = model.get('w')
	Xs = (X - modelmeans) / modelstds
	Xs1 = np.hstack((np.ones((Xs.shape[0],1)),Xs))
	return Xs1 @ w

def rmse(predict,T):
	rmse = np.sqrt(np.mean((T-predict)**2))
	return rmse

def trainSGD(X,T, learningRate,numberOfIterations ):
	d = {}
	means = np.mean(X,axis=0)
	stds = np.std(X,axis=0)
	Xs = (X-means) / stds
	X1 = np.insert(Xs, 0, 1,axis=1)
	w = np.zeros((X1.shape[1],T.shape[1]))
	for iter in range(numberOfIterations):
		for n in range(X1.shape[0]):
			predicted = X1[n:n+1,:] @ w
			w += learningRate * X1[n:n+1,:].T * (T[n:n+1,:]- predicted)
	d.update({'means':means})
	d.update({'stds':stds})
	d.update({'w':w})
	return d


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

def partitiondata(request):
	dfcolumnvalues = pd.read_csv('media/4cols.csv')
	targetvalues = dfcolumnvalues[['lights']].values
	inputvalues = dfcolumnvalues[['Appliances','T1','RH_1']].values
	Xtrain,Ttrain, Xtest, Ttest = partition(inputvalues,targetvalues,0.8,True)
	print("Xtrain: ",Xtrain)
	dfXtrain = pd.DataFrame(Xtrain) 
	print("Ttrain: ",Ttrain)
	dfTtrain = pd.DataFrame(Ttrain)
	print("Xtest: ",Xtest)
	dfXtest = pd.DataFrame(Xtest)
	print("Ttest: ",Ttest)
	dfTtest = pd.DataFrame(Ttest)
	model = train(inputvalues,targetvalues)
	print("model ",model)
	return render(request, 'PartitionedData.html', {'Xtrain1':dfXtrain.to_html,'Ttrain1':dfTtrain.to_html,'Xtest1':dfXtest.to_html,'Ttest1':dfTtest.to_html,'model':model})

def CreateModel(request):
	dfcolumnvalues = pd.read_csv('media/4cols.csv')
	targetvalues = dfcolumnvalues[['lights']].values
	inputvalues = dfcolumnvalues[['Appliances','T1','RH_1']].values
	model = train(inputvalues,targetvalues)
	print("model ",model)
	predicted = use(model,inputvalues)
	print('predictedmodel ',predicted)
	dfpredicted = pd.DataFrame(predicted)
	error = rmse(dfpredicted,targetvalues)
	print("error ", error )

	x= [1,2,2,4,5]
	y= [1,2,3.5,4,5]
	

	plot = figure(title = 'Line Graph',x_axis_label='X-Axis',y_axis_label= 'Y-Axis',plot_width=400,plot_height=400 )
	plot.circle(x,y)
	# show(plot)
	html = file_html(plot, CDN, "my plot")

	
	return render(request, 'CreateModel.html', {'model':model,'predictedmodel':dfpredicted.to_html,'error':error,'html':html})

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
	print("targetvalues",targetvalues)
	flatlist =flatten(targetvalues.flatten())
	print("flatlist str[0] ",flatlist)
	plot = figure(title = 'Line Graph',x_axis_label='X-Axis',y_axis_label= 'Y-Axis',plot_width=400,plot_height=400)
	plot.circle([1,2,3],flatlist)
	# show(plot)
	html = file_html(plot, CDN, "my plot")


	


	return render(request, 'preprocess.html', {'loaded_data': data_html,'filedatahtml':filedf,'Xtrain':dfXtrain.to_html,'Ttrain':dfTtrain.to_html,'Xtest':dfXtest.to_html,'Ttest':dfTtest.to_html,'figure':html})
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
	#return HttpResponseRedirect(reverse("MachineLearningApi:upload_csv"))
	messages.success(request, 'Your file was uploaded successfully!')
	return render(request, 'thanks.html')


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
