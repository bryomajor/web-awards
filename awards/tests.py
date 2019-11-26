from django.test import TestCase
from .models import Profile,Projects,Rates


class ProfileTestClass(TestCase):
    def setUp(self):
        self.wanjiku = Profile(profile_photo='default.jpg',bio='heey its me', phone_number='0797803412')

    def test_instance(self):
        self.assertTrue(isinstance(self.wanjiku,Profile))

    def test_save(self):
        self.wanjiku.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
 

class ProjectsTestClass(TestCase):
    def setUp(self):
        self.wanjiku = Profile()
        self.wanjiku.save_profile()

        self.new_project =Projects(description="testing testing 1,2",profile=self.wanjiku)
        self.new_project.save()

    def tearDown(self):
        Profile.objects.all().delete()
        Projects.objects.all().delete()    

    def test_projects(self):
        projects = Projects.objects.all()
        self.assertTrue(len(projects)>0)


class RatesTestClass(TestCase):
    def setUp(self):
        self.user = User(username='john',email='john@gmail.com',password='12345')
        
        self.rate = Rates(design=10,usability=10,content=10,user=self.user,project=10)
        self.rate.save()
        
        self.assertTrue(isinstance(self.rate,Rate))        
