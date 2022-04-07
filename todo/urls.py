from django.conf.urls import url
from todo.views import todolist,todoadd,about,contact,todoedit,tododelete

urlpatterns=[
    url(r'^$',todolist,name='todolist'),
    url(r'^add/$',todoadd,name='todoadd'),

    url(r'^about/$',about,name='about'),
    url(r'^contact/$',contact,name='contact'),

    url(r'^edit/(?P<pk>\d+)$',todoedit,name='todoedit'),
    url(r'^delete/(?P<pk>\d+)$',tododelete,name='tododelete'),
]