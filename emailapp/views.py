from django.http import JsonResponse
from django.shortcuts import render,redirect
from .email import get_Email_list,get_Email_by_id, delete_Email_by_id,add_new_email
from .models import Email



def home(request):
    query= request.GET.get('q')
    emails=get_Email_list()
    if query:
         emails=[email for email in emails if query.lower() in email.title.lower()]
    return render(request, 'home.html',{'emails':emails})
def detail_email(request,id):
     email=get_Email_by_id(id)
     return render(request, 'detail_email.html',{'email':email})
def search_email(request):
     query=request.GET.get('q')
     
     return JsonResponse({
          'query':query
         
     })
def delete_email(request,id):
     if request.method=="POST":     
          delete_Email_by_id(id)
     return redirect('home')
def add_email(request):
    if request.method == 'POST':
       
        title = request.POST.get('title')
        description = request.POST.get('description')
       
        import datetime
        current_time = datetime.datetime.now().strftime("%d/%m/%Y") 
        
       
        add_new_email(title, description, current_time)

        return redirect('home')
        

    return redirect('home')