from .filters import CompanyFilter
from django.views import generic
from .models import CompanyDetail, Tests, CompanyTests
from django.shortcuts import render
from django.http import HttpResponse


# for finding companies in a particular area
def home(request):
    return render(request, 'deep_diagnose/user_location.html')


# for showing result --->companies nearby
def result(request):
    company_list = CompanyDetail.objects.all().order_by('company_name')
    company_filter = CompanyFilter(request.GET, queryset=company_list)
    return render(request, 'deep_diagnose/company_list.html', {'filter': company_filter})


# gives list of all the companies
class CompanyList(generic.ListView):
    template_name = 'deep_diagnose/all_companies.html'
    context_object_name = 'all_companies'

    def get_queryset(self):
        return CompanyDetail.objects.all().order_by('company_name')


# gives details about the company->tests,price,contact info
class CompanyDetails(generic.DetailView):
    model = CompanyDetail
    template_name = 'deep_diagnose/company_details.html'
    context_object_name = 'company'


# list of all tests
class TestList(generic.ListView):
    template_name = 'deep_diagnose/all_tests.html'
    context_object_name = 'all_tests'

    def get_queryset(self):
        return Tests.objects.all().order_by('test_name')


# gives details about selected test
class TestDetail(generic.DetailView):
    model = Tests
    template_name = 'deep_diagnose/test_detail.html'
    context_object_name = 'test'


# returns company name on the basis search item in searchbox
def put_list(request):
    polls = Tests.objects.all()
    search_term=''
    if 'search' in request.GET:
        search_term = request.GET['search']
        polls = polls.filter(test_name__icontains=search_term)

    context = {'search_term': search_term, 'polls': polls, }
    return render(request, 'deep_diagnose/base.html', context)


def show_results(request, abc):
    # search=request.GET['search']
    polls = CompanyTests.objects.filter(tests__test_name=abc)
    """search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        polls = polls.filter(test__icontains=search_term)"""

    context = {
        'polls': polls
    }
    return render(request, 'deep_diagnose/base.html', context)













