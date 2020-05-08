from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.authorization.forms.sign_up import SignUpForm
from apps.authorization.utils.verification import start_verification


class SignUpView(FormView):
    template_name = "authorization/sign_up.html"
    form_class = SignUpForm
    success_url = reverse_lazy("authorization:sign_up_confirmed")

    @transaction.atomic()
    def form_valid(self, form):
        user = form.save()
        start_verification(self.request, user)
        return super().form_valid(form)
