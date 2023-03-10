from django.shortcuts import render,HttpResponse
from home.models import list
# Create your views here.

def home(request):
    context = {'success' : False}
    if request.method == "POST":
        title = request.POST['title']
        task = request.POST['task']

        ins = list(title = title,task = task)
        ins.save()
        # print("the data has been return to the db")
        context = {'success' : True}
    return render(request,'index.html',context)


def task(request):
    # this will deletes empty task list
    list.objects.filter(title='').delete()
    
    # fetches all the task from list model
    tasks = list.objects.all()
    context = {'tasks' : tasks}
    return render(request,'task.html',context)
