from rest_framework import serializers
from django.contrib.auth.models import User

from base.models import Dream, Budget, BudgetType


class DreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dream
        fields = ('id',
                  'name',
                  'description',
                  'visibility',
                  'status',
                  'created_by',
                  'created_at',
                  'total_budget'
                  )


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


class UserSerializer(serializers.ModelSerializer):
    dreams = serializers.PrimaryKeyRelatedField(
            many=True,
            queryset=Dream.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'dreams')
