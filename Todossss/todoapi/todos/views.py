from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import todo_list

# Create your views here.
def todos(request):
    todos_list=todo_list.objects.all()
    data = {
        "todos":list(todos_list.values( "todo" , "status"))
    }
    return JsonResponse(data)

def single_todo(request, pk):
    todo = get_object_or_404(todo_list, pk=pk)
    data={
        "todo" : todo.todo, 
        "status" : todo.status
    }
    return JsonResponse(data)