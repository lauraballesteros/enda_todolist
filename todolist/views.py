from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from.models import todoItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import requests
from .forms import todoForm
# Create your views here.
def home(request):
    return render(request, 'home.html', {})


@login_required   
def showItems (request):
    all_todo_items = todoItem.objects.filter(author_id=request.user)
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})

@login_required   
def showCompleted (request):
    all_todo_items = todoItem.objects.filter(author_id=request.user,is_completed=True)
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})
    
@login_required   
def showUncompleted (request):
    all_todo_items = todoItem.objects.filter(author_id=request.user,is_completed=False)
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})

@login_required   
def addTodo(request):
    #create a new todo all_items and save it
    #then redirect the browser to /todolist/
    new_item=todoItem(author=request.user,content=request.POST['content'])
    # new_item.author=request.user
    new_item.save()
    return HttpResponseRedirect('/todolist')

@login_required   
def deleteTodo(request, todo_id):
    item_to_delete = todoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todolist')

@login_required   
def cross_off(request,todo_id):
    item_to_cross = todoItem.objects.get(id=todo_id)
    item_to_cross.is_completed = True
    item_to_cross.save()
    return HttpResponseRedirect('/todolist')
    
@login_required   
def uncross(request,todo_id):
    item_to_uncross = todoItem.objects.get(id=todo_id)
    item_to_uncross.is_completed = False
    item_to_uncross.save()
    return HttpResponseRedirect('/todolist')

def translate_to_es(request,todo_id):
    
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    item = todoItem.objects.get(id=todo_id)
    text = item.content.replace(' ','%20')
    payload = "source=en&q="+text+"&target=es"
    headers = {
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': "",
        'accept-encoding': "application/gzip",
        'content-type': "application/x-www-form-urlencoded"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    res=response.json()
    item.content=res['data']['translations'][0]['translatedText']
    item.save(update_fields=['content'])
    return HttpResponseRedirect('/todolist')
    
def translate_to_en(request,todo_id):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    item = todoItem.objects.get(id=todo_id)
    text = item.content.replace(' ','%20')
    payload = "source=es&q="+text+"&target=en"
    headers = {
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': "",
        'accept-encoding': "application/gzip",
        'content-type': "application/x-www-form-urlencoded"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    res=response.json()
    item.content=res['data']['translations'][0]['translatedText']
    item.save(update_fields=['content'])
    return HttpResponseRedirect('/todolist')

@login_required   
def edit_item(request, todo_id):
    if request.method == 'POST':
        item = todoItem.objects.get(id=todo_id)

        item.content = request.POST['item']
        item.save(update_fields=['content'])
        return HttpResponseRedirect('/todolist')
        
    else:
        item = todoItem.objects.get(id=todo_id)
        return render(request, 'edit_item.html',{'item':item})
    