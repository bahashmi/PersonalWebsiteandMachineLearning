from django.shortcuts import render
from django.views.generic import View
from MachineLearningApi.models import CSVFile,UserDetails,dataCleaningModels,replaceNaNvaluesModels
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EventsForm,UserModelForm,replaceNaNvaluesModelsForm
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
import pandas as pd
import numpy as np
from matplotlib import pylab
import matplotlib.pyplot as plt
import mpld3 as mpld3
from bokeh.plotting import figure,output_file,show
from bokeh.embed import components,file_html
from bokeh.resources import CDN
from collections import Iterable
from django.contrib import messages
from IPython.display import HTML
import os
 



from .forms import UserModelForm,dataCleaningForm
from .forms import NameForm
def Datacleaned(request): 
	print("herllohfkjnfcgy")
	path="media/"  
	img_list =os.listdir(path)
	print("list of files inside 16 june 2020 ",img_list)
	
	nfry= CSVFile.objects.all()

	fileindex = img_list.index(nfry[len(nfry)-1].name)
	print("img_list[fileindex]: ",img_list[fileindex])
	filepath =  path + img_list[fileindex] 
	
	dfcolumnvalues = pd.read_csv(filepath,encoding='utf-8')
	# dfcolumnvalues = pd.read_csv("media/May27th.csv")
	# print("dfcolumns : ", dfcolumnvalues.columns.values)
	# print(dfcolumnvalues[['lights']].values)

	DBcolums = replaceNaNvaluesModels.objects.all()
	print("replaceNaNvaluesModels ",DBcolums)
	# print(" dfcolumnvalues[[DBcolums[len(DBcolums) -1].changeTypeCol]].values ",dfcolumnvalues[[DBcolums[len(DBcolums) -1].changeTypeCol]].values)
	
	df = request.session['df']
	print("request.session['df']")
	print(df)

	return render(request, 'datacleaned.html')

def Datacleaning(request):
	# form_class = replaceNaNvaluesModelsForm
	# # if request is not post, initialize an empty form
	# form = form_class(request.POST)

	path="media/"  
	img_list =os.listdir(path)
	nfry= CSVFile.objects.all()
	print("request ", request)

	fileindex = img_list.index(nfry[len(nfry)-1].name)
	filepath =  path + img_list[fileindex] 
	DBcolums = UserDetails.objects.all()
	dfcolumnvalues = pd.read_csv(filepath,encoding='utf-8')
	# dfcolumnvalues = pd.read_csv("media/May27th.csv")
	# print("dfcolumns : ", dfcolumnvalues.columns.values)
	# print(dfcolumnvalues[[DBcolums[len(DBcolums) -1].changeTypeCol]].values)

	
	# print("UserDetailsDBcolumns ",DBcolums[len(DBcolums) -1].changeTypeCol)
	# print("UserDetailsDBcolumns.values ",dfcolumnvalues[[DBcolums[len(DBcolums) -1].changeTypeCol]].values)
	df = dfcolumnvalues.astype({DBcolums[len(DBcolums) -1].changeTypeCol: DBcolums[len(DBcolums) -1].changeColTypeTo})
	# print("df after changing col type to float: ", df)
	df = df.to_json()
	request.session['df'] = df


	if request.method == 'POST':
		form = replaceNaNvaluesModelsForm(request.POST)
		if form.is_valid():
			u = form.save()
			users = replaceNaNvaluesModels.objects.all()
			print("replaceNaNvaluesModelsUsers: ", users.values)
			return render(request, 'datacleaned.html',{'users': users})

            
		form_class = replaceNaNvaluesModelsForm
	
	return render(request, 'datacleaning.html', {
        'form': form_class,'df':df
    })

# def Datacleaning(request):
# 	print("hello we are about to start data cleaning")
# 	path="media/"  
# 	img_list =os.listdir(path)
# 	print("list of files inside 12 march ",img_list)

# 	nfry= CSVFile.objects.all()
# 	print("nfry[len(nfry)-1].name, ", nfry[len(nfry)-1].name)
# 	return render(request, 'datacleaning.html',{'filename': nfry[len(nfry)-1].name})

def userDetails(request):
	if request.method == 'POST':
		form = UserModelForm(request.POST)
		if form.is_valid():
			u = form.save()
			users = UserDetails.objects.all()
			print("Users: ", users.values)
			return render(request, 'display.html',{'users': users})

            # u = form.save(commit=False)
            # u.title = "New Name"
            # context = {
            # 'u' : u
            # }
            #
            # template = loader.get_template('display.html')
            #
            # return HttpResponse(template.render(context, request))
	else:
		form_class = UserModelForm
	
	return render(request, 'userdetails.html', {
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
	path="media/"  
	img_list =os.listdir(path)
	print("list of files inside 15jan ",img_list)

	nfry= CSVFile.objects.all()
	print("nfry[len(nfry)-1].name, ", nfry[len(nfry)-1].name)

	# targetCol = ''
	# form = UserModelForm(request.POST)
	# if form.is_valid():
	# 	targetCol = form.cleaned_data.get("targetcols")

	# print("targetCol = ", form.cleaned_data)



	Userdetailsobjects = UserDetails.objects.all()
	print("Userdetailsobjects: ", len(Userdetailsobjects))

	filepath = "\"" + path + nfry[len(nfry)-1].name + "\""
	print("filepath = ", filepath)
	dfcolumnvalues = pd.read_csv("media/4cols.csv")
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

	dfcolumnvalues = pd.read_csv('media/4cols.csv')
	print('dfcolumnvalues[[lights]] ',dfcolumnvalues[['lights']])
	filedf = dfcolumnvalues[['lights']].to_html
	
	
	x= [1,2,3,4,5,6,7,8,9]
	y= [60.0,19.89,46.693333,50.0,19.89,46.30000060,60.0,19.89,46.693333]
	

	plot = figure(title = 'Line Graph',x_axis_label='X-Axis',y_axis_label= 'Y-Axis',plot_width=400,plot_height=400 )
	plot.circle(x,y)
	# show(plot)
	html = file_html(plot, CDN, "my plot")

	return render(request, 'PartitionedData.html', {'Xtrain1':dfXtrain.to_html,'filedf':filedf ,'Ttrain1':dfTtrain.to_html,'Xtest1':dfXtest.to_html,'Ttest1':dfTtest.to_html,'model':model,'figure':html})

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

	
	return render(request, 'CreateModel.html', {'model':model, 'predictedmodel':dfpredicted.to_html,'error':error,'html':html})

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
	plot.circle([1,2,3,4],flatlist)
	# show(plot)
	html = file_html(plot, CDN, "my plot")
	if request.method == 'POST':
		form = UserModelForm(request.POST)
		if form.is_valid():
			u = form.save()
			users = UserDetails.objects.all()
			print("Users: ", users.values)
			return render(request, 'preprocess.html', {'loaded_data': data_html,'filedatahtml':filedf,'Xtrain':dfXtrain.to_html,'Ttrain':dfTtrain.to_html,'Xtest':dfXtest.to_html,'Ttest':dfTtest.to_html,'figure':html,'users': users}) 
			# render(request, 'display.html',{'users': users})
            # u = form.save(commit=False)
            # u.title = "New Name"
            # context = {
            # 'u' : u
            # }
            #
            # template = loader.get_template('display.html')
            #
            # return HttpResponse(template.render(context, request))
	else:
		form_class = UserModelForm


	


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
	# p = CSVFile(name=csv_file.name)
	# p.save()
	# print("p.name ",p.name)
	# print("uploaded file in upload_csv update jan 14",csv_file.name)

	# print("CSVfile objects = ",CSVFile.objects.values_list('name', flat=True))


	fruit = CSVFile.objects.create(name=filename)
	fruit.save()
	print(fruit.name)
	
	print("CSVFile.objects name ", CSVFile.objects.filter(name__startswith=filename).values('name'))

	# nfry= CSVFile.objects.filter(name__startswith=filename).values('name')
	# nfry= CSVFile.objects.filter(name__startswith=filename)[0].name
	# print(nfry)

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
		name = request.FILES['myfile'].name
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

	


		
