from django.forms import fields
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import products
import time
from dashboard.views import pagination

# Create your views here.
def disp_pro(request):
    data=pagination(products.objects.all(),request)
    context={"data":data,"page":data}
    return render(request,"product/disproduct.html",context)
def add_pro(request):
    if request.method=="POST":
        product=products()
        pname=request.POST.get("pname").title()
        try:
            products.objects.get(pname=pname)
            messages.warning(request,"Product Already Present")
        except:
            product.pid=int(time.time())
            product.pname=pname
            product.qty=request.POST.get("pqty")
            product.save()
            messages.success(request,"Product added successfully")
    return render(request,"product/addproduct.html")
def edit_pro(request,pk=None):
    if request.method=="POST":
        product=products.objects.get(pid=pk)
        product.pname=request.POST.get("pname")
        product.qty=request.POST.get("pqty")
        product.save()
        messages.success(request,"Product Updated successfully")
        return redirect(disp_pro)
    context={"data":products.objects.get(pid=pk)}
    return render(request,"product/editproduct.html",context)
def delete(request,pk):
    products.objects.get(pid=pk).delete()
    messages.error(request,"Product deleted successfully")
    return redirect(disp_pro)


