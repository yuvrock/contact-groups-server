from django.db import models

#contacts
class Contact(models.Model):
    name = models.TextField('Contact name', max_length=100)
    numbers = models.TextField('Number', max_length=400) #(first number), (2th number), ...

# group
class Group(models.Model):
    name = models.TextField('Name of group', max_length=100)
    contact = models.TextField('list of contacts', max_length=400) # (first contact), (2th contact), ...
