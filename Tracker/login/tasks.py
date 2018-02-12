# from celery import Celery
# import datetime
#
#
#
# app = Celery()
#
# # @app.on_after_configure.connect
# # def setup_periodic_tasks(sender, **kwargs):
# #     sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
# #
# #     # Calls test('world') every 30 seconds
# #     sender.add_periodic_task(30.0, test.s('world'), expires=10)
# #
# #     # Executes every Monday morning at 7:30 a.m.
# #     sender.add_periodic_task(
# #         crontab(hour=7, minute=30, day_of_week=1),
# #         test.s('Happy Mondays!'),
# #     )
# #
# #
# @app.task
# def test(arg):
#     from login.models import (
#         Device, DeviceHistory,ProductReadinessHistory, VideoContentHistory, DigitalContentHistory,
#     CallCenterTrainingHistory, CallCenterOperationsHistory, ProductSupportHistory, WarehouseHistory, FieldServiceHistory,
#     TechSupportHistory, ServiceMarketingHistory, ServiceTrainingHistory, PartsHistory
#     )
#     from . import extra_utils
#     device = Device.objects.all().order_by("LaunchDate")
#     for D in device:
#         print(D.Name)
#         New= DeviceHistory(Completed=D.completed, device= D)
#         New.save()
#         zipped_data = extra_utils.delayedElements(D)
#         counter = 0
#         for i, j, k, l in zipped_data:
#             counter += 1
#             Total = i + j + k + l
#             if counter == 1:
#                 if Total != 0:
#                     PercentI = round(((i / Total) * 100), 2)
#                     PercentJ = round(((j / Total) * 100), 2)
#                     PercentK = round(((k / Total) * 100), 2)
#                     PercentL = round(((l / Total) * 100), 2)
#                     ProductReadiness = ProductReadinessHistory(Delayed=PercentJ, Completed=PercentI, DueSoon=PercentK,
#                                                                OnTime=PercentL, Device= D)
#                 else:
#                     ProductReadiness = ProductReadinessHistory(Delayed=0, Completed=0, DueSoon=0,
#                                                                OnTime=0, Device= D)
#                 ProductReadiness.save()
#
#             if counter == 2:
#                 if Total != 0:
#                     PercentI = round(((i / Total) * 100), 2)
#                     PercentJ = round(((j / Total) * 100), 2)
#                     PercentK = round(((k / Total) * 100), 2)
#                     PercentL = round(((l / Total) * 100), 2)
#                     VideoContent = VideoContentHistory(Delayed=PercentJ, Completed=PercentI,
#                                                               DueSoon=PercentK, OnTime=PercentL, Device=D)
#                 else:
#                     VideoContent = VideoContentHistory(Delayed=0, Completed=0, DueSoon=0,
#                                                                OnTime=0, Device=D)
#                 VideoContent.save()
#             if counter == 3:
#                 if Total != 0:
#                     PercentI = round(((i / Total) * 100), 2)
#                     PercentJ = round(((j / Total) * 100), 2)
#                     PercentK = round(((k / Total) * 100), 2)
#                     PercentL = round(((l / Total) * 100), 2)
#                     DigitalContent = DigitalContentHistory(Delayed=PercentJ, Completed=PercentI,
#                                                                DueSoon=PercentK,
#                                                                OnTime=PercentL, Device=D)
#                 else:
#                     DigitalContent = DigitalContentHistory(Delayed=0, Completed=0, DueSoon=0,
#                                                                OnTime=0, Device=D)
#                 DigitalContent.save()
#
#             if counter == 4:
#                 if Total != 0:
#                     PercentI = round(((i / Total) * 100), 2)
#                     PercentJ = round(((j / Total) * 100), 2)
#                     PercentK = round(((k / Total) * 100), 2)
#                     PercentL = round(((l / Total) * 100), 2)
#                     CallCenterTraining = CallCenterTrainingHistory(Delayed=PercentJ, Completed=PercentI,
#                                                                DueSoon=PercentK, OnTime=PercentL, Device=D)
#                 else:
#                     CallCenterTraining = CallCenterTrainingHistory(Delayed=0, Completed=0, DueSoon=0,
#                                                                OnTime=0, Device=D)
#                 CallCenterTraining.save()
#
#             if counter == 5:
#                 if Total != 0:
#                     PercentI = round(((i / Total) * 100), 2)
#                     PercentJ = round(((j / Total) * 100), 2)
#                     PercentK = round(((k / Total) * 100), 2)
#                     PercentL = round(((l / Total) * 100), 2)
#                     CallCenterOperations = CallCenterOperationsHistory(Delayed=PercentJ, Completed=PercentI,
#                                                                DueSoon=PercentK,
#                                                                OnTime=PercentL, Device=D)
#                 else:
#                     CallCenterOperations = CallCenterOperationsHistory(Delayed=0, Completed=0, DueSoon=0,
#                                                                OnTime=0, Device=D)
#                 CallCenterOperations.save()
#
#             if counter == 6:
#                 if Total != 0:
#                     PercentI = round(((i / Total) * 100), 2)
#                     PercentJ = round(((j / Total) * 100), 2)
#                     PercentK = round(((k / Total) * 100), 2)
#                     PercentL = round(((l / Total) * 100), 2)
#                     ProductSupport = ProductSupportHistory(Delayed=PercentJ, Completed=PercentI,
#                                                                DueSoon=PercentK, OnTime=PercentL, Device=D)
#                 else:
#                     ProductSupport = ProductSupportHistory(Delayed=0, Completed=0, DueSoon=0,
#                                                                OnTime=0, Device=D)
#                 ProductSupport.save()
#             if counter == 7:
#                 if Total != 0:
#                     PercentI = round(((i / Total) * 100), 2)
#                     PercentJ = round(((j / Total) * 100), 2)
#                     PercentK = round(((k / Total) * 100), 2)
#                     PercentL = round(((l / Total) * 100), 2)
#                     Warehouse = WarehouseHistory(Delayed=PercentJ, Completed=PercentI,
#                                                                DueSoon=PercentK,
#                                                                OnTime=PercentL, Device=D)
#                 else:
#                     Warehouse = WarehouseHistory(Delayed=0, Completed=0, DueSoon=0,
#                                                                OnTime=0, Device=D)
#                 Warehouse.save()
#
#             if counter == 8:
#                 if Total != 0:
#                     PercentI = round(((i / Total) * 100), 2)
#                     PercentJ = round(((j / Total) * 100), 2)
#                     PercentK = round(((k / Total) * 100), 2)
#                     PercentL = round(((l / Total) * 100), 2)
#                     FieldService = FieldServiceHistory(Delayed=PercentJ, Completed=PercentI,
#                                                                DueSoon=PercentK, OnTime=PercentL, Device=D)
#                 else:
#                     FieldService = FieldServiceHistory(Delayed=0, Completed=0, DueSoon=0,
#                                                                OnTime=0, Device=D)
#                 FieldService.save()
#
#             if counter == 9:
#                 if Total != 0:
#                     PercentI = round(((i / Total) * 100), 2)
#                     PercentJ = round(((j / Total) * 100), 2)
#                     PercentK = round(((k / Total) * 100), 2)
#                     PercentL = round(((l / Total) * 100), 2)
#                     TechSupport = TechSupportHistory(Delayed=PercentJ, Completed=PercentI,
#                                                                DueSoon=PercentK,
#                                                                OnTime=PercentL, Device=D)
#                 else:
#                     TechSupport = TechSupportHistory(Delayed=0, Completed=0, DueSoon=0,
#                                                                OnTime=0, Device=D)
#                 TechSupport.save()
#
#             if counter == 10:
#                 if Total != 0:
#                     PercentI = round(((i / Total) * 100), 2)
#                     PercentJ = round(((j / Total) * 100), 2)
#                     PercentK = round(((k / Total) * 100), 2)
#                     PercentL = round(((l / Total) * 100), 2)
#                     ServiceMarketing = ServiceMarketingHistory(Delayed=PercentJ, Completed=PercentI,
#                                                                DueSoon=PercentK, OnTime=PercentL, Device=D)
#                 else:
#                     ServiceMarketing = ServiceMarketingHistory(Delayed=0, Completed=0, DueSoon=0,
#                                                                OnTime=0, Device=D)
#                 ServiceMarketing.save()
#             if counter == 11:
#                 if Total != 0:
#                     PercentI = round(((i / Total) * 100), 2)
#                     PercentJ = round(((j / Total) * 100), 2)
#                     PercentK = round(((k / Total) * 100), 2)
#                     PercentL = round(((l / Total) * 100), 2)
#                     ServiceTraining = ServiceTrainingHistory(Delayed=PercentJ, Completed=PercentI,
#                                                                DueSoon=PercentK,
#                                                                OnTime=PercentL, Device=D)
#                 else:
#                     ServiceTraining = ServiceTrainingHistory(Delayed=0, Completed=0, DueSoon=0,
#                                                                OnTime=0, Device=D)
#                 ServiceTraining.save()
#
#             if counter == 12:
#                 if Total != 0:
#                     PercentI = round(((i / Total) * 100), 2)
#                     PercentJ = round(((j / Total) * 100), 2)
#                     PercentK = round(((k / Total) * 100), 2)
#                     PercentL = round(((l / Total) * 100), 2)
#                     Parts = PartsHistory(Delayed=PercentJ, Completed=PercentI,
#                                                                DueSoon=PercentK, OnTime=PercentL, Device=D)
#                 else:
#                     Parts = PartsHistory(Delayed=0, Completed=0, DueSoon=0,
#                                                                OnTime=0, Device=D)
#                 Parts.save()
#

# To DO - Define a function to populate the email content by making a report of all the delayed and due soon tasks
# To Do - Optimize the front page calculation by adding distributed content.