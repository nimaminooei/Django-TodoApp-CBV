from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from faker import Faker
import random
from todo.models import Tasks
class Command(BaseCommand):
    help = "insert fake data into database"
    def __init__(self,*args,**kwargs):
        super(Command, self).__init__(*args,**kwargs)
        self.fake = Faker(['it_IT', 'ja_JP'])
    def handle(self, *args, **options):
        user = User.objects.get(id=5)
        for i in range(5):
            Tasks.objects.create(
                user = user,
                task = self.fake.paragraph(nb_sentences=2),
                status = random.choice([True, False])
            )
        print("5 task added to nima user")