from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,"index.html")


def register(request):
    
    if request.method=="POST":
        em=request.POST['emaillogin']
        us=request.POST['usernamelogin']
        ps = request.POST['passwordlogin']
        User = get_user_model()
        user = User.objects.create_user(em,us,ps)
        user.save()
    return render(request,"suplier_regis.html")

def suplier_register(request):
    
    if request.method=="POST":
        em=request.POST['emaillogin']
        us=request.POST['usernamelogin']
        ps = request.POST['passwordlogin']
        User = get_user_model()
        user = User.objects.create_staffuser(em,us,ps)
        user.save()
    return render(request,"registration.html")

def loginus(request):
    if request.method=="POST":
        em=request.POST['emaillogin']
        ps = request.POST['passwordlogin']
        user = authenticate(email=em, password=ps) 
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect("/admin")
            else:
                res = HttpResponseRedirect('/cust_dashboard')
                # if "rememberme" in r.POST:
                #     res.set_cookie("user_id",user.id)
                #     res.set_cookie("date_login",datetime.now())
                return res
            
            # if user.is_staff:
            #     return HttpResponseRedirect('/sel_dashboard')

            # if user.is_active:

            #     return HttpResponseRedirect('/cust_dashboard')
        else:
            return render(request,"index.html")
    return render(request,"login.html")

def cust_dashboard(request):
    return render(request,"cust_dashboard.html")
       

def contactus(request):
    return render(request,"contact.html")
def cart(request):
    return render(request,"cart.html")
def checkout(request):
    return render(request,"checkout.html")
def shopgrid(request):
    return render(request,"shop-grid.html")
def blog(request):
    return render(request,"blog-single-sidebar.html")


    