from ..models import Message, Person, Tag

import factory
import random

TAGS = ["family", "friend", "best friends", "abroad", "social connections", "coworkers", "gym buddies", "IT club"]


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message

    title = factory.Faker("sentence", nb_words=5)
    content = factory.Faker("sentence", nb_words=30)

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.tag.add(tag)


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    birthday = factory.Faker("date_of_birth", minimum_age=10, maximum_age=40)
    frequency = factory.LazyFunction(lambda: random.choice(Person.FREQUENCY)[0])

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.tag.add(tag)


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Faker("sentence", nb_words=2)
