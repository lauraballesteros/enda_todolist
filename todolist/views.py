from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from.models import todoItem
from django.contrib import messages
# Create your views here.
def homeView (request):
    all_todo_items = todoItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})

def addTodo(request):
    #create a new todo all_items and save it
    #then redirect the browser to /todolist/
    new_item=todoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todolist')

def deleteTodo(request, todo_id):
    item_to_delete = todoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todolist')

def cross_off(request,todo_id):
    item_to_cross = todoItem.objects.get(id=todo_id)
    item_to_cross.is_completed = True
    item_to_cross.save()
    return HttpResponseRedirect('/todolist')
    
def uncross(request,todo_id):
    item_to_uncross = todoItem.objects.get(id=todo_id)
    item_to_uncross.is_completed = False
    item_to_uncross.save()
    return HttpResponseRedirect('/todolist')
