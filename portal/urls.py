from django.urls import path
from.views import *

urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('video/', Videoview.as_view(), name='video'),
    path('category/<str:category_name>/', category_view, name='category_view' ),
    # path('category/<slug>', CategoryView.as_view(), name = 'category'),
    path('contact/', contact, name='contact' ),
    path('aboutus/', aboutus, name='aboutus' ),
    path('privacy/', privacy, name='privacy' ),
    path('help/', help, name='help' ),
    path('eachcat/', eachcat, name='eachcat' ),
    path('catnews/', catnews, name='catnews' )
]

