from django.db.models.query import RawQuerySet
from django.db.models import F
from django.shortcuts import render,redirect
import time,datetime
from dashboard.views import pagination
from django.contrib import messages
from product.models import products
from location.models import locations
from dashboard.models import balance
from .models import prod_move
import django
django.setup() # To resolve importing products class error

# Create your views here.
def add_prodmove(request,pk):
    context={"data": products.objects.get(pid=pk),"loc":locations.objects.all()}
    return render(request,"product_movement/addprodmove.html",context)

def disp_prodmove(request):
    if request.method=='POST':
        prod=prod_move()
        bal=balance()
        prod.mid=int(time.time())
        prod.timestamp=datetime.datetime.now()
        chkloc=request.POST.get("sname")
        if chkloc:
            prod.f_location=chkloc
        else:
            prod.f_location='Warehouse'
        prod.t_location=request.POST.get("dname")
        prod.qty=request.POST.get("pqty")
        pk=request.POST.get("pid")
        prod.pid=products.objects.get(pid=pk)
        if chkloc==prod.t_location:
            messages.warning(request,"Cannot move product to the same location")
            return redirect (request.META['HTTP_REFERER'])
        prod.save()
        if chkloc:
            edit_bal(prod)
            add_bal(prod,bal,pk)
        else:
            add_bal(prod,bal,pk)
            ded_qty(prod,pk)
    data=pagination(prod_move.objects.all(),request)
    context={'data':data,'page':data}
    return render(request,"product_movement/prodmovement.html",context)

def edit_prodmove(request,pk):
    prod=prod_move.objects.get(mid=pk)
    bal=balance.objects.get(pid=prod.pid,warehouse=locations.objects.get(location=prod.t_location))
    context={'data':prod,"loc":locations.objects.all(),'bal':bal}
    return render(request,"product_movement/editprodmove.html",context)

def ded_qty(prod,pk):
    product=products.objects.get(pid=pk)
    product.qty=F('qty')-prod.qty
    product.save()

def add_bal(prod,bal,pk):
    try:
        addbal=balance.objects.get(pid=prod.pid,warehouse=locations.objects.get(location=prod.t_location))
        addbal.qty=F('qty')+prod.qty
        addbal.save()
    except:
        bal.bid=int(time.time())
        bal.pid=products.objects.get(pid=pk)
        bal.warehouse=locations.objects.get(location=prod.t_location)
        bal.qty=prod.qty
        bal.save()

def edit_bal(prod):
    dedbal=balance.objects.get(pid=prod.pid,warehouse=locations.objects.get(location=prod.f_location))
    dedbal.qty=F('qty')-prod.qty
    dedbal.save()





