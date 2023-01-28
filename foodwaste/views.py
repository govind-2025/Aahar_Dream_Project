import random

from django.contrib.auth import authenticate, logout, login
from django.db.models import Q
from django.shortcuts import render, redirect
# render is used for render url to html page so we import
from datetime import date
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
 
def food_Available(request):
    food = Food.objects.all()
    return render(request, 'food_Available.html', locals())
    # locals will collect all variables that you created inside function.

def checkFoodAvailable(request,pid):
    food = Food.objects.get(id=pid)
    foodid = food.id

    if request.method == "POST":
        fullName = request.POST['fullName']
        mobileNumber = request.POST['mobileNumber']
        message = request.POST['message']
        requestNumber = str(random.randint(10000000, 99999999))
        try:
            Foodrequests.objects.create(food=food, fullName=fullName, mobileNumber=mobileNumber, message=message,
                                   requestNumber=requestNumber)
            error = "no"
        except:
            error = "yes"
    return render(request, 'checkFoodAvailable.html', locals())

def contact(request):
    error = ""
    if request.method == "POST":
        fullName = request.POST['fullName']
        Email = request.POST['Email']
        Phone = request.POST['Phone']
        Message = request.POST['Message']

        try:
            Contact.objects.create(fullName=fullName, Email=Email, Phone=Phone, Message=Message)
            error = "no"
        except:
            error = "yes"
    return render(request, 'contact.html', locals())

def donor_login(request):
    error = ""
    if request.method == 'POST':
        e = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=e, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'donor_login.html', locals())

def signup(request):
    error = ""
    if request.method == "POST":
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        MobileNumber = request.POST['MobileNumber']
        email = request.POST['Email']
        password = request.POST['Password']

        try:
            user = User.objects.create_user(username=email, password=password, first_name=fname, last_name=lname)
            Donor.objects.create(user=user, MobileNumber=MobileNumber)
            error = "no"
        except:
            error = "yes"
    return render(request, 'signup.html', locals())

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    totalstate = State.objects.all().count()
    totalcity = City.objects.all().count()
    totaldonor = Donor.objects.all().count()
    totalfood = Food.objects.all().count()
    totalrequest = Foodrequests.objects.all().count()
    totalnewrequest = Foodrequests.objects.filter(status=None).count()
    totalrejectrequest = Foodrequests.objects.filter(status='Request Rejected').count()
    totalcompleterequest = Foodrequests.objects.filter(status='Food Take Away/ Request Completed').count()
    return render(request, 'admin/dashboard.html', locals())

def addState(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == "POST":
        StateName = request.POST['StateName']

        try:
            State.objects.create(StateName=StateName)
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/addState.html', locals())

def manageState(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    state = State.objects.all()
    return render(request, 'admin/manageState.html', locals())

def editState(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    state = State.objects.get(id=pid)
    if request.method == "POST":
        StateName = request.POST['StateName']

        state.StateName = StateName
        try:
            state.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/editState.html', locals())

def deleteState(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    state = State.objects.get(id=pid)
    state.delete()
    return redirect('manageState')

def addCity(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    state = State.objects.all()
    if request.method == "POST":
        sid = request.POST['state']
        stateid = State.objects.get(id=sid)

        cityname = request.POST['CityName']

        try:
            City.objects.create(state=stateid, CityName=cityname)
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/addCity.html', locals())

def manageCity(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    city = City.objects.all()
    return render(request, 'admin/manageCity.html', locals())

def editCity(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    state = State.objects.all()
    city = City.objects.get(id=pid)
    if request.method == "POST":
        sid = request.POST['state']
        state1 = State.objects.get(id=sid)
        cityname = request.POST['CityName']

        city.state = state1
        city.CityName = cityname

        try:
            city.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/editCity.html', locals())

def deleteCity(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    city = City.objects.get(id=pid)
    city.delete()
    return redirect('manageCity')

def regFoodDonor(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donor = Donor.objects.all()
    return render(request, 'admin/regFoodDonor.html', locals())

def deleteDonor(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donor = Donor.objects.get(id=pid)
    donor.delete()
    return redirect('regFoodDonor')

def listedFood(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    food = Food.objects.all()
    return render(request, 'admin/listedFood.html', locals())

def foodDetails(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    food = Food.objects.get(id=pid)
    return render(request, 'admin/foodDetails.html', locals())

def newRequest(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    foodrequest = Foodrequests.objects.filter(status__isnull=True)
    return render(request, 'admin/newRequest.html', locals())

def completeRequest(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    foodrequest = Foodrequests.objects.filter(status='Food Take Away/ Request Completed')
    return render(request, 'admin/completeRequest.html', locals())

def rejectRequest(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    foodrequest = Foodrequests.objects.filter(status='Request Rejected')
    return render(request, 'admin/rejectRequest.html', locals())

def allRequest(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    foodrequest = Foodrequests.objects.all()
    return render(request, 'admin/allRequest.html', locals())

def view_requestDtls(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    foodrequest = Foodrequests.objects.get(id=pid)
    return render(request, 'admin/view_requestDtls.html', locals())

def unreadEnquiry(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.filter(IsRead__isnull=True)
    return render(request, 'admin/unreadEnquiry.html', locals())

def readEnquiry(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.filter(IsRead='yes')
    return render(request, 'admin/readEnquiry.html', locals())

def viewEnquiry(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = Contact.objects.get(id=pid)
    contact.IsRead = "yes"
    contact.save()
    return render(request, 'admin/viewEnquiry.html', locals())

def reportDonatedFood(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        fd = request.POST['fromDate']
        td = request.POST['toDate']
        food = Food.objects.filter(Q(CreationDate__gte=fd) & Q(CreationDate__lte=td))
        return render(request, 'admin/reportdonatedbtwdates.html', locals())
    return render(request, 'admin/reportDonatedFood.html')

def reportregfoodDonor(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        fd = request.POST['fromDate']
        td = request.POST['toDate']
        donor = Donor.objects.filter(Q(RegDate__gte=fd) & Q(RegDate__lte=td))
        return render(request, 'admin/donarbtwdates.html', locals())

    return render(request, 'admin/reportregfoodDonor.html')

def searchFood(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    sd = None
    if request.method == 'POST':
        sd = request.POST['search']
    try:
        foodrequest = Foodrequests.objects.filter(Q(requestNumber=sd) | Q(fullName=sd) | Q(mobileNumber=sd))
    except:
        foodrequest = ""
    return render(request, 'admin/searchFood.html', locals())

def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'admin/changePassword.html', locals())

def Logout(request):
    logout(request)
    return redirect('index')


# ========================  Donor Here ====================================

def donorDashboard(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    food = Food.objects.filter(donorid=donor)

    totalfoodlist = Food.objects.filter(donorid=donor).count()
    totalallreq = Foodrequests.objects.filter(food__in=food).count()
    totalnewreq = Foodrequests.objects.filter(food__in=food, status__isnull=True).count()
    totalrejectreq = Foodrequests.objects.filter(food__in=food, status='Request Rejected').count()
    totalcomreq = Foodrequests.objects.filter(food__in=food, status='Food Take Away/ Request Completed').count()

    return render(request, 'donor/donorDashboard.html', locals())

def addFood(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    state = State.objects.all()
    city = City.objects.all()

    user = User.objects.get(id=request.user.id)
    donor = Donor.objects.get(user=user)

    if request.method == "POST":
        cid = request.POST['city']
        cityid = City.objects.get(id=cid)

        foodId = str(random.randint(10000000, 99999999))
        FoodItems = request.POST['FoodItems']
        Description = request.POST['Description']
        PickupDate = request.POST['PickupDate']
        PickupAddress = request.POST['PickupAddress']
        ContactPerson = request.POST['ContactPerson']
        CPMobNumber = request.POST['CPMobNumber']
        Image = request.FILES['Image']

        try:
            Food.objects.create(donorid=donor, city=cityid, foodId=foodId, FoodItems=FoodItems, Description=Description,
                                      PickupDate=PickupDate, PickupAddress=PickupAddress, ContactPerson=ContactPerson, CPMobNumber=CPMobNumber, Image=Image)
            error = "no"
        except:
            error = "yes"
    return render(request, 'donor/addFood.html', locals())

def manageFood(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = User.objects.get(id=request.user.id)
    donor = Donor.objects.get(user=user)
    food = Food.objects.filter(donorid=donor)
    return render(request, 'donor/manageFood.html', locals())

def editFood(request,pid):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    city = City.objects.all()
    state = State.objects.all()
    food = Food.objects.get(id=pid)
    if request.method == "POST":
        cid = request.POST['city']
        cityid = City.objects.get(id=cid)

        FoodItems = request.POST['FoodItems']
        Description = request.POST['Description']
        PickupDate = request.POST['PickupDate']
        PickupAddress = request.POST['PickupAddress']
        ContactPerson = request.POST['ContactPerson']
        CPMobNumber = request.POST['CPMobNumber']

        food.city = cityid
        food.FoodItems = FoodItems
        food.Description = Description
        food.PickupDate = PickupDate
        food.PickupAddress = PickupAddress
        food.ContactPerson = ContactPerson
        food.CPMobNumber = CPMobNumber
        food.UpdationDate = date.today()

        try:
            food.save()
            error = "no"
        except:
            error = "yes"

        try:
            Image = request.FILES['Image']
            food.Image = Image
            food.save()
        except:
            pass
    return render(request, 'donor/editFood.html', locals())

def deleteFood(request,pid):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    food = Food.objects.get(id=pid)
    food.delete()
    return redirect('manageFood')


def load_city(request):
    stateid = request.GET.get('state')
    city = City.objects.filter(state=stateid).order_by('CityName')
    return render(request, 'donor/city_dropdown_list_options.html', locals())

def donorNewRequest(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)

    food = [i.id for i in Food.objects.filter(donorid=donor)]
    foodrequest = Foodrequests.objects.filter(food__in=food, status=None)
    return render(request, 'donor/donorNewRequest.html', locals())

def donorCompletedRequest(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)

    food = [i.id for i in Food.objects.filter(donorid=donor)]
    foodrequest = Foodrequests.objects.filter(food__in=food, status='Food Take Away/ Request Completed')
    return render(request, 'donor/donorCompletedRequest.html', locals())

def donorRejectRequest(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)

    food = [i.id for i in Food.objects.filter(donorid=donor)]
    foodrequest = Foodrequests.objects.filter(food__in=food, status='Request Rejected')
    return render(request, 'donor/donorRejectRequest.html', locals())

def donorAllRequest(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)

    food = [i.id for i in Food.objects.filter(donorid=donor)]
    foodrequest = Foodrequests.objects.filter(food__in=food)
    return render(request, 'donor/donorAllRequest.html', locals())

def viewRequestDetails(request,pid):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    foodrequest = Foodrequests.objects.get(id=pid)

    if request.method == "POST":
        status = request.POST['status']
        donorRemark = request.POST['donorRemark']

        try:
            foodrequest.status = status
            foodrequest.donorRemark = donorRemark
            foodrequest.requestCompletionDate = date.today()

            foodrequest.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'donor/viewRequestDetails.html', locals())

def deleteRequest(request,pid):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    foodrequest = Foodrequests.objects.get(id=pid)
    foodrequest.delete()
    return redirect('donorAllRequest')

def donorSearch(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    sd = None
    if request.method == 'POST':
        sd = request.POST['search']

        try:
            foodrequest = Foodrequests.objects.filter(Q(requestNumber=sd) | Q(fullName=sd) | Q(mobileNumber=sd))
        except:
            foodrequest = ""
    return render(request, 'donor/donorSearch.html', locals())

def profile(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = User.objects.get(id=request.user.id)
    donor = Donor.objects.get(user=user)

    if request.method == "POST":
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        mob = request.POST['MobileNumber']

        donor.user.first_name = fname
        donor.user.last_name = lname
        donor.MobileNumber = mob

        try:
            donor.save()
            donor.user.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'donor/profile.html', locals())

def donorChangePassword(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'donor/donorChangePassword.html', locals())

