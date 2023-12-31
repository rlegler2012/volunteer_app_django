from typing import Any, Dict
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from .models import Professional, Location
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("professional_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


class Home(TemplateView):
    template_name = "home.html"  

class About(TemplateView):
    template_name = "about.html"



### Professional List ##########
@method_decorator(login_required, name='dispatch')
class ProfessionalList(TemplateView):
    template_name = "professional_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["professionals"] = Professional.objects.filter(
                name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["professionals"] = Professional.objects.filter(user=self.request.user)
            # context["header"] = "Trending Professional"
        return context


class ProfessionalDetail(DetailView):
    model = Professional
    template_name = "professional_detail.html"

class ProfessionalCreate(CreateView):
    model = Professional
    fields = ['name', 'img', 'bio']
    template_name = "professional_create.html"

    #new method that will add the user into our submitted form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfessionalCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('professional_detail', kwargs={'pk': self.object.pk}) 
    
class ProfessionalUpdate(UpdateView):
    model = Professional
    fields = ['name', 'img', 'bio']
    template_name = "professional_update.html"

    def get_success_url(self):
        return reverse('professional_detail', kwargs={'pk': self.object.pk})

class ProfessionalDelete(DeleteView):
    model = Professional
    template_name = "professional_delete_confirmation.html"
    success_url = "/professionals/"   
    
    
##### Location List #########
locations = [
  Location("testing", "test",
          "testtesttest"),
    ]

# @method_decorator(login_required, name='dispatch')
class LocationList(TemplateView):
    template_name = "location_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["locations"] = locations
        return context

class LocationCreate(View):

    def post(self, request, pk):
        event_name = request.POST.get("event_name")
        city = request.POST.get("city")
        state = request.POST.get("state")
        # link = request.POST.get("link")
        professional = Professional.objects.get(pk=pk)
        Location.objects.create(event_name=event_name, city=city, state=state, professional=professional)
        return redirect('professional_detail', pk=pk)