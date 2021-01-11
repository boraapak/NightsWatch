from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from ..models import Movie, Comment


def index(request):
    movies = Movie.objects.all()
    return render(request, "movie_list.html", {
        'movies': movies
    })


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    comments = comment(request, movie_id, shouldRender=False)
    return render(request, "movie_detail.html", {
        'movie': movie,
        'comments': comments
    })


def comment(request, movie_id, shouldRender=True):
    if request.method == "POST":
        content = request.POST['content'] if 'content' in request.POST else None
        if content is not None:
            comment = Comment(created_by=request.user,
                              content=content, movie_id=movie_id)
            comment.save()

        next_page = request.POST['next']
        return redirect(next_page)
    else:
        comments = Comment.objects.filter(
            movie__id=movie_id).order_by("-created_date").all()
        if shouldRender:
            return render(request, "movie_comments.html", {
                'comments': comments,
                'movie_id': movie_id
            })
        return comments
