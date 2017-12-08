from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    group = models.ManyToManyField(Group)


class ContactNumber(models.Model):
    number = models.DecimalField(max_digits=20, decimal_places=0)
    contact = models.ForeignKey(Contact, related_name='numbers', on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.number)
