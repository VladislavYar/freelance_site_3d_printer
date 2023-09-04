from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from account.forms import CastomUserCreationForm, CastomUserChangeForm


User = get_user_model()


class SignUpView(CreateView):
    """View регистрации нового пользователя."""
    form_class = CastomUserCreationForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/signup.html'


@login_required
def profile_update(request):
    user = get_object_or_404(User, username=request.user)
    if request.method != 'POST':
        form = CastomUserChangeForm(
            request.POST or None,
            files=request.FILES or None,
            instance=user
        )
        return render(request, 'account/edit.html', {'form': form})
    form = CastomUserChangeForm(
        request.POST or None,
        files=request.FILES or None,
        instance=user
    )
    if not form.is_valid():
        return render(request, 'account/edit.html', {'form': form})
    form.save()
    return redirect('account:profile')


@login_required
def profile(request):
    """View профиля пользователя."""
    username = request.user.username
    user = get_object_or_404(User, username=username)
    context = {
        'user': user,
    }
    return render(request, 'account/profile.html', context)
