from general.models import Product
import datetime
from datetime import timedelta


def update() :
    devices = Product.objects.all().order_by("LaunchDate")
    for device in devices:
        if device.Archive == False:
            teams = device.team_set.all().order_by('id')
            OverallTasks = 0
            OverallCompletedTasks = 0
            for team in teams:
                today = datetime.date.today()
                tasks = team.task_set.all().order_by('id')
                Taskcompleted = 0
                NumberOfTasks = 0
                for task in tasks:
                    OverallTasks = OverallTasks + 1
                    NumberOfTasks = NumberOfTasks + 1
                    if task.CompleteDate:
                        task.Warning = False
                        task.Alert = False
                        OverallCompletedTasks = OverallCompletedTasks + 1
                        Taskcompleted = Taskcompleted + 1
                    if task.EndDate:
                        Time_delta = task.EndDate - today
                        if Time_delta < timedelta(team.Time_Delta_For_Warning) and Time_delta > timedelta(0) and \
                                not task.CompleteDate:
                            task.Warning = True
                            team.Status = 'At Risk'
                        elif Time_delta < timedelta(0) and not task.CompleteDate:
                            task.Warning = False
                            task.Alert = True
                    else:
                        Time_delta = None
                    task.save()

                for task in tasks:
                    if task.Alert == True:
                        team.Status = 'Delayed'
                    task.save()

                if NumberOfTasks != 0:
                    PercentCompleted = int((Taskcompleted * 100) / NumberOfTasks)
                    team.completed = PercentCompleted
                    team.save()
            if OverallTasks != 0:
                OverallCompletedPercent = int((OverallCompletedTasks * 100) / OverallTasks)
                device.completed = OverallCompletedPercent
                device.save()

    return

def delayedElements(Devices):
    teamname = []
    Delayed = []
    DueSoon = []
    Completed = []
    OnTime = []
    teams = Devices.team_set.all().order_by('id')
    for team in teams:
        complete = 0
        delay = 0
        due = 0
        ontime = 0
        teamname.append(team.TeamName)
        tasks = team.task_set.all()
        for task in tasks:
            if task.CompleteDate:
                complete +=1
            elif task.Alert:
                delay +=1
            elif task.Warning:
                due +=1
            else:
                ontime +=1

        Completed.append(complete)
        Delayed.append(delay)
        DueSoon.append(due)
        OnTime.append(ontime)

    return zip(Completed,Delayed,DueSoon,OnTime,teamname)