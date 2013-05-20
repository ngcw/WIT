from django.http import HttpResponse
from LibraryTraffic.models import *
from django.template import Context, loader
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

@csrf_protect
def index(request):
    if request.method != "POST":
        return render(request, 'login.html')
    if 'UniEmail' in request.POST:
    	Submitted_Email = request.POST['UniEmail'] 
    	Submitted_Pas = request.POST['Password']             
    	Users = User.objects.all()
    	for user in Users:
    	    if Submitted_Email == user.UniEmail and Submitted_Pas == user.Password:	
		return redirect('/LibraryTraffic/mainpage')
	
    	return render(request, "login.html", {'match_error': '1'})

    
    
def mainpage(request):
    Libraries = Library.objects.all()
    template = loader.get_template('LibraryTraffic/mainpage.html')
    context = Context({
		    'Libraries': Libraries,
		})
    return HttpResponse(template.render(context))		
    
def detail(request, Library_id):
    LibraryDetails =  Library.objects.filter(id=Library_id)
    template = loader.get_template('LibraryTraffic/library_info.html')
    context = Context({
        'Library': LibraryDetails[0],
    })
    return HttpResponse(template.render(context))
    
    
def bookroom(request, Library_id):
    LibraryRooms =  Room.objects.filter(Library=Library_id)
    Libraries = Library.objects.filter(id=Library_id)
    template = loader.get_template('LibraryTraffic/bookroom.html')
    context = Context({
        'LibraryRooms': LibraryRooms,
        'Libraries'  : Libraries[0],
    })
    return HttpResponse(template.render(context))     
