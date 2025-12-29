from django.urls import path
from .views import *

urlpatterns = [
    path('', demo, name='demo'),
    path('first/',first,name='first'),
    path('style/',style,name='style'),
    path('show/',show,name='show'),
    path('showimg/',showimg,name='showimg'),

    path('storeimg/', storeimg,name='storeimg'),
    path('index/',index,name='index')
    
    #
    #path('store/',store,name='store'),
    #path('storeget/',storeget,name='storeget'),
  
]