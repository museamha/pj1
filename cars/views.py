from django.shortcuts import render
from django.views import View
from .models import car
# Create your views here.
class FrontPageView(View):
    tempate_name = "cars/home.html"
    

    def get(self, request, *args, **kwargs):
        allcars = car.objects.all()
        context = {"cars": allcars}
        return render(request,"cars/home.html" , context)

    
class SinglePageView(View):
    template_name= "cars/single.html"
    
    def get(self, request,slug, *args, **kwargs):
        single = car.objects.get(slug=slug)
        context = {"car": single}
        return render(request,self.template_name, context )