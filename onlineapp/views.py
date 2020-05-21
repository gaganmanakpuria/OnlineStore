from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")

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
    