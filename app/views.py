from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'name':"loki","age":12}
    return render(request,'condition.html',context=d)
def loop(request):
    s={'name':"sneha","age":21}
    return render(request,'loop.html',context=s)