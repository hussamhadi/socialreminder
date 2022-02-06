from django.urls import path
from django.views.generic import TemplateView

from .views import (
    MessageView, MessagesView,
    PersonView, PersonsView,
    TagView, TagsView
)

urlpatterns = [
    path("messages/", MessagesView.as_view(), name="messages"),
    path("message/<int:pk>/", MessageView.as_view(), name="message"),
    path("persons/", PersonsView.as_view(), name="persons"),
    path("person/<int:pk>/", PersonView.as_view(), name="person"),
    path("tags/", TagsView.as_view(), name="tags"),
    path("tag/<int:pk>/", TagView.as_view(), name="tag"),
    path("", TemplateView.as_view(template_name="base.html"), name="base"),
]
