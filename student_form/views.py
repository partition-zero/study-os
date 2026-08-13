from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import StudentState, Availability
from  .forms import add_form , AvailabilityForm

# Create your views here.
def home_page(request):
    return render(request, 'index.html')


def register_student(request):
    form=add_form()
    if request.method == "POST":
        form =add_form(request.POST)
        if form.is_valid():
            student=form.save()
            return redirect('add-availability', pk=student.pk)
    else:
        form = add_form()
    return render(request, 'form.html', {'form': form})


def add_availability(request, pk):
    student = get_object_or_404(StudentState, pk=pk)

    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)  # don't save yet
            availability.student = student           # attach the student
            availability.save()                      # now save
            return redirect('student-schedule', pk=student.pk)
    else:
        form = AvailabilityForm()

    return render(request, 'availability.html', {'form': form, 'student': student})


def student_schedule(request, pk):
    student = get_object_or_404(StudentState, pk=pk)
    availabilities = student.availabilities.all()#type:ignore
    return render(request, 'schedule.html', {
        'student': student,
        'availabilities': availabilities,
    })