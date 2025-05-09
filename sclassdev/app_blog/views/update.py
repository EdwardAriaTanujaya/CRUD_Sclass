from django.shortcuts import render, redirect
from app_blog.utility import query

def view(request, id):
        post = query("SELECT * FROM blog_post WHERE id = %s", [id])
        print(post)

        if not post:
            return render(request, 'app_blog/notfound.html', status=404)
        
        post = post[0] if post else None

        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')

            query('UPDATE blog_post SET title = %s, content = %s WHERE id = %s', [title,content,id])

            return redirect(f"/blog/read/{id}")
        
        return render(request, "app_blog/update.html", {"post": post})