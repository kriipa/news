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

# def vid_cont(request):
#     vid_list = Vid_cont.objects.all()
#     paginator = Paginator(vid_list, 4)  # Display 4 videos per page
#     page_number = request.GET.get('page')
#     vid_page = paginator.get_page(page_number)

#     return render(request, 'user/videos.html', {'vid_page': vid_page})


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


# def register(request):
#     if request.method == 'POST':
#         uname = request.POST.get('username')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('password')
#         pass2 = request.POST.get('confirm_password')
    

#         if pass1 != pass2:
#             messages.error(request, "Your password and confirm password are not the same!")
#         else:
#             my_user = User.objects.create_user(uname, email, pass1)
#             my_user.save()

#             # Create a Customer instance and associate it with the User
#             customer = Customer.objects.create(username=uname, email=email,  )
#             customer.save()

#             return redirect('/login')

#     return render(request, '/register')



# def loginview(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         pass1=request.POST.get('password')
#         user=authenticate(request,username=username,password=pass1)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             messages.error ("Username or Password is incorrect!!!")

#     return render (request,'login.html')



# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'home.html', {'login_form': form})

# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'home.html', {'register_form': form})

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