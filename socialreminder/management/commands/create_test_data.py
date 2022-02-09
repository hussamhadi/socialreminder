from django.core.management.base import BaseCommand
from ...util.factories import MessageFactory, PersonFactory, TagFactory, TAGS
from ...models import Person


class Command(BaseCommand):
    """
    Generates test data in the sqlite DB
    """
    help = "Generates test data in the sqlite DB"

    def handle(self, *args, **options):
        count = Person.objects.count()
        if count > 100:
            self.stderr.write("It appears you already have enough data populated")
            return
        tags = TagFactory.create_batch(size=10)
        for _ in range(100):
            PersonFactory(tags=tags[:2])
            MessageFactory(tags=tags)

        self.stdout.write("100 Person objects created")
