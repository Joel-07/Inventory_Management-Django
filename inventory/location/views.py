from django.shortcuts import redirect, render
from .models import locations
from django.contrib import messages
import time
from dashboard.views import pagination
# Create your views here.
def disp_loc(request):
    if request.method=='POST':
        location=locations()
        lname=request.POST.get("lname").title()
        try:
            locations.objects.get(location=lname)
            messages.warning(request,"Location Already Present")
        except:
            location.lid=int(time.time())
            location.location=lname
            location.save()
            messages.success(request,"Location added successfully")
    loc=pagination(locations.objects.all(),request)
    context={"data":loc,'page':loc}
    return render(request,"location/displocation.html",context)
def edit_loc(request,pk=None):
    if request.method=='POST':
        location=locations.objects.get(lid=pk)
        location.location=request.POST.get("lname")
        location.save()    
        return redirect (disp_loc)    
    context={"d":locations.objects.get(lid=pk),"data":locations.objects.all()}
    return render(request,'location/displocation.html',context)
def delete(request,pk):
    locations.objects.get(lid=pk).delete()
    messages.error(request,"Location deleted successfully")
    return redirect(disp_loc)
