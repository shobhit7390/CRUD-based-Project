from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ag=fm.cleaned_data['age']
            crs=fm.cleaned_data['course']
            obj=User(name=nm,email=em,age=ag,course=crs)
            obj.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    std=User.objects.all()
    return render(request, 'djdata/addandshowdata.html', {'form':fm, 'stu':std})

#This method will update data
def update_data(request,id):
    if request.method=="POST":
        d=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=d)
        if fm.is_valid():
            fm.save()
    d=User.objects.get(pk=id)
    fm=StudentRegistration(instance=d)
    return render(request,'djdata/updatedata.html', {'form':fm})




#This method will delete the things using id
def delete_data(request,id):
    if request.method=='POST':
        d=User.objects.get(pk=id)
        d.delete()
        return HttpResponseRedirect('/')