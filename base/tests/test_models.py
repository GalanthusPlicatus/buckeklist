from django.test import TestCase, RequestFactory, Client
from base.models import Dream, Budget, BudgetType


class ModelTestCase(TestCase):
    def test_dream_model(self):
        # check dream model is created
        self.assertEqual(Dream.objects.count(), 0)
        # create dream object
        dream = Dream.objects.create(
            name="trip to coimbatore",
            description="chilling out",
        )
        self.assertEqual(Dream.objects.count(), 1)
        self.assertEqual(dream.status, 1)
        self.assertEqual(dream.visibility, 0)

        # print dream.created_by

    def test_calcalation_of_budget(self):
        self.assertEqual(Dream.objects.count(), 0)
        # create dream object
        dream = Dream.objects.create(
            name="trip to coimbatore",
            description="chilling out",
        )
        self.assertEqual(Budget.objects.count(), 0)
        budget = Budget.objects.create(
            amount=2000.00,
            dream=dream
        )
        budget_type = BudgetType.objects.create(
            name='food'
        )
        self.assertEqual(Budget.objects.count(), 1)
        self.assertEqual(Dream.objects.count(), 1)
        # print dream


