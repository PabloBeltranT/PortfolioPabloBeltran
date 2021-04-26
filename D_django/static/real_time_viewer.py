from random import randint


# Llamar a arduino para solicitar partes por millon
def parts_per_million():

    ppm = {
        'ppm_01':randint(0, 1000),
        'ppm_02':randint(0, 1000),
        'ppm_03':randint(0, 1000),
        'ppm_04':randint(0, 1000),
        'ppm_05':randint(0, 1000),
        'ppm_06':randint(0, 1000),
        'ppm_07':randint(0, 1000),
        'ppm_08':randint(0, 1000),
        'ppm_09':randint(0, 1000),
        'ppm_10':randint(0, 1000),
        'ppm_11':randint(0, 1000),
        'ppm_12':randint(0, 1000),
        'ppm_13':randint(0, 1000),
        'ppm_14':randint(0, 1000),
        'ppm_15':randint(0, 1000),
        'ppm_16':randint(0, 1000),
        'ppm_17':randint(0, 1000),
        'ppm_18':randint(0, 1000),
        'ppm_19':randint(0, 1000),
        'ppm_20':randint(0, 1000),
    }
    return ppm


# Llamar a arduino para solicitar alarmas
def alarms():

    ppm = {
        'a_01':randint(0, 1),
        'a_02':randint(0, 1),
        'a_03':randint(0, 1),
        'a_04':randint(0, 1),
        'a_05':randint(0, 1),
        'a_06':randint(0, 1),
        'a_07':randint(0, 1),
        'a_08':randint(0, 1),
        'a_09':randint(0, 1),
        'a_10':randint(0, 1),
        'a_11':randint(0, 1),
        'a_12':randint(0, 1),
        'a_13':randint(0, 1),
        'a_14':randint(0, 1),
        'a_15':randint(0, 1),
        'a_16':randint(0, 1),
        'a_17':randint(0, 1),
        'a_18':randint(0, 1),
        'a_19':randint(0, 1),
        'a_20':randint(0, 1),
    }
    return ppm


# Llamar a arduino para solicitar pre alarmas
def pre_alarms():

    ppm = {
        'p_01':randint(0, 1),
        'p_02':randint(0, 1),
        'p_03':randint(0, 1),
        'p_04':randint(0, 1),
        'p_05':randint(0, 1),
        'p_06':randint(0, 1),
        'p_07':randint(0, 1),
        'p_08':randint(0, 1),
        'p_09':randint(0, 1),
        'p_10':randint(0, 1),
        'p_11':randint(0, 1),
        'p_12':randint(0, 1),
        'p_13':randint(0, 1),
        'p_14':randint(0, 1),
        'p_15':randint(0, 1),
        'p_16':randint(0, 1),
        'p_17':randint(0, 1),
        'p_18':randint(0, 1),
        'p_19':randint(0, 1),
        'p_20':randint(0, 1),
    }
    return ppm


# definir los nombre de ca sensor.
def nombres():
    nombres = {
        'n_01':'Sensor 01',
        'n_02':'Sensor 02',
        'n_03':'Sensor 03',
        'n_04':'Sensor 04',
        'n_05':'Sensor 05',
        'n_06':'Sensor 06',
        'n_07':'Sensor 07',
        'n_08':'Sensor 08',
        'n_09':'Sensor 09',
        'n_10':'Sensor 10',
        'n_11':'Sensor 11',
        'n_12':'Sensor 12',
        'n_13':'Sensor 13',
        'n_14':'Sensor 14',
        'n_15':'Sensor 15',
        'n_16':'Sensor 16',
        'n_17':'Sensor 17',
        'n_18':'Sensor 18',
        'n_19':'Sensor 19',
        'n_20':'Sensor 20',
    }
    return nombres


# Iformacion completa
def information():
    information = {
        'ppm':parts_per_million(),
        'alarm':alarms(),
        'pre_alarm':pre_alarms(),
        'nombre':nombres(),
    }
    return information