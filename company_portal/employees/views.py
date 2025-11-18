from django.shortcuts import render
from django.views import View
from employees.forms import Addviewforms
# Create your views here.

class Addview(View):
    def get(self,request):
        form_instance = Addviewforms()
        context = {'form': form_instance}
        return render(request,'records.html',context)

    def post(self,request):
        form_instance = Addviewforms(request.POST)
        if form_instance.is_valid():
           form_instance.save()
           context = {'form': form_instance}
           return render(request, 'records.html', context)

