from django.shortcuts import render
from home.models import donation_data
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def makedonation(request):
    if request.method == "POST":
        #print("This is post")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        cause = request.POST['cause']
        ifsc = request.POST['ifsc']
        amount = request.POST['amount']
        ins = donation_data(name=name, email = email, phone = phone, cause = cause, ifsc=ifsc, amount=amount)
        ins.save()
        print("saved")
    return render(request, 'makeDonate.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')
