from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.


class Base(View):
    views = {}

class Homeview(Base):
    def get(self, request):
        # self.views['trending'] = News.objects.filter(LABELS)
        self.views['newws'] = News.objects.all()
        return render(request, 'user/home.html', self.views)

class Videoview(Base):
    def get(self, request):
        self.views['vids'] = Vid_cont.objects.all()
        return render(request, 'user/videos.html', self.views)


def category_view(request, category_name):
    category = Category.objects.get(name = category_name)
    newws=News.objects.filter(category=category)
    context = {
        'category' : category,
        'newws':newws,
    }
    return render(request, 'user/eachCat.html', context)


def newsdetail(request):
    views={}
    views['news-single']=News.objects.filter(id=id)
    return render(request, 'user/categoryNews.html',views)

def news_single(request, id):
    views = {}
    views['news_detail'] = News.objects.filter(id = id)
    return render(request, 'user/categoryNews.html', views)

class SearchView(Base):
    def get(self,request):
        if request.method == 'GET':
            query = request.GET['query']
            if query != "":
                self.views['search_news'] = News.objects.filter(name__icontains = query )
            else:
                redirect('/')
        
        return render(request, 'user/search.html', self.views)



def contact(request):
    views = {}
    views['contactus'] = Contactus.objects.all()
    if request.method == 'POST':
        # form maa bahyeko names
        mail = request.POST['email']
        num = request.POST['number']
        msg = request.POST['message']
        data = Contact.objects.create(
            # field ko names
            email = mail,
            number = num,
            message = msg,
        )
        data.save()
    return render(request, 'user/contact.html', views)

def aboutus(request):
    return render(request, 'user/aboutus.html')

def privacy(request):
    return render(request, 'user/privacy.html')

def profile(request):
    return render(request, 'user/profilepage.html')

def edit_profile(request):
    return render(request, 'user/editprofile.html')

def help(request):
    return render(request, 'user/help.html')

def eachcat(request):
    return render(request, 'user/eachCat.html')

def catnews(request):
    return render(request, 'user/categoryNews.html')

# login

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('/login')
        else:
            messages.error ("Password does not match!")
    else:
        return render(request, 'user/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # redirect to home page
        else:
            messages.error (request, "Your credentials does not match!")
            return render(request, 'user/login.html')
    else:
        return render(request, 'user/login.html')


def LogoutPage(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render
from .models import Profile, Customer
@login_required
def profile_view(request):
    # Retrieve the customer profile
    customer = Customer.objects.get(username=request.user.username)

    # Retrieve the corresponding profile
    profile = Profile.objects.get(username=request.user.username)

    context = {
        'customer': customer,
        'profile': profile
    }

    return render(request, 'user/profilepage.html', context)
