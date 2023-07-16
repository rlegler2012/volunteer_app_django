from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Professional
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

class Home(TemplateView):
    template_name = "home.html"  

class About(TemplateView):
    template_name = "about.html"


### Professional List ####################
class ProfessionalList(TemplateView):
    template_name = "professional_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["professionals"] = Professional.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["professionals"] = Professional.objects.all()
            # default header for not searching 
            context["header"] = "Professionals"
        return context

class ProfessionalDetail(DetailView):
    model = Professional
    template_name = "professional_detail.html"
    
class ProfessionalCreate(CreateView):
    model = Professional
    fields = ['name', 'img', 'bio']
    template_name = "professional_create.html"
    # this will get the pk from the route and redirect to professional view
    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})
        
        
class ProfessionalUpdate(UpdateView):
    model = Professional
    fields = ['name', 'img', 'bio']
    template_name = "professional_update.html"

    def get_success_url(self):
        return reverse('professional_detail', kwargs={'pk': self.object.pk})
    
    
    
    
##### Location List #####################
class Location:
    def __init__(self, name, img, bio):
        self.name = name
        self.img = img
        self.bio = bio


locations = [
  Location("adsfasdf", "dafds",
          "sefwert"),
    ]

class LocationList(TemplateView):
    template_name = "location_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["locations"] = locations
        return context
