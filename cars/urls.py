from .import views
from django.urls import path


urlpatterns = [
    path("",views.FrontPageView.as_view(), name="front-page"),
    path("posts/<slug:slug>", views.SinglePageView.as_view(),
         name="detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]
