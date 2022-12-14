from django.shortcuts import render,redirect
from.models import Cu_user,CustomUser
from django.contrib.auth import authenticate
# Create your views here.
def reg(request):
    msg=""
    if request.POST:
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        address=request.POST['address']
        username=request.POST['uname']
        password=request.POST['password']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']
        try:
            u=CustomUser.objects.create_user(username=username,password=password,userType="Customer")
            u.save()
            user=Cu_user.objects.create(first_name=firstname,last_name=lastname,address=address,user_name=username,password=password,city=city,state=state,zip=zip,user=u)
            user.save()
        except:
            msg="username already existed"
    return render(request,"form.html",{"msg":msg})

def login(request):
    msg=""
    if request.POST:
        uName = request.POST['uname']
        password = request.POST['password']

        user = authenticate(username=uName, password=password)
        
        if user is None:
            msg="Invalid Login"
        else:
            if user.userType == 'admin':
                return redirect("/adminHome")
            elif user.userType == "Customer":
                cust = Cu_user.objects.get(user_name=uName)
                request.session["id"] = cust.id
                return redirect("/custHome")

    return render(request,"login.html")


def adminHome(request):

    return render(request, "adminHome.html")

def custHome(request):
    custId = request.session["id"]
    cust = Cu_user.objects.get(id=custId)

    return render(request, "custHome.html",{"cust":cust})
