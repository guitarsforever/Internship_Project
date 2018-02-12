from celery import Celery
import datetime



app = Celery()

@app.task
def test(arg):
    from hahe.models import (Product, DeviceHistory, TeamHistory
    )
    device = Product.objects.all().order_by("LaunchDate")
    for D in device:
        print(D.Name)
        New= DeviceHistory(Completed=D.completed, device= D)
        New.save()
        teams = D.team_set.all().order_by('id')
        for team in teams:
            complete = 0
            delay = 0
            due = 0
            ontime = 0
            tasks = team.task_set.all()
            for task in tasks:
                if task.CompleteDate:
                    complete += 1
                elif task.Alert:
                    delay += 1
                elif task.Warning:
                    due += 1
                else:
                    ontime += 1
            Total = complete + delay + due + ontime

            if Total != 0:
                PercentI = round(((complete/Total)*100),2)
                PercentJ = round(((delay/Total)*100),2)
                PercentK = round(((due/Total)*100),2)
                PercentL = round(((ontime/Total)*100),2)
                NewTeam = TeamHistory(Delayed = PercentJ,Completed = PercentI,DueSoon = PercentK, OnTime = PercentL,
                                      device = D, team = team)
                NewTeam.save()
                print (PercentI,PercentJ, PercentK,PercentL, team.TeamName)
            else:
                NewTeam = TeamHistory(Delayed=0, Completed=0, DueSoon=0, OnTime=0,
                                      device=D, team=team)
                NewTeam.save()