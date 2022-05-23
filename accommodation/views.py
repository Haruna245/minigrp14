from dataclasses import field
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .forms import RegisterUserform
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Apartment,Booking_details
from renting.models import Houses
from django.contrib.auth.models import User

# Create your views here.
""" def home(request):

    return render(request,"index.html") """

def login_user(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        
        new_var = None
        print(user)
        if user is not new_var:
            login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credential")
            return redirect('login')
        
    else:
        return render(request,'login.html') 

def signup(request):
    print(request.method)
    if request.method == 'POST':
        """ data = request.POST
        data._mutable = True """
        
        """ print(data) """
        username = request.POST['username']
        password = request.POST['password1']
        email =  request.POST['email']
        """ data['username'] = request.POST['username']
        data['email'] = request.POST['email']
        data['password1'] = request.POST['password1']
        data['password2'] = request.POST['password2'] """
        #form = RegisterUserform(data or None)
        form = User.objects.create_user(username, email, password)
        form.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        # Redirect to a success page.
        
        else:
            messages.error(request,'Invalid credential')
        # Return an 'invalid login' error message.
        """ if form.is_valid():
            #form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Registration succesful')
            return redirect("/")

        else:
            messages.error(request,'Invalid credential')
            form = RegisterUserform() """
    else:
        form = RegisterUserform()
    return render(request,'signup.html',{'form':form})

def logoutUser(request):
    logout(request)
    return redirect('/')


class HomeView(ListView):
    model = Houses
    template_name = 'index1.html'

class add_Post(CreateView):
    model = Houses
    template_name = 'addPost.html'
    fields = '__all__'

class update_Post(UpdateView):
    model = Houses
    template_name = 'update.html'
    fields = '__all__'

""" class Post_Detail(DetailView):
    model = Apartment
    template_name = 'detail.html' """


def detail_view(request,id):
    product = get_object_or_404(Houses,id=id)
    print(request.method)
    if request.method == 'POST':
        product.book = True
        product.save()
    return render(request,'detail.html',{'product':product,})  

""" class book(CreateView):
    model = Booking_details
    template_name = 'booking.html'
    fields = ('tel_no','occupation','gender') """

def post(request):
    if request.method == 'POST':
        customer = request.user
        tel_no = request.POST['tel_no']
        occupation = request.POST['occupation']
        gender = request.POST['gender']

        b = Booking_details(customer=customer, tel_no=tel_no,occupation=occupation,gender=gender)
        b.save()

        return HttpResponse('')
    return render(request,'booking.html')


        