
from django.conf.urls import url

from blog.views import index

from blog import urls

urlpatterns = [
url(r'^index/', index , name='index'),
]
