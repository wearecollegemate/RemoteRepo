from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import ProData,StoryData,CmtData,FeedData
from .forms import RegistrationForm,UpdationForm
import string
import random
from django.core.mail import send_mail
import datetime as dt
date1=dt.datetime.now()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def home(request):
    if request.session.get('active'):
       sdata = StoryData.objects.all()
       cdata = CmtData.objects.all()
       img = ProData.objects.filter(user='{0}'.format(request.session.get('active')))
       return render(request, 'login.html', {'img': img, 'sdata': sdata, 'cdata': cdata })

    else:
       return render(request, 'home.html')


def registration_view(request):

    try:

            form = RegistrationForm(request.POST,request.FILES or None)
            context = {
                'form': form
            }

            if form.is_valid():
                print(form.cleaned_data)

                name = form.cleaned_data.get('name')
                rollno = form.cleaned_data.get('rollno')
                regno = form.cleaned_data.get('regno')
                email = form.cleaned_data.get('email')
                college = form.cleaned_data.get('college')
                branch = form.cleaned_data.get('branch')
                user = form.cleaned_data.get('email')
                pwd = id_generator(6, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
                image = form.cleaned_data.get('image')
                date=date1
                data = ProData(
                   name=name,
                   rollno=rollno,
                   regno=regno,
                   email=email,
                   college=college,
                   branch=branch,
                   user=user,
                   pwd=pwd,
                   image=image,
                   date=date)
                data.save()
                # user1 = str(user)
                m1 = 'Welcome '
                m2 = name
                m3 = '!\nYou are one step to Sign in.\nYour Username : '
                m4 = user
                m5 = '\nPassword:'
                m6 = pwd
                m7 = '\nClick This link to open Login Page-> '
                m8 = 'http://iambrijesh95.pythonanywhere.com/'
                message = m1+m2+m3+m4+m5+m6+m7+m8
                send_mail('Welcome Message!', message, 'wearecollegemate@gmail.com', [user])
                s="Registration is Successful!! Please Check Your Email!!"
                return render(request,'home.html',{'s': s})
            i = "Please Fill All Fields!!"
            return render(request, 'reg.html',{'form':form, 'i': i})

    except:
               i = "Please Fill Correct Fields!!"
               form = RegistrationForm()
               return render(request, 'reg.html', {'form': form,'i': i})


def login_view(request):
    if request.method == "POST":
        uname = request.POST.get('user')
        password = request.POST.get('pwd')

        uname1 = ProData.objects.filter(user=uname)
        pwd = ProData.objects.filter(pwd=password)
        if uname1 and pwd:
            request.session.set_test_cookie()
            request.session['active'] = uname
            img = ProData.objects.filter(user=uname)
            sdata = StoryData.objects.all()
            cdata = CmtData.objects.all()
            return render(request, 'login.html', {'img': img,'cdata': cdata, 'sdata': sdata})
        else:
            x = "Invalid User Data!"
            return render(request, 'home.html', {'x': x})
    elif request.session.get('active'):
        user = request.session.get('active')
        img = ProData.objects.filter(user=user)
        sdata = StoryData.objects.all()
        cdata = CmtData.objects.all()
        return render(request, 'login.html', {'img': img, 'cdata': cdata, 'sdata': sdata})
    else:
        return render(request, 'home.html')




def family(request):
    if request.session.get('active'):
        alldata = ProData.objects.all()
        return render(request,'family.html',{'alldata':alldata})
    else:
        return render(request, 'home.html')


def member(request):
    if request.session.get('active'):
        alldata=ProData.objects.all()
        return render(request, 'member.html', {'alldata': alldata})
    else:
        return render(request, 'home.html')


def success_view(request):
    if request.session.get('active'):
        sdata = StoryData.objects.all()
        cdata = CmtData.objects.all()
        img=ProData.objects.filter(user='{0}'.format(request.session.get('active')))
        return render(request, 'login.html',{'img': img,'sdata': sdata,'cdata': cdata})
    else:
        return render(request, 'home.html')


def link(request):
    try:
       del request.session['active']
    except:
        pass
    finally:
      return render(request, 'home.html')


def storypad(request):
    if request.session.get('active'):
        if request.method == "POST":
            story = request.POST.get('story')
            upost=request.session.get('active')
            mpost=ProData.objects.filter(user=upost).values_list('name', flat=True)
            rdata = StoryData(upost=mpost[0])
            data = StoryData(date=date1, story=story, upost=rdata)
            data.save()
            img=ProData.objects.filter(user=upost)
            sdata = StoryData.objects.all()
            cdata = CmtData.objects.all()
            return render(request, 'login.html', {'sdata': sdata,'img':img,'cdata': cdata})
        else:
            sdata = StoryData.objects.all()
            cdata = CmtData.objects.all()
            img=ProData.objects.filter(user='{0}'.format(request.session.get('active')))
            return render(request, 'login.html', {'sdata': sdata, 'img': img,'cdata': cdata})
    else:
          return render(request, 'home.html')


def cmt(request):
    if request.session.get('active'):
        if request.method == "POST":
            cmt1 = request.POST.get('cmt')
            id = request.POST.get('id')
            upost = request.session.get('active')
            mpost = ProData.objects.filter(user=upost).values_list('name', flat=True)
            rdata =mpost[0]
            data = CmtData(storydata_id=id,cmt=cmt1, cpost=rdata, cdate=date1)
            data.save()
            img=ProData.objects.filter(user=upost)
            sdata = StoryData.objects.all()
            cdata = CmtData.objects.all()
            sdata1 = StoryData.objects.filter(id=id).values_list('id', flat=True)
            sdata2 = sdata1[0]
            cdata1 = CmtData.objects.filter(storydata_id=id).values_list('storydata_id', flat=True)
            cdata2 = cdata1[0]

            return render(request, 'login.html', {'sdata': sdata,'img':img,'cdata': cdata, 'sdata2': sdata2, 'cdata2': cdata2})
        else:
            sdata = StoryData.objects.all()
            cdata = CmtData.objects.all()
            img = ProData.objects.filter(user="{0}".format(request.session.get('active')))
            return render(request, 'login.html', {'sdata': sdata, 'cdata': cdata, 'img': img})
    else:
          return render(request, 'home.html')


def feedback(request):
    if request.session.get('active'):
        if request.method == "POST":
            feed = request.POST.get('feed')
            upost=request.session.get('active')
            mpost=ProData.objects.filter(user=upost).values_list('name', flat=True)
            rdata = mpost[0]
            data = FeedData(fdate=date1, feed=feed, fpost=rdata)
            data.save()
            fdata = FeedData.objects.all()
            return render(request, 'feedback.html', {'fdata': fdata})
        else:
            fdata = FeedData.objects.all()
            return render(request, 'feedback.html', {'fdata':fdata})
    else:
          return render(request, 'home.html')


def reset(request):
    try:
        if request.method=="POST":
            user=request.POST.get('user')
            opwd=request.POST.get('pwd')
            npwd=request.POST.get('npwd')
            npwd2=request.POST.get('npwd2')
            uname=ProData.objects.filter(user=user)
            pwd=ProData.objects.filter(pwd=opwd)
            if uname and pwd:
                if npwd==npwd2:
                    pwd.update(pwd=npwd)
                    c="Your Password Reset Is Successful!!"
                    return render(request,'home.html',{'c': c})
                else:
                    d="New Password Should Match!!"
                    return render(request,'home.html',{'d': d})
            else:
                e="Invalid User Data!!"
                return render(request,'home.html',{'e': e })
        return render(request,'home.html')
    except:
        f="Enter Valid Details!!"
        return render(request,'home.html',{'f': f })


def update(request):
        if request.session.get('active'):
            try:
                uform = UpdationForm(request.POST, request.FILES or None)
                context = {
                    'uform': uform
                }
                if uform.is_valid():
                    print(uform.cleaned_data)
                    image = uform.cleaned_data.get('image')
                    upost = request.session.get('active')
                    mpost1 = ProData.objects.filter(user=upost).values_list('name', flat=True)
                    name = mpost1[0]
                    mpost2 = ProData.objects.filter(user=upost).values_list('rollno', flat=True)
                    rollno = mpost2[0]
                    mpost3 = ProData.objects.filter(user=upost).values_list('regno', flat=True)
                    regno = mpost3[0]
                    mpost4 = ProData.objects.filter(user=upost).values_list('email', flat=True)
                    email = mpost4[0]
                    mpost5 = ProData.objects.filter(user=upost).values_list('college', flat=True)
                    college = mpost5[0]
                    mpost6 = ProData.objects.filter(user=upost).values_list('branch', flat=True)
                    branch = mpost6[0]
                    mpost7 = ProData.objects.filter(user=upost).values_list('user', flat=True)
                    user = mpost7[0]
                    mpost8 = ProData.objects.filter(user=upost).values_list('pwd', flat=True)
                    pwd = mpost8[0]
                    mpost9 = ProData.objects.filter(user=upost).values_list('date', flat=True)
                    date = mpost9[0]


                    data = ProData(
                        name=name,
                        rollno=rollno,
                        regno=regno,
                        email=email,
                        college=college,
                        branch=branch,
                        user=user,
                        pwd=pwd,
                        image=image,
                        date=date)
                    data.save()
                    img = ProData.objects.filter(user=upost)
                    sdata = StoryData.objects.all()
                    cdata = CmtData.objects.all()
                    return render(request, 'login.html', {'img': img, 'cdata': cdata, 'sdata': sdata})
                return render(request, 'update.html', context)

            except:
                i = "Please Fill All Fields!!"
                uform = UpdationForm()
                return render(request, 'update.html', {'uform': uform, 'i': i})
        else:
            return render(request, 'home.html')


def forget(request):
    try:
        if request.method=="POST":
            user=request.POST.get('user')
            rollno=request.POST.get('rollno')
            mpost1 = ProData.objects.filter(user=user).values_list('name', flat=True)
            name = mpost1[0]
            mpost8 = ProData.objects.filter(user=user).values_list('pwd', flat=True)
            pwd = mpost8[0]
            mpost2 = ProData.objects.filter(user=user).values_list('rollno', flat=True)
            roll2 = mpost2[0]
            mpost7 = ProData.objects.filter(user=user).values_list('email', flat=True)
            email = mpost7[0]
            roll2==rollno
            m1 = 'Welcome '
            m2 = name
            m3 = '!\nYou are one step to Sign in.\nYour Username : '
            m4 = user
            m5 = '\nPassword:'
            m6 = pwd
            m7 = '\nClick This link to open Login Page-> '
            m8 = 'http://iambrijesh95.pythonanywhere.com/'
            message = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8
            send_mail('Account Recovery!',message,'wearecollegemate@gmail.com',[email])
            s = "Registration is Successful!! Please Check Your Email!!"
            return render(request, 'home.html', {'s': s})
        return render(request, 'home.html')
    except:
        h="Invalid Data Entered!!"
        return render(request,'home.html',{'h': h})



