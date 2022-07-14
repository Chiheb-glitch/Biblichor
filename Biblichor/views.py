from django.shortcuts import render 

def home (request):

	return render (request ,'Home.html')
def help (request):
	return render (request ,'help.html')
def underconst (request):
	return render (request ,'under.html')