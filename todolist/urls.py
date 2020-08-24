from django.urls import path
from todolist.views import showItems, addTodo, deleteTodo, cross_off, uncross

urlpatterns = [
    path('todolist/',showItems, name = 'list'),
    path('addTodo/',addTodo),
    path('deleteTodo/<int:todo_id>/',deleteTodo),
    path('cross_off/<int:todo_id>/',cross_off),
    path('uncross/<int:todo_id>/',uncross),
]
