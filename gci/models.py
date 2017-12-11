from django.db import models

#contacts
class Contact(models.Model):
    name = models.CharField('Contact name', max_length=100)
    numbers = models.TextField('Number', max_length=400) #(first number), (2th number), ...

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

# group
class Group(models.Model):
    name = models.CharField('Name of group', max_length=100)
    contact = models.TextField('List of contacts', max_length=400) # (first contact), (2th contact), ...

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'group'
        verbose_name_plural = 'groups'
