
from django.shortcuts import render
from product1.models import product
from django.views.generic import ListView

class searchproductview(ListView):
    #queryset = product.objects.all()
    template_name="search/view.html"

    def get_context_data(self,*args,**kwargs):
    	context = super(searchproductview,self).get_context_data(*args,**kwargs)
    	query = self.request.GET.get('q')
    	context['query'] = query
    	return context
   
    def get_queryset(self,*args,**kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q',None) #method_dict['q']
        print(query)
        if query is not None:
        	
        	return product.objects.search(query)
        return product.objects.featured()