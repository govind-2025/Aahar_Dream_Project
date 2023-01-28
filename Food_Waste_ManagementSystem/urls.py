from django.contrib import admin
from django.urls import path
from foodwaste.views import *
# import view from folder foodwaste all function(*)
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    # inside path 1st-> url 8000/about/ , 2nd->about(function name in view.py) 3rd-->
    path('food_Available', food_Available, name='food_Available'),
    path('checkFoodAvailable/<int:pid>', checkFoodAvailable, name='checkFoodAvailable'),
    path('contact/', contact, name='contact'),
    path('donor_login',donor_login, name='donor_login'),
    path('signup', signup, name='signup'),
    path('admin_login', admin_login, name='admin_login'),

    path('dashboard', dashboard, name='dashboard'),
    path('addState', addState, name='addState'),
    path('manageState', manageState, name='manageState'),
    path('editState<int:pid>', editState, name='editState'),
    path('deleteState<int:pid>', deleteState, name='deleteState'),
    path('addCity', addCity, name='addCity'),
    path('manageCity', manageCity, name='manageCity'),
    path('editCity<int:pid>', editCity, name='editCity'),
    path('deleteCity<int:pid>', deleteCity, name='deleteCity'),
    path('regFoodDonor', regFoodDonor, name='regFoodDonor'),
    path('deleteDonor<int:pid>', deleteDonor, name='deleteDonor'),
    path('listedFood', listedFood, name='listedFood'),
    path('foodDetails<int:pid>', foodDetails, name='foodDetails'),
    path('newRequest', newRequest, name='newRequest'),
    path('completeRequest', completeRequest, name='completeRequest'),
    path('rejectRequest', rejectRequest, name='rejectRequest'),
    path('allRequest', allRequest, name='allRequest'),
    path('view_requestDtls<int:pid>', view_requestDtls, name='view_requestDtls'),
    path('unreadEnquiry', unreadEnquiry, name='unreadEnquiry'),
    path('readEnquiry', readEnquiry, name='readEnquiry'),
    path('viewEnquiry<int:pid>', viewEnquiry, name='viewEnquiry'),
    path('reportDonatedFood', reportDonatedFood, name='reportDonatedFood'),
    path('reportregfoodDonor', reportregfoodDonor, name='reportregfoodDonor'),
    path('searchFood', searchFood, name='searchFood'),
    path('changePassword', changePassword, name='changePassword'),
    path('logout/', Logout, name='logout'),

    path('donorDashboard', donorDashboard, name='donorDashboard'),
    path('addFood', addFood, name='addFood'),
    path('manageFood', manageFood, name='manageFood'),
    path('editFood<int:pid>', editFood, name='editFood'),
    path('deleteFood<int:pid>', deleteFood, name='deleteFood'),
    path('load_city',load_city, name="ajax_load_city"),
    path('donorNewRequest', donorNewRequest, name='donorNewRequest'),
    path('donorCompletedRequest', donorCompletedRequest, name='donorCompletedRequest'),
    path('donorRejectRequest', donorRejectRequest, name='donorRejectRequest'),
    path('donorAllRequest', donorAllRequest, name='donorAllRequest'),
    path('viewRequestDetails<int:pid>', viewRequestDetails, name='viewRequestDetails'),
    path('deleteRequest<int:pid>', deleteRequest, name='deleteRequest'),
    path('donorSearch', donorSearch, name='donorSearch'),
    path('profile', profile, name='profile'),
    path('donorChangePassword', donorChangePassword, name='donorChangePassword'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 