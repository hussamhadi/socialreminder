from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Message, Person, Tag


class MessageView(DetailView):
    """
    Detail view of a Person object
    """
    model = Message


class MessagesView(ListView):
    """
    A view to list all Person objects
    """
    model = Message


class PersonView(DetailView):
    """
    Detail view of a Person object
    """
    model = Person


class PersonsView(ListView):
    """
    A view to list all Person objects
    """
    model = Person


class TagView(DetailView):
    """
    Detail view of a Tag object
    """
    model = Tag


class TagsView(ListView):
    """
    A view to list all Tag objects
    """
    model = Tag

