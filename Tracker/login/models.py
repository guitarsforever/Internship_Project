from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default = '')
    city = models.CharField(max_length=100, default = '')
    website = models.URLField(default = '')
    phone = models.IntegerField(default = 0)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class ProductReadiness(models.Model):
    Poc1 = models.CharField(max_length=100, default='Michael Vigliotti')
    Poc1_email = models.EmailField(max_length=100, default='m.vigliotti@samsung.com')
    poc2 = models.CharField(max_length=100, default='Patrick Koo')
    poc3_email = models.EmailField(max_length=100, default='patrick.koo@samsung.com')
    Task1_Name = models.CharField(max_length=100, blank=True,default='Project Kickoff Meeting')
    Task1_Start_Date = models.DateField(blank=True, null=True)
    Task1_End_Date = models.DateField(blank=True, null=True)
    Task1_complete_date = models.DateField(blank=True, null=True)
    Task1_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task2_Name = models.CharField(max_length=100, blank=True, default='Receive PR Samples from HQ')
    Task2_Start_Date = models.DateField(blank=True, null=True)
    Task2_End_Date = models.DateField(blank=True, null=True)
    Task2_complete_date = models.DateField(blank=True, null=True)
    Task2_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task3_Name = models.CharField(max_length=100,blank=True, default='Develop Schedule and requirements')
    Task3_Start_Date = models.DateField(blank=True, null=True)
    Task3_End_Date = models.DateField(blank=True, null=True)
    Task3_complete_date = models.DateField(blank=True, null=True)
    Task3_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task4_Name = models.CharField(max_length=100, blank=True, default='Determine Field Test Requirement')
    Task4_Start_Date = models.DateField(blank=True, null=True)
    Task4_End_Date = models.DateField(blank=True, null=True)
    Task4_complete_date = models.DateField(blank=True, null=True)
    Task4_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task5_Name = models.CharField(max_length=100, blank=True, default='Marketing Deck Distribution')
    Task5_Start_Date = models.DateField(blank=True, null=True)
    Task5_End_Date = models.DateField(blank=True, null=True)
    Task5_complete_date = models.DateField(blank=True, null=True)
    Task5_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task6_Name = models.CharField(max_length=100, blank=True, default='User Manual Distribution')
    Task6_Start_Date = models.DateField(blank=True, null=True)
    Task6_End_Date = models.DateField(blank=True, null=True)
    Task6_complete_date = models.DateField(blank=True, null=True)
    Task6_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task7_Name = models.CharField(max_length=100, blank=True, default='Distribute Full List of SKUs')
    Task7_Start_Date = models.DateField(blank=True, null=True)
    Task7_End_Date = models.DateField(blank=True, null=True)
    Task7_complete_date = models.DateField(blank=True, null=True)
    Task7_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task8_Name = models.CharField(max_length=100, blank=True, default='Production Samples (order/Send)')
    Task8_Start_Date = models.DateField(blank=True, null=True)
    Task8_End_Date = models.DateField(blank=True, null=True)
    Task8_complete_date = models.DateField(blank=True, null=True)
    Task8_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task9_Name = models.CharField(max_length=100, blank=True, default='User Manuals (on.com)(received)')
    Task9_Start_Date = models.DateField(blank=True, null=True)
    Task9_End_Date = models.DateField(blank=True, null=True)
    Task9_complete_date = models.DateField(blank=True, null=True)
    Task9_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task10_Name = models.CharField(max_length=100, blank=True, default='')
    Task10_Start_Date = models.DateField(blank=True, null=True)
    Task10_End_Date = models.DateField(blank=True, null=True)
    Task10_complete_date = models.DateField(blank=True, null=True)
    Task10_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task11_Name = models.CharField(max_length=100, blank=True, default='')
    Task11_Start_Date = models.DateField(blank=True, null=True)
    Task11_End_Date = models.DateField(blank=True, null=True)
    Task11_complete_date = models.DateField(blank=True, null=True)
    Task11_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task12_Name = models.CharField(max_length=100, blank=True, default='')
    Task12_Start_Date = models.DateField(blank=True, null=True)
    Task12_End_Date = models.DateField(blank=True, null=True)
    Task12_complete_date = models.DateField(blank=True, null=True)
    Task12_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task13_Name = models.CharField(max_length=100, blank=True, default='')
    Task13_Start_Date = models.DateField(blank=True, null=True)
    Task13_End_Date = models.DateField(blank=True, null=True)
    Task13_complete_date = models.DateField(blank=True, null=True)
    Task13_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task14_Name = models.CharField(max_length=100, blank=True, default='')
    Task14_Start_Date = models.DateField(blank=True, null=True)
    Task14_End_Date = models.DateField(blank=True, null=True)
    Task14_complete_date = models.DateField(blank=True, null=True)
    Task14_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task15_Name = models.CharField(max_length=100, blank=True, default='')
    Task15_Start_Date = models.DateField(blank=True, null=True)
    Task15_End_Date = models.DateField(blank=True, null=True)
    Task15_complete_date = models.DateField(blank=True, null=True)
    Task15_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task16_Name = models.CharField(max_length=100, blank=True, default='')
    Task16_Start_Date = models.DateField(blank=True, null=True)
    Task16_End_Date = models.DateField(blank=True, null=True)
    Task16_complete_date = models.DateField(blank=True, null=True)
    Task16_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task17_Name = models.CharField(max_length=100, blank=True, default='')
    Task17_Start_Date = models.DateField(blank=True, null=True)
    Task17_End_Date = models.DateField(blank=True, null=True)
    Task17_complete_date = models.DateField(blank=True, null=True)
    Task17_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task18_Name = models.CharField(max_length=100, blank=True, default='')
    Task18_Start_Date = models.DateField(blank=True, null=True)
    Task18_End_Date = models.DateField(blank=True, null=True)
    Task18_complete_date = models.DateField(blank=True, null=True)
    Task18_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task19_Name = models.CharField(max_length=100, blank=True, default='')
    Task19_Start_Date = models.DateField(blank=True, null=True)
    Task19_End_Date = models.DateField(blank=True, null=True)
    Task19_complete_date = models.DateField(blank=True, null=True)
    Task19_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task20_Name = models.CharField(max_length=100, blank=True, default='')
    Task20_Start_Date = models.DateField(blank=True, null=True)
    Task20_End_Date = models.DateField(blank=True, null=True)
    Task20_complete_date = models.DateField(blank=True, null=True)
    Task20_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Time_Delta_For_Warning = models.IntegerField(default=7)
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    Task1_warning = models.BooleanField(default=False)
    Task2_warning = models.BooleanField(default=False)
    Task3_warning = models.BooleanField(default=False)
    Task4_warning = models.BooleanField(default=False)
    Task5_warning = models.BooleanField(default=False)
    Task6_warning = models.BooleanField(default=False)
    Task7_warning = models.BooleanField(default=False)
    Task8_warning = models.BooleanField(default=False)
    Task9_warning = models.BooleanField(default=False)
    Task10_warning = models.BooleanField(default=False)
    Task11_warning = models.BooleanField(default=False)
    Task12_warning = models.BooleanField(default=False)
    Task13_warning = models.BooleanField(default=False)
    Task14_warning = models.BooleanField(default=False)
    Task15_warning = models.BooleanField(default=False)
    Task16_warning = models.BooleanField(default=False)
    Task17_warning = models.BooleanField(default=False)
    Task18_warning = models.BooleanField(default=False)
    Task19_warning = models.BooleanField(default=False)
    Task20_warning = models.BooleanField(default=False)
    Task1_alert = models.BooleanField(default=False)
    Task2_alert = models.BooleanField(default=False)
    Task3_alert = models.BooleanField(default=False)
    Task4_alert = models.BooleanField(default=False)
    Task5_alert = models.BooleanField(default=False)
    Task6_alert = models.BooleanField(default=False)
    Task7_alert = models.BooleanField(default=False)
    Task8_alert = models.BooleanField(default=False)
    Task9_alert = models.BooleanField(default=False)
    Task10_alert = models.BooleanField(default=False)
    Task11_alert = models.BooleanField(default=False)
    Task12_alert = models.BooleanField(default=False)
    Task13_alert = models.BooleanField(default=False)
    Task14_alert = models.BooleanField(default=False)
    Task15_alert = models.BooleanField(default=False)
    Task16_alert = models.BooleanField(default=False)
    Task17_alert = models.BooleanField(default=False)
    Task18_alert = models.BooleanField(default=False)
    Task19_alert = models.BooleanField(default=False)
    Task20_alert = models.BooleanField(default=False)
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')


class Task1StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task2StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task3StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task4StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task5StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task6StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task7StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task8StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task9StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task10StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task11StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task12StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task13StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task14StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task15StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task16StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task17StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task18StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task19StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task20StatusProductReadiness(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(ProductReadiness, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

class videocontent(models.Model):
    Poc1 = models.CharField(max_length=100, default='Allison Graham')
    Poc1_email = models.EmailField(max_length=100, default='a1.graham@partner.samsung.com')
    poc2 = models.CharField(max_length=100, default='Nicole Cantwell')
    poc3_email = models.EmailField(max_length=100, default='n.waud@samsung.com')
    Task1_Name = models.CharField(max_length=100, default='Topic Lists')
    Task1_Start_Date = models.DateField(blank=True,null=True)
    Task1_End_Date = models.DateField(blank=True,null=True)
    Task1_complete_date = models.DateField(blank=True, null=True)
    Task1_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task2_Name = models.CharField(max_length=100, default='Scripts')
    Task2_Start_Date = models.DateField(blank=True,null=True)
    Task2_End_Date = models.DateField(blank=True,null=True)
    Task2_complete_date = models.DateField(blank=True, null=True)
    Task2_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task3_Name = models.CharField(max_length=100,blank=True, default='Finalize Video')
    Task3_Start_Date = models.DateField(blank=True,null=True)
    Task3_End_Date = models.DateField(blank=True,null=True)
    Task3_complete_date = models.DateField(blank=True, null=True)
    Task3_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task4_Name = models.CharField(max_length=100, blank=True,default='')
    Task4_Start_Date = models.DateField(blank=True,null=True)
    Task4_End_Date = models.DateField(blank=True,null=True)
    Task4_complete_date = models.DateField(blank=True, null=True)
    Task4_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task5_Name = models.CharField(max_length=100,blank=True, default='')
    Task5_Start_Date = models.DateField(blank=True,null=True)
    Task5_End_Date = models.DateField(blank=True,null=True)
    Task5_complete_date = models.DateField(blank=True, null=True)
    Task5_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task6_Name = models.CharField(max_length=100,blank=True, default='')
    Task6_Start_Date = models.DateField(blank=True,null=True)
    Task6_End_Date = models.DateField(blank=True,null=True)
    Task6_complete_date = models.DateField(blank=True, null=True)
    Task6_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task7_Name = models.CharField(max_length=100, blank=True,default='')
    Task7_Start_Date = models.DateField(blank=True,null=True)
    Task7_End_Date = models.DateField(blank=True,null=True)
    Task7_complete_date = models.DateField(blank=True, null=True)
    Task7_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task8_Name = models.CharField(max_length=100,blank=True, default='')
    Task8_Start_Date = models.DateField(blank=True,null=True)
    Task8_End_Date = models.DateField(blank=True,null=True)
    Task8_complete_date = models.DateField(blank=True, null=True)
    Task8_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task9_Name = models.CharField(max_length=100, blank=True,default='')
    Task9_Start_Date = models.DateField(blank=True,null=True)
    Task9_End_Date = models.DateField(blank=True,null=True)
    Task9_complete_date = models.DateField(blank=True, null=True)
    Task9_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task10_Name = models.CharField(max_length=100, blank=True,default='')
    Task10_Start_Date = models.DateField(blank=True,null=True)
    Task10_End_Date = models.DateField(blank=True,null=True)
    Task10_complete_date = models.DateField(blank=True, null=True)
    Task10_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task11_Name = models.CharField(max_length=100, blank=True,default='')
    Task11_Start_Date = models.DateField(blank=True,null=True)
    Task11_End_Date = models.DateField(blank=True,null=True)
    Task11_complete_date = models.DateField(blank=True, null=True)
    Task11_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task12_Name = models.CharField(max_length=100, blank=True,default='')
    Task12_Start_Date = models.DateField(blank=True,null=True)
    Task12_End_Date = models.DateField(blank=True,null=True)
    Task12_complete_date = models.DateField(blank=True, null=True)
    Task12_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task13_Name = models.CharField(max_length=100, blank=True,default='')
    Task13_Start_Date = models.DateField(blank=True,null=True)
    Task13_End_Date = models.DateField(blank=True,null=True)
    Task13_complete_date = models.DateField(blank=True, null=True)
    Task13_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task14_Name = models.CharField(max_length=100,blank=True, default='')
    Task14_Start_Date = models.DateField(blank=True,null=True)
    Task14_End_Date = models.DateField(blank=True,null=True)
    Task14_complete_date = models.DateField(blank=True, null=True)
    Task14_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task15_Name = models.CharField(max_length=100,blank=True, default='')
    Task15_Start_Date = models.DateField(blank=True,null=True)
    Task15_End_Date = models.DateField(blank=True,null=True)
    Task15_complete_date = models.DateField(blank=True, null=True)
    Task15_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task16_Name = models.CharField(max_length=100,blank=True, default='')
    Task16_Start_Date = models.DateField(blank=True,null=True)
    Task16_End_Date = models.DateField(blank=True,null=True)
    Task16_complete_date = models.DateField(blank=True, null=True)
    Task16_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task17_Name = models.CharField(max_length=100,blank=True, default='')
    Task17_Start_Date = models.DateField(blank=True,null=True)
    Task17_End_Date = models.DateField(blank=True,null=True)
    Task17_complete_date = models.DateField(blank=True, null=True)
    Task17_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task18_Name = models.CharField(max_length=100,blank=True, default='')
    Task18_Start_Date = models.DateField(blank=True,null=True)
    Task18_End_Date = models.DateField(blank=True,null=True)
    Task18_complete_date = models.DateField(blank=True, null=True)
    Task18_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task19_Name = models.CharField(max_length=100,blank=True, default='')
    Task19_Start_Date = models.DateField(blank=True,null=True)
    Task19_End_Date = models.DateField(blank=True,null=True)
    Task19_complete_date = models.DateField(blank=True, null=True)
    Task19_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task20_Name = models.CharField(max_length=100,blank=True, default='')
    Task20_Start_Date = models.DateField(blank=True,null=True)
    Task20_End_Date = models.DateField(blank=True,null=True)
    Task20_complete_date = models.DateField(blank=True, null=True)
    Task20_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Time_Delta_For_Warning=models.IntegerField(default=7)
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    Task1_warning = models.BooleanField(default=False)
    Task2_warning = models.BooleanField(default=False)
    Task3_warning = models.BooleanField(default=False)
    Task4_warning = models.BooleanField(default=False)
    Task5_warning = models.BooleanField(default=False)
    Task6_warning = models.BooleanField(default=False)
    Task7_warning = models.BooleanField(default=False)
    Task8_warning = models.BooleanField(default=False)
    Task9_warning = models.BooleanField(default=False)
    Task10_warning = models.BooleanField(default=False)
    Task11_warning = models.BooleanField(default=False)
    Task12_warning = models.BooleanField(default=False)
    Task13_warning = models.BooleanField(default=False)
    Task14_warning = models.BooleanField(default=False)
    Task15_warning = models.BooleanField(default=False)
    Task16_warning = models.BooleanField(default=False)
    Task17_warning = models.BooleanField(default=False)
    Task18_warning = models.BooleanField(default=False)
    Task19_warning = models.BooleanField(default=False)
    Task20_warning = models.BooleanField(default=False)
    Task1_alert = models.BooleanField(default=False)
    Task2_alert = models.BooleanField(default=False)
    Task3_alert = models.BooleanField(default=False)
    Task4_alert = models.BooleanField(default=False)
    Task5_alert = models.BooleanField(default=False)
    Task6_alert = models.BooleanField(default=False)
    Task7_alert = models.BooleanField(default=False)
    Task8_alert = models.BooleanField(default=False)
    Task9_alert = models.BooleanField(default=False)
    Task10_alert = models.BooleanField(default=False)
    Task11_alert = models.BooleanField(default=False)
    Task12_alert = models.BooleanField(default=False)
    Task13_alert = models.BooleanField(default=False)
    Task14_alert = models.BooleanField(default=False)
    Task15_alert = models.BooleanField(default=False)
    Task16_alert = models.BooleanField(default=False)
    Task17_alert = models.BooleanField(default=False)
    Task18_alert = models.BooleanField(default=False)
    Task19_alert = models.BooleanField(default=False)
    Task20_alert = models.BooleanField(default=False)
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')

class Task1StatusVideoContent (models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

class Task2StatusVideoContent (models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

class Task3StatusVideoContent (models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

class Task4StatusVideoContent (models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

class Task5StatusVideoContent (models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task6StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task7StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task8StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task9StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task10StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task11StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task12StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task13StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task14StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task15StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task16StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task17StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task18StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task19StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task20StatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    VideoContent = models.ForeignKey(videocontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class ExtraTasks_VideoContent(models.Model):
    ExtraTask_Name = models.CharField(max_length=100, default='')
    ExtraTask_Start_Date = models.DateField(blank=True,null=True)
    ExtraTask_End_Date = models.DateField(blank=True,null=True)
    ExtraTask_complete_date = models.DateField(blank=True, null=True)
    videocontent_instance = models.ForeignKey(videocontent,on_delete=models.CASCADE, null=True)

class ExtraTaskStatusVideoContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ExtraTasksVideoContent = models.ForeignKey(ExtraTasks_VideoContent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

########################################################################################################################

class digitalcontent(models.Model):
    Poc1 = models.CharField(max_length=100, default='Joseph Suplickii')
    Poc1_email = models.EmailField(max_length=100, default='joseph.s@samsung.com')
    poc2 = models.CharField(max_length=100, default='Jessie Trochez')
    poc3_email = models.EmailField(max_length=100, default='j.trochez@samsung.com')
    Task1_Name = models.CharField(max_length=100, blank=True,default='Samples (received)')
    Task1_Start_Date = models.DateField(blank=True,null=True)
    Task1_End_Date = models.DateField(blank=True,null=True)
    Task1_complete_date = models.DateField(blank=True, null=True)
    Task1_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task2_Name = models.CharField(max_length=100,blank=True, default='Pre-sales FAQ (received/posted)')
    Task2_Start_Date = models.DateField(blank=True,null=True)
    Task2_End_Date = models.DateField(blank=True,null=True)
    Task2_complete_date = models.DateField(blank=True, null=True)
    Task2_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task3_Name = models.CharField(max_length=100, blank=True,default='Customer Content (samsung.com)')
    Task3_Start_Date = models.DateField(blank=True,null=True)
    Task3_End_Date = models.DateField(blank=True,null=True)
    Task3_complete_date = models.DateField(blank=True, null=True)
    Task3_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task4_Name = models.CharField(max_length=100, blank=True,default='Agent Content: (Decision Tree)')
    Task4_Start_Date = models.DateField(blank=True,null=True)
    Task4_End_Date = models.DateField(blank=True,null=True)
    Task4_complete_date = models.DateField(blank=True, null=True)
    Task4_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task5_Name = models.CharField(max_length=100, blank=True,default='Application: Samsung+(content)')
    Task5_Start_Date = models.DateField(blank=True,null=True)
    Task5_End_Date = models.DateField(blank=True,null=True)
    Task5_complete_date = models.DateField(blank=True, null=True)
    Task5_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task6_Name = models.CharField(max_length=100,blank=True, default='Simulators')
    Task6_Start_Date = models.DateField(blank=True,null=True)
    Task6_End_Date = models.DateField(blank=True,null=True)
    Task6_complete_date = models.DateField(blank=True, null=True)
    Task6_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task7_Name = models.CharField(max_length=100, blank=True,default='')
    Task7_Start_Date = models.DateField(blank=True,null=True)
    Task7_End_Date = models.DateField(blank=True,null=True)
    Task7_complete_date = models.DateField(blank=True, null=True)
    Task7_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task8_Name = models.CharField(max_length=100,blank=True, default='')
    Task8_Start_Date = models.DateField(blank=True,null=True)
    Task8_End_Date = models.DateField(blank=True,null=True)
    Task8_complete_date = models.DateField(blank=True, null=True)
    Task8_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task9_Name = models.CharField(max_length=100, blank=True,default='')
    Task9_Start_Date = models.DateField(blank=True,null=True)
    Task9_End_Date = models.DateField(blank=True,null=True)
    Task9_complete_date = models.DateField(blank=True, null=True)
    Task9_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task10_Name = models.CharField(max_length=100, blank=True,default='')
    Task10_Start_Date = models.DateField(blank=True,null=True)
    Task10_End_Date = models.DateField(blank=True,null=True)
    Task10_complete_date = models.DateField(blank=True, null=True)
    Task10_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task11_Name = models.CharField(max_length=100, blank=True,default='')
    Task11_Start_Date = models.DateField(blank=True,null=True)
    Task11_End_Date = models.DateField(blank=True,null=True)
    Task11_complete_date = models.DateField(blank=True, null=True)
    Task11_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task12_Name = models.CharField(max_length=100, blank=True,default='')
    Task12_Start_Date = models.DateField(blank=True,null=True)
    Task12_End_Date = models.DateField(blank=True,null=True)
    Task12_complete_date = models.DateField(blank=True, null=True)
    Task12_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task13_Name = models.CharField(max_length=100, blank=True,default='')
    Task13_Start_Date = models.DateField(blank=True,null=True)
    Task13_End_Date = models.DateField(blank=True,null=True)
    Task13_complete_date = models.DateField(blank=True, null=True)
    Task13_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task14_Name = models.CharField(max_length=100,blank=True, default='')
    Task14_Start_Date = models.DateField(blank=True,null=True)
    Task14_End_Date = models.DateField(blank=True,null=True)
    Task14_complete_date = models.DateField(blank=True, null=True)
    Task14_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task15_Name = models.CharField(max_length=100,blank=True, default='')
    Task15_Start_Date = models.DateField(blank=True,null=True)
    Task15_End_Date = models.DateField(blank=True,null=True)
    Task15_complete_date = models.DateField(blank=True, null=True)
    Task15_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task16_Name = models.CharField(max_length=100,blank=True, default='')
    Task16_Start_Date = models.DateField(blank=True,null=True)
    Task16_End_Date = models.DateField(blank=True,null=True)
    Task16_complete_date = models.DateField(blank=True, null=True)
    Task16_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task17_Name = models.CharField(max_length=100,blank=True, default='')
    Task17_Start_Date = models.DateField(blank=True,null=True)
    Task17_End_Date = models.DateField(blank=True,null=True)
    Task17_complete_date = models.DateField(blank=True, null=True)
    Task17_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task18_Name = models.CharField(max_length=100,blank=True, default='')
    Task18_Start_Date = models.DateField(blank=True,null=True)
    Task18_End_Date = models.DateField(blank=True,null=True)
    Task18_complete_date = models.DateField(blank=True, null=True)
    Task18_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task19_Name = models.CharField(max_length=100,blank=True, default='')
    Task19_Start_Date = models.DateField(blank=True,null=True)
    Task19_End_Date = models.DateField(blank=True,null=True)
    Task19_complete_date = models.DateField(blank=True, null=True)
    Task19_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task20_Name = models.CharField(max_length=100,blank=True, default='')
    Task20_Start_Date = models.DateField(blank=True,null=True)
    Task20_End_Date = models.DateField(blank=True,null=True)
    Task20_complete_date = models.DateField(blank=True, null=True)
    Task20_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Time_Delta_For_Warning=models.IntegerField(default=7)
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    Task1_warning = models.BooleanField(default=False)
    Task2_warning = models.BooleanField(default=False)
    Task3_warning = models.BooleanField(default=False)
    Task4_warning = models.BooleanField(default=False)
    Task5_warning = models.BooleanField(default=False)
    Task6_warning = models.BooleanField(default=False)
    Task7_warning = models.BooleanField(default=False)
    Task8_warning = models.BooleanField(default=False)
    Task9_warning = models.BooleanField(default=False)
    Task10_warning = models.BooleanField(default=False)
    Task11_warning = models.BooleanField(default=False)
    Task12_warning = models.BooleanField(default=False)
    Task13_warning = models.BooleanField(default=False)
    Task14_warning = models.BooleanField(default=False)
    Task15_warning = models.BooleanField(default=False)
    Task16_warning = models.BooleanField(default=False)
    Task17_warning = models.BooleanField(default=False)
    Task18_warning = models.BooleanField(default=False)
    Task19_warning = models.BooleanField(default=False)
    Task20_warning = models.BooleanField(default=False)
    Task1_alert = models.BooleanField(default=False)
    Task2_alert = models.BooleanField(default=False)
    Task3_alert = models.BooleanField(default=False)
    Task4_alert = models.BooleanField(default=False)
    Task5_alert = models.BooleanField(default=False)
    Task6_alert = models.BooleanField(default=False)
    Task7_alert = models.BooleanField(default=False)
    Task8_alert = models.BooleanField(default=False)
    Task9_alert = models.BooleanField(default=False)
    Task10_alert = models.BooleanField(default=False)
    Task11_alert = models.BooleanField(default=False)
    Task12_alert = models.BooleanField(default=False)
    Task13_alert = models.BooleanField(default=False)
    Task14_alert = models.BooleanField(default=False)
    Task15_alert = models.BooleanField(default=False)
    Task16_alert = models.BooleanField(default=False)
    Task17_alert = models.BooleanField(default=False)
    Task18_alert = models.BooleanField(default=False)
    Task19_alert = models.BooleanField(default=False)
    Task20_alert = models.BooleanField(default=False)
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')

class Task1StatusDigitalContent (models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

class Task2StatusDigitalContent (models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

class Task3StatusDigitalContent (models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

class Task4StatusDigitalContent (models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

class Task5StatusDigitalContent (models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task6StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task7StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task8StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task9StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task10StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task11StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task12StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task13StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task14StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task15StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task16StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task17StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task18StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task19StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task20StatusDigitalContent(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    DigitalContent = models.ForeignKey(digitalcontent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

########################################################################################################################

class callcentertraining(models.Model):
    Poc1 = models.CharField(max_length=100, default='Ly Nguyen')
    Poc1_email = models.EmailField(max_length=100, default='ly.nguyen@partner.samsung.com')
    poc2 = models.CharField(max_length=100, default='Casey Cribbin')
    poc3_email = models.EmailField(max_length=100, default='c.cribbin@samsung.com')
    Task1_Name = models.CharField(max_length=100, blank=True,default='Create Training: Agents')
    Task1_Start_Date = models.DateField(blank=True,null=True)
    Task1_End_Date = models.DateField(blank=True,null=True)
    Task1_complete_date = models.DateField(blank=True, null=True)
    Task1_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task2_Name = models.CharField(max_length=100, blank=True,default='Training Expectation Rollout')
    Task2_Start_Date = models.DateField(blank=True,null=True)
    Task2_End_Date = models.DateField(blank=True,null=True)
    Task2_complete_date = models.DateField(blank=True, null=True)
    Task2_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task3_Name = models.CharField(max_length=100, blank=True,default='Training the trainer')
    Task3_Start_Date = models.DateField(blank=True,null=True)
    Task3_End_Date = models.DateField(blank=True,null=True)
    Task3_complete_date = models.DateField(blank=True, null=True)
    Task3_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task4_Name = models.CharField(max_length=100, blank=True,default='Train: Agents')
    Task4_Start_Date = models.DateField(blank=True,null=True)
    Task4_End_Date = models.DateField(blank=True,null=True)
    Task4_complete_date = models.DateField(blank=True, null=True)
    Task4_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task5_Name = models.CharField(max_length=100, blank=True,default='')
    Task5_Start_Date = models.DateField(blank=True,null=True)
    Task5_End_Date = models.DateField(blank=True,null=True)
    Task5_complete_date = models.DateField(blank=True, null=True)
    Task5_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task6_Name = models.CharField(max_length=100,blank=True, default='')
    Task6_Start_Date = models.DateField(blank=True,null=True)
    Task6_End_Date = models.DateField(blank=True,null=True)
    Task6_complete_date = models.DateField(blank=True, null=True)
    Task6_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task7_Name = models.CharField(max_length=100, blank=True,default='')
    Task7_Start_Date = models.DateField(blank=True,null=True)
    Task7_End_Date = models.DateField(blank=True,null=True)
    Task7_complete_date = models.DateField(blank=True, null=True)
    Task7_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task8_Name = models.CharField(max_length=100,blank=True, default='')
    Task8_Start_Date = models.DateField(blank=True,null=True)
    Task8_End_Date = models.DateField(blank=True,null=True)
    Task8_complete_date = models.DateField(blank=True, null=True)
    Task8_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task9_Name = models.CharField(max_length=100, blank=True,default='')
    Task9_Start_Date = models.DateField(blank=True,null=True)
    Task9_End_Date = models.DateField(blank=True,null=True)
    Task9_complete_date = models.DateField(blank=True, null=True)
    Task9_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task10_Name = models.CharField(max_length=100, blank=True,default='')
    Task10_Start_Date = models.DateField(blank=True,null=True)
    Task10_End_Date = models.DateField(blank=True,null=True)
    Task10_complete_date = models.DateField(blank=True, null=True)
    Task10_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task11_Name = models.CharField(max_length=100, blank=True,default='')
    Task11_Start_Date = models.DateField(blank=True,null=True)
    Task11_End_Date = models.DateField(blank=True,null=True)
    Task11_complete_date = models.DateField(blank=True, null=True)
    Task11_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task12_Name = models.CharField(max_length=100, blank=True,default='')
    Task12_Start_Date = models.DateField(blank=True,null=True)
    Task12_End_Date = models.DateField(blank=True,null=True)
    Task12_complete_date = models.DateField(blank=True, null=True)
    Task12_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task13_Name = models.CharField(max_length=100, blank=True,default='')
    Task13_Start_Date = models.DateField(blank=True,null=True)
    Task13_End_Date = models.DateField(blank=True,null=True)
    Task13_complete_date = models.DateField(blank=True, null=True)
    Task13_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task14_Name = models.CharField(max_length=100,blank=True, default='')
    Task14_Start_Date = models.DateField(blank=True,null=True)
    Task14_End_Date = models.DateField(blank=True,null=True)
    Task14_complete_date = models.DateField(blank=True, null=True)
    Task14_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task15_Name = models.CharField(max_length=100,blank=True, default='')
    Task15_Start_Date = models.DateField(blank=True,null=True)
    Task15_End_Date = models.DateField(blank=True,null=True)
    Task15_complete_date = models.DateField(blank=True, null=True)
    Task15_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task16_Name = models.CharField(max_length=100,blank=True, default='')
    Task16_Start_Date = models.DateField(blank=True,null=True)
    Task16_End_Date = models.DateField(blank=True,null=True)
    Task16_complete_date = models.DateField(blank=True, null=True)
    Task16_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task17_Name = models.CharField(max_length=100,blank=True, default='')
    Task17_Start_Date = models.DateField(blank=True,null=True)
    Task17_End_Date = models.DateField(blank=True,null=True)
    Task17_complete_date = models.DateField(blank=True, null=True)
    Task17_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task18_Name = models.CharField(max_length=100,blank=True, default='')
    Task18_Start_Date = models.DateField(blank=True,null=True)
    Task18_End_Date = models.DateField(blank=True,null=True)
    Task18_complete_date = models.DateField(blank=True, null=True)
    Task18_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task19_Name = models.CharField(max_length=100,blank=True, default='')
    Task19_Start_Date = models.DateField(blank=True,null=True)
    Task19_End_Date = models.DateField(blank=True,null=True)
    Task19_complete_date = models.DateField(blank=True, null=True)
    Task19_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task20_Name = models.CharField(max_length=100,blank=True, default='')
    Task20_Start_Date = models.DateField(blank=True,null=True)
    Task20_End_Date = models.DateField(blank=True,null=True)
    Task20_complete_date = models.DateField(blank=True, null=True)
    Task20_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Time_Delta_For_Warning=models.IntegerField(default=7)
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    Task1_warning = models.BooleanField(default=False)
    Task2_warning = models.BooleanField(default=False)
    Task3_warning = models.BooleanField(default=False)
    Task4_warning = models.BooleanField(default=False)
    Task5_warning = models.BooleanField(default=False)
    Task6_warning = models.BooleanField(default=False)
    Task7_warning = models.BooleanField(default=False)
    Task8_warning = models.BooleanField(default=False)
    Task9_warning = models.BooleanField(default=False)
    Task10_warning = models.BooleanField(default=False)
    Task11_warning = models.BooleanField(default=False)
    Task12_warning = models.BooleanField(default=False)
    Task13_warning = models.BooleanField(default=False)
    Task14_warning = models.BooleanField(default=False)
    Task15_warning = models.BooleanField(default=False)
    Task16_warning = models.BooleanField(default=False)
    Task17_warning = models.BooleanField(default=False)
    Task18_warning = models.BooleanField(default=False)
    Task19_warning = models.BooleanField(default=False)
    Task20_warning = models.BooleanField(default=False)
    Task1_alert = models.BooleanField(default=False)
    Task2_alert = models.BooleanField(default=False)
    Task3_alert = models.BooleanField(default=False)
    Task4_alert = models.BooleanField(default=False)
    Task5_alert = models.BooleanField(default=False)
    Task6_alert = models.BooleanField(default=False)
    Task7_alert = models.BooleanField(default=False)
    Task8_alert = models.BooleanField(default=False)
    Task9_alert = models.BooleanField(default=False)
    Task10_alert = models.BooleanField(default=False)
    Task11_alert = models.BooleanField(default=False)
    Task12_alert = models.BooleanField(default=False)
    Task13_alert = models.BooleanField(default=False)
    Task14_alert = models.BooleanField(default=False)
    Task15_alert = models.BooleanField(default=False)
    Task16_alert = models.BooleanField(default=False)
    Task17_alert = models.BooleanField(default=False)
    Task18_alert = models.BooleanField(default=False)
    Task19_alert = models.BooleanField(default=False)
    Task20_alert = models.BooleanField(default=False)
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')

class Task1StatusCallCenterTraining (models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

class Task2StatusCallCenterTraining (models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

class Task3StatusCallCenterTraining (models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

class Task4StatusCallCenterTraining (models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

class Task5StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task6StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task7StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task8StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task9StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task10StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task11StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task12StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task13StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task14StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task15StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task16StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task17StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task18StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task19StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task20StatusCallCenterTraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterTraining = models.ForeignKey(callcentertraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

########################################################################################################################

class callcenteropertaions(models.Model):
    Poc1 = models.CharField(max_length=100, default='Martha Lee')
    Poc1_email = models.EmailField(max_length=100, default='martha.lee@samsung.com')
    poc2 = models.CharField(max_length=100, default='Seung Yeon Cho')
    poc3_email = models.EmailField(max_length=100, default='sy7378.cho@samsung.com')
    Task1_Name = models.CharField(max_length=100,blank=True, default='Sales Forecast (received)')
    Task1_Start_Date = models.DateField(blank=True, null=True)
    Task1_End_Date = models.DateField(blank=True, null=True)
    Task1_complete_date = models.DateField(blank=True, null=True)
    Task1_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task2_Name = models.CharField(max_length=100, blank=True,default='Define Support Hours (received)')
    Task2_Start_Date = models.DateField(blank=True, null=True)
    Task2_End_Date = models.DateField(blank=True, null=True)
    Task2_complete_date = models.DateField(blank=True, null=True)
    Task2_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task3_Name = models.CharField(max_length=100,blank=True, default='Contact Volume Forecast')
    Task3_Start_Date = models.DateField(blank=True, null=True)
    Task3_End_Date = models.DateField(blank=True, null=True)
    Task3_complete_date = models.DateField(blank=True, null=True)
    Task3_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task4_Name = models.CharField(max_length=100,blank=True, default='Staffing Plan (Voice & Digital)')
    Task4_Start_Date = models.DateField(blank=True, null=True)
    Task4_End_Date = models.DateField(blank=True, null=True)
    Task4_complete_date = models.DateField(blank=True, null=True)
    Task4_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task5_Name = models.CharField(max_length=100, blank=True,default='')
    Task5_Start_Date = models.DateField(blank=True, null=True)
    Task5_End_Date = models.DateField(blank=True, null=True)
    Task5_complete_date = models.DateField(blank=True, null=True)
    Task5_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task6_Name = models.CharField(max_length=100,blank=True, default='')
    Task6_Start_Date = models.DateField(blank=True, null=True)
    Task6_End_Date = models.DateField(blank=True, null=True)
    Task6_complete_date = models.DateField(blank=True, null=True)
    Task6_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task7_Name = models.CharField(max_length=100, blank=True, default='')
    Task7_Start_Date = models.DateField(blank=True, null=True)
    Task7_End_Date = models.DateField(blank=True, null=True)
    Task7_complete_date = models.DateField(blank=True, null=True)
    Task7_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task8_Name = models.CharField(max_length=100, blank=True, default='')
    Task8_Start_Date = models.DateField(blank=True, null=True)
    Task8_End_Date = models.DateField(blank=True, null=True)
    Task8_complete_date = models.DateField(blank=True, null=True)
    Task8_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task9_Name = models.CharField(max_length=100, blank=True, default='')
    Task9_Start_Date = models.DateField(blank=True, null=True)
    Task9_End_Date = models.DateField(blank=True, null=True)
    Task9_complete_date = models.DateField(blank=True, null=True)
    Task9_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task10_Name = models.CharField(max_length=100, blank=True, default='')
    Task10_Start_Date = models.DateField(blank=True, null=True)
    Task10_End_Date = models.DateField(blank=True, null=True)
    Task10_complete_date = models.DateField(blank=True, null=True)
    Task10_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task11_Name = models.CharField(max_length=100, blank=True, default='')
    Task11_Start_Date = models.DateField(blank=True, null=True)
    Task11_End_Date = models.DateField(blank=True, null=True)
    Task11_complete_date = models.DateField(blank=True, null=True)
    Task11_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task12_Name = models.CharField(max_length=100, blank=True, default='')
    Task12_Start_Date = models.DateField(blank=True, null=True)
    Task12_End_Date = models.DateField(blank=True, null=True)
    Task12_complete_date = models.DateField(blank=True, null=True)
    Task12_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task13_Name = models.CharField(max_length=100, blank=True, default='')
    Task13_Start_Date = models.DateField(blank=True, null=True)
    Task13_End_Date = models.DateField(blank=True, null=True)
    Task13_complete_date = models.DateField(blank=True, null=True)
    Task13_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task14_Name = models.CharField(max_length=100, blank=True, default='')
    Task14_Start_Date = models.DateField(blank=True, null=True)
    Task14_End_Date = models.DateField(blank=True, null=True)
    Task14_complete_date = models.DateField(blank=True, null=True)
    Task14_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task15_Name = models.CharField(max_length=100, blank=True, default='')
    Task15_Start_Date = models.DateField(blank=True, null=True)
    Task15_End_Date = models.DateField(blank=True, null=True)
    Task15_complete_date = models.DateField(blank=True, null=True)
    Task15_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task16_Name = models.CharField(max_length=100, blank=True, default='')
    Task16_Start_Date = models.DateField(blank=True, null=True)
    Task16_End_Date = models.DateField(blank=True, null=True)
    Task16_complete_date = models.DateField(blank=True, null=True)
    Task16_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task17_Name = models.CharField(max_length=100, blank=True, default='')
    Task17_Start_Date = models.DateField(blank=True, null=True)
    Task17_End_Date = models.DateField(blank=True, null=True)
    Task17_complete_date = models.DateField(blank=True, null=True)
    Task17_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task18_Name = models.CharField(max_length=100, blank=True, default='')
    Task18_Start_Date = models.DateField(blank=True, null=True)
    Task18_End_Date = models.DateField(blank=True, null=True)
    Task18_complete_date = models.DateField(blank=True, null=True)
    Task18_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task19_Name = models.CharField(max_length=100, blank=True, default='')
    Task19_Start_Date = models.DateField(blank=True, null=True)
    Task19_End_Date = models.DateField(blank=True, null=True)
    Task19_complete_date = models.DateField(blank=True, null=True)
    Task19_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task20_Name = models.CharField(max_length=100, blank=True, default='')
    Task20_Start_Date = models.DateField(blank=True, null=True)
    Task20_End_Date = models.DateField(blank=True, null=True)
    Task20_complete_date = models.DateField(blank=True, null=True)
    Task20_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Time_Delta_For_Warning = models.IntegerField(default=7)
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    Task1_warning = models.BooleanField(default=False)
    Task2_warning = models.BooleanField(default=False)
    Task3_warning = models.BooleanField(default=False)
    Task4_warning = models.BooleanField(default=False)
    Task5_warning = models.BooleanField(default=False)
    Task6_warning = models.BooleanField(default=False)
    Task7_warning = models.BooleanField(default=False)
    Task8_warning = models.BooleanField(default=False)
    Task9_warning = models.BooleanField(default=False)
    Task10_warning = models.BooleanField(default=False)
    Task11_warning = models.BooleanField(default=False)
    Task12_warning = models.BooleanField(default=False)
    Task13_warning = models.BooleanField(default=False)
    Task14_warning = models.BooleanField(default=False)
    Task15_warning = models.BooleanField(default=False)
    Task16_warning = models.BooleanField(default=False)
    Task17_warning = models.BooleanField(default=False)
    Task18_warning = models.BooleanField(default=False)
    Task19_warning = models.BooleanField(default=False)
    Task20_warning = models.BooleanField(default=False)
    Task1_alert = models.BooleanField(default=False)
    Task2_alert = models.BooleanField(default=False)
    Task3_alert = models.BooleanField(default=False)
    Task4_alert = models.BooleanField(default=False)
    Task5_alert = models.BooleanField(default=False)
    Task6_alert = models.BooleanField(default=False)
    Task7_alert = models.BooleanField(default=False)
    Task8_alert = models.BooleanField(default=False)
    Task9_alert = models.BooleanField(default=False)
    Task10_alert = models.BooleanField(default=False)
    Task11_alert = models.BooleanField(default=False)
    Task12_alert = models.BooleanField(default=False)
    Task13_alert = models.BooleanField(default=False)
    Task14_alert = models.BooleanField(default=False)
    Task15_alert = models.BooleanField(default=False)
    Task16_alert = models.BooleanField(default=False)
    Task17_alert = models.BooleanField(default=False)
    Task18_alert = models.BooleanField(default=False)
    Task19_alert = models.BooleanField(default=False)
    Task20_alert = models.BooleanField(default=False)
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')


class Task1Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task2Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task3Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task4Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task5Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task6Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task7Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task8Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task9Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task10Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task11Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task12Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task13Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task14Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task15Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task16Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task17Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task18Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task19Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task20Statuscallcenteropertaions(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    CallCenterOpertaions = models.ForeignKey(callcenteropertaions, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

########################################################################################################################

class productsupport(models.Model):
    Poc1 = models.CharField(max_length=100, default='Scott Whitman')
    Poc1_email = models.EmailField(max_length=100, default='s.whitman@samsung.com')
    poc2 = models.CharField(max_length=100, default='Khaled Abuali')
    poc3_email = models.EmailField(max_length=100, default='k.abuali@samsung.com')
    Task1_Name = models.CharField(max_length=100,blank=True, default='PV/PR Sample (received)')
    Task1_Start_Date = models.DateField(blank=True, null=True)
    Task1_End_Date = models.DateField(blank=True, null=True)
    Task1_complete_date = models.DateField(blank=True, null=True)
    Task1_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task2_Name = models.CharField(max_length=100, blank=True,default='Serviceablity Test')
    Task2_Start_Date = models.DateField(blank=True, null=True)
    Task2_End_Date = models.DateField(blank=True, null=True)
    Task2_complete_date = models.DateField(blank=True, null=True)
    Task2_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task3_Name = models.CharField(max_length=100, blank=True,default='Doc Review: Service Manual')
    Task3_Start_Date = models.DateField(blank=True, null=True)
    Task3_End_Date = models.DateField(blank=True, null=True)
    Task3_complete_date = models.DateField(blank=True, null=True)
    Task3_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task4_Name = models.CharField(max_length=100, blank=True,default='Doc Review: Box Art')
    Task4_Start_Date = models.DateField(blank=True, null=True)
    Task4_End_Date = models.DateField(blank=True, null=True)
    Task4_complete_date = models.DateField(blank=True, null=True)
    Task4_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task5_Name = models.CharField(max_length=100, blank=True,default='PR Evaluation')
    Task5_Start_Date = models.DateField(blank=True, null=True)
    Task5_End_Date = models.DateField(blank=True, null=True)
    Task5_complete_date = models.DateField(blank=True, null=True)
    Task5_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task6_Name = models.CharField(max_length=100, blank=True,default='UL/FCC/Agency Testing (received)')
    Task6_Start_Date = models.DateField(blank=True, null=True)
    Task6_End_Date = models.DateField(blank=True, null=True)
    Task6_complete_date = models.DateField(blank=True, null=True)
    Task6_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task7_Name = models.CharField(max_length=100, blank=True, default='OBE/Functionality Test')
    Task7_Start_Date = models.DateField(blank=True, null=True)
    Task7_End_Date = models.DateField(blank=True, null=True)
    Task7_complete_date = models.DateField(blank=True, null=True)
    Task7_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task8_Name = models.CharField(max_length=100, blank=True, default='OBE/Performance Test')
    Task8_Start_Date = models.DateField(blank=True, null=True)
    Task8_End_Date = models.DateField(blank=True, null=True)
    Task8_complete_date = models.DateField(blank=True, null=True)
    Task8_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task9_Name = models.CharField(max_length=100, blank=True, default='Update STG')
    Task9_Start_Date = models.DateField(blank=True, null=True)
    Task9_End_Date = models.DateField(blank=True, null=True)
    Task9_complete_date = models.DateField(blank=True, null=True)
    Task9_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task10_Name = models.CharField(max_length=100, blank=True, default='')
    Task10_Start_Date = models.DateField(blank=True, null=True)
    Task10_End_Date = models.DateField(blank=True, null=True)
    Task10_complete_date = models.DateField(blank=True, null=True)
    Task10_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task11_Name = models.CharField(max_length=100, blank=True, default='')
    Task11_Start_Date = models.DateField(blank=True, null=True)
    Task11_End_Date = models.DateField(blank=True, null=True)
    Task11_complete_date = models.DateField(blank=True, null=True)
    Task11_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task12_Name = models.CharField(max_length=100, blank=True, default='')
    Task12_Start_Date = models.DateField(blank=True, null=True)
    Task12_End_Date = models.DateField(blank=True, null=True)
    Task12_complete_date = models.DateField(blank=True, null=True)
    Task12_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task13_Name = models.CharField(max_length=100, blank=True, default='')
    Task13_Start_Date = models.DateField(blank=True, null=True)
    Task13_End_Date = models.DateField(blank=True, null=True)
    Task13_complete_date = models.DateField(blank=True, null=True)
    Task13_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task14_Name = models.CharField(max_length=100, blank=True, default='')
    Task14_Start_Date = models.DateField(blank=True, null=True)
    Task14_End_Date = models.DateField(blank=True, null=True)
    Task14_complete_date = models.DateField(blank=True, null=True)
    Task14_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task15_Name = models.CharField(max_length=100, blank=True, default='')
    Task15_Start_Date = models.DateField(blank=True, null=True)
    Task15_End_Date = models.DateField(blank=True, null=True)
    Task15_complete_date = models.DateField(blank=True, null=True)
    Task15_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task16_Name = models.CharField(max_length=100, blank=True, default='')
    Task16_Start_Date = models.DateField(blank=True, null=True)
    Task16_End_Date = models.DateField(blank=True, null=True)
    Task16_complete_date = models.DateField(blank=True, null=True)
    Task16_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task17_Name = models.CharField(max_length=100, blank=True, default='')
    Task17_Start_Date = models.DateField(blank=True, null=True)
    Task17_End_Date = models.DateField(blank=True, null=True)
    Task17_complete_date = models.DateField(blank=True, null=True)
    Task17_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task18_Name = models.CharField(max_length=100, blank=True, default='')
    Task18_Start_Date = models.DateField(blank=True, null=True)
    Task18_End_Date = models.DateField(blank=True, null=True)
    Task18_complete_date = models.DateField(blank=True, null=True)
    Task18_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task19_Name = models.CharField(max_length=100, blank=True, default='')
    Task19_Start_Date = models.DateField(blank=True, null=True)
    Task19_End_Date = models.DateField(blank=True, null=True)
    Task19_complete_date = models.DateField(blank=True, null=True)
    Task19_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task20_Name = models.CharField(max_length=100, blank=True, default='')
    Task20_Start_Date = models.DateField(blank=True, null=True)
    Task20_End_Date = models.DateField(blank=True, null=True)
    Task20_complete_date = models.DateField(blank=True, null=True)
    Task20_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Time_Delta_For_Warning = models.IntegerField(default=7)
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    Task1_warning = models.BooleanField(default=False)
    Task2_warning = models.BooleanField(default=False)
    Task3_warning = models.BooleanField(default=False)
    Task4_warning = models.BooleanField(default=False)
    Task5_warning = models.BooleanField(default=False)
    Task6_warning = models.BooleanField(default=False)
    Task7_warning = models.BooleanField(default=False)
    Task8_warning = models.BooleanField(default=False)
    Task9_warning = models.BooleanField(default=False)
    Task10_warning = models.BooleanField(default=False)
    Task11_warning = models.BooleanField(default=False)
    Task12_warning = models.BooleanField(default=False)
    Task13_warning = models.BooleanField(default=False)
    Task14_warning = models.BooleanField(default=False)
    Task15_warning = models.BooleanField(default=False)
    Task16_warning = models.BooleanField(default=False)
    Task17_warning = models.BooleanField(default=False)
    Task18_warning = models.BooleanField(default=False)
    Task19_warning = models.BooleanField(default=False)
    Task20_warning = models.BooleanField(default=False)
    Task1_alert = models.BooleanField(default=False)
    Task2_alert = models.BooleanField(default=False)
    Task3_alert = models.BooleanField(default=False)
    Task4_alert = models.BooleanField(default=False)
    Task5_alert = models.BooleanField(default=False)
    Task6_alert = models.BooleanField(default=False)
    Task7_alert = models.BooleanField(default=False)
    Task8_alert = models.BooleanField(default=False)
    Task9_alert = models.BooleanField(default=False)
    Task10_alert = models.BooleanField(default=False)
    Task11_alert = models.BooleanField(default=False)
    Task12_alert = models.BooleanField(default=False)
    Task13_alert = models.BooleanField(default=False)
    Task14_alert = models.BooleanField(default=False)
    Task15_alert = models.BooleanField(default=False)
    Task16_alert = models.BooleanField(default=False)
    Task17_alert = models.BooleanField(default=False)
    Task18_alert = models.BooleanField(default=False)
    Task19_alert = models.BooleanField(default=False)
    Task20_alert = models.BooleanField(default=False)
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')


class Task1Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task2Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task3Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task4Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task5Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task6Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task7Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task8Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task9Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task10Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task11Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task12Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task13Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task14Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task15Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task16Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task17Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task18Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task19Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task20Statusproductsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ProductSupport = models.ForeignKey(productsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

########################################################################################################################

class warehouse(models.Model):
    Poc1 = models.CharField(max_length=100, default='Hyun Dae Kwon')
    Poc1_email = models.EmailField(max_length=100, default='@samsung.com')
    poc2 = models.CharField(max_length=100, default='James Kim')
    poc3_email = models.EmailField(max_length=100, default='kimsung.kook@samsung.com')
    Task1_Name = models.CharField(max_length=100, blank=True,default='Packing Test (Pre-Production)')
    Task1_Start_Date = models.DateField(blank=True, null=True)
    Task1_End_Date = models.DateField(blank=True, null=True)
    Task1_complete_date = models.DateField(blank=True, null=True)
    Task1_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task2_Name = models.CharField(max_length=100, blank=True,default='Cross Inspection (Factory)')
    Task2_Start_Date = models.DateField(blank=True, null=True)
    Task2_End_Date = models.DateField(blank=True, null=True)
    Task2_complete_date = models.DateField(blank=True, null=True)
    Task2_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task3_Name = models.CharField(max_length=100, blank=True,default='Customer Experience Test')
    Task3_Start_Date = models.DateField(blank=True, null=True)
    Task3_End_Date = models.DateField(blank=True, null=True)
    Task3_complete_date = models.DateField(blank=True, null=True)
    Task3_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task4_Name = models.CharField(max_length=100, blank=True,default='')
    Task4_Start_Date = models.DateField(blank=True, null=True)
    Task4_End_Date = models.DateField(blank=True, null=True)
    Task4_complete_date = models.DateField(blank=True, null=True)
    Task4_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task5_Name = models.CharField(max_length=100,blank=True, default='')
    Task5_Start_Date = models.DateField(blank=True, null=True)
    Task5_End_Date = models.DateField(blank=True, null=True)
    Task5_complete_date = models.DateField(blank=True, null=True)
    Task5_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task6_Name = models.CharField(max_length=100, blank=True,default='')
    Task6_Start_Date = models.DateField(blank=True, null=True)
    Task6_End_Date = models.DateField(blank=True, null=True)
    Task6_complete_date = models.DateField(blank=True, null=True)
    Task6_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task7_Name = models.CharField(max_length=100, blank=True, default='')
    Task7_Start_Date = models.DateField(blank=True, null=True)
    Task7_End_Date = models.DateField(blank=True, null=True)
    Task7_complete_date = models.DateField(blank=True, null=True)
    Task7_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task8_Name = models.CharField(max_length=100, blank=True, default='')
    Task8_Start_Date = models.DateField(blank=True, null=True)
    Task8_End_Date = models.DateField(blank=True, null=True)
    Task8_complete_date = models.DateField(blank=True, null=True)
    Task8_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task9_Name = models.CharField(max_length=100, blank=True, default='')
    Task9_Start_Date = models.DateField(blank=True, null=True)
    Task9_End_Date = models.DateField(blank=True, null=True)
    Task9_complete_date = models.DateField(blank=True, null=True)
    Task9_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task10_Name = models.CharField(max_length=100, blank=True, default='')
    Task10_Start_Date = models.DateField(blank=True, null=True)
    Task10_End_Date = models.DateField(blank=True, null=True)
    Task10_complete_date = models.DateField(blank=True, null=True)
    Task10_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task11_Name = models.CharField(max_length=100, blank=True, default='')
    Task11_Start_Date = models.DateField(blank=True, null=True)
    Task11_End_Date = models.DateField(blank=True, null=True)
    Task11_complete_date = models.DateField(blank=True, null=True)
    Task11_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task12_Name = models.CharField(max_length=100, blank=True, default='')
    Task12_Start_Date = models.DateField(blank=True, null=True)
    Task12_End_Date = models.DateField(blank=True, null=True)
    Task12_complete_date = models.DateField(blank=True, null=True)
    Task12_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task13_Name = models.CharField(max_length=100, blank=True, default='')
    Task13_Start_Date = models.DateField(blank=True, null=True)
    Task13_End_Date = models.DateField(blank=True, null=True)
    Task13_complete_date = models.DateField(blank=True, null=True)
    Task13_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task14_Name = models.CharField(max_length=100, blank=True, default='')
    Task14_Start_Date = models.DateField(blank=True, null=True)
    Task14_End_Date = models.DateField(blank=True, null=True)
    Task14_complete_date = models.DateField(blank=True, null=True)
    Task14_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task15_Name = models.CharField(max_length=100, blank=True, default='')
    Task15_Start_Date = models.DateField(blank=True, null=True)
    Task15_End_Date = models.DateField(blank=True, null=True)
    Task15_complete_date = models.DateField(blank=True, null=True)
    Task15_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task16_Name = models.CharField(max_length=100, blank=True, default='')
    Task16_Start_Date = models.DateField(blank=True, null=True)
    Task16_End_Date = models.DateField(blank=True, null=True)
    Task16_complete_date = models.DateField(blank=True, null=True)
    Task16_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task17_Name = models.CharField(max_length=100, blank=True, default='')
    Task17_Start_Date = models.DateField(blank=True, null=True)
    Task17_End_Date = models.DateField(blank=True, null=True)
    Task17_complete_date = models.DateField(blank=True, null=True)
    Task17_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task18_Name = models.CharField(max_length=100, blank=True, default='')
    Task18_Start_Date = models.DateField(blank=True, null=True)
    Task18_End_Date = models.DateField(blank=True, null=True)
    Task18_complete_date = models.DateField(blank=True, null=True)
    Task18_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task19_Name = models.CharField(max_length=100, blank=True, default='')
    Task19_Start_Date = models.DateField(blank=True, null=True)
    Task19_End_Date = models.DateField(blank=True, null=True)
    Task19_complete_date = models.DateField(blank=True, null=True)
    Task19_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task20_Name = models.CharField(max_length=100, blank=True, default='')
    Task20_Start_Date = models.DateField(blank=True, null=True)
    Task20_End_Date = models.DateField(blank=True, null=True)
    Task20_complete_date = models.DateField(blank=True, null=True)
    Task20_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Time_Delta_For_Warning = models.IntegerField(default=7)
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    Task1_warning = models.BooleanField(default=False)
    Task2_warning = models.BooleanField(default=False)
    Task3_warning = models.BooleanField(default=False)
    Task4_warning = models.BooleanField(default=False)
    Task5_warning = models.BooleanField(default=False)
    Task6_warning = models.BooleanField(default=False)
    Task7_warning = models.BooleanField(default=False)
    Task8_warning = models.BooleanField(default=False)
    Task9_warning = models.BooleanField(default=False)
    Task10_warning = models.BooleanField(default=False)
    Task11_warning = models.BooleanField(default=False)
    Task12_warning = models.BooleanField(default=False)
    Task13_warning = models.BooleanField(default=False)
    Task14_warning = models.BooleanField(default=False)
    Task15_warning = models.BooleanField(default=False)
    Task16_warning = models.BooleanField(default=False)
    Task17_warning = models.BooleanField(default=False)
    Task18_warning = models.BooleanField(default=False)
    Task19_warning = models.BooleanField(default=False)
    Task20_warning = models.BooleanField(default=False)
    Task1_alert = models.BooleanField(default=False)
    Task2_alert = models.BooleanField(default=False)
    Task3_alert = models.BooleanField(default=False)
    Task4_alert = models.BooleanField(default=False)
    Task5_alert = models.BooleanField(default=False)
    Task6_alert = models.BooleanField(default=False)
    Task7_alert = models.BooleanField(default=False)
    Task8_alert = models.BooleanField(default=False)
    Task9_alert = models.BooleanField(default=False)
    Task10_alert = models.BooleanField(default=False)
    Task11_alert = models.BooleanField(default=False)
    Task12_alert = models.BooleanField(default=False)
    Task13_alert = models.BooleanField(default=False)
    Task14_alert = models.BooleanField(default=False)
    Task15_alert = models.BooleanField(default=False)
    Task16_alert = models.BooleanField(default=False)
    Task17_alert = models.BooleanField(default=False)
    Task18_alert = models.BooleanField(default=False)
    Task19_alert = models.BooleanField(default=False)
    Task20_alert = models.BooleanField(default=False)
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')


class Task1Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task2Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task3Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task4Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task5Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task6Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task7Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task8Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task9Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task10Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task11Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task12Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task13Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task14Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task15Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task16Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task17Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task18Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task19Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task20Statuswarehouse(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

########################################################################################################################

class fieldservice(models.Model):
    Poc1 = models.CharField(max_length=100, default='Andrew yoo')
    Poc1_email = models.EmailField(max_length=100, default='jeongyup.y@samsung.com')
    poc2 = models.CharField(max_length=100, default='Ted Lee')
    poc3_email = models.EmailField(max_length=100, default='tedh.lee@samsung.com')
    Task1_Name = models.CharField(max_length=100, default='Determine service category')
    Task1_Start_Date = models.DateField(blank=True, null=True)
    Task1_End_Date = models.DateField(blank=True, null=True)
    Task1_complete_date = models.DateField(blank=True, null=True)
    Task1_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task2_Name = models.CharField(max_length=100, default='Warranty Review')
    Task2_Start_Date = models.DateField(blank=True, null=True)
    Task2_End_Date = models.DateField(blank=True, null=True)
    Task2_complete_date = models.DateField(blank=True, null=True)
    Task2_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task3_Name = models.CharField(max_length=100, default='Develop new service procedure')
    Task3_Start_Date = models.DateField(blank=True, null=True)
    Task3_End_Date = models.DateField(blank=True, null=True)
    Task3_complete_date = models.DateField(blank=True, null=True)
    Task3_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task4_Name = models.CharField(max_length=100,blank=True, default='')
    Task4_Start_Date = models.DateField(blank=True, null=True)
    Task4_End_Date = models.DateField(blank=True, null=True)
    Task4_complete_date = models.DateField(blank=True, null=True)
    Task4_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task5_Name = models.CharField(max_length=100,blank=True, default='')
    Task5_Start_Date = models.DateField(blank=True, null=True)
    Task5_End_Date = models.DateField(blank=True, null=True)
    Task5_complete_date = models.DateField(blank=True, null=True)
    Task5_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task6_Name = models.CharField(max_length=100,blank=True, default='')
    Task6_Start_Date = models.DateField(blank=True, null=True)
    Task6_End_Date = models.DateField(blank=True, null=True)
    Task6_complete_date = models.DateField(blank=True, null=True)
    Task6_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task7_Name = models.CharField(max_length=100, blank=True, default='')
    Task7_Start_Date = models.DateField(blank=True, null=True)
    Task7_End_Date = models.DateField(blank=True, null=True)
    Task7_complete_date = models.DateField(blank=True, null=True)
    Task7_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task8_Name = models.CharField(max_length=100, blank=True, default='')
    Task8_Start_Date = models.DateField(blank=True, null=True)
    Task8_End_Date = models.DateField(blank=True, null=True)
    Task8_complete_date = models.DateField(blank=True, null=True)
    Task8_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task9_Name = models.CharField(max_length=100, blank=True, default='')
    Task9_Start_Date = models.DateField(blank=True, null=True)
    Task9_End_Date = models.DateField(blank=True, null=True)
    Task9_complete_date = models.DateField(blank=True, null=True)
    Task9_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task10_Name = models.CharField(max_length=100, blank=True, default='')
    Task10_Start_Date = models.DateField(blank=True, null=True)
    Task10_End_Date = models.DateField(blank=True, null=True)
    Task10_complete_date = models.DateField(blank=True, null=True)
    Task10_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task11_Name = models.CharField(max_length=100, blank=True, default='')
    Task11_Start_Date = models.DateField(blank=True, null=True)
    Task11_End_Date = models.DateField(blank=True, null=True)
    Task11_complete_date = models.DateField(blank=True, null=True)
    Task11_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task12_Name = models.CharField(max_length=100, blank=True, default='')
    Task12_Start_Date = models.DateField(blank=True, null=True)
    Task12_End_Date = models.DateField(blank=True, null=True)
    Task12_complete_date = models.DateField(blank=True, null=True)
    Task12_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task13_Name = models.CharField(max_length=100, blank=True, default='')
    Task13_Start_Date = models.DateField(blank=True, null=True)
    Task13_End_Date = models.DateField(blank=True, null=True)
    Task13_complete_date = models.DateField(blank=True, null=True)
    Task13_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task14_Name = models.CharField(max_length=100, blank=True, default='')
    Task14_Start_Date = models.DateField(blank=True, null=True)
    Task14_End_Date = models.DateField(blank=True, null=True)
    Task14_complete_date = models.DateField(blank=True, null=True)
    Task14_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task15_Name = models.CharField(max_length=100, blank=True, default='')
    Task15_Start_Date = models.DateField(blank=True, null=True)
    Task15_End_Date = models.DateField(blank=True, null=True)
    Task15_complete_date = models.DateField(blank=True, null=True)
    Task15_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task16_Name = models.CharField(max_length=100, blank=True, default='')
    Task16_Start_Date = models.DateField(blank=True, null=True)
    Task16_End_Date = models.DateField(blank=True, null=True)
    Task16_complete_date = models.DateField(blank=True, null=True)
    Task16_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task17_Name = models.CharField(max_length=100, blank=True, default='')
    Task17_Start_Date = models.DateField(blank=True, null=True)
    Task17_End_Date = models.DateField(blank=True, null=True)
    Task17_complete_date = models.DateField(blank=True, null=True)
    Task17_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task18_Name = models.CharField(max_length=100, blank=True, default='')
    Task18_Start_Date = models.DateField(blank=True, null=True)
    Task18_End_Date = models.DateField(blank=True, null=True)
    Task18_complete_date = models.DateField(blank=True, null=True)
    Task18_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task19_Name = models.CharField(max_length=100, blank=True, default='')
    Task19_Start_Date = models.DateField(blank=True, null=True)
    Task19_End_Date = models.DateField(blank=True, null=True)
    Task19_complete_date = models.DateField(blank=True, null=True)
    Task19_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task20_Name = models.CharField(max_length=100, blank=True, default='')
    Task20_Start_Date = models.DateField(blank=True, null=True)
    Task20_End_Date = models.DateField(blank=True, null=True)
    Task20_complete_date = models.DateField(blank=True, null=True)
    Task20_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Time_Delta_For_Warning = models.IntegerField(default=7)
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    Task1_warning = models.BooleanField(default=False)
    Task2_warning = models.BooleanField(default=False)
    Task3_warning = models.BooleanField(default=False)
    Task4_warning = models.BooleanField(default=False)
    Task5_warning = models.BooleanField(default=False)
    Task6_warning = models.BooleanField(default=False)
    Task7_warning = models.BooleanField(default=False)
    Task8_warning = models.BooleanField(default=False)
    Task9_warning = models.BooleanField(default=False)
    Task10_warning = models.BooleanField(default=False)
    Task11_warning = models.BooleanField(default=False)
    Task12_warning = models.BooleanField(default=False)
    Task13_warning = models.BooleanField(default=False)
    Task14_warning = models.BooleanField(default=False)
    Task15_warning = models.BooleanField(default=False)
    Task16_warning = models.BooleanField(default=False)
    Task17_warning = models.BooleanField(default=False)
    Task18_warning = models.BooleanField(default=False)
    Task19_warning = models.BooleanField(default=False)
    Task20_warning = models.BooleanField(default=False)
    Task1_alert = models.BooleanField(default=False)
    Task2_alert = models.BooleanField(default=False)
    Task3_alert = models.BooleanField(default=False)
    Task4_alert = models.BooleanField(default=False)
    Task5_alert = models.BooleanField(default=False)
    Task6_alert = models.BooleanField(default=False)
    Task7_alert = models.BooleanField(default=False)
    Task8_alert = models.BooleanField(default=False)
    Task9_alert = models.BooleanField(default=False)
    Task10_alert = models.BooleanField(default=False)
    Task11_alert = models.BooleanField(default=False)
    Task12_alert = models.BooleanField(default=False)
    Task13_alert = models.BooleanField(default=False)
    Task14_alert = models.BooleanField(default=False)
    Task15_alert = models.BooleanField(default=False)
    Task16_alert = models.BooleanField(default=False)
    Task17_alert = models.BooleanField(default=False)
    Task18_alert = models.BooleanField(default=False)
    Task19_alert = models.BooleanField(default=False)
    Task20_alert = models.BooleanField(default=False)
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')


class Task1Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task2Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task3Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task4Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task5Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task6Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task7Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task8Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task9Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task10Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task11Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task12Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task13Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task14Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task15Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task16Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task17Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task18Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task19Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task20Statusfieldservice(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    FieldService = models.ForeignKey(fieldservice, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

########################################################################################################################

class techsupport(models.Model):
    Poc1 = models.CharField(max_length=100, default='Jeffery Brutman')
    Poc1_email = models.EmailField(max_length=100, default='j.brutman@samsung.com')
    poc2 = models.CharField(max_length=100, default='Rick Heal')
    poc3_email = models.EmailField(max_length=100, default='f.heal@samsung.com')
    Task1_Name = models.CharField(max_length=100, default='User Manual received')
    Task1_Start_Date = models.DateField(blank=True, null=True)
    Task1_End_Date = models.DateField(blank=True, null=True)
    Task1_complete_date = models.DateField(blank=True, null=True)
    Task1_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task2_Name = models.CharField(max_length=100, default='User Manual Review and Revisions')
    Task2_Start_Date = models.DateField(blank=True, null=True)
    Task2_End_Date = models.DateField(blank=True, null=True)
    Task2_complete_date = models.DateField(blank=True, null=True)
    Task2_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task3_Name = models.CharField(max_length=100, default='User Manual Completion and Approval')
    Task3_Start_Date = models.DateField(blank=True, null=True)
    Task3_End_Date = models.DateField(blank=True, null=True)
    Task3_complete_date = models.DateField(blank=True, null=True)
    Task3_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task4_Name = models.CharField(max_length=100,blank=True, default='')
    Task4_Start_Date = models.DateField(blank=True, null=True)
    Task4_End_Date = models.DateField(blank=True, null=True)
    Task4_complete_date = models.DateField(blank=True, null=True)
    Task4_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task5_Name = models.CharField(max_length=100,blank=True, default='')
    Task5_Start_Date = models.DateField(blank=True, null=True)
    Task5_End_Date = models.DateField(blank=True, null=True)
    Task5_complete_date = models.DateField(blank=True, null=True)
    Task5_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task6_Name = models.CharField(max_length=100,blank=True, default='')
    Task6_Start_Date = models.DateField(blank=True, null=True)
    Task6_End_Date = models.DateField(blank=True, null=True)
    Task6_complete_date = models.DateField(blank=True, null=True)
    Task6_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task7_Name = models.CharField(max_length=100, blank=True, default='')
    Task7_Start_Date = models.DateField(blank=True, null=True)
    Task7_End_Date = models.DateField(blank=True, null=True)
    Task7_complete_date = models.DateField(blank=True, null=True)
    Task7_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task8_Name = models.CharField(max_length=100, blank=True, default='')
    Task8_Start_Date = models.DateField(blank=True, null=True)
    Task8_End_Date = models.DateField(blank=True, null=True)
    Task8_complete_date = models.DateField(blank=True, null=True)
    Task8_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task9_Name = models.CharField(max_length=100, blank=True, default='')
    Task9_Start_Date = models.DateField(blank=True, null=True)
    Task9_End_Date = models.DateField(blank=True, null=True)
    Task9_complete_date = models.DateField(blank=True, null=True)
    Task9_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task10_Name = models.CharField(max_length=100, blank=True, default='')
    Task10_Start_Date = models.DateField(blank=True, null=True)
    Task10_End_Date = models.DateField(blank=True, null=True)
    Task10_complete_date = models.DateField(blank=True, null=True)
    Task10_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task11_Name = models.CharField(max_length=100, blank=True, default='')
    Task11_Start_Date = models.DateField(blank=True, null=True)
    Task11_End_Date = models.DateField(blank=True, null=True)
    Task11_complete_date = models.DateField(blank=True, null=True)
    Task11_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task12_Name = models.CharField(max_length=100, blank=True, default='')
    Task12_Start_Date = models.DateField(blank=True, null=True)
    Task12_End_Date = models.DateField(blank=True, null=True)
    Task12_complete_date = models.DateField(blank=True, null=True)
    Task12_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task13_Name = models.CharField(max_length=100, blank=True, default='')
    Task13_Start_Date = models.DateField(blank=True, null=True)
    Task13_End_Date = models.DateField(blank=True, null=True)
    Task13_complete_date = models.DateField(blank=True, null=True)
    Task13_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task14_Name = models.CharField(max_length=100, blank=True, default='')
    Task14_Start_Date = models.DateField(blank=True, null=True)
    Task14_End_Date = models.DateField(blank=True, null=True)
    Task14_complete_date = models.DateField(blank=True, null=True)
    Task14_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task15_Name = models.CharField(max_length=100, blank=True, default='')
    Task15_Start_Date = models.DateField(blank=True, null=True)
    Task15_End_Date = models.DateField(blank=True, null=True)
    Task15_complete_date = models.DateField(blank=True, null=True)
    Task15_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task16_Name = models.CharField(max_length=100, blank=True, default='')
    Task16_Start_Date = models.DateField(blank=True, null=True)
    Task16_End_Date = models.DateField(blank=True, null=True)
    Task16_complete_date = models.DateField(blank=True, null=True)
    Task16_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task17_Name = models.CharField(max_length=100, blank=True, default='')
    Task17_Start_Date = models.DateField(blank=True, null=True)
    Task17_End_Date = models.DateField(blank=True, null=True)
    Task17_complete_date = models.DateField(blank=True, null=True)
    Task17_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task18_Name = models.CharField(max_length=100, blank=True, default='')
    Task18_Start_Date = models.DateField(blank=True, null=True)
    Task18_End_Date = models.DateField(blank=True, null=True)
    Task18_complete_date = models.DateField(blank=True, null=True)
    Task18_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task19_Name = models.CharField(max_length=100, blank=True, default='')
    Task19_Start_Date = models.DateField(blank=True, null=True)
    Task19_End_Date = models.DateField(blank=True, null=True)
    Task19_complete_date = models.DateField(blank=True, null=True)
    Task19_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task20_Name = models.CharField(max_length=100, blank=True, default='')
    Task20_Start_Date = models.DateField(blank=True, null=True)
    Task20_End_Date = models.DateField(blank=True, null=True)
    Task20_complete_date = models.DateField(blank=True, null=True)
    Task20_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Time_Delta_For_Warning = models.IntegerField(default=7)
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    Task1_warning = models.BooleanField(default=False)
    Task2_warning = models.BooleanField(default=False)
    Task3_warning = models.BooleanField(default=False)
    Task4_warning = models.BooleanField(default=False)
    Task5_warning = models.BooleanField(default=False)
    Task6_warning = models.BooleanField(default=False)
    Task7_warning = models.BooleanField(default=False)
    Task8_warning = models.BooleanField(default=False)
    Task9_warning = models.BooleanField(default=False)
    Task10_warning = models.BooleanField(default=False)
    Task11_warning = models.BooleanField(default=False)
    Task12_warning = models.BooleanField(default=False)
    Task13_warning = models.BooleanField(default=False)
    Task14_warning = models.BooleanField(default=False)
    Task15_warning = models.BooleanField(default=False)
    Task16_warning = models.BooleanField(default=False)
    Task17_warning = models.BooleanField(default=False)
    Task18_warning = models.BooleanField(default=False)
    Task19_warning = models.BooleanField(default=False)
    Task20_warning = models.BooleanField(default=False)
    Task1_alert = models.BooleanField(default=False)
    Task2_alert = models.BooleanField(default=False)
    Task3_alert = models.BooleanField(default=False)
    Task4_alert = models.BooleanField(default=False)
    Task5_alert = models.BooleanField(default=False)
    Task6_alert = models.BooleanField(default=False)
    Task7_alert = models.BooleanField(default=False)
    Task8_alert = models.BooleanField(default=False)
    Task9_alert = models.BooleanField(default=False)
    Task10_alert = models.BooleanField(default=False)
    Task11_alert = models.BooleanField(default=False)
    Task12_alert = models.BooleanField(default=False)
    Task13_alert = models.BooleanField(default=False)
    Task14_alert = models.BooleanField(default=False)
    Task15_alert = models.BooleanField(default=False)
    Task16_alert = models.BooleanField(default=False)
    Task17_alert = models.BooleanField(default=False)
    Task18_alert = models.BooleanField(default=False)
    Task19_alert = models.BooleanField(default=False)
    Task20_alert = models.BooleanField(default=False)
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')


class Task1Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task2Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task3Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task4Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task5Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task6Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task7Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task8Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task9Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task10Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task11Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task12Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task13Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task14Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task15Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task16Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task17Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task18Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task19Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task20Statustechsupport(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    TechSupport = models.ForeignKey(techsupport, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

########################################################################################################################

class servicemarketing(models.Model):
    Poc1 = models.CharField(max_length=100, default='Jessica Yu')
    Poc1_email = models.EmailField(max_length=100, default='jessica.yu@samsung.com')
    poc2 = models.CharField(max_length=100, default='Mohsen Sheikh')
    poc3_email = models.EmailField(max_length=100, default='m.sheikh@samsung.com')
    Task1_Name = models.CharField(max_length=100, default='Determin VIP status')
    Task1_Start_Date = models.DateField(blank=True, null=True)
    Task1_End_Date = models.DateField(blank=True, null=True)
    Task1_complete_date = models.DateField(blank=True, null=True)
    Task1_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task2_Name = models.CharField(max_length=100, default='Flag GCIC, Develop content')
    Task2_Start_Date = models.DateField(blank=True, null=True)
    Task2_End_Date = models.DateField(blank=True, null=True)
    Task2_complete_date = models.DateField(blank=True, null=True)
    Task2_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task3_Name = models.CharField(max_length=100, default='Train Agents')
    Task3_Start_Date = models.DateField(blank=True, null=True)
    Task3_End_Date = models.DateField(blank=True, null=True)
    Task3_complete_date = models.DateField(blank=True, null=True)
    Task3_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task4_Name = models.CharField(max_length=100,blank=True, default='Train Network (demo checklist)')
    Task4_Start_Date = models.DateField(blank=True, null=True)
    Task4_End_Date = models.DateField(blank=True, null=True)
    Task4_complete_date = models.DateField(blank=True, null=True)
    Task4_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task5_Name = models.CharField(max_length=100,blank=True, default='')
    Task5_Start_Date = models.DateField(blank=True, null=True)
    Task5_End_Date = models.DateField(blank=True, null=True)
    Task5_complete_date = models.DateField(blank=True, null=True)
    Task5_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task6_Name = models.CharField(max_length=100,blank=True, default='')
    Task6_Start_Date = models.DateField(blank=True, null=True)
    Task6_End_Date = models.DateField(blank=True, null=True)
    Task6_complete_date = models.DateField(blank=True, null=True)
    Task6_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task7_Name = models.CharField(max_length=100, blank=True, default='')
    Task7_Start_Date = models.DateField(blank=True, null=True)
    Task7_End_Date = models.DateField(blank=True, null=True)
    Task7_complete_date = models.DateField(blank=True, null=True)
    Task7_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task8_Name = models.CharField(max_length=100, blank=True, default='')
    Task8_Start_Date = models.DateField(blank=True, null=True)
    Task8_End_Date = models.DateField(blank=True, null=True)
    Task8_complete_date = models.DateField(blank=True, null=True)
    Task8_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task9_Name = models.CharField(max_length=100, blank=True, default='')
    Task9_Start_Date = models.DateField(blank=True, null=True)
    Task9_End_Date = models.DateField(blank=True, null=True)
    Task9_complete_date = models.DateField(blank=True, null=True)
    Task9_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task10_Name = models.CharField(max_length=100, blank=True, default='')
    Task10_Start_Date = models.DateField(blank=True, null=True)
    Task10_End_Date = models.DateField(blank=True, null=True)
    Task10_complete_date = models.DateField(blank=True, null=True)
    Task10_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task11_Name = models.CharField(max_length=100, blank=True, default='')
    Task11_Start_Date = models.DateField(blank=True, null=True)
    Task11_End_Date = models.DateField(blank=True, null=True)
    Task11_complete_date = models.DateField(blank=True, null=True)
    Task11_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task12_Name = models.CharField(max_length=100, blank=True, default='')
    Task12_Start_Date = models.DateField(blank=True, null=True)
    Task12_End_Date = models.DateField(blank=True, null=True)
    Task12_complete_date = models.DateField(blank=True, null=True)
    Task12_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task13_Name = models.CharField(max_length=100, blank=True, default='')
    Task13_Start_Date = models.DateField(blank=True, null=True)
    Task13_End_Date = models.DateField(blank=True, null=True)
    Task13_complete_date = models.DateField(blank=True, null=True)
    Task13_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task14_Name = models.CharField(max_length=100, blank=True, default='')
    Task14_Start_Date = models.DateField(blank=True, null=True)
    Task14_End_Date = models.DateField(blank=True, null=True)
    Task14_complete_date = models.DateField(blank=True, null=True)
    Task14_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task15_Name = models.CharField(max_length=100, blank=True, default='')
    Task15_Start_Date = models.DateField(blank=True, null=True)
    Task15_End_Date = models.DateField(blank=True, null=True)
    Task15_complete_date = models.DateField(blank=True, null=True)
    Task15_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task16_Name = models.CharField(max_length=100, blank=True, default='')
    Task16_Start_Date = models.DateField(blank=True, null=True)
    Task16_End_Date = models.DateField(blank=True, null=True)
    Task16_complete_date = models.DateField(blank=True, null=True)
    Task16_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task17_Name = models.CharField(max_length=100, blank=True, default='')
    Task17_Start_Date = models.DateField(blank=True, null=True)
    Task17_End_Date = models.DateField(blank=True, null=True)
    Task17_complete_date = models.DateField(blank=True, null=True)
    Task17_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task18_Name = models.CharField(max_length=100, blank=True, default='')
    Task18_Start_Date = models.DateField(blank=True, null=True)
    Task18_End_Date = models.DateField(blank=True, null=True)
    Task18_complete_date = models.DateField(blank=True, null=True)
    Task18_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task19_Name = models.CharField(max_length=100, blank=True, default='')
    Task19_Start_Date = models.DateField(blank=True, null=True)
    Task19_End_Date = models.DateField(blank=True, null=True)
    Task19_complete_date = models.DateField(blank=True, null=True)
    Task19_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task20_Name = models.CharField(max_length=100, blank=True, default='')
    Task20_Start_Date = models.DateField(blank=True, null=True)
    Task20_End_Date = models.DateField(blank=True, null=True)
    Task20_complete_date = models.DateField(blank=True, null=True)
    Task20_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Time_Delta_For_Warning = models.IntegerField(default=7)
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    Task1_warning = models.BooleanField(default=False)
    Task2_warning = models.BooleanField(default=False)
    Task3_warning = models.BooleanField(default=False)
    Task4_warning = models.BooleanField(default=False)
    Task5_warning = models.BooleanField(default=False)
    Task6_warning = models.BooleanField(default=False)
    Task7_warning = models.BooleanField(default=False)
    Task8_warning = models.BooleanField(default=False)
    Task9_warning = models.BooleanField(default=False)
    Task10_warning = models.BooleanField(default=False)
    Task11_warning = models.BooleanField(default=False)
    Task12_warning = models.BooleanField(default=False)
    Task13_warning = models.BooleanField(default=False)
    Task14_warning = models.BooleanField(default=False)
    Task15_warning = models.BooleanField(default=False)
    Task16_warning = models.BooleanField(default=False)
    Task17_warning = models.BooleanField(default=False)
    Task18_warning = models.BooleanField(default=False)
    Task19_warning = models.BooleanField(default=False)
    Task20_warning = models.BooleanField(default=False)
    Task1_alert = models.BooleanField(default=False)
    Task2_alert = models.BooleanField(default=False)
    Task3_alert = models.BooleanField(default=False)
    Task4_alert = models.BooleanField(default=False)
    Task5_alert = models.BooleanField(default=False)
    Task6_alert = models.BooleanField(default=False)
    Task7_alert = models.BooleanField(default=False)
    Task8_alert = models.BooleanField(default=False)
    Task9_alert = models.BooleanField(default=False)
    Task10_alert = models.BooleanField(default=False)
    Task11_alert = models.BooleanField(default=False)
    Task12_alert = models.BooleanField(default=False)
    Task13_alert = models.BooleanField(default=False)
    Task14_alert = models.BooleanField(default=False)
    Task15_alert = models.BooleanField(default=False)
    Task16_alert = models.BooleanField(default=False)
    Task17_alert = models.BooleanField(default=False)
    Task18_alert = models.BooleanField(default=False)
    Task19_alert = models.BooleanField(default=False)
    Task20_alert = models.BooleanField(default=False)
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')


class Task1Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task2Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task3Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task4Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task5Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task6Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task7Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task8Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task9Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task10Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task11Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task12Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task13Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task14Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task15Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task16Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task17Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task18Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task19Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task20Statusservicemarketing(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicemarketing, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

########################################################################################################################

class servicetraining(models.Model):
    Poc1 = models.CharField(max_length=100, default='Nicholas Webert')
    Poc1_email = models.EmailField(max_length=100, default='n.webert@samsung.com')
    poc2 = models.CharField(max_length=100, default='Micheal Yelo')
    poc3_email = models.EmailField(max_length=100, default='m.yelo@samsung.com')
    Task1_Name = models.CharField(max_length=100, default='Doc Review: Training Manual')
    Task1_Start_Date = models.DateField(blank=True, null=True)
    Task1_End_Date = models.DateField(blank=True, null=True)
    Task1_complete_date = models.DateField(blank=True, null=True)
    Task1_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task2_Name = models.CharField(max_length=100, default='TV Certification Training Guide')
    Task2_Start_Date = models.DateField(blank=True, null=True)
    Task2_End_Date = models.DateField(blank=True, null=True)
    Task2_complete_date = models.DateField(blank=True, null=True)
    Task2_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task3_Name = models.CharField(max_length=100, default='Update eLearning')
    Task3_Start_Date = models.DateField(blank=True, null=True)
    Task3_End_Date = models.DateField(blank=True, null=True)
    Task3_complete_date = models.DateField(blank=True, null=True)
    Task3_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task4_Name = models.CharField(max_length=100,blank=True, default='Train Tech Support')
    Task4_Start_Date = models.DateField(blank=True, null=True)
    Task4_End_Date = models.DateField(blank=True, null=True)
    Task4_complete_date = models.DateField(blank=True, null=True)
    Task4_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task5_Name = models.CharField(max_length=100,blank=True, default='Train the trainer')
    Task5_Start_Date = models.DateField(blank=True, null=True)
    Task5_End_Date = models.DateField(blank=True, null=True)
    Task5_complete_date = models.DateField(blank=True, null=True)
    Task5_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task6_Name = models.CharField(max_length=100,blank=True, default='Fast Track')
    Task6_Start_Date = models.DateField(blank=True, null=True)
    Task6_End_Date = models.DateField(blank=True, null=True)
    Task6_complete_date = models.DateField(blank=True, null=True)
    Task6_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task7_Name = models.CharField(max_length=100, blank=True, default='')
    Task7_Start_Date = models.DateField(blank=True, null=True)
    Task7_End_Date = models.DateField(blank=True, null=True)
    Task7_complete_date = models.DateField(blank=True, null=True)
    Task7_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task8_Name = models.CharField(max_length=100, blank=True, default='')
    Task8_Start_Date = models.DateField(blank=True, null=True)
    Task8_End_Date = models.DateField(blank=True, null=True)
    Task8_complete_date = models.DateField(blank=True, null=True)
    Task8_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task9_Name = models.CharField(max_length=100, blank=True, default='')
    Task9_Start_Date = models.DateField(blank=True, null=True)
    Task9_End_Date = models.DateField(blank=True, null=True)
    Task9_complete_date = models.DateField(blank=True, null=True)
    Task9_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task10_Name = models.CharField(max_length=100, blank=True, default='')
    Task10_Start_Date = models.DateField(blank=True, null=True)
    Task10_End_Date = models.DateField(blank=True, null=True)
    Task10_complete_date = models.DateField(blank=True, null=True)
    Task10_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task11_Name = models.CharField(max_length=100, blank=True, default='')
    Task11_Start_Date = models.DateField(blank=True, null=True)
    Task11_End_Date = models.DateField(blank=True, null=True)
    Task11_complete_date = models.DateField(blank=True, null=True)
    Task11_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task12_Name = models.CharField(max_length=100, blank=True, default='')
    Task12_Start_Date = models.DateField(blank=True, null=True)
    Task12_End_Date = models.DateField(blank=True, null=True)
    Task12_complete_date = models.DateField(blank=True, null=True)
    Task12_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task13_Name = models.CharField(max_length=100, blank=True, default='')
    Task13_Start_Date = models.DateField(blank=True, null=True)
    Task13_End_Date = models.DateField(blank=True, null=True)
    Task13_complete_date = models.DateField(blank=True, null=True)
    Task13_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task14_Name = models.CharField(max_length=100, blank=True, default='')
    Task14_Start_Date = models.DateField(blank=True, null=True)
    Task14_End_Date = models.DateField(blank=True, null=True)
    Task14_complete_date = models.DateField(blank=True, null=True)
    Task14_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task15_Name = models.CharField(max_length=100, blank=True, default='')
    Task15_Start_Date = models.DateField(blank=True, null=True)
    Task15_End_Date = models.DateField(blank=True, null=True)
    Task15_complete_date = models.DateField(blank=True, null=True)
    Task15_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task16_Name = models.CharField(max_length=100, blank=True, default='')
    Task16_Start_Date = models.DateField(blank=True, null=True)
    Task16_End_Date = models.DateField(blank=True, null=True)
    Task16_complete_date = models.DateField(blank=True, null=True)
    Task16_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task17_Name = models.CharField(max_length=100, blank=True, default='')
    Task17_Start_Date = models.DateField(blank=True, null=True)
    Task17_End_Date = models.DateField(blank=True, null=True)
    Task17_complete_date = models.DateField(blank=True, null=True)
    Task17_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task18_Name = models.CharField(max_length=100, blank=True, default='')
    Task18_Start_Date = models.DateField(blank=True, null=True)
    Task18_End_Date = models.DateField(blank=True, null=True)
    Task18_complete_date = models.DateField(blank=True, null=True)
    Task18_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task19_Name = models.CharField(max_length=100, blank=True, default='')
    Task19_Start_Date = models.DateField(blank=True, null=True)
    Task19_End_Date = models.DateField(blank=True, null=True)
    Task19_complete_date = models.DateField(blank=True, null=True)
    Task19_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task20_Name = models.CharField(max_length=100, blank=True, default='')
    Task20_Start_Date = models.DateField(blank=True, null=True)
    Task20_End_Date = models.DateField(blank=True, null=True)
    Task20_complete_date = models.DateField(blank=True, null=True)
    Task20_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Time_Delta_For_Warning = models.IntegerField(default=7)
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    Task1_warning = models.BooleanField(default=False)
    Task2_warning = models.BooleanField(default=False)
    Task3_warning = models.BooleanField(default=False)
    Task4_warning = models.BooleanField(default=False)
    Task5_warning = models.BooleanField(default=False)
    Task6_warning = models.BooleanField(default=False)
    Task7_warning = models.BooleanField(default=False)
    Task8_warning = models.BooleanField(default=False)
    Task9_warning = models.BooleanField(default=False)
    Task10_warning = models.BooleanField(default=False)
    Task11_warning = models.BooleanField(default=False)
    Task12_warning = models.BooleanField(default=False)
    Task13_warning = models.BooleanField(default=False)
    Task14_warning = models.BooleanField(default=False)
    Task15_warning = models.BooleanField(default=False)
    Task16_warning = models.BooleanField(default=False)
    Task17_warning = models.BooleanField(default=False)
    Task18_warning = models.BooleanField(default=False)
    Task19_warning = models.BooleanField(default=False)
    Task20_warning = models.BooleanField(default=False)
    Task1_alert = models.BooleanField(default=False)
    Task2_alert = models.BooleanField(default=False)
    Task3_alert = models.BooleanField(default=False)
    Task4_alert = models.BooleanField(default=False)
    Task5_alert = models.BooleanField(default=False)
    Task6_alert = models.BooleanField(default=False)
    Task7_alert = models.BooleanField(default=False)
    Task8_alert = models.BooleanField(default=False)
    Task9_alert = models.BooleanField(default=False)
    Task10_alert = models.BooleanField(default=False)
    Task11_alert = models.BooleanField(default=False)
    Task12_alert = models.BooleanField(default=False)
    Task13_alert = models.BooleanField(default=False)
    Task14_alert = models.BooleanField(default=False)
    Task15_alert = models.BooleanField(default=False)
    Task16_alert = models.BooleanField(default=False)
    Task17_alert = models.BooleanField(default=False)
    Task18_alert = models.BooleanField(default=False)
    Task19_alert = models.BooleanField(default=False)
    Task20_alert = models.BooleanField(default=False)
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')


class Task1Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task2Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task3Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task4Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task5Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task6Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task7Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task8Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task9Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task10Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task11Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task12Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task13Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task14Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task15Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceMarketing = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task16Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task17Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task18Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task19Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task20Statusservicetraining(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    ServiceTraining = models.ForeignKey(servicetraining, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

########################################################################################################################

class parts(models.Model):
    Poc1 = models.CharField(max_length=100, default='David Caldwell')
    Poc1_email = models.EmailField(max_length=100, default='d.caldwell@samsung.com')
    poc2 = models.CharField(max_length=100, default='Gregory Pak')
    poc3_email = models.EmailField(max_length=100, default='greg.pak@samsung.com')
    Task1_Name = models.CharField(max_length=100, default='BOM Review')
    Task1_Start_Date = models.DateField(blank=True, null=True)
    Task1_End_Date = models.DateField(blank=True, null=True)
    Task1_complete_date = models.DateField(blank=True, null=True)
    Task1_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task2_Name = models.CharField(max_length=100, default='Initial Parts Ordering')
    Task2_Start_Date = models.DateField(blank=True, null=True)
    Task2_End_Date = models.DateField(blank=True, null=True)
    Task2_complete_date = models.DateField(blank=True, null=True)
    Task2_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task3_Name = models.CharField(max_length=100, default='Parts Available: Panel')
    Task3_Start_Date = models.DateField(blank=True, null=True)
    Task3_End_Date = models.DateField(blank=True, null=True)
    Task3_complete_date = models.DateField(blank=True, null=True)
    Task3_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task4_Name = models.CharField(max_length=100,blank=True, default='Parts Available: TV/Main')
    Task4_Start_Date = models.DateField(blank=True, null=True)
    Task4_End_Date = models.DateField(blank=True, null=True)
    Task4_complete_date = models.DateField(blank=True, null=True)
    Task4_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task5_Name = models.CharField(max_length=100,blank=True, default='Parts Available: OCB/OCM')
    Task5_Start_Date = models.DateField(blank=True, null=True)
    Task5_End_Date = models.DateField(blank=True, null=True)
    Task5_complete_date = models.DateField(blank=True, null=True)
    Task5_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task6_Name = models.CharField(max_length=100,blank=True, default='Parts Available: SMPS')
    Task6_Start_Date = models.DateField(blank=True, null=True)
    Task6_End_Date = models.DateField(blank=True, null=True)
    Task6_complete_date = models.DateField(blank=True, null=True)
    Task6_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task7_Name = models.CharField(max_length=100, blank=True, default='Parts Available: Light Dimming')
    Task7_Start_Date = models.DateField(blank=True, null=True)
    Task7_End_Date = models.DateField(blank=True, null=True)
    Task7_complete_date = models.DateField(blank=True, null=True)
    Task7_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task8_Name = models.CharField(max_length=100, blank=True, default='')
    Task8_Start_Date = models.DateField(blank=True, null=True)
    Task8_End_Date = models.DateField(blank=True, null=True)
    Task8_complete_date = models.DateField(blank=True, null=True)
    Task8_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task9_Name = models.CharField(max_length=100, blank=True, default='')
    Task9_Start_Date = models.DateField(blank=True, null=True)
    Task9_End_Date = models.DateField(blank=True, null=True)
    Task9_complete_date = models.DateField(blank=True, null=True)
    Task9_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task10_Name = models.CharField(max_length=100, blank=True, default='')
    Task10_Start_Date = models.DateField(blank=True, null=True)
    Task10_End_Date = models.DateField(blank=True, null=True)
    Task10_complete_date = models.DateField(blank=True, null=True)
    Task10_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task11_Name = models.CharField(max_length=100, blank=True, default='')
    Task11_Start_Date = models.DateField(blank=True, null=True)
    Task11_End_Date = models.DateField(blank=True, null=True)
    Task11_complete_date = models.DateField(blank=True, null=True)
    Task11_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task12_Name = models.CharField(max_length=100, blank=True, default='')
    Task12_Start_Date = models.DateField(blank=True, null=True)
    Task12_End_Date = models.DateField(blank=True, null=True)
    Task12_complete_date = models.DateField(blank=True, null=True)
    Task12_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task13_Name = models.CharField(max_length=100, blank=True, default='')
    Task13_Start_Date = models.DateField(blank=True, null=True)
    Task13_End_Date = models.DateField(blank=True, null=True)
    Task13_complete_date = models.DateField(blank=True, null=True)
    Task13_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task14_Name = models.CharField(max_length=100, blank=True, default='')
    Task14_Start_Date = models.DateField(blank=True, null=True)
    Task14_End_Date = models.DateField(blank=True, null=True)
    Task14_complete_date = models.DateField(blank=True, null=True)
    Task14_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task15_Name = models.CharField(max_length=100, blank=True, default='')
    Task15_Start_Date = models.DateField(blank=True, null=True)
    Task15_End_Date = models.DateField(blank=True, null=True)
    Task15_complete_date = models.DateField(blank=True, null=True)
    Task15_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task16_Name = models.CharField(max_length=100, blank=True, default='')
    Task16_Start_Date = models.DateField(blank=True, null=True)
    Task16_End_Date = models.DateField(blank=True, null=True)
    Task16_complete_date = models.DateField(blank=True, null=True)
    Task16_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task17_Name = models.CharField(max_length=100, blank=True, default='')
    Task17_Start_Date = models.DateField(blank=True, null=True)
    Task17_End_Date = models.DateField(blank=True, null=True)
    Task17_complete_date = models.DateField(blank=True, null=True)
    Task17_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task18_Name = models.CharField(max_length=100, blank=True, default='')
    Task18_Start_Date = models.DateField(blank=True, null=True)
    Task18_End_Date = models.DateField(blank=True, null=True)
    Task18_complete_date = models.DateField(blank=True, null=True)
    Task18_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task19_Name = models.CharField(max_length=100, blank=True, default='')
    Task19_Start_Date = models.DateField(blank=True, null=True)
    Task19_End_Date = models.DateField(blank=True, null=True)
    Task19_complete_date = models.DateField(blank=True, null=True)
    Task19_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Task20_Name = models.CharField(max_length=100, blank=True, default='')
    Task20_Start_Date = models.DateField(blank=True, null=True)
    Task20_End_Date = models.DateField(blank=True, null=True)
    Task20_complete_date = models.DateField(blank=True, null=True)
    Task20_dependent_task = models.CharField(max_length=250,blank=True, default='')
    Time_Delta_For_Warning = models.IntegerField(default=7)
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    Task1_warning = models.BooleanField(default=False)
    Task2_warning = models.BooleanField(default=False)
    Task3_warning = models.BooleanField(default=False)
    Task4_warning = models.BooleanField(default=False)
    Task5_warning = models.BooleanField(default=False)
    Task6_warning = models.BooleanField(default=False)
    Task7_warning = models.BooleanField(default=False)
    Task8_warning = models.BooleanField(default=False)
    Task9_warning = models.BooleanField(default=False)
    Task10_warning = models.BooleanField(default=False)
    Task11_warning = models.BooleanField(default=False)
    Task12_warning = models.BooleanField(default=False)
    Task13_warning = models.BooleanField(default=False)
    Task14_warning = models.BooleanField(default=False)
    Task15_warning = models.BooleanField(default=False)
    Task16_warning = models.BooleanField(default=False)
    Task17_warning = models.BooleanField(default=False)
    Task18_warning = models.BooleanField(default=False)
    Task19_warning = models.BooleanField(default=False)
    Task20_warning = models.BooleanField(default=False)
    Task1_alert = models.BooleanField(default=False)
    Task2_alert = models.BooleanField(default=False)
    Task3_alert = models.BooleanField(default=False)
    Task4_alert = models.BooleanField(default=False)
    Task5_alert = models.BooleanField(default=False)
    Task6_alert = models.BooleanField(default=False)
    Task7_alert = models.BooleanField(default=False)
    Task8_alert = models.BooleanField(default=False)
    Task9_alert = models.BooleanField(default=False)
    Task10_alert = models.BooleanField(default=False)
    Task11_alert = models.BooleanField(default=False)
    Task12_alert = models.BooleanField(default=False)
    Task13_alert = models.BooleanField(default=False)
    Task14_alert = models.BooleanField(default=False)
    Task15_alert = models.BooleanField(default=False)
    Task16_alert = models.BooleanField(default=False)
    Task17_alert = models.BooleanField(default=False)
    Task18_alert = models.BooleanField(default=False)
    Task19_alert = models.BooleanField(default=False)
    Task20_alert = models.BooleanField(default=False)
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')


class Task1Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task2Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task3Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task4Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task5Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task6Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task7Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task8Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task9Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task10Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task11Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task12Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task13Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task14Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task15Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task16Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task17Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task18Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task19Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)


class Task20Statusparts(models.Model):
    post = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    Parts = models.ForeignKey(parts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

########################################################################################################################

class Device(models.Model):
    HE = 'HE'
    HA = 'HA'
    MOBILE = 'MOBILE'
    Device_Choice = (
        (HE, 'HE'),
        (HA, 'HA'),
        (MOBILE, 'Mobile'),
    )

    Device_Category = models.CharField(max_length=10, choices=Device_Choice, default='')
    Name = models.CharField(max_length=100, default = '')
    LaunchDate = models.DateField()
    ProductReadiness = models.OneToOneField(ProductReadiness,blank=True, on_delete=models.CASCADE, default='')
    VideoContent = models.OneToOneField(videocontent,blank=True, on_delete=models.CASCADE, default='')
    DigitalContent = models.OneToOneField(digitalcontent, blank=True,on_delete=models.CASCADE, default='')
    CallCenterTraining = models.OneToOneField(callcentertraining,blank=True, on_delete=models.CASCADE, default='')
    CallCenterOpertaions = models.OneToOneField(callcenteropertaions,blank=True, on_delete=models.CASCADE, default='')
    ProductSupport = models.OneToOneField(productsupport,blank=True, on_delete=models.CASCADE, default='')
    Warehouse = models.OneToOneField(warehouse,blank=True, on_delete=models.CASCADE, default='')
    FieldService = models.OneToOneField(fieldservice,blank=True, on_delete=models.CASCADE, default='')
    TechSupport = models.OneToOneField(techsupport,blank=True, on_delete=models.CASCADE, default='')
    ServiceMarketing = models.OneToOneField(servicemarketing,blank=True, on_delete=models.CASCADE, default='')
    ServiceTraining = models.OneToOneField(servicetraining,blank=True, on_delete=models.CASCADE, default='')
    Parts = models.OneToOneField(parts, blank=True,on_delete=models.CASCADE, default='')
    completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    ProductDescription = models.CharField(max_length=100, default = '')
    On_Time = 'On Time'
    At_Risk = 'At Risk'
    Delayed = 'Delayed'
    Status_Choice = (
        (On_Time, 'On Time'),
        (At_Risk, 'At Risk'),
        (Delayed, 'Delayed'),
    )

    Status = models.CharField(max_length=10, choices=Status_Choice, default='On_Time')
    Archive = models.BooleanField(default=False)

    def __str__(self):
        return self.Name

class DeviceHistory(models.Model):
    Completed = IntegerRangeField(min_value=0, max_value=100, default=0)
    Created = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

class ProductReadinessHistory(models.Model):
    Delayed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Completed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    DueSoon = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    OnTime = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Created = models.DateTimeField(auto_now_add=True)
    Device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

class VideoContentHistory(models.Model):
    Delayed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Completed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    DueSoon = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    OnTime = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Created = models.DateTimeField(auto_now_add=True)
    Device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

class DigitalContentHistory(models.Model):
    Delayed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Completed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    DueSoon = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    OnTime = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Created = models.DateTimeField(auto_now_add=True)
    Device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

class CallCenterTrainingHistory(models.Model):
    Delayed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Completed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    DueSoon = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    OnTime = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Created = models.DateTimeField(auto_now_add=True)
    Device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

class CallCenterOperationsHistory(models.Model):
    Delayed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Completed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    DueSoon = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    OnTime = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Created = models.DateTimeField(auto_now_add=True)
    Device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

class ProductSupportHistory(models.Model):
    Delayed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Completed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    DueSoon = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    OnTime = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Created = models.DateTimeField(auto_now_add=True)
    Device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

class WarehouseHistory(models.Model):
    Delayed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Completed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    DueSoon = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    OnTime = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Created = models.DateTimeField(auto_now_add=True)
    Device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

class FieldServiceHistory(models.Model):
    Delayed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Completed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    DueSoon = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    OnTime = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Created = models.DateTimeField(auto_now_add=True)
    Device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

class TechSupportHistory(models.Model):
    Delayed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Completed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    DueSoon = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    OnTime = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Created = models.DateTimeField(auto_now_add=True)
    Device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

class ServiceMarketingHistory(models.Model):
    Delayed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Completed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    DueSoon = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    OnTime = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Created = models.DateTimeField(auto_now_add=True)
    Device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

class ServiceTrainingHistory(models.Model):
    Delayed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Completed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    DueSoon = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    OnTime = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Created = models.DateTimeField(auto_now_add=True)
    Device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

class PartsHistory(models.Model):
    Delayed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Completed = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    DueSoon = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    OnTime = models.DecimalField(max_digits=5,decimal_places=2, default = 0)
    Created = models.DateTimeField(auto_now_add=True)
    Device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)

class DashboardControlDevice(models.Model):
    Device = models.OneToOneField(Device,blank=True, on_delete=models.CASCADE, default='')


class Announcements(models.Model):
    post = models.TextField(blank=True,default='')
    information = 'information'
    warning = 'warning'
    alert = 'alert'
    Status_Choice = (
        (information, 'information'),
        (warning, 'warning'),
        (alert, 'alert'),
    )

    Severity = models.CharField(max_length=20, choices=Status_Choice, default='information')

class reference(models.Model):
    Launch_Date = models.DateField(blank=True, null=True)

def get_default_my_date():
  try:
      ref = reference.objects.count()
      date = ref.Launch_Date
      print (ref)
  except:
      date = None
      print ("None")
  return date

class test(models.Model):
    Date = models.DateField(blank=True, null=True, default=get_default_my_date)