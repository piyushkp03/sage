from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import bhyhospital,vasaihospital,vaccinename,vmain,noti
from django.db.models.functions import Lower
from math import radians,sin,cos,asin,sqrt
from geopy import distance
from . import getlocation
from datetime import datetime, timedelta
import datetime as dt
import time
import smtplib
from .thread import emailthread

context={}
vac=[]

slot1=[]
slot2=[]
for c in range(9,17):
    slot2.append([str(c)+":0 - "+str(c)+":15",str(c)+":15 - "+str(c)+":30",str(c) + ":30 - " + str(c) + ":45",str(c)+":45 - "+str(c+1)+":0"])



    if(c/10==0):
        if((c+1)/10==0):
            slot1.append("0"+str(c)+" - "+"0"+str(c+1)+"hrs")
        else:
            slot1.append("0" + str(c) + " - " + str(c + 1) +"hrs")
    else:
        slot1.append( str(c) + " - " + str(c + 1) +"hrs")






def home(request):
    print("The slot is:",slot1,slot2)

    return render(request, 'index.html',{'slot1':slot1,'slot2':slot2})

def urapp(request):
    m=list(noti.objects.filter(email=request.user.email))
    l=len(m)
    print(type(l),l)
    return render(request, 'urapp.html',{'book':m,'leng':l})

def aboutus(request):
    # l='hi'
    return render(request,'aboutus.html')

def sortbyprice(request):

    vac=vmain.objects.all().order_by('vprice')
    return render(request, 'vmain.html',{'list':vac,'context':context})

def vaccinemain(request):
    # city = request.POST.get('citysystem',None)
    vaccine = request.POST.get('system', None)
    city = request.POST.get('cityname',None)
    
    context['vaccine'] = vaccine
    context['city'] = city
    # print(city,vaccine)
    # city=request.POST['bhy']
    # vaccine=request.POST['system']
    vac=vmain.objects.all()
    print(context['vaccine'],context['city'])
    return render(request, 'vmain.html',{'list':vac,'context':context})


def vaccinelist(request):
    city = request.POST.get('citysystem',None)
    vac=vaccinename.objects.all()

    return render(request,'vaccinename.html',{'vac':vac,'city':city})

    
def signupuser(request):

    # messages.error(request,"checking error")

    if(request.method=='POST'):
        uname=request.POST['uname']
        email=request.POST['email']
        passw=request.POST['pass']
        cnfpass=request.POST["cnfpass"]
        print(uname,email,passw,cnfpass)
        print(type(passw))
        print(passw==cnfpass)
        if not uname.isalnum():
            messages.error(request,"Username must only contain no and letters")
            return redirect('home')

        if (passw != cnfpass):
            messages.error(request,"Passwords should match")
            return redirect('home')

        if(passw==cnfpass):

            myuser=User.objects.create_user(uname, email, passw)
            myuser.save()
            messages.success(request, "User registered successfully")
            return redirect('home')

    else:
        return HttpResponse('404..Not Found')



    return render(request,'index.html')

def loginuser(request):
    uname = request.POST['uname']
    passw = request.POST['passw']
    l=User.objects.all()
    print(l)
    for u in l:
        print(u)
    usr=authenticate( username=uname, password=passw)
    print(usr)
    if usr is not None:
        login(request, usr)
        messages.success(request, "Logged in successfully")
        return redirect("home")
    else:
        messages.error(request, "Invalid credentials")
        return redirect('home')


def loginuser1(request):
    uname = request.POST['uname']
    passw = request.POST['passw']
    l=User.objects.all()
    print("The request loginuser1",request)
    for u in l:
        print(u)
    usr=authenticate( username=uname, password=passw)
    print(usr)
    if usr is not None:
        login(request, usr)
        messages.success(request, "Logged in successfully")
        return redirect("hospitalpage1")
    else:
        messages.error(request, "Invalid credentials")
        return redirect('hospitalpage1')







def logoutuser(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect('home')


    
def bhyhosp(request):
    h2=bhyhospital.objects.all()
    # request.session['city']='vasai'
    for hosp in h2:
        print(hosp.hlink)
        hos='bhy'


    return render(request, 'area.html',{'hdetail':h2,'hosp':hos})

# def bhyhosp(request):
#     n=bhyhospital.objects.all()
#     hos='bhy'
#     # request.session['city'] = 'bhayandar'

#     #ref=bhyhospital(hdis=dis)

    lat1, lon1= '0','0'  #getuserlocation



    i=1
    for hosp in n:
        lat2, lon2= map(float,hosp.hcordinate.split(","))
        loc1 = (lat1, lon1)
        loc2 = (lat2, lon2)
        print(loc1,loc2)
        dis=distance.distance(loc1, loc2).km
        bhy=bhyhospital.objects.get(pk=i)
        bhy.hdis=dis
        bhy.save()
        i+=1

    h1=bhyhospital.objects.all()
    




    return render(request,'area.html',{'hdetail':h1,'hosp':hos})

def sortbynamebhy(request):
    print("The request is:",request)


    m = bhyhospital.objects.all().order_by(Lower('hname'))
    print("sorted by name",m)
    return render(request, 'area.html', {'hdetail': m})
def sortbynamevasai(request):


    m = vasaihospital.objects.all().order_by(Lower('hname'))
    print("sorted by name",m)
    return render(request, 'area.html', {'hdetail': m})

def sortbydisbhy(request):
    n = bhyhospital.objects.all()
    # ref=bhyhospital(hdis=dis)

    lat1,lon1 = getlocation.getloc()



    i = 1
    for hosp in n:
        lat2, lon2 = map(float, hosp.hcordinate.split(","))
        loc1 = (lat1, lon1)
        loc2 = (lat2, lon2)
        dis = distance.distance(loc1, loc2).km
        bhy = bhyhospital.objects.get(pk=i)
        bhy.hdis = dis
        print(bhy.hdis,type(bhy.hdis))
        bhy.save()
        i += 1
    m = bhyhospital.objects.all().order_by(('hdis'))
    print("sortedby dis",m)
    return render(request, 'area.html', {'hdetail': m})





def sortbynamevasai(request):

    m = vasaihospital.objects.all().order_by(Lower('hname'))
    print("sorted by name",m)
    return render(request, 'area.html', {'hdetail': m})

def sortbydisvasai(request):
    n = vasaihospital.objects.all()
    # ref=bhyhospital(hdis=dis)

    lat1 = 28.6129186
    lon1 = 77.2294273


    i = 1
    for hosp in n:
        lat2, lon2 = map(float, hosp.hcordinate.split(","))
        loc1 = (lat1, lon1)
        loc2 = (lat2, lon2)
        dis = distance.distance(loc1, loc2).km
        bhy = vasaihospital.objects.get(pk=i)
        bhy.hdis = dis
        print(bhy.hdis,type(bhy.hdis))
        bhy.save()
        i += 1
    m = vasaihospital.objects.all().order_by(('hdis'))
    print("sortedby dis",m)
    return render(request, 'area.html', {'hdetail': m})





def vasaihosp(request):
    h2=vasaihospital.objects.all()
    request.session['city']='vasai'
    for hosp in h2:
        print(hosp.hlink)
        hos='vasi'


    return render(request, 'area.html',{'hdetail':h2,'hosp':hos})

def appoint(request):
   
    if(not request.user.is_authenticated):
        print("Not authenticated")
        messages.error(request,"Please login to book appointment")
        return redirect('home')

    nov2=request.POST['nov2']
    if(float(nov2)>0):
        vname=request.POST['vname']
        date=request.POST.get('cars',None)
        # print(date)
        final=request.POST.get('final',None)
        hname=request.POST['hname']
        city=request.POST['city']
        # nov2=request.POST['nov2',None] 
        presentday = datetime.now()
        tomorrow = presentday + timedelta(1)
        tomorrow2 = tomorrow + timedelta(1)
        tomorrow=tomorrow.strftime('%d-%m-%Y')
        tomorrow2=tomorrow2.strftime('%d-%m-%Y')
        # context={}
        # context['vname']=vname
        # context['hname']=hname
        # context['nov2']=nov2
        # context['tomorrow']=tomorrow
        # context['tomorrow2']=tomorrow2
        l3=[]
        va=request.POST['hidd']
        slotzip=zip(slot1,slot2)
        t1,t2=va.split("-")
        hr1,m1=map(int,t1.split(":"))
        hr2,m2=map(int,t2.split(":"))
        while((hr1*60+m1)<(hr2*60+m2)):
            if(m1==60):
                m1=0
                hr1 += 1
            if (m1 == 45):
                l3.append(str(hr1)+":"+str(m1)+" - "+str(hr1+1)+":"+"0")


            else:
                l3.append(str(hr1) + ":" + str(m1) + " - " + str(hr1) + ":" + str(m1+15))


            m1+=15
        return render(request,'appoint.html',{'date':date,'final':final,'city':city,'vname':vname,'hname':hname,'nov2':nov2,'l3':l3,'slot2':slot2,'slots':slotzip,'tomorrow':tomorrow,'tomorrow2':tomorrow2})
    
    else:
        messages.error(request,"Vaccine Not Available")
        return redirect('home')

# def send_email(user,y,z):
#     email_user = 'teproject69@gmail.com'
#     server = smtplib.SMTP ('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(email_user, 'te123456')
#     #EMAIL
#     msg = 'sending this from python!'
#     server.sendmail(email_user, user, msg)
#     server.quit()



def success(request):
   
    user=request.user.email
    print(user)
    vname1 = request.POST.get('vname', None)
    date = request.POST.get('cars', None)
    print(date)
    final = request.POST.get('final', None)
    # nov2=request.POST.get('nov2', None)
    # city = request.POST.get('city',None)
    hname1 = request.POST.get('hname',None)
    # notii=noti.objects.all()
    a = noti(email = user, date = date, time = final,hname = hname1, vname = vname1)
    a.save()
    y=date.split("-")
    z=final.split(":")
    print(y,z)
   
    #send_time = dt.datetime(2021,5,13,10,30,0)
    send_time = dt.datetime(int(y[2]),int(y[1]),int(y[0]),int(z[0])-1,0,0) # set your sending time in UTC


    #time.sleep(send_time.timestamp() - time.time())
    obj=emailthread(send_time.timestamp(), time.time(),user,date,final,hname1,vname1)
    obj.start()
    print('email sent')
    sx=vmain.objects.get(hname=hname1,vname=vname1)
    print(sx.nov)
    sx.nov=sx.nov-1
    sx.save()
    messages.success(request,"Book Successfully")
    # return render(request,'index.html',{'user':user,'date':date,'final':final,'city':city,'vname':vname,'hname':hname,'nov2':nov2})
    return redirect('home')




