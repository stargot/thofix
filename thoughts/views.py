from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Thought


class ThoughtsList(ListView):
    model = Thought
    paginate_by = 30
    template_name = "list.html"


class AddThought(CreateView):
    model = Thought
    fields = ['description']
    template_name = "add.html"
    success_url = "/"