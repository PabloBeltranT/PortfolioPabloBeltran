from django.shortcuts import render
from .models import Sesion

#
def django(request):
    return render(request, 'info.html', {'title':'Django'})


#
def login(request):
    try:
        admin_sesion = Sesion.objects.filter(user='aptechnologies').get()
        if admin_sesion.user == 'aptechnologies':
            return render(request, 'login.html', {})
    except:
        admin_sesion = Sesion(user='aptechnologies', password='appasswd')
        admin_sesion.save()

        return render(request, 'login.html', {'text':'login'})


#
def configuration(request):
    try:

        normal_sesion = Sesion.objects.filter(user=request.POST['usernamein']).get()
        if request.POST['usernamein'] == normal_sesion.user and request.POST['pass'] == normal_sesion.password:
            return render(request, 'configuration.html', {})
        else:
            return render(request, 'login.html', {'message':'Invalid Sesion!'})

    except:
        print('no entro')
        return render(request, 'login.html', {'message':'Invalid Sesion!'})


#
def real_time_viewer(request):
    try:

        if request.method == 'POST':
            return render(request, 'real_time_viewer.html', {'names':new_names(request), 'states':states(request)})
            #{'names':new_names(request), 'states':states(request)}
        else:
            return render(request, 'login.html', {'message':'Get Sesion!'})

    except:
        return render(request, 'login.html', {'message':'Get Sesion!'})

    



''' Other functions '''
# Obtain new names.
def new_names(request):
    
    new_names = {
        'm_01':request.POST['new_name01'],
        'm_02':request.POST['new_name02'],
        'm_03':request.POST['new_name03'],
        'm_04':request.POST['new_name04'],
        'm_05':request.POST['new_name05'],
        'm_06':request.POST['new_name06'],
        'm_07':request.POST['new_name07'],
        'm_08':request.POST['new_name08'],
        'm_09':request.POST['new_name01'],
        'm_10':request.POST['new_name10'],
        'm_11':request.POST['new_name11'],
        'm_12':request.POST['new_name12'],
        'm_13':request.POST['new_name13'],
        'm_14':request.POST['new_name14'],
        'm_15':request.POST['new_name15'],
        'm_16':request.POST['new_name16'],
        'm_17':request.POST['new_name17'],
        'm_18':request.POST['new_name18'],
        'm_19':request.POST['new_name19'],
        'm_20':request.POST['new_name20'],
    }

    default_names = {
        'm_01':'Sensor #01',
        'm_02':'Sensor #02',
        'm_03':'Sensor #03',
        'm_04':'Sensor #04',
        'm_05':'Sensor #05',
        'm_06':'Sensor #06',
        'm_07':'Sensor #07',
        'm_08':'Sensor #08',
        'm_09':'Sensor #09',
        'm_10':'Sensor #10',
        'm_11':'Sensor #11',
        'm_12':'Sensor #12',
        'm_13':'Sensor #13',
        'm_14':'Sensor #14',
        'm_15':'Sensor #15',
        'm_16':'Sensor #16',
        'm_17':'Sensor #17',
        'm_18':'Sensor #18',
        'm_19':'Sensor #19',
        'm_20':'Sensor #20',
    }

    for module in  new_names:
        if new_names[module] == '':
            new_names[module] = default_names[module]
    return new_names


# Set states of modules.
def states(request):
    states = {
        'state01':False,
        'state02':False,
        'state03':False,
        'state04':False,
        'state05':False,
        'state06':False,
        'state07':False,
        'state08':False,
        'state09':False,
        'state10':False,
        'state11':False,
        'state12':False,
        'state13':False,
        'state14':False,
        'state15':False,
        'state16':False,
        'state17':False,
        'state18':False,
        'state19':False,
        'state20':False,
    }
    for module in states:
        try:
            states[module] = request.POST[module]
        except:
            states[module] = False
    return states