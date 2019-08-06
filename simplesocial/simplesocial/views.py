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

class HomePage(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
