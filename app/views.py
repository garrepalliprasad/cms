from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# home view
def home(request):
    return render(request,'home.html')

# backend view
@login_required(login_url='backend')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def backend(request):
    return render(request,'backend.html')