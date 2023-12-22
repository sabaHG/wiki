from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Photo
from .forms import PhotoForm, CommentForm
from django.contrib.auth.decorators import login_required

def gallery(request):
    gallery = Photo.objects.all()
    return render(request, 'gallery/gallery.html', {'gallery': gallery})

def detail(request, slug):
    # Используйте slug для поиска фото в базе данных
    photo = get_object_or_404(Photo, slug=slug)
    return render(request, "gallery/photo_detail.html", {"photo": photo})


@login_required
def add(request):
    error = ''
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
        else:
            data = {
                'form': form,
                'error': 'Invalid form data. Please correct the errors below.',
            }
            return render(request, 'gallery/add.html', data)
    else:
        form = PhotoForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'gallery/add.html', data)

@login_required
def add_comment(request, slug):
    post = get_object_or_404(Photo, slug=slug)
    comment = None
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect(reverse("detail", args=[post.slug]))
    else:
        form = CommentForm()
    return render(
        request,
        "add_comment.html",
        {
            "form": form,
            "post": post,
            "comment": comment,
        },
    )
