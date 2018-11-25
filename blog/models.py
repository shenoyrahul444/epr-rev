from django.db.models import *


class Author(Model):
    first_name = CharField(max_length=40)
    last_name = CharField(max_length=40)
    organization = CharField(max_length= 40)
    description = CharField(max_length=120)

    def __str__(self):
        return self.first_name + "  " + self.last_name

class Post(Model):
    title = CharField(max_length=140)
    body = TextField()
    date = DateField()
    auth_id = ForeignKey(Author, on_delete=CASCADE)

    def __str__(self):
        return self.title