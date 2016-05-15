from django.test import TestCase, RequestFactory, Client

class ModelTestCase(TestCase):


    def test_dream_model(self):
        #check dream model is created
        self.assertEqual(Dream.objects.count(),0)
        #create dream object
        dream = Dream.objects.create(
            name="trip to coimbatore",
            description="chilling out",
        )
        self.assertEqual(Dream.objects.count(),1)
        self.assertEqual(dream.status,1)
        pass
        
