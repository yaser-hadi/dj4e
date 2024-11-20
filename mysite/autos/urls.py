from django.urls import path

from .migrations import views

app_name = "autos"
urlpatterns = [
    path("", TemplateView.as_view.as_view(template_name='autos/main.html')),
   
]
