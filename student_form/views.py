from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def landing_view(request):
    # If they are already logged in, skip the home page and go to dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'landing.html')

def login_action(request):
    if request.method == 'POST':
        # For the overnight build, we'll extract the data from the form
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Note: Django uses 'username' by default, you may need to map email to username
        # or use a custom user model. Assuming standard setup for now:
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Send them back with an error (keep it simple for now)
            return render(request, 'landing.html', {'error': 'Invalid credentials'})

    return redirect('landing')

def logout_action(request):
    logout(request)
    return redirect('landing')

@login_required(login_url='landing')
def dashboard_view(request):
    return render(request, 'dashboard.html')