from django.shortcuts import render
from app_todolist.utility import query

def view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        deadline = request.POST.get('deadline')
        detail = request.POST.get('detail')

        result = query("INSERT INTO todo_list (title, deadline, detail) VALUES (%s, %s, %s)", [title, deadline, detail])
        print(result)

    return render(request, 'app_todolist/create.html')