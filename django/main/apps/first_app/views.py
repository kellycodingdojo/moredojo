from django.shortcuts import render, HttpResponse
  # Create your views here.
def index(request):
   print "Hello, I am your first request!"
   return render(request,'my_first_app/index.html')

def show(request):
   print request.method
   return render(request, 'my_first_app/show_users.html')