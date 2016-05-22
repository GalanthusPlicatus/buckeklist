from rest_framework import serializers

from base.models import Dream
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class DreamSerializer(serializers.ModelSerializer):
    id = IntegerField(label='ID', read_only=True)
    name = CharField(max_length=200, read_only=True)

    class Meta:
        model = Dream
        fields = ('id', 'name')
