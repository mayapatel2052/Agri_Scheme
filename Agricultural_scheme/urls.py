"""Agricultural_scheme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Agricultural_scheme import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('super_admin_dashboard/',views.super_admin_dashboard,name='super_admin_dashboard'),
    path('super_admin_approval/',views.super_admin_approval,name='super_admin_approval'),
    path('super_admin_farm_info/',views.super_admin_farm_info,name='super_admin_farm_info'),
    path('super_admin_addscheme/',views.super_admin_addscheme,name='super_admin_addscheme'),
    path('super_admin_app_approove/',views.super_admin_app_approove,name='super_admin_app_approove'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('admin_approval/',views.admin_approval,name='admin_approval'),
    path('admin_farm_info/',views.admin_farm_info,name='admin_farm_info'),
    path('admin_scheme/',views.admin_scheme,name='admin_scheme'),
    path('farmer_dashboard/',views.farmer_dashboard,name='farmer_dashboard'),
    path('farmer_ava_scheme/',views.farmer_ava_scheme,name='farmer_ava_scheme'),
    path('farmer_status_app/',views.farmer_status_app,name='farmer_status_app'),
    path('farmer_apply_scheme/<str:Schemes_id>',views.farmer_apply_scheme,name='farmer_apply_scheme'),
    path('approve_sarapanch/<str:mobile_num>',views.approve_sarapanch,name='approve_sarapanch'),
    path('approve_farmer/<str:mobile_num>',views.approve_farmer,name='approve_farmer'),
    path('logout/<str:type>',views.logout,name='logout'),
    path('decline/<str:mobile_num>',views.decline,name='decline'),
    path('sadeleteuser/<str:mobile_num>',views.sadeleteuser,name='sadeleteuser'),
    path('sdelete/<int:s_id>',views.sdelete,name='sdelete'),
    path('admindeleteuser/<str:mobile_num>',views.admindeleteuser,name='admindeleteuser'),
    path('changepass/<str:user_name>',views.changepass,name='changepass'),
    path('fedit/<str:user_name>',views.fedit,name='fedit'),
    path('sedit/<str:user_name>',views.sedit,name='sedit'),
    path('aedituser/<str:user_mobile>',views.aedituser,name='aedituser'),
    path('sedituser/<str:user_mobile>',views.sedituser,name='sedituser'),
    path('editscheme/<int:id>',views.editscheme,name='editscheme'),
    path('applyscheme/<int:s_id>',views.applyscheme,name='applyscheme'),
    path('changestatus/',views.changestatus,name='changestatus'),
]
