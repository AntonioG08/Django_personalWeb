from django.urls import path
from . import views

"""We use the argument name, so in the HTML instead of using the whole path name, we only put 
   the 'tag' name, for example the name home. Check the script 'base.html' to se more about this"""
urlpatterns = [
    path('portfolio/', views.portafolio, name="portfolio"),
]