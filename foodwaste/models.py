from django.db import models
from django.contrib.auth.models import User

class State(models.Model):
    StateName = models.CharField(max_length=100, null=True)
    RegDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.StateName

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    CityName = models.CharField(max_length=100, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.CityName

class Contact(models.Model):
    fullName = models.CharField(max_length=150, null=True)
    Email = models.CharField(max_length=100, null=True)
    Phone = models.CharField(max_length=15, null=True)
    Message = models.CharField(max_length=250, null=True)
    EnquiryDate = models.DateTimeField(auto_now_add=True)
    IsRead = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.fullName

class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    MobileNumber = models.CharField(max_length=100, null=True)
    RegDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

class Food(models.Model):
    donorid = models.ForeignKey(Donor, on_delete=models.CASCADE, null=True)
    foodId = models.CharField(max_length=150, null=True)
    FoodItems = models.CharField(max_length=250, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    Description = models.CharField(max_length=300, null=True)
    PickupDate = models.DateField(null=True)
    PickupAddress = models.CharField(max_length=250, null=True)
    ContactPerson = models.CharField(max_length=150, null=True)
    CPMobNumber = models.CharField(max_length=15, null=True)
    Image = models.FileField(null=True,blank=True)
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateField(null=True)

    def __str__(self):
        return self.foodId

class Foodrequests(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    requestNumber = models.CharField(max_length=150, null=True)
    fullName = models.CharField(max_length=250, null=True)
    mobileNumber = models.CharField(max_length=15, null=True)
    message = models.CharField(max_length=350, null=True)
    requestDate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, null=True) #tobc
    donorRemark = models.CharField(max_length=250, null=True)
    requestCompletionDate = models.DateField(null=True)

    def __str__(self):
        return self.fullName
