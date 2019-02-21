from django.urls import path


from .views import searchproductview
app_name = 'search'
urlpatterns = [
   
    path('', searchproductview.as_view(), name="query"),
   
    
   
]  
