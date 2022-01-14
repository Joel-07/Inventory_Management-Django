from django import forms
from django.core import paginator
from django.shortcuts import render
from django.db.models import Q
from .models import balance
from product.models import products
from .form import searchform
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def disp(request):
    form=searchform(request.POST or None)
    bal_del()
    posts=pagination(balance.objects.all(),request)
    if request.method=="POST":
        posts=pagination(balance.objects.filter(pid__pid__icontains=form['pid'].value(),warehouse__lid__icontains=form['warehouse'].value().title()),request)
    context={'data':posts,'form':form,'page':posts}
    return render(request,"dashboard/display.html",context)


def pagination(val,request):
    paginator=Paginator(val, 5)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)   
    return posts

def bal_del():
    bal=balance.objects.filter(qty=0).delete()
