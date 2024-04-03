from django.http import HttpResponse
from django.shortcuts import render

# Example view that returns a simple HttpResponse
def monitoring_view(request):
    # You can integrate your monitoring logic here
    return HttpResponse("Welcome to TH Monitoring Dashboard.")
