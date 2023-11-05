from django.shortcuts import render, redirect
from .models import Bookshelfgit
from .forms import BookshelfForm


def Books_upload(request):
    if request.method == "POST":
        form = BookshelfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Books_list')
        else:
            form = BookshelfForm()
        return render(request, 'Books_upload.html', {'form': form})


def Books_list(request):
    images = Bookshelf.objects.all()
    return render(request, 'Books_list.html', {'Bookshelf': Bookshelf})
