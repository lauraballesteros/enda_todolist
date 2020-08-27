from django.urls import path
from todolist.views import showItems, addTodo, deleteTodo, cross_off, uncross, home, showCompleted, showUncompleted, translate_to_en

urlpatterns = [
    
    path('todolist/',showItems, name = 'list'),
    path('showCompleted/',showCompleted),
    path('showUncompleted/',showUncompleted),
    path('addTodo/',addTodo),
    path('deleteTodo/<int:todo_id>/',deleteTodo),
    path('cross_off/<int:todo_id>/',cross_off),
    path('uncross/<int:todo_id>/',uncross),
    path('translate_to_en/<int:todo_id>/',translate_to_en),
    path('',home, name = 'home'),
]
