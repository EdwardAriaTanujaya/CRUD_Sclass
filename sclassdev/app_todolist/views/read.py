from django.shortcuts import render
from app_todolist.utility import query

def view(request, id):
    if request.method == 'GET':  # Retrieve 'id' from query parameters
        post = query("SELECT * FROM todo_list WHERE id = %s", [id])
        if post:
            return render(request, 'app_todolist/read.html', {
            'post': post[0]
        })
    
    return render(request, 'app_todolist/notfound.html', status=404)
    
    