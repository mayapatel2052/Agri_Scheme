from django.db import models

class user(models.Model):
    Id = models.AutoField(primary_key=True)
    Mobile_number = models.CharField(max_length=10,unique=True)
    Name = models.CharField(max_length=100)
    User_type = models.CharField(max_length=20)
    Valid_user_or_not = models.BooleanField()
    Servay_num = models.CharField(max_length=10)
    Password = models.CharField(max_length=12)
    District = models.CharField(max_length=30)
    Taluka = models.CharField(max_length=30)
    Village = models.CharField(max_length=30)
    Land_area = models.CharField(max_length=20)

class schemes(models.Model):
    Schemes_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Eligibility = models.CharField(max_length=1000)
    For_district = models.CharField(max_length=30)
    For_taluka = models.CharField(max_length=30)
    Starting_date = models.DateField(max_length=20)
    Ending_date = models.DateField(max_length=20)
    Schemes_desc = models.CharField(max_length=2000)

class Applied_Schemes(models.Model):
    Id = models.AutoField(primary_key=True)
    Schemes_status = models.CharField(max_length=100)
    Farmer_Adhar_Card = models.CharField(max_length=16)
    Farmer_Bank_Name = models.CharField(max_length=50)
    Farmer_Bank_IFSC = models.CharField(max_length=11)
    Farmer_Account_num = models.CharField(max_length=20)
    Sch = models.ForeignKey(schemes, on_delete=models.CASCADE)
    Usr = models.ForeignKey(user, on_delete=models.CASCADE)