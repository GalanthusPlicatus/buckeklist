from base.models import Dream, Budget, BudgetType
from django.test import TestCase, RequestFactory, Client

""" Goals

- The goals of the kind of testing outlined here are simplicity,loose or no
coupling, and speed:
- Tests should be as simple as possible, while exercising the
application-under-test (AUT) completely.
- Tests should run as quickly as possible,to encourage running them frequently.
- Tests should avoid coupling with other tests, or with parts of the AUT which
they are not responsible for testing.

"""


class ModelTestCase(TestCase):
    """TestCases to test Dream,Budget,BudgetType models.
    whenever a dream is created, Budgettype(expenses) and
    Budget also created."""

    def test_dream_model(self):
        "Test to check dream's status and visibility default."
        # check dream model is created
        self.assertEqual(Dream.objects.count(), 0)
        # create dream object
        dream = Dream.objects.create(
            name="trip to coimbatore",
            description="chilling out",
        )
        self.assertEqual(Dream.objects.count(), 1)
        self.assertEqual(dream.status, 'CRD')
        self.assertEqual(dream.visibility, 'PUB')

        # print dream.created_by

    def test_calcalation_of_budget_one_budgettype(self):
        "Test to check total budget calculation with one type of expense."
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
        self.assertEqual(dream.total_budget, 2000.00)
        # print dream.total_budget

    def test_calcalation_of_budget_many_budgettype(self):
        """Test to check total budget calculation with multiple type of
        expenses.
        """
        self.assertEqual(Dream.objects.count(), 0)
        # create dream object
        dream = Dream.objects.create(
            name="trip to coimbatore",
            description="chilling out",
        )
        self.assertEqual(Budget.objects.count(), 0)
        budget_type1 = BudgetType.objects.create(
            name='food'
        )
        budget_type2 = BudgetType.objects.create(
            name='travel'
        )
        budget_type3 = BudgetType.objects.create(
            name='stay'
        )
        budget1 = Budget.objects.create(
            budget_type=budget_type1,
            amount=2000.00,
            dream=dream
        )
        budget2 = Budget.objects.create(
            budget_type=budget_type2,
            amount=4000.00,
            dream=dream
        )
        budget3 = Budget.objects.create(
            budget_type=budget_type3,
            amount=5000.00,
            dream=dream
        )

        self.assertEqual(Budget.objects.count(), 3)
        self.assertEqual(
            Budget.objects.count(),
            BudgetType.objects.count()
        )
        self.assertEqual(Dream.objects.count(), 1)
        self.assertEqual(dream.total_budget, 11000.00)
        # print dream.total_budget

    def test_budgettype_str_representation(self):
        bt = BudgetType(name='travel')
        self.assertEqual(str(bt), 'travel')

    def test_dream_str_representation(self):
        d = Dream(
            name='test_dream',
            description="chilling out",
        )
        self.assertEqual(str(d), 'test_dream')

    def test_budget_str_representation(self):
        d = Dream(
            name='test_dream',
            description="chilling out",
        )
        bt = BudgetType(name='travel')
        b = Budget(
            budget_type=bt,
            dream=d,
            amount=21.0
        )
        self.assertEqual(str(b), '21.0 test_dream')
