from django.contrib.auth. models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.contrib.auth import logout
from django.template.response import TemplateResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/sign/login/'


def logout_view(request):
    logout(request)
    return TemplateResponse(request,'logout.html')


@login_required
def upgrate_me(request):
    user = request.user
    author_group = Group.objects.get(name='author')
    if not request.user.groups.filter(name='author').exists():
        author_group.user_set.add(user)
    return HttpResponseRedirect('/')







