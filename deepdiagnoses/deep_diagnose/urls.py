from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'deep_diagnose'

urlpatterns = [
    # /home/
    # for finding nearby companies
    url(r'^home/$', views.home, name='find'),


    # /
    # for list of all companies
    url(r'^$', views.CompanyList.as_view(), name='company_list'),

    # /company/id(1,2..)
    # giving company details like tests and their price
    url(r'^company/(?P<pk>[0-9]+)/$', views.CompanyDetails.as_view(), name='company_detail'),

    # /test_list/
    # for list of all tests
    url(r'^test_list/$', views.TestList.as_view(), name='test_list'),

    # /result/
    # shows result according to users location
    url(r'^result/$', views.result, name='result'),

    # /test/pk(1,2 ..)
    # for test details like about_test companies offering that test with price
    url(r'^tests/(?P<pk>[0-9]+)/$', views.TestDetail.as_view(), name='tests_detail'),

    url(r'^response/$', views.put_list, name='response'),

    path('response1/<str:abc>', views.show_results),


 ]
