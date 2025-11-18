from django.shortcuts import render
from django.views import View
from app1.forms import Additionform,Factorialform,Bmiform,Signupform
class Addition(View):
    def get(self,request):
        form_instance=Additionform()
        context={'form':form_instance}
        return render(request,'addition.html',context)

    def post(self,request):

        # creating form object using submitted data

        form_instance=Additionform(request.POST)

        # check whether data is valid or not

        if form_instance.is_valid():
            # process the data after validation
            data=form_instance.cleaned_data
            print('cleaned_data',data)
            n1=data['num1']
            n2=data['num2']
            s=int(n1)+int(n2)
            context={'result':s,'form':form_instance}
            return render(request,'addition.html',context)



class Factorial(View):
    def get(self,request):
        form_instance=Factorialform()
        context={'form':form_instance}
        return render(request,'factorial.html',context)

    def post(self,request):
        form_instance=Factorialform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            print(data)
            n=data['num']
            fact=1
            for i in range(1,n+1):
                fact=fact*i
            context={'result':fact,'form':form_instance}
            return render(request,'factorial.html',context)


class Bmi(View):
    def get(self,request):
        form_instance=Bmiform()
        context={'form':form_instance}
        return render(request,'bmi.html',context)

    def post(self,request):
        form_instance=Bmiform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            w=data['weight']
            h=data['height']
            b=w/((h/100)**2)
            context={'result':b,'form':form_instance}
            return render(request,'bmi.html',context)


class Signup(View):
    def get(self,request):
        form_instance = Signupform()
        context = {'form': form_instance}
        return render(request, 'sign.html', context)

    def post(self,request):
        form_instance=Signupform(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            username =data['username']
            password = data['password']
            email = data['email']
            phone =data['phone']
            address =data['address']
            gender=data['gender']
            role=data['role']

            context={'user':username,'pass':password,'email':email,'p':phone,'a':address,'r':role}
            return render(request,'sign.html',context)


