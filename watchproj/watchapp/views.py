from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def Home(request, c_slug=None):
    c_page=None
    product_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        print(c_page)
        product_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        product_list=Product.objects.all().filter(available=True) 
          #paginator
    paginator=Paginator(product_list,6)

    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    #for invalid page and empty page
        
    try:
        products=paginator.page(page)
    except:
        page=1
    #for invalid page and empty page
    try:
        products=paginator.page(page)
    except(EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)  
    categories = Category.objects.all() 
       
    
    return render(request,'index.html',{'data':product_list,'category':c_page,'products':products ,'categories': categories})
    # return render(request, 'index.html', {'category': c_page, 'products': products})



def product(request, c_slug=None):
    c_page=None
    product_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        print(c_page)
        product_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        product_list=Product.objects.all().filter(available=True) 
          #paginator
    paginator=Paginator(product_list,50)

    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    #for invalid page and empty page
        
    try:
        products=paginator.page(page)
    except:
        page=1
    #for invalid page and empty page
    try:
        products=paginator.page(page)
    except(EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)   
       
    
    return render(request,'product.html',{'data':product_list,'category':c_page,'products':products})
    # return render(request, 'index.html', {'category': c_page, 'products': products})





def Details(req,id):
    data=Product.objects.get(id=id)
    return render(req,'details.html',{'data':data})


