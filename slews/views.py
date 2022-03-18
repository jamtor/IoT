from enum import auto
from http import client
from django.shortcuts import render
from slews.forms import UserForm,UserProfileInfoForm
from slews import influxcon

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings

import json
import folium

# m = folium.Map(width=800, height=500, location=[6.9214, 122.0490])

# Create your views here.
def index(request):
    return render(request,'slews/index.html')

def main(request):
    slewsmap = folium.Map(location=[7.038800, 122.100025], zoom_start=12, tiles="cartodbpositron",
               scrollWheelZoom=False)

    acceV = get_accelerometer('SELECT mean(value) FROM device_frmpayload_data_Accelerometer WHERE (dev_eui = \'b02fd62ef52074de\') AND time >= now() - 1h and time <= now() GROUP BY time(5s) fill(null)')
    incliV = get_gyro('SELECT mean(value) FROM device_frmpayload_data_Gyro WHERE (dev_eui = \'b02fd62ef52074de\') AND time >= now() - 1h and time <= now() GROUP BY time(5s) fill(null)')
    soilV = get_soilm('SELECT mean(value) FROM device_frmpayload_data_SoilMoisture WHERE (dev_eui = \'b02fd62ef52074de\') AND time >= now() - 1h and time <= now() GROUP BY time(5s) fill(null)')
    tempV = get_temperature('SELECT mean(value) FROM device_frmpayload_data_Temperature WHERE (dev_eui = \'b02fd62ef52074de\') AND time >= now() - 1h and time <= now() GROUP BY time(5s) fill(null)')


    folium.Marker([7.12634318821439, 121.9271515462821], tooltip='Click to see details', popup="Accelerometer: " + '{:.2f}'.format(acceV) +
                                    "<br> Inclinometer: " + '{:.2f}'.format(incliV) + "<br> Soil Moisture: " + '{:.2f}'.format(soilV) +
                                    "<br> Temperature: " + '{:.2f}'.format(tempV),
                                    icon=folium.Icon(color='green')).add_to(slewsmap)


    # folium.Marker([7.12634318821439, 121.9271515462821], tooltip='Click to see details', popup="Rating: 63% Warning<br>Soil moisture: 52% <br>Movement:4m2",
    #                 icon=folium.Icon(color='red')).add_to(m)
    # folium.Marker([7.1286123128787136, 121.9294096569382], tooltip='Click to see details', popup="Rating: 63% Warning<br>Soil moisture: 52% <br>Movement:4m2",
    #                 icon=folium.Icon(color='orange')).add_to(m)
    # folium.Marker([7.128935217462367, 121.93124274798035], tooltip='Click to see details', popup="Rating: 63% Warning<br>Soil moisture: 52% <br>Movement:4m2",
    #                 icon=folium.Icon(color='red')).add_to(m)
    slewsmap = slewsmap._repr_html_()

    return render(request,'slews/main.html',{
                                'slewsmap':slewsmap
    })

@login_required
def dashboard(request):

    # nodeAccelerometer = list(influxcon.get_influxdb_client().query('SELECT mean(value) FROM device_frmpayload_data_Accelerometer WHERE time >= now() - 6h GROUP BY time(10m) fill(linear)'))
    # nodeGyro = list(influxcon.get_influxdb_client().query('SELECT mean(value) FROM device_frmpayload_data_Gyro WHERE time >= now() - 6h GROUP BY time(10m) fill(linear)'))
    # nodeSoil = list(influxcon.get_influxdb_client().query('SELECT mean(value) FROM device_frmpayload_data_SoilMoisture WHERE time >= now() - 6h GROUP BY time(10m) fill(linear)'))
    # nodeTemperature = list(influxcon.get_influxdb_client().query('SELECT mean(value) FROM device_frmpayload_data_Temperature WHERE time >= now() - 6h GROUP BY time(10m) fill(linear)'))
    # nodeTemperatureGauge = list(influxcon.get_influxdb_client().query('SELECT mean(value) FROM device_frmpayload_data_Temperature WHERE time >= now() - 30m GROUP BY dev_eui'))
    # nodeSoilGauge = list(influxcon.get_influxdb_client().query('SELECT mean(value) FROM device_frmpayload_data_SoilMoisture WHERE time >= now() - 30m GROUP BY dev_eui'))

    # print(nodeSoilGauge[0])
    # for item in nodeSoilGauge:
    #     for data_item in item:
    #         print(data_item['mean'])

    # nodeAc = json.dumps(nodeAccelerometer)
    # nodeGy = json.dumps(nodeGyro)
    # nodeSo = json.dumps(nodeSoil)
    # nodeTe = json.dumps(nodeTemperature)
    # nodeTeG = json.dumps(nodeTemperatureGauge)
    # nodeSoG = json.dumps(nodeSoilGauge)
    #6.926468, 122.089632
    f = folium.Figure(height=500)
    armsmap = folium.Map(location=[7.127715, 121.959492], zoom_start=14, tiles="cartodbpositron",
               scrollWheelZoom=False).add_to(f)

    folium.Marker([7.12634318821439, 121.9271515462821],
                     icon=folium.Icon(color='red')).add_to(armsmap)

    folium.Marker([7.1286123128787136, 121.9294096569382],
                     icon=folium.Icon(color='green')).add_to(armsmap)
    
    folium.Marker([7.128935217462367, 121.93124274798035],
                     icon=folium.Icon(color='green')).add_to(armsmap)

    armsmap = armsmap._repr_html_()

    return render(request,'slews/dashboardslews.html',{
                                'armsmap':armsmap
    })


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method =="POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'slews/registration.html',{
                            'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered
    })

def user_login(request):

    if request.method =='POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        username = get_user(email)

        user = authenticate(username=username,password=password)
        # print(user)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('main'))

            else:
                return HttpResponse('Account Not Active')

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("invalid login details supplied!")

    else:
        return render(request,'slews/index.html',{})

def get_user(email):
    try:
        return User.objects.get(email=email.lower())
    except User.DoesNotExist:
        return None

def get_accelerometer(query):
    nodeAcc = list(influxcon.get_influxdb_client().query(query))
    acceV = 0.00
    for item in nodeAcc:
        for data_item in item:
            if data_item['mean'] is not None:
                acceV = float(data_item['mean'])
    return acceV

def get_gyro(query):
    nodeGyro = list(influxcon.get_influxdb_client().query(query))
    incliV = 0.00
    for item in nodeGyro:
        for data_item in item:
            if data_item['mean'] is not None:
                incliV = float(data_item['mean'])
    return incliV

def get_soilm(query):
    nodeSoil = list(influxcon.get_influxdb_client().query(query))
    soilV = 0.00
    for item in nodeSoil:
        for data_item in item:
            if data_item['mean'] is not None:
                soilV = float(data_item['mean'])
    return soilV

def get_temperature(query):
    nodeTemperature = list(influxcon.get_influxdb_client().query(query))
    tempV = 0.00
    for item in nodeTemperature:
        for data_item in item:
            if data_item['mean'] is not None:
                tempV = float(data_item['mean'])
    return tempV
