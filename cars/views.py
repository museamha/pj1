from django.shortcuts import render , redirect
from django.views.generic import ListView
from django.views import View
from .models import car
from django.http import HttpResponseRedirect



# Create your views here.
class FrontPageView(ListView):
    template_name = "cars/home.html"
    model = car
    ordering = ["-yearofpp"]
    context_object_name = "allcars"

    
class SinglePageView(View):
    template_name= "cars/single.html"
    
    def get(self, request,slug, *args, **kwargs):
        single = car.objects.get(slug=slug)
        context = {"car": single}
        return render(request,self.template_name, context )
    
    def is_stored_post(self, request, car_id):
        incart = request.session.get("incart")
        if incart is not None:
          is_saved_for_later = car_id in incart
        else:
          is_saved_for_later = False

        return is_saved_for_later
    

class ReadLaterView(View):
    def get(self, request):
        incart = request.session.get("incart", [])

        context = {}
        if not incart:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = car.objects.filter(id__in=incart)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "cars/incart.html", context)

    def post(self, request):
        incart = request.session.get("incart", [])
        
        car_id = int(request.POST["car_id"])

        if car_id not in incart:
            incart.append(car_id)
        else:
            incart.remove(car_id)

        request.session["incart"] = incart
        return redirect("read-later")