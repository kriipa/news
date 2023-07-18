from django.urls import path
from.views import *

urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    # path('video/', Videoview.as_view(), name='video'),
    path('category/<str:category_name>/', category_view, name='category_view' ),
    # path('category/<slug>', CategoryView.as_view(), name = 'category'),
    path('contact/', contact, name='contact' ),
    path('video/', video_view, name="video"),
    path('video_single/<int:id>', video_single, name="video_single"),
    path('register/', register, name='register' ),
    path('aboutus/', aboutus, name='aboutus' ),
    path('privacy/', privacy, name='privacy' ),
    path('help/', help, name='help' ),
    path('eachcat/', eachcat, name='eachcat' ),
    path('profile/', display_profile, name='profile' ),
    path('edit_profile/', edit_profile, name='edit_profile' ),
  path('news_single/<int:news_id>/post_comment/', post_comment, name='post_comment'),
   path('news_single/<int:id>/', news_single, name='news_single'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('search/', SearchView.as_view(), name='search'),
    path('logout/', LogoutPage, name='logout'),
    path('rank1/', rank1, name='rank1'),
]

