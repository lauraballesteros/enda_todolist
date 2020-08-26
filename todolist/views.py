from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from.models import todoItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

@login_required   
def showItems (request):
    all_todo_items = todoItem.objects.filter(author_id=request.user)
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
