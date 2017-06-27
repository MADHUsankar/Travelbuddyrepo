# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from ..app_reglogin.models import User
from .models import Tripschedule
from django.core.urlresolvers import reverse

# Create your views here.
def homepage(request):
    #Tripschedule.objects.all().delete()
    context = {
                    'Tripscheduledata' :  Tripschedule.objects.all(),
                    "name": request.session['name'],             
                    "userid" :  request.session['userid'] 
                }
   
    return render(request,'app_travel/homepage.html', context)


def addtravelplan(request):

    if request.method == "POST":
        print request.POST
        context = {
                "name": request.session['name'],
                "userid" :  request.session['userid'] 
                }
      
        result = Tripschedule.objects.addtravelplan(request.POST,context)
        print  result['status']
        if not result['status']:
             
            for error in result['errors']:
                messages.error(request,error)
                print "here"
            return redirect(reverse('travels:add_travelplan'))
        else: 
            messages.success(request,"Successful")
            return redirect(reverse('travels:home_page'))
            
    else:
            print "ENTERED GET"
            context = {
                    'Tripscheduledata' :  Tripschedule.objects.all(),
                    "name": request.session['name']    
             }
    return render(request,'app_travel/addtravelplan.html',context )


def destination(request,id):
 
    context = {
        "name": request.session['name'],
        'trip' :Tripschedule.objects.get(id=id)
        }
     
        #return redirect(reverse('show',kwargs={'id':id}))
    return render(request,'app_travel/destination.html', context)



def addlike(request,id):    
    context = {
                "tripid" :id,
                "userid" :  request.session['userid'] ,
                "name": request.session['name']
                }
    result = Tripschedule.objects.addlike(context)
    if not result['status']:
            for error in result['errors']:
                messages.error(request,error)
                print "here"
            #return redirect(reverse('secrets:add_like',kwargs={'id': id}))
            return redirect(reverse('travels:home_page'))
    else: 
            messages.success(request,"Successful")
            return redirect(reverse('travels:home_page'))


def logout(request):
    request.session.clear()
    return redirect('users:my_index')
