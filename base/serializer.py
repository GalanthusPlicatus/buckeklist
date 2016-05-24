from rest_framework import serializers

from base.models import Dream, Budget, BudgetType
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class DreamSerializer(serializers.ModelSerializer):
    # id = IntegerField(label='ID', read_only=True)
    # name = CharField(max_length=200, read_only=True)

    class Meta:
        model = Dream
        fields = ('id', 'name')


class BudgetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetType
        fields = ('id', 'name')


class BudgetSerializer(serializers.ModelSerializer):
    dream = DreamSerializer()
    budget_type = BudgetTypeSerializer()

    class Meta:
        model = Budget
        fields = ('id', 'amount', 'dream', 'budget_type')
