from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product



class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = "products/featured-detail.html"
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()




def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset,
    }
    return render(request,"products/list.html",context)

class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/detail.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product Doesnot exist")
        return instance

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"
    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Product, slug=slug, active=True)

        return instance

def product_detail_view(request,pk=None):
    # queryset = Product.objects.get(pk=pk)
    # queryset = get_object_or_404(Product, pk=pk)
    # queryset = Product.objects.filter(pk=pk)
    # if queryset.exists() and queryset.count() == 1:
    #     instance = queryset.first()
    # else:
    #     raise Http404("Product Doesnot exists")
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product Doesnot exist")
    context = {
            'object':instance,
        }
    return render(request,"products/detail.html",context)
