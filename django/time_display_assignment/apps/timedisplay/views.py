from django.shortcuts import render, HttpResponse, redirect
import datetime
  

# def speak(request):
#    print "Hello, I am your first request!"
#    return render(request,'index.html')

def show(request):
    print request.method
    return render(request, 'show_users.html')

 
def get_time(request):
	time = datetime.datetime.now()
	context = {
	"somekey": time
	}
	return render(request,'index.html', context)

def create(request):
 if request.method == "POST":
  print "*"*50
  print request.POST
  print request.method
  print "*"*50
  request.session['name'] = request.POST['first_name']
  return redirect("/")
 else:
  return redirect("/")	

