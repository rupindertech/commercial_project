from django.shortcuts import render , HttpResponse
from app.models import Product

# Create your views here.
def index(request):
    related_cato=Product.objects.all()
    data_to_temp={"category":related_cato}
    return render(request,"index.html",data_to_temp)