from django.shortcuts import render, redirect
from app_todolist.utility import query

def view(request, id):
        post = query("SELECT * FROM todo_list WHERE id = %s", [id])
        print(post)

        if not post:
            return render(request, 'app_todolist/notfound.html', status=404)
        
        post = post[0] if post else None
  
        if request.method == 'POST':
            title = request.POST.get('title')
            deadline = request.POST.get('deadline')
            detail = request.POST.get('detail')

            query('UPDATE todo_list SET title = %s, deadline = %s, detail = %s WHERE id = %s', [title,deadline,detail,id])

            return redirect(f"/todo/read/{id}")
        
        return render(request, "app_todolist/update.html", {"post": post})