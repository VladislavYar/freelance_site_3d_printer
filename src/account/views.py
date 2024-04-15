from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.timezone import localdate
from django.views.generic import CreateView

from account.forms import CastomUserChangeForm, CastomUserCreationForm
from account.models import User as ClassUser
from order.models import Order

User = get_user_model()


class SignUpView(CreateView):
    """View регистрации нового пользователя."""
    form_class = CastomUserCreationForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/signup.html'


@login_required
def profile_update(request):
    if request.method != 'POST':
        form = CastomUserChangeForm(
            request.POST or None,
            files=request.FILES or None,
            instance=request.user
        )
        return render(request, 'account/edit.html', {'form': form})
    form = CastomUserChangeForm(
        request.POST or None,
        files=request.FILES or None,
        instance=request.user
    )
    if not form.is_valid():
        return render(request, 'account/edit.html', {'form': form})
    form.save()
    return redirect('account:profile')


def get_orders(user: ClassUser) -> tuple[list[Order]]:
    """Отдаёт заказы/предложения."""
    orders = Order.objects.filter(user_id=user)
    orders_customer = []
    orders_no_customer = []
    for order in orders:
        order.days_left = settings.DAYS_LIFE_ORDER - (
            localdate() - order.date
            ).days
        if order.is_customer:
            orders_customer.append(order)
            continue
        orders_no_customer.append(order)
    return orders_customer, orders_no_customer


@login_required
def profile(request):
    """View профиля пользователя."""
    user = request.user
    orders_customer, orders_no_customer = get_orders(user)
    context = {
        'user': user,
        'orders_customer': orders_customer,
        'orders_no_customer': orders_no_customer,

    }
    return render(request, 'account/profile.html', context)
