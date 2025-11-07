
# Create your views here.
from django.shortcuts import render
from datetime import datetime

def home(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, "index.html", {"time": current_time})
