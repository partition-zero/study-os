from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from  .forms import S_form

# Create your views here.
def init_form(request):
    form=S_form()
    if request.method == "POST":
        form = S_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Your Data has been Recordered. Proceed Further") #type: ignore

    return render(request, 'form.html', {'form': form})
