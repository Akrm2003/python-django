from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
	return render(request, 'hello.html', {'name': 'akrm'}) ### try without dictionarys
	# return render(request, 'hello.html')

### note : if u render the same file twice the first rendering happens and the second gets ignored
# Create your views here.
#### a view function takes a request and returns a response ####
#### request handler ####