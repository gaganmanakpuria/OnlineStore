from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import Persons,MembershipsBase,AvailableLanguages
from django.contrib.auth import authenticate,login,logout
from django.apps import apps
# from django.contrib.auth.models import User
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
    return render(request,"registration.html")

def suplier_register(request):
    
    if request.method=="POST":
        fn=request.POST['firstnamesel']
        ln=request.POST['lastnamesel']
        em=request.POST['emailsel']
        us=request.POST['usernamesel']
        ps = request.POST['passwordsel']
        # phnnum= request.POST['phonenumbersel']
        # mobilenum= request.POST['Mobilenumbersel']
        # Dob=request.POST['dateofbirthsel']
        # # maritalstatus=request.POST['maritalstatussel']
        # gen= request.POST['gendersel']
        # Supplier= request.POST['supliersel']
        # crditlimit=request.POST['creditlimitsel']
        # Apinc = request.POST['approximateincomesel']
        User = get_user_model()
        user = User.objects.create_staffuser(em,us,ps)
        user.first_name=fn

        user.save()

        # a=User(firstname=fn,lastname=ln,credit_limit=crditlimit,approximate_income=Apinc,gender=gen,marital_status_code=None,date_of_birth=Dob,mobile_phone_number=mobilenum,phone_number=phnnum)
        # a.save()
         
    return render(request,"suplier_regis.html")

def loginus(request):
    if request.method=="POST":
        em=request.POST['emaillogin']
        ps = request.POST['passwordlogin']
        user = authenticate(email=em, password=ps) 
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect("/admin_dashboard")
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

def admin_dashboard(request):
    context={}
    
    User= get_user_model()
    Sellers = User.objects.all().filter(is_staff=True)
    context['sellers'] =Sellers
    user=User.objects.filter(is_staff=False,is_active=False)
    context['user'] =user
    if request.method=="POST":
        if 'approve' in request.POST:
            sidd =request.POST['ssid']
            user=User.objects.get(id=sidd)
            user.is_staff=True
            user.is_active=True
            user.save()
        if 'cancel' in request.POST:
            sidd =request.POST['ssid']
            user=User.objects.get(id=sidd)
            user.save()
        if 'delete_sel_btn' in request.POST:
            email=request.POST['delte_sel_email']
            delte_seler= User.objects.get(email=email)
            delte_seler.delete()


    return render(request,"admin/tables.html",context)
# def g(r):
#     User= get_user_model()
#     user=User.objects.filter(is_staff=False,is_active=False)
#     context['user'] =user
#     if request.method=="GET":
#         sidd =request.GET['ssid']
#         print(sidd)
#         user=User.objects.get(id=sidd)
#         print(user)
def Membershipsbase(request):
    context={}
    membership= MembershipsBase.objects.all()
    context['membership']=membership
    if request.method=="POST":
        if "Add" in request.POST:
            addMembership=request.POST['addMembership']
            new=MembershipsBase(membership_type_code=addMembership)
            new.save()
        if "update" in request.POST:
            updateMembership=request.POST['updateMembership']
            previd=request.POST['prevMembership']
            check=MembershipsBase.objects.get(id=previd)
            check.membership_type_code=updateMembership
            check.save()
        if "delete" in request.POST:
            deleteMembership=request.POST['deleteMembership']
            membership=MembershipsBase(id=deleteMembership)
            membership.delete()
    return render(request,"admin/Membershipbas.html",context)

def AvailableLanguage(request):
    context={}
    languages= AvailableLanguages.objects.all()
    context['languages']=languages
    if request.method=="POST":
        if "Add" in request.POST:
            addLang=request.POST['addLanguage']
            new=AvailableLanguages(language=addLang)
            new.save()
        if "update" in request.POST:
            updateLang=request.POST['updateLanguage']
            previd=request.POST['previd']
            check=AvailableLanguages.objects.get(id=previd)
            check.language=updateLang
            check.save()
        if "delete" in request.POST:
            del_lang_id=request.POST['deleteLanguage']
            Lang=AvailableLanguages(id=del_lang_id)
            Lang.delete()
    return render(request,"admin/Language.html",context)

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


    