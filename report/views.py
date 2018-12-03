from django.shortcuts import render

# Create your views here.

def snpsector(request):
    return render(request, 'report/snpsector.html', {})
    
def snpsectorwip(request):
    return render(request,'report/snspsectorwip.html',{})
