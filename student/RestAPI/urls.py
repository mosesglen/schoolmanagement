
from django.urls import path
from .views import getprofile, getprofile_by_id


urlpatterns = [
   path('', getprofile.as_view()),
   path('<str:key>', getprofile_by_id.as_view(), name="studentdetails"),
  
]
