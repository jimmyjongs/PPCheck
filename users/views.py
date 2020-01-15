from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    """
    when the register url is mapped to this function, if it is a GET request
    a form will be rendered. If it is a POST request

    :param request:
    :return:
    """

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created! Log in below.')
            return redirect('login')

    else:
        # django takes care of generating forms and user validation
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# @ denotes a decorator; adds more functionality to a function
@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your user profile has been updated!')
            return redirect('profile')


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)