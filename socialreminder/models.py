from django.db import models


class Tag(models.Model):
    """
    Simple tag object for adding tags to other models
    """
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):
    """
    Represents a person
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField()
    tag = models.ManyToManyField(Tag, related_name="person", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_tags(self):
        return "to be defined"


class Message(models.Model):
    """
    A message that can be sent
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ManyToManyField(Tag, related_name="message", blank=True)

    def __str__(self):
        return f"{self.title}"
