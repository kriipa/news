from django.urls import path
from.views import *

urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('video/', Videoview.as_view(), name='video'),
    path('category/<str:category_name>/', category_view, name='category_view' ),
    # path('category/<slug>', CategoryView.as_view(), name = 'category'),
    path('contact/', contact, name='contact' ),
    # path('login/', loginview, name='login' ),
    path('register/', register, name='register' ),
    path('aboutus/', aboutus, name='aboutus' ),
    path('privacy/', privacy, name='privacy' ),
    path('help/', help, name='help' ),
    path('eachcat/', eachcat, name='eachcat' ),
    path('profile/', profile, name='profile' ),
    path('edit_profile/', edit_profile, name='edit_profile' ),
    path('catnews/', catnews, name='catnews' ),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('search/', SearchView.as_view(), name='search'),
]

