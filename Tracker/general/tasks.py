from celery import Celery
import datetime



app = Celery()

@app.task
def test1(arg):
    from general.models import (Product, DeviceHistory
    )
    device = Product.objects.all().order_by("LaunchDate")
    for D in device:
        print(D.Name)
        New= DeviceHistory(Completed=D.completed, device= D)
        New.save()