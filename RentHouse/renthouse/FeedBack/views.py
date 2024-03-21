from django.shortcuts import render, redirect
from .models import FeedBack
from django.contrib import messages 
from .forms import FeedBackCreateForm

def FeedBack(request):
    if request.method == 'POST':
        form = FeedBackCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeedBackCreateForm()
    return render(request, 'feedback/feedback.html', {'form': form})