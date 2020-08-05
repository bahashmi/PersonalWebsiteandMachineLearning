from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'test.html'

class PreprocessPage(TemplateView):
    template_name = 'preprocess.html'

class partitiondata(TemplateView):
    template_name = 'PartitionedData.html'

class CreateModel(TemplateView):
    template_name = 'CreateModel.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class display(TemplateView):
    template_name = 'display.html'

class HomePage(TemplateView):
    template_name = 'index.html'

class details(TemplateView):
    template_name = 'details.html'
class create(TemplateView):
    template_name = 'create.html'

class datacleaning(TemplateView):
    template_name = 'datacleaning.html'

class datacleaned(TemplateView):
    template_name = "datacleaned.html"

class replaceValues(TemplateView):
    template_name = "replaceValues.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
