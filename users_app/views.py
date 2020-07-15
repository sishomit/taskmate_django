from django.shortcuts import render, redirect
from django.contrib import messages
from users_app.forms import custom_reg_form


def register(request):
    if request.method == 'POST':
        register_form = custom_reg_form(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'New User Created! You Can Log In Now')
            return redirect('login')

    else:
        register_form = custom_reg_form()
    return render(request, 'register.html', {'register_form': register_form})


def change_password(request):
    if request.method == 'POST':
        change_form = change_p_form(request.POST)
        if change_form.is_valid():
            change_form.save()
            messages.success(request, 'Password has been changed!')
            return redirect('todolist')
        else:
            change_form = change_p_form()
    return render(request, 'change_password.html', {'change_form': change_form})
