

from django.urls import path


from .views import productlistview,productdetailslugview
app_name = 'product1'
urlpatterns = [
   
    path('', productlistview.as_view(), name="list"),
   
    path('<slug:slug>/', productdetailslugview.as_view(), name="detail"),
   
]  

