from .import views
from django.urls import path


urlpatterns = [
    path("",views.FrontPageView.as_view(), name="front-page"),
    path("cars/<slug:slug>/",views.SinglePageView.as_view(), name="detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("companies/<str:name>", views.SingleProducersView.as_view(), name="single-companies"),
    path("companies",views.ProducersView.as_view(), name="companies")
]
