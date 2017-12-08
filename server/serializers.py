from rest_framework import serializers

from server.models import Contact, Group, ContactNumber


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class ContactNumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactNumber
        fields = ('number',)


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)
    numbers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Contact
        fields = ('name', 'groups', 'numbers')
