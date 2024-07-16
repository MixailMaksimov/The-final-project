from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import Student


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            logout(request)  # Разлогинить текущего пользователя
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                form = LoginForm()  # Очистить форму
                return redirect('requests:index')  # Перенаправление на личный кабинет после успешного входа
    else:
        form = LoginForm()
    return render(request, 'personal_account/login.html', {'form': form})


@login_required
def profile(request):
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)

        context = {
            'student': student,
        }
        return render(request, 'personal_account/profile.html', context)
    else:
        return redirect('login')  # Перенаправить на страницу входа, если пользователь не аутентифицирован


def user_logout(request):
    logout(request)
    return redirect('login')
