import datetime
import os

def check_time(today_hour, today_min, shutdown_hour, shutdown_min):

    if today_hour > shutdown_hour:
        print("[+] ERROR: La hora introducida es menor que la hora actual")
        print("[+] INFO: La hora actual es " + str(today_hour) + ":" + str(today_min))
        print("[+] INFO: La hora introducida es " + str(shutdown_hour) + ":" + str(shutdown_min))
        exit(1)
    elif today_hour == shutdown_hour and today_min > shutdown_min:
        print("[+] ERROR: La hora introducida es menor que la hora actual")
        print("[+] INFO: La hora actual es " + str(today_hour) + ":" + str(today_min))
        print("[+] INFO: La hora introducida es " + str(shutdown_hour) + ":" + str(shutdown_min))
        exit(1)

    return True


def get_seconds(today_hour, today_min, shutdown_hour, shutdown_min):

    total_seconds = 0

    # Hours and minutes to seconds
    if today_hour == shutdown_hour:
        total_seconds = total_seconds + 0 # Hours
        total_seconds = total_seconds + ((shutdown_min - today_min) * 60) # Minutes
    else:
        total_seconds = total_seconds + ((shutdown_hour - today_hour) * 3600) # Hours
        hours_distance = shutdown_hour - today_hour
        if today_min < shutdown_min: # Minutes
            total_seconds = total_seconds + ((shutdown_min - today_min) * 60)
        else:
            today_rest_seconds = (60 - today_min) * 60
            shutdown_seconds = shutdown_min * 60
            total_seconds = (total_seconds + today_rest_seconds + shutdown_seconds) - (hours_distance * 3600)


    return total_seconds

def get_shutdown_date(today, date):

    # Get today hour and min
    today_time = str(today).split(" ")[1]
    today_hour = str(today_time).split(":")[0]
    today_min = str(today_time).split(":")[1]

    try:
        # Get shutdown hour and min
        shutdown_hour = str(date).split(":")[0]
        shutdown_min = str(date).split(":")[1]
    except IndexError:
        print("[+] ERROR: Formato de fecha incorrecto")
        exit(1)

    is_time_ok = check_time(int(today_hour), int(today_min), int(shutdown_hour), int(shutdown_min))

    if is_time_ok:
        print("[+] INFO: La fecha introducida es correcta.")

    total_seconds = get_seconds(int(today_hour), int(today_min), int(shutdown_hour), int(shutdown_min))
    print("[+] INFO: El equipo se apagara en " + str(total_seconds) + " segundos...")

    return total_seconds


shutdown = input("A que hora quieres apagar hoy el equipo ? (Formato: hh:mm. Introduce 0, para cancelar el apagado): ")
try:
    shutdown = int(shutdown)
    os.system("shutdown /a")
except ValueError:
    today = datetime.datetime.today()
    shutdown_date = get_shutdown_date(today, shutdown)
    os.system("shutdown /s /t " + str(shutdown_date))