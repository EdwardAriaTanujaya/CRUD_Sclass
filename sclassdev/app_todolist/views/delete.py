from django.shortcuts import render, redirect
from app_todolist.utility import query

def view(request, id):
    if request.method == 'GET':
        post = query("SELECT * FROM todo_list WHERE id = %s", [id])
        print(post)
        if not post:
            return render(request, 'todo_list/notfound.html', status=404)
        post = query("DELETE FROM todo_list WHERE id = %s", [id])

    return redirect("/todo/list/", name="blog_list")