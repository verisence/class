from django.db import models

# Create your models here.
class Stude(models.Model):
    CLASS_CHOICES = [
        ('2019MPFT-Aug5-Sep6','2019MPFT-Aug5-Sep6'),
    ]
    PARTICIPATE_CHOICES = [
        ('Yes','Yes'),
        ('No','NO'),
        ('Maybe','Maybe')
    ]
    CORE_CHOICES = [
        ('Yes','Yes'),
        ('No','NO'),
        ('Maybe','Maybe')
    ]
    INFLUENCE_CHOICES = [
        ('Facebook','Facebook'),
        ('Twitter','Twitter'),
        ('Alumni','Alumni'),
        ('Event','Event'),
        ('Instagram','Instagram'),
        ('Moringa-Website','Moringa-Website'),
        ('Referall','Referall'),
        ('Google','Google'),
        ('Nairobi-Tech-Week','Nairobi-Tech-Week'),
        ('Other','Other')
    ]
    HEAR_CHOICES = [
        ('Facebook','Facebook'),
        ('Twitter','Twitter'),
        ('Alumni','Alumni'),
        ('Event','Event'),
        ('Instagram','Instagram'),
        ('Moringa-Website','Moringa-Website'),
        ('Referall','Referall'),
        ('Google','Google'),
        ('Nairobi-Tech-Week','Nairobi-Tech-Week'),
        ('Other','Other')
    ]
    EDUCATION_CHOICES = [
        ('High-School','High-School'),
        ('Diploma','Diploma'),
        ('Bachelor-Degree','Bachelor-Degree'),
        ('Masters','Masters'),
        ('Doctorate','Doctorate'),
        ('Other','Other')

    ]
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
        ('Prefer not to say','Prefer not to say')
    ]
    PAY_CHOICES = [
        ('Yes','Yes'),
        ('No','No')
    ]
    first_name = models.CharField(max_length =40)
    last_name = models.CharField(max_length =40)
    email = models.CharField(max_length =100)
    class_name = models.CharField(max_length =100,choices=CLASS_CHOICES)
    phone_Number =   models.IntegerField(default=0, null=True)
    Gender = models.CharField(max_length =100,choices=GENDER_CHOICES, null=True)
    Have_you_participated_in_a_Moringa_School_training_before = models.CharField(max_length =100,choices=PARTICIPATE_CHOICES, null=True)
    Are_you_interested_in_joining_Moringa_Core_after_Moringa_Prep =models.CharField(max_length =100,choices=CORE_CHOICES, null=True)
    Where_did_you_hear_about_Moringa_School = models.CharField(max_length =100,choices=HEAR_CHOICES, null=True)
    Whcih_avenue_was_most_influential_in_joining_Moringa_School =models.CharField(max_length =100,choices=INFLUENCE_CHOICES, null=True)
    Do_you_understand_that_you_need_to_pay_the_full_amount= models.CharField(max_length =100,choices=PAY_CHOICES, null=True)
    What_is_your_highest_level_of_education_completed =models.CharField(max_length =100,choices=EDUCATION_CHOICES, null=True)
    article_link = models.CharField(max_length =100)

    def __str__(self):
        name = self.first_name     
        return name
