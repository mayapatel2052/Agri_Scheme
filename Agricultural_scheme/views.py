from django.shortcuts import redirect, render
from model.models import *
from django.contrib.auth import authenticate,get_user_model
from django.contrib import messages


def home(request):
    return render(request,'home.html')


def login(request):
    if request.method == 'POST':
        mobile = request.POST['mobile']
        password = request.POST['password']
        a = authenticate(username=mobile,password=password)
        if a is not None:
            request.session['super'] = a.username
            request.session['supername'] = 'Admin'
            return redirect(super_admin_dashboard)
        chk = user.objects.filter(Mobile_number=mobile,Password=password).values()
        if chk.exists():
            if chk[0]['Valid_user_or_not']:
                if chk[0]['User_type'] == 'farmer':
                    request.session['farmer'] = chk[0]['Mobile_number']
                    request.session['fname'] = chk[0]['Name']
                    return redirect(farmer_dashboard)
                if chk[0]['User_type'] == 'sarpanch':
                    request.session['sarpanch'] = chk[0]['Mobile_number']
                    request.session['sname'] = chk[0]['Name']
                    return redirect(admin_dashboard)
            else:
                messages.error(request,"User Not Approoved By Admin!")
                # return HttpResponse("<script>alert('User Not Approoved By Admin'); location.href='../'</script>")
        else:
            messages.error(request,"Invalid Mobile Number Or Password!")
            # return HttpResponse("<script>alert('Invalid UserName Or Password'); location.href='../'</script>")
    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        valid = False
        type = request.POST['type']
        if type == 'sarpanch':
            area = 'null'
            servay = 'null'
        else:
            area = request.POST['area']
            servay = request.POST['servay']
        name = request.POST['name']
        mobile = request.POST['mobile']
        password = request.POST['password']
        district = request.POST['district'].upper()
        taluka = request.POST['taluka'].upper()
        village = (request.POST['village']).upper()
        user_data = user(Mobile_number=mobile, Name=name.strip(), User_type=type, Valid_user_or_not=valid, Servay_num=servay,
                         Password=password, District=district.strip(), Taluka=taluka.strip(), Village=village.strip(), Land_area=area)
        user_data.save()
        messages.success(request,"Account Created Successfully! Wait For Admin Approval!!")
        return render(request, 'login.html')
    else:
        return render(request, 'registration.html')




# supe admin

def super_admin_dashboard(request):
    if request.session.has_key('super'):
        global aname,auser
        aname = request.session['supername']
        auser = request.session['super']
        scheme = schemes.objects.all()
        sdata = user.objects.filter(User_type='sarpanch',Valid_user_or_not=True).values()
        fdata = user.objects.filter(User_type='farmer',Valid_user_or_not=True).values()
        context ={
            'scheme' : len(scheme),
            'sarpanch' : len(sdata),
            'farmer' : len(fdata),
            'aname' : aname,
            'auser' : auser,
        }
        return render(request, 'super_admin_dashboard.html',context)
    else:
        return redirect(login)


def super_admin_approval(request):
    if request.session.has_key('super'):
        data = user.objects.filter(User_type='sarpanch',Valid_user_or_not=False).values()
        context={
            'data' : data,
            'aname' : aname,
            'auser' : auser,
        }
        return render(request, 'super_admin_approval.html',context)
    else:
        return redirect(login)


def super_admin_addscheme(request):
    if request.session.has_key('super'):
        if request.method == 'POST':
            Name = request.POST['sname']
            Eligibility = request.POST['eligi']
            For_district = request.POST['sdistrict'].upper()
            For_taluka = request.POST['staluka'].upper()
            Starting_date = request.POST['sdate']
            Ending_date = request.POST['edate']
            Schemes_desc = request.POST['sdesc']
            scheme = schemes(Name=Name,Eligibility=Eligibility,For_district=For_district.strip(),For_taluka=For_taluka.strip(),Starting_date=Starting_date,Ending_date=Ending_date,Schemes_desc=Schemes_desc)
            scheme.save()
        scheme_data = schemes.objects.all()
        context={
            'scheme_data' : scheme_data,
            'aname' : aname,
            'auser' : auser,
        }
        return render(request, 'super_admin_addscheme.html',context)
    else:
        return redirect(login)


def super_admin_farm_info(request):
    if request.session.has_key('super'):
        data_farmer = user.objects.filter(User_type='farmer',Valid_user_or_not=True).values()
        data_sarpanch = user.objects.filter(User_type='sarpanch',Valid_user_or_not=True).values()
        context={
            'data_farmer' : data_farmer,
            'data_sarpanch' : data_sarpanch,
            'aname' : aname,
            'auser' : auser,
        }
        return render(request, 'super_admin_farm_info.html',context)
    else:
        return redirect(login)


def super_admin_app_approove(request):
    if request.session.has_key('super'):
        statusapp = Applied_Schemes.objects.all()
        context={
            'statusapp' : statusapp,
            'aname' : aname,
            'auser' : auser,
        }
        return render(request, 'super_admin_app_approove.html',context)
    else:
        return redirect(login)



# admin

def admin_dashboard(request):
    if request.session.has_key('sarpanch'):
        global sname,suser,sdata
        sname = request.session['sname']
        suser = request.session['sarpanch']
        sdata = user.objects.filter(Mobile_number=suser).values()
        scheme = schemes.objects.all()
        farmers = user.objects.filter(User_type='farmer',Valid_user_or_not=True).values()
        vdata = user.objects.filter(Mobile_number=request.session['sarpanch']).values()
        farmer = user.objects.filter(User_type='farmer',Valid_user_or_not=True,Village=vdata[0]['Village']).values()
        context ={
            'scheme' : len(scheme),
            'farmers' : len(farmers),
            'farmer' : len(farmer),
            'sname' : sname,
            'suser' : suser,
            'sdata' : sdata,
        }
        return render(request, 'admin_dashboard.html',context)
    else:
        return redirect(login)


def admin_approval(request):
    if request.session.has_key('sarpanch'):
        vdata = user.objects.filter(Mobile_number=request.session['sarpanch']).values()
        data = user.objects.filter(User_type='farmer',Valid_user_or_not=False,Village=vdata[0]['Village']).values()
        context={
            'data' : data,
            'sname' : sname,
            'suser' : suser,
            'sdata' : sdata,
        }
        return render(request, 'admin_approval.html',context)
    else:
        return redirect(login)

def admin_scheme(request):
    if request.session.has_key('sarpanch'):
        fname = request.session['sname']
        vdata = user.objects.get(Mobile_number=suser)
        dist = vdata.District
        taluka = vdata.Taluka
        schemedata1 = schemes.objects.filter(For_district='ALL').values()
        schemedata2 = schemes.objects.filter(For_district=dist,For_taluka='ALL').values()
        schemedata3 = schemes.objects.filter(For_district=dist,For_taluka=taluka).values()
        context={
            'schemedata1' : schemedata1,
            'schemedata2' : schemedata2,
            'schemedata3' : schemedata3,
            'sname' : sname,
            'suser' : suser,
            'sdata' : sdata,
        }
        return render(request, 'admin_scheme.html',context)
    else:
        return redirect(login)


def admin_farm_info(request):
    if request.session.has_key('sarpanch'):
        vdata = user.objects.filter(Mobile_number=request.session['sarpanch']).values()
        data_farmer = user.objects.filter(User_type='farmer',Village=vdata[0]['Village'],Valid_user_or_not=True).values()
        context={
            'data_farmer' : data_farmer,
            'sname' : sname,
            'suser' : suser,
            'sdata' : sdata,
        }
        return render(request, 'admin_farm_info.html',context)
    else:
        return redirect(login)



# farmer

def farmer_dashboard(request):
    if request.session.has_key('farmer'):
        global fname,fuser,fdata
        fname = request.session['fname']
        fuser = request.session['farmer']
        fdata = user.objects.filter(Mobile_number=fuser).values()
        context={
            'fname' : fname,
            'fuser' : fuser,
            'fdata' : fdata,
        }
        return render(request, 'farmer_dashboard.html',context)
    else:
        return redirect(login)


def farmer_ava_scheme(request):
    if request.session.has_key('farmer'):
        fname = request.session['fname']
        vdata = user.objects.get(Mobile_number=fuser)
        dist = vdata.District
        taluka = vdata.Taluka
        schemedata1 = schemes.objects.filter(For_district='ALL').values()
        schemedata2 = schemes.objects.filter(For_district=dist,For_taluka='ALL').values()
        schemedata3 = schemes.objects.filter(For_district=dist,For_taluka=taluka).values()
        context={
            'schemedata1' : schemedata1,
            'schemedata2' : schemedata2,
            'schemedata3' : schemedata3,
            'fname' : fname,
            'fuser' : fuser,
            'fdata' : fdata,
        }
        return render(request, 'farmer_ava_scheme.html',context)
    else:
        return redirect(login)



def farmer_status_app(request):
    if request.session.has_key('farmer'):
        fname = request.session['fname']
        appstatus = Applied_Schemes.objects.all()
        context={
            'fname' : fname,
            'fuser' : fuser,
            'fdata' : fdata,
            'appstatus' : appstatus,
        }
        return render(request, 'farmer_status_app.html',context)
    else:
        return redirect(login)




#approve

def approve_sarapanch(request,mobile_num):
    if request.session.has_key('super'):
        if request.method == 'POST':
            userdata = user.objects.get(Mobile_number=mobile_num)
            userdata.Valid_user_or_not = True
            userdata.save()
        return redirect(super_admin_approval)
    else:
        return redirect(login)


def approve_farmer(request,mobile_num):
    if request.session.has_key('sarpanch'):
        if request.method == 'POST':
            userdata = user.objects.get(Mobile_number=mobile_num)
            userdata.Valid_user_or_not = True
            userdata.save()
        return redirect(admin_approval)
    else:
        return redirect(login)


#apply scheme

def farmer_apply_scheme(request,Schemes_id):
    if request.session.has_key('farmer'):
        usr = user.objects.get(Mobile_number=fuser)
        sch = schemes.objects.get(Schemes_id=Schemes_id)
        appstat = Applied_Schemes.objects.filter(Usr=usr,Sch=sch)
        if appstat:
            if appstat[0].Schemes_status == 'Approved By Authority':
                messages.error(request,'You Already Apply This Scheme')
                return redirect(farmer_ava_scheme)
            elif appstat[0].Schemes_status == 'Pending':
                messages.error(request,'You Already Apply This Scheme')
                return redirect(farmer_ava_scheme)
            else:
                messages.error(request,'Your Application was rejected by authority due to some incorrect information! Re-Apply with the correct information')
                fname = request.session['fname']
                schemedata = schemes.objects.filter(Schemes_id=Schemes_id).values()
                userdata = user.objects.filter(Mobile_number=fuser).values()
                context={
                    'fname' : fname,
                    'fuser' : fuser,
                    'schemedata' : schemedata,
                    'userdata' : userdata,
                    'fdata' : fdata,
                    's_id' : Schemes_id,
                }
                return render(request,'farmer_apply_scheme.html',context)
        else:
            fname = request.session['fname']
            schemedata = schemes.objects.filter(Schemes_id=Schemes_id).values()
            userdata = user.objects.filter(Mobile_number=fuser).values()
            context={
                'fname' : fname,
                'fuser' : fuser,
                'schemedata' : schemedata,
                'userdata' : userdata,
                'fdata' : fdata,
                's_id' : Schemes_id,
            }
            return render(request,'farmer_apply_scheme.html',context)
    else:
        return redirect(login)

def applyscheme(request,s_id):
    if request.session.has_key('farmer'):
        if request.method == 'POST':
            bname = request.POST['bname']
            baccount = request.POST['baccount']
            bifsc = request.POST['bifsc']
            adhar = request.POST['adhar']
            sch = schemes.objects.get(Schemes_id=s_id)
            usr = user.objects.get(Mobile_number=fuser)
            appsch = Applied_Schemes(Schemes_status='Pending',Farmer_Adhar_Card=adhar,Farmer_Bank_Name=bname,Farmer_Bank_IFSC=bifsc,Farmer_Account_num=baccount,Sch=sch,Usr=usr)
            appsch.save()
            messages.success(request,'Application submitted Successfully! Wait for approval!')
        return redirect(farmer_ava_scheme)
    else:
        return redirect(login)

#decline

def decline(request,mobile_num):
    if request.session.has_key('super') or request.session.has_key('sarpanch') or request.session.has_key('farmer'):
        userdata = user.objects.get(Mobile_number=mobile_num)
        if userdata.User_type == 'sarpanch':
            userdata.delete()
            return redirect(super_admin_approval)
        else:
            userdata.delete()
            return redirect(admin_approval)
    else:
        return redirect(login)

#delete user

def sadeleteuser(request,mobile_num):
    if request.session.has_key('super') or request.session.has_key('sarpanch') or request.session.has_key('farmer'):
        userdata = user.objects.get(Mobile_number=mobile_num)
        userdata.delete()
        return redirect(super_admin_farm_info)
    else:
        return redirect(login)

def admindeleteuser(request,mobile_num):
    if request.session.has_key('super') or request.session.has_key('sarpanch') or request.session.has_key('farmer'):
        userdata = user.objects.get(Mobile_number=mobile_num)
        userdata.delete()
        return redirect(admin_farm_info)
    else:
        return redirect(login)


#scheme delete 
def sdelete(request,s_id):
    if request.session.has_key('super') or request.session.has_key('sarpanch') or request.session.has_key('farmer'):
        s = schemes.objects.get(Schemes_id=s_id)
        s.delete()
        return redirect(super_admin_addscheme)
    else:
        return redirect(login)

#logout

def logout(request,type):
    if type == 'super':
        try:
            del request.session['super']
            del request.session['supername']
        except KeyError:
            pass
    if type == 'admin':
        try:
            del request.session['sarpanch']
            del request.session['sname']
        except KeyError:
            pass
    if type == 'farmer':
        try:
            del request.session['farmer']
            del request.session['fname']
        except KeyError:
            pass
    return redirect(login)




#change password

def changepass(request,user_name):
    if request.session.has_key('super') or request.session.has_key('sarpanch') or request.session.has_key('farmer'):
        if request.method == 'POST':
            current_password = request.POST['cpsw']
            new_password = request.POST['npsw']
            global userdata
            try:
                userdata = user.objects.get(Mobile_number=user_name)
                if userdata.User_type == 'sarpanch':
                    if userdata.Password == current_password:
                        userdata.Password = new_password
                        userdata.save()
                        messages.success(request,"Your Password Changed Successfully")
                        return redirect(admin_dashboard )
                    else:
                        messages.error(request,"Current password does not match")
                        return redirect(admin_dashboard)
                elif userdata.User_type == 'farmer':
                    if userdata.Password == current_password:
                        userdata.Password = new_password
                        userdata.save()
                        messages.success(request,"Your Password Changed Successfully")
                        return redirect(farmer_dashboard)
                    else:
                        messages.error(request,"Current password does not match")
                        return redirect(farmer_dashboard)
            except:
                superuser = authenticate(username=user_name,password=current_password)
                if superuser is not None:
                    usr = get_user_model().objects.get(username=request.session['super'])
                    usr.set_password(new_password)
                    usr.save()
                    messages.success(request,"Your Password Changed Successfully")
                    return redirect(super_admin_dashboard)
                else:
                    messages.error(request,"Current password does not match")
                    return redirect(super_admin_dashboard)
    else:
        return redirect(login)


#edit profile
def fedit(request,user_name):
    if request.session.has_key('farmer'):
        if request.method == 'POST':
            name = request.POST['name']
            usr = user.objects.get(Mobile_number=user_name)
            usr.Name = name
            usr.save()
            request.session['fname'] = name
        return redirect(farmer_dashboard)
    else:
        return redirect(login)


def sedit(request,user_name):
    if request.session.has_key('sarpanch'):
        if request.method == 'POST':
            name = request.POST['name']
            usr = user.objects.get(Mobile_number=user_name)
            usr.Name = name
            usr.save()
            request.session['sname'] = name
        return redirect(admin_dashboard)
    else:
        return redirect(login)




#edit user

def aedituser(request,user_mobile):
    if request.session.has_key('super') or request.session.has_key('sarpanch'):
        if request.method == 'POST':
            name = request.POST['name']
            mobile = request.POST['mobile']
            district = request.POST['district']
            taluka = request.POST['taluka']
            village = request.POST['village']
            area = request.POST['area']
            servay = request.POST['servay']
            userdata = user.objects.get(Mobile_number=user_mobile)
            userdata.Name = name
            userdata.Mobile_number = mobile
            userdata.District = district
            userdata.Taluka = taluka
            userdata.Village = village
            userdata.Land_area = area
            userdata.Servay_num = servay
            userdata.save()
            messages.success(request,"User Details Edited Successfully")
            return redirect(admin_farm_info)
    else:
        return redirect(login)

def sedituser(request,user_mobile):
    if request.session.has_key('super') or request.session.has_key('sarpanch'):
        if request.method == 'POST':
            name = request.POST['name']
            mobile = request.POST['mobile']
            district = request.POST['district']
            taluka = request.POST['taluka']
            village = request.POST['village']
            area = request.POST['area']
            servay = request.POST['servay']
            userdata = user.objects.get(Mobile_number=user_mobile)
            userdata.Name = name
            userdata.Mobile_number = mobile
            userdata.District = district
            userdata.Taluka = taluka
            userdata.Village = village
            userdata.Land_area = area
            userdata.Servay_num = servay
            userdata.save()
            messages.success(request,"User Details Edited Successfully")
            return redirect(super_admin_farm_info)
    else:
        return redirect(login)


def editscheme(request,id):
    if request.session.has_key('super'):
        if request.method == 'POST':
            sname = request.POST['sname']
            sdate = request.POST['sdate']
            edate = request.POST['edate']
            sdistrict = request.POST['sdistrict']
            staluka = request.POST['staluka']
            eligi = request.POST['eligi']
            sdesc = request.POST['sdesc']
            schemedata = schemes.objects.get(Schemes_id=id)
            schemedata.Name = sname
            schemedata.Eligibility = eligi
            schemedata.For_district = sdistrict
            schemedata.For_taluka = staluka
            schemedata.Starting_date = sdate
            schemedata.Ending_date = edate
            schemedata.Schemes_desc = sdesc
            schemedata.save()
            messages.success(request,'Scheme Edited Successfully!')
        return redirect(super_admin_addscheme)
    else:
        return redirect(login)

#change status of scheme  
def changestatus(request):
    if request.session.has_key('super'):
        if request.method == 'POST':
            action = request.POST['action']
            sid = request.POST['s_id']
            uid = request.POST['u_id']
            appstatus = Applied_Schemes.objects.get(Usr=uid,Sch=sid)
            if action == 'APPROVE':
                appstatus.Schemes_status = 'Approved By Authority'
                appstatus.save()
                messages.success(request,'Scheme Approved!')
            else:
                appstatus.Schemes_status = 'Rejected By Authority'
                appstatus.save()
                messages.success(request,'Scheme Rejected!')
        return redirect(super_admin_app_approove)
    else:
        return redirect(login)