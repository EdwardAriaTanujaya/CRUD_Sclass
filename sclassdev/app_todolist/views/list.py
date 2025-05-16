from django.shortcuts import render
from app_todolist.utility import query

def view(request):
    if request.method == 'GET':
        posts = query("SELECT * FROM todo_list ORDER BY deadline ASC")
    return render(request, 'app_todolist/list.html', {
        'posts': posts,
    })