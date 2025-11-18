from django.shortcuts import render,redirect
from django.views import View
from app1.forms import AddTaskforms
from app1.models import Todo
# Create your views here.



class Home(View):
    def get(self, request):
        form_instance = AddTaskforms()
        t=Todo.objects.all()
        context={'form1': form_instance,'Todo':t}
        return render(request, 'home.html', context)

    def post(self, request):
        form_instance = AddTaskforms(request.POST)

        if form_instance.is_valid():
            form_instance.save()

            form_instance = AddTaskforms()
            t=Todo.objects.all()

            context={'form1': form_instance,'Todo':t}
            return render(request, 'home.html', context)






class Edit(View):
    def get(self,request,i):
        t=Todo.objects.get(id=i)
        form_instance=AddTaskforms(instance=t)
        context={'form':form_instance}

        return render(request,'edit.html',context)

    def post(self,request,i):

            t=Todo.objects.get(id=i)

            form_instance=AddTaskforms(request.POST,instance=t)
            if form_instance.is_valid():
                form_instance.save()


                return redirect('home')



class Delete(View):
    def get(self, request, i):
        t=Todo.objects.get(id=i)
        t.delete()
        return redirect('home')

