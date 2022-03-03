from django.shortcuts import render

# Create your views here.

def count_view(request):
    count=int(request.COOKIES.get('count',0))
    newcount=count+1
    response = render(request,'cookie_app/home.html',{'count':newcount})
    response.set_cookie('count',newcount,max_age=180)
    return response


