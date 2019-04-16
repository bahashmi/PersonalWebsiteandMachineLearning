from django.shortcuts import render
from django.views.generic import View
from MachineLearningApi.models import CSVFile
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EventsForm
# Create your views here.


def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "thanks.html", data)
    # if not GET, then proceed

	csv_file = request.FILES["csv_file"]
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


class DataImportFile(View):

    def get(self, request, *args, **kwargs):
        print("dhgdey")
        return render(request,"thanks.html")

    def get_redirect_url(self, *args, **kwargs):
        return reverse("simplesocial:home")
