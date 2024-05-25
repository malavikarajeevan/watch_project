from django.shortcuts import render
from watchapp.models import Product
from django.db.models import Q

# Create your views here.
def SearchResult(request):
    query = None
    products = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        print(query)
        products = Product.objects.filter(Q(name__icontains=query)|Q(desc__icontains=query))

    return render(request,'search.html',{'query':query,'products':products})