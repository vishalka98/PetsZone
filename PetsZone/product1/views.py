from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import product
from django.views.generic import ListView,DetailView

from carts.models import Cart

# Create your views here.

class productfeaturedlistview(ListView):
    #queryset = product.objects.all()
    template_name="product1/list.html"
   
    def get_queryset(self,*args,**kwargs):
        request = self.request
        return product.objects.all().featured()


class productfeatureddetailview(DetailView):
    #queryset = product.objects.all()
    template_name="product1/featured-detail.html"
    def get_context_data(self,*args,**kwargs):
        request = self.request
        return product.objects.all().featured()

    




class productlistview(ListView):
    #queryset = product.objects.all()
    template_name="product1/list.html"
    #def get_context_data(self,*args,**kwargs):
    #	context = super(productlistview,self).get_context_data(*args,**kwargs)
    #	print(context)
    #	return context
    def get_queryset(self,*args,**kwargs):
        request = self.request
        return product.objects.all()


def product_list_view(request):
    queryset=product.objects.all()
    context={'object_list':queryset}
    return render (request,"product1/list.html",context)




class productdetailslugview(DetailView):
    queryset = product.objects.all()
    template_name = "product1/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(productdetailslugview,self).get_context_data(*args,**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(product,slug=slug,active=True)
        try:
            instance = product.objects.get(slug=slug, active=True)
        except product.DoesNotExist:
            raise Http404("Not Found")
        except product.MultipleObjectsReturned:
            qs = product.objects.filter(slug=slug,active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm")



        return instance




class productdetailview(DetailView):
    queryset = product.objects.all()
    template_name="product1/detail.html"
    def get_context_data(self,*args,**kwargs):
    	context = super(productdetailview,self).get_context_data(*args,**kwargs)
    	print(context)
    	return context

    def get_object(self,*args,**kwargs):
        request =self.request
        pk = self.kwargs.get('pk')
        instance = product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("product does'ny exists")
        return instance





def product_detail_view(request,pk=None,*args,**kwargs):

    #instance=product.objects.get(pk=pk,featured=True)
    #instance=get_object_or_404(product,pk=pk)
    # queryset=product.objects.all()
    # context={'object_list':queryset}
    #try:
     #   instance=product.objects.get(id=pk)
    #except product.DoesNotExist: 
    #    print('no product found')
    #    raise Http404('product does not exist')
    #except:
    #    print('huh?')
    instance = product.objects.get_by_id(pk)
    #print(instance)
    if instance is None:
        raise Http404("product does'ny exists")
    #qs = product.objects.filter(id=pk)
    #if qs.exists() and qs.count() == 1:
    #    instance  = qs.first()
    #else:
    #    raise Http404('product does not exist')


    context={'object':instance}
    return render (request,"product1/detail.html",context)