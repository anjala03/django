from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getting_start(request):
    return render (request, "home/index.html", context={"peoples":peoples})
#http response is not feasible for all, hence the render
peoples=[
      {"name":"anjala", "age":22},
      {"name":"ajita", "age":24},
      {"name":"asmita", "age":26},
      {"name":"adarsh", "age":12}
]
def another_demo(request):
        print('hihihihihih')
        return HttpResponse ("<h1> Welcome its just a testing one, sorry to bother </h1>")