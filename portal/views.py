from django.shortcuts import render
from .models import *
from django.views import View
from django.core.paginator import Paginator

# Create your views here.


class Base(View):
    views = {}

class Homeview(Base):
    def get(self, request):
        # self.views['trending'] = News.objects.filter(LABELS)
        self.views['newws'] = News.objects.all()
        return render(request, 'user/home.html', self.views)


# def home(request):
#     views = {}
#     return render(request, 'user/home.html', views)

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

# class CategoryView(Base):
#     def get(self, request, slug):
#         cat_id = Category.objects.get(slug = slug).id
#         self.views['categories'] = Category.objects.all()
#         return render(request, 'eachCat.html', self.views)

def category_view(request, category_name):
    category = Category.objects.get(name = category_name)
    context = {
        'category' : category,
    }
    return render(request, 'user/eachCat.html', context)


def newsdetail(request):
    views={}
    views['news-single']=News.objects.filter(id=id)
    return render(request, 'user/categoryNews.html',views)

def contact(request):
    return render(request, 'user/contactus.html')

def aboutus(request):
    return render(request, 'user/aboutus.html')

def privacy(request):
    return render(request, 'user/privacy.html')

def help(request):
    return render(request, 'user/help.html')

def eachcat(request):
    return render(request, 'user/eachCat.html')

def catnews(request):
    return render(request, 'user/categoryNews.html')

