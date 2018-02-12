from login.models import Device
import datetime
from datetime import timedelta

def delayedElements(Devices):
            Delayed = []
            DueSoon = []
            Completed = []
            OnTime = []
            complete = 0
            delay = 0
            due = 0
            ontime = 0
            if Devices.ProductReadiness.Task1_End_Date:
                print ("inside product readiness")
                if Devices.ProductReadiness.Task1_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task1_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task1_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task2_End_Date:
                if Devices.ProductReadiness.Task2_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task2_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task2_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task3_End_Date:
                if Devices.ProductReadiness.Task3_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task3_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task3_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task4_End_Date:
                if Devices.ProductReadiness.Task4_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task4_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task4_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task5_End_Date:
                if Devices.ProductReadiness.Task5_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task5_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task5_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task6_End_Date:
                if Devices.ProductReadiness.Task6_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task6_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task6_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task7_End_Date:
                if Devices.ProductReadiness.Task7_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task7_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task7_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task8_End_Date:
                if Devices.ProductReadiness.Task8_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task8_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task8_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task9_End_Date:
                if Devices.ProductReadiness.Task9_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task9_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task9_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task10_End_Date:
                if Devices.ProductReadiness.Task10_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task10_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task10_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task11_End_Date:
                if Devices.ProductReadiness.Task11_complete_date:
                    complete += 1 
                elif Devices.ProductReadiness.Task11_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task11_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task12_End_Date:
                if Devices.ProductReadiness.Task12_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task12_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task12_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task13_End_Date:
                if Devices.ProductReadiness.Task13_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task13_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task13_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task14_End_Date:
                if Devices.ProductReadiness.Task14_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task14_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task14_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task15_End_Date:
                if Devices.ProductReadiness.Task15_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task15_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task15_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task16_End_Date:
                if Devices.ProductReadiness.Task16_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task16_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task16_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task17_End_Date:
                if Devices.ProductReadiness.Task17_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task17_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task17_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task18_End_Date:
                if Devices.ProductReadiness.Task18_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task18_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task18_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task19_End_Date:
                if Devices.ProductReadiness.Task19_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task19_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task19_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductReadiness.Task20_End_Date:
                if Devices.ProductReadiness.Task20_complete_date:
                    complete += 1
                elif Devices.ProductReadiness.Task20_alert == True:
                    delay += 1
                elif Devices.ProductReadiness.Task20_warning == True:
                    due += 1
                else:
                    ontime += 1
            Completed.append(complete)
            Delayed.append(delay)
            DueSoon.append(due)
            OnTime.append(ontime)
            complete = 0
            delay = 0
            due = 0
            ontime = 0
            if Devices.VideoContent.Task1_End_Date:
                print ("inside Video Content")
                if Devices.VideoContent.Task1_complete_date is None:
                    complete += 1
                elif Devices.VideoContent.Task1_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task1_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task2_End_Date:
                if Devices.VideoContent.Task2_complete_date is None:
                    complete += 1
                elif Devices.VideoContent.Task2_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task2_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task3_End_Date:
                if Devices.VideoContent.Task3_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task3_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task3_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task4_End_Date:
                if Devices.VideoContent.Task4_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task4_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task4_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task5_End_Date:
                if Devices.VideoContent.Task5_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task5_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task5_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task6_End_Date:
                if Devices.VideoContent.Task6_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task6_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task6_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task7_End_Date:
                if Devices.VideoContent.Task7_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task7_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task7_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task8_End_Date:
                if Devices.VideoContent.Task8_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task8_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task8_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task9_End_Date:
                if Devices.VideoContent.Task9_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task9_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task9_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task10_End_Date:
                if Devices.VideoContent.Task10_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task10_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task10_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task11_End_Date:
                if Devices.VideoContent.Task11_complete_date:
                    complete += 1 
                elif Devices.VideoContent.Task11_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task11_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task12_End_Date:
                if Devices.VideoContent.Task12_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task12_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task12_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task13_End_Date:
                if Devices.VideoContent.Task13_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task13_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task13_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task14_End_Date:
                if Devices.VideoContent.Task14_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task14_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task14_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task15_End_Date:
                if Devices.VideoContent.Task15_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task15_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task15_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task16_End_Date:
                if Devices.VideoContent.Task16_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task16_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task16_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task17_End_Date:
                if Devices.VideoContent.Task17_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task17_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task17_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task18_End_Date:
                if Devices.VideoContent.Task18_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task18_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task18_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task19_End_Date:
                if Devices.VideoContent.Task19_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task19_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task19_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.VideoContent.Task20_End_Date:
                if Devices.VideoContent.Task20_complete_date:
                    complete += 1
                elif Devices.VideoContent.Task20_alert == True:
                    delay += 1
                elif Devices.VideoContent.Task20_warning == True:
                    due += 1
                else:
                    ontime += 1
            Completed.append(complete)
            Delayed.append(delay)
            DueSoon.append(due)
            OnTime.append(ontime)
            complete = 0
            delay = 0
            due = 0
            ontime = 0
            if Devices.DigitalContent.Task1_End_Date:
                if Devices.DigitalContent.Task1_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task1_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task1_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task2_End_Date:
                if Devices.DigitalContent.Task2_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task2_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task2_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task3_End_Date:
                if Devices.DigitalContent.Task3_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task3_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task3_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task4_End_Date:
                if Devices.DigitalContent.Task4_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task4_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task4_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task5_End_Date:
                if Devices.DigitalContent.Task5_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task5_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task5_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task6_End_Date:
                if Devices.DigitalContent.Task6_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task6_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task6_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task7_End_Date:
                if Devices.DigitalContent.Task7_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task7_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task7_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task8_End_Date:
                if Devices.DigitalContent.Task8_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task8_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task8_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task9_End_Date:
                if Devices.DigitalContent.Task9_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task9_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task9_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task10_End_Date:
                if Devices.DigitalContent.Task10_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task10_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task10_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task11_End_Date:
                if Devices.DigitalContent.Task11_complete_date:
                    complete += 1 
                elif Devices.DigitalContent.Task11_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task11_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task12_End_Date:
                if Devices.DigitalContent.Task12_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task12_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task12_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task13_End_Date:
                if Devices.DigitalContent.Task13_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task13_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task13_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task14_End_Date:
                if Devices.DigitalContent.Task14_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task14_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task14_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task15_End_Date:
                if Devices.DigitalContent.Task15_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task15_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task15_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task16_End_Date:
                if Devices.DigitalContent.Task16_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task16_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task16_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task17_End_Date:
                if Devices.DigitalContent.Task17_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task17_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task17_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task18_End_Date:
                if Devices.DigitalContent.Task18_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task18_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task18_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task19_End_Date:
                if Devices.DigitalContent.Task19_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task19_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task19_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.DigitalContent.Task20_End_Date:
                if Devices.DigitalContent.Task20_complete_date:
                    complete += 1
                elif Devices.DigitalContent.Task20_alert == True:
                    delay += 1
                elif Devices.DigitalContent.Task20_warning == True:
                    due += 1
                else:
                    ontime += 1
            Completed.append(complete)
            Delayed.append(delay)
            DueSoon.append(due)
            OnTime.append(ontime)
            complete = 0
            delay = 0
            due = 0
            ontime = 0 
            if Devices.CallCenterTraining.Task1_End_Date:
                if Devices.CallCenterTraining.Task1_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task1_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task1_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task2_End_Date:
                if Devices.CallCenterTraining.Task2_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task2_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task2_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task3_End_Date:
                if Devices.CallCenterTraining.Task3_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task3_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task3_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task4_End_Date:
                if Devices.CallCenterTraining.Task4_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task4_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task4_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task5_End_Date:
                if Devices.CallCenterTraining.Task5_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task5_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task5_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task6_End_Date:
                if Devices.CallCenterTraining.Task6_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task6_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task6_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task7_End_Date:
                if Devices.CallCenterTraining.Task7_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task7_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task7_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task8_End_Date:
                if Devices.CallCenterTraining.Task8_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task8_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task8_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task9_End_Date:
                if Devices.CallCenterTraining.Task9_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task9_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task9_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task10_End_Date:
                if Devices.CallCenterTraining.Task10_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task10_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task10_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task11_End_Date:
                if Devices.CallCenterTraining.Task11_complete_date:
                    complete += 1 
                elif Devices.CallCenterTraining.Task11_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task11_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task12_End_Date:
                if Devices.CallCenterTraining.Task12_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task12_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task12_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task13_End_Date:
                if Devices.CallCenterTraining.Task13_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task13_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task13_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task14_End_Date:
                if Devices.CallCenterTraining.Task14_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task14_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task14_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task15_End_Date:
                if Devices.CallCenterTraining.Task15_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task15_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task15_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task16_End_Date:
                if Devices.CallCenterTraining.Task16_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task16_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task16_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task17_End_Date:
                if Devices.CallCenterTraining.Task17_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task17_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task17_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task18_End_Date:
                if Devices.CallCenterTraining.Task18_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task18_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task18_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task19_End_Date:
                if Devices.CallCenterTraining.Task19_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task19_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task19_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterTraining.Task20_End_Date:
                if Devices.CallCenterTraining.Task20_complete_date:
                    complete += 1
                elif Devices.CallCenterTraining.Task20_alert == True:
                    delay += 1
                elif Devices.CallCenterTraining.Task20_warning == True:
                    due += 1
                else:
                    ontime += 1
            Completed.append(complete)
            Delayed.append(delay)
            DueSoon.append(due)
            OnTime.append(ontime)
            complete = 0
            delay = 0
            due = 0
            ontime = 0 
            if Devices.CallCenterOpertaions.Task1_End_Date:
                if Devices.CallCenterOpertaions.Task1_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task1_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task1_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task2_End_Date:
                if Devices.CallCenterOpertaions.Task2_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task2_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task2_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task3_End_Date:
                if Devices.CallCenterOpertaions.Task3_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task3_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task3_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task4_End_Date:
                if Devices.CallCenterOpertaions.Task4_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task4_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task4_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task5_End_Date:
                if Devices.CallCenterOpertaions.Task5_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task5_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task5_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task6_End_Date:
                if Devices.CallCenterOpertaions.Task6_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task6_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task6_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task7_End_Date:
                if Devices.CallCenterOpertaions.Task7_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task7_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task7_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task8_End_Date:
                if Devices.CallCenterOpertaions.Task8_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task8_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task8_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task9_End_Date:
                if Devices.CallCenterOpertaions.Task9_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task9_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task9_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task10_End_Date:
                if Devices.CallCenterOpertaions.Task10_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task10_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task10_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task11_End_Date:
                if Devices.CallCenterOpertaions.Task11_complete_date:
                    complete += 1 
                elif Devices.CallCenterOpertaions.Task11_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task11_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task12_End_Date:
                if Devices.CallCenterOpertaions.Task12_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task12_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task12_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task13_End_Date:
                if Devices.CallCenterOpertaions.Task13_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task13_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task13_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task14_End_Date:
                if Devices.CallCenterOpertaions.Task14_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task14_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task14_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task15_End_Date:
                if Devices.CallCenterOpertaions.Task15_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task15_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task15_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task16_End_Date:
                if Devices.CallCenterOpertaions.Task16_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task16_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task16_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task17_End_Date:
                if Devices.CallCenterOpertaions.Task17_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task17_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task17_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task18_End_Date:
                if Devices.CallCenterOpertaions.Task18_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task18_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task18_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task19_End_Date:
                if Devices.CallCenterOpertaions.Task19_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task19_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task19_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.CallCenterOpertaions.Task20_End_Date:
                if Devices.CallCenterOpertaions.Task20_complete_date:
                    complete += 1
                elif Devices.CallCenterOpertaions.Task20_alert == True:
                    delay += 1
                elif Devices.CallCenterOpertaions.Task20_warning == True:
                    due += 1
                else:
                    ontime += 1
            Completed.append(complete)
            Delayed.append(delay)
            DueSoon.append(due)
            OnTime.append(ontime)
            complete = 0
            delay = 0
            due = 0
            ontime = 0 
            if Devices.ProductSupport.Task1_End_Date:
                if Devices.ProductSupport.Task1_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task1_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task1_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task2_End_Date:
                if Devices.ProductSupport.Task2_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task2_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task2_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task3_End_Date:
                if Devices.ProductSupport.Task3_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task3_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task3_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task4_End_Date:
                if Devices.ProductSupport.Task4_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task4_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task4_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task5_End_Date:
                if Devices.ProductSupport.Task5_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task5_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task5_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task6_End_Date:
                if Devices.ProductSupport.Task6_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task6_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task6_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task7_End_Date:
                if Devices.ProductSupport.Task7_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task7_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task7_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task8_End_Date:
                if Devices.ProductSupport.Task8_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task8_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task8_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task9_End_Date:
                if Devices.ProductSupport.Task9_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task9_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task9_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task10_End_Date:
                if Devices.ProductSupport.Task10_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task10_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task10_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task11_End_Date:
                if Devices.ProductSupport.Task11_complete_date:
                    complete += 1 
                elif Devices.ProductSupport.Task11_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task11_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task12_End_Date:
                if Devices.ProductSupport.Task12_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task12_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task12_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task13_End_Date:
                if Devices.ProductSupport.Task13_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task13_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task13_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task14_End_Date:
                if Devices.ProductSupport.Task14_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task14_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task14_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task15_End_Date:
                if Devices.ProductSupport.Task15_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task15_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task15_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task16_End_Date:
                if Devices.ProductSupport.Task16_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task16_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task16_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task17_End_Date:
                if Devices.ProductSupport.Task17_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task17_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task17_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task18_End_Date:
                if Devices.ProductSupport.Task18_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task18_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task18_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task19_End_Date:
                if Devices.ProductSupport.Task19_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task19_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task19_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ProductSupport.Task20_End_Date:
                if Devices.ProductSupport.Task20_complete_date:
                    complete += 1
                elif Devices.ProductSupport.Task20_alert == True:
                    delay += 1
                elif Devices.ProductSupport.Task20_warning == True:
                    due += 1
                else:
                    ontime += 1
            Completed.append(complete)
            Delayed.append(delay)
            DueSoon.append(due)
            OnTime.append(ontime)
            complete = 0
            delay = 0
            due = 0
            ontime = 0 
            if Devices.Warehouse.Task1_End_Date:
                if Devices.Warehouse.Task1_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task1_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task1_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task2_End_Date:
                if Devices.Warehouse.Task2_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task2_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task2_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task3_End_Date:
                if Devices.Warehouse.Task3_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task3_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task3_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task4_End_Date:
                if Devices.Warehouse.Task4_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task4_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task4_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task5_End_Date:
                if Devices.Warehouse.Task5_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task5_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task5_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task6_End_Date:
                if Devices.Warehouse.Task6_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task6_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task6_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task7_End_Date:
                if Devices.Warehouse.Task7_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task7_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task7_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task8_End_Date:
                if Devices.Warehouse.Task8_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task8_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task8_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task9_End_Date:
                if Devices.Warehouse.Task9_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task9_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task9_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task10_End_Date:
                if Devices.Warehouse.Task10_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task10_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task10_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task11_End_Date:
                if Devices.Warehouse.Task11_complete_date:
                    complete += 1 
                elif Devices.Warehouse.Task11_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task11_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task12_End_Date:
                if Devices.Warehouse.Task12_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task12_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task12_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task13_End_Date:
                if Devices.Warehouse.Task13_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task13_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task13_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task14_End_Date:
                if Devices.Warehouse.Task14_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task14_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task14_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task15_End_Date:
                if Devices.Warehouse.Task15_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task15_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task15_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task16_End_Date:
                if Devices.Warehouse.Task16_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task16_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task16_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task17_End_Date:
                if Devices.Warehouse.Task17_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task17_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task17_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task18_End_Date:
                if Devices.Warehouse.Task18_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task18_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task18_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task19_End_Date:
                if Devices.Warehouse.Task19_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task19_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task19_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Warehouse.Task20_End_Date:
                if Devices.Warehouse.Task20_complete_date:
                    complete += 1
                elif Devices.Warehouse.Task20_alert == True:
                    delay += 1
                elif Devices.Warehouse.Task20_warning == True:
                    due += 1
                else:
                    ontime += 1
            Completed.append(complete)
            Delayed.append(delay)
            DueSoon.append(due)
            OnTime.append(ontime)
            complete = 0
            delay = 0
            due = 0
            ontime = 0 
            if Devices.FieldService.Task1_End_Date:
                if Devices.FieldService.Task1_complete_date:
                    complete += 1
                elif Devices.FieldService.Task1_alert == True:
                    delay += 1
                elif Devices.FieldService.Task1_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task2_End_Date:
                if Devices.FieldService.Task2_complete_date:
                    complete += 1
                elif Devices.FieldService.Task2_alert == True:
                    delay += 1
                elif Devices.FieldService.Task2_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task3_End_Date:
                if Devices.FieldService.Task3_complete_date:
                    complete += 1
                elif Devices.FieldService.Task3_alert == True:
                    delay += 1
                elif Devices.FieldService.Task3_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task4_End_Date:
                if Devices.FieldService.Task4_complete_date:
                    complete += 1
                elif Devices.FieldService.Task4_alert == True:
                    delay += 1
                elif Devices.FieldService.Task4_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task5_End_Date:
                if Devices.FieldService.Task5_complete_date:
                    complete += 1
                elif Devices.FieldService.Task5_alert == True:
                    delay += 1
                elif Devices.FieldService.Task5_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task6_End_Date:
                if Devices.FieldService.Task6_complete_date:
                    complete += 1
                elif Devices.FieldService.Task6_alert == True:
                    delay += 1
                elif Devices.FieldService.Task6_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task7_End_Date:
                if Devices.FieldService.Task7_complete_date:
                    complete += 1
                elif Devices.FieldService.Task7_alert == True:
                    delay += 1
                elif Devices.FieldService.Task7_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task8_End_Date:
                if Devices.FieldService.Task8_complete_date:
                    complete += 1
                elif Devices.FieldService.Task8_alert == True:
                    delay += 1
                elif Devices.FieldService.Task8_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task9_End_Date:
                if Devices.FieldService.Task9_complete_date:
                    complete += 1
                elif Devices.FieldService.Task9_alert == True:
                    delay += 1
                elif Devices.FieldService.Task9_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task10_End_Date:
                if Devices.FieldService.Task10_complete_date:
                    complete += 1
                elif Devices.FieldService.Task10_alert == True:
                    delay += 1
                elif Devices.FieldService.Task10_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task11_End_Date:
                if Devices.FieldService.Task11_complete_date:
                    complete += 1 
                elif Devices.FieldService.Task11_alert == True:
                    delay += 1
                elif Devices.FieldService.Task11_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task12_End_Date:
                if Devices.FieldService.Task12_complete_date:
                    complete += 1
                elif Devices.FieldService.Task12_alert == True:
                    delay += 1
                elif Devices.FieldService.Task12_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task13_End_Date:
                if Devices.FieldService.Task13_complete_date:
                    complete += 1
                elif Devices.FieldService.Task13_alert == True:
                    delay += 1
                elif Devices.FieldService.Task13_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task14_End_Date:
                if Devices.FieldService.Task14_complete_date:
                    complete += 1
                elif Devices.FieldService.Task14_alert == True:
                    delay += 1
                elif Devices.FieldService.Task14_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task15_End_Date:
                if Devices.FieldService.Task15_complete_date:
                    complete += 1
                elif Devices.FieldService.Task15_alert == True:
                    delay += 1
                elif Devices.FieldService.Task15_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task16_End_Date:
                if Devices.FieldService.Task16_complete_date:
                    complete += 1
                elif Devices.FieldService.Task16_alert == True:
                    delay += 1
                elif Devices.FieldService.Task16_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task17_End_Date:
                if Devices.FieldService.Task17_complete_date:
                    complete += 1
                elif Devices.FieldService.Task17_alert == True:
                    delay += 1
                elif Devices.FieldService.Task17_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task18_End_Date:
                if Devices.FieldService.Task18_complete_date:
                    complete += 1
                elif Devices.FieldService.Task18_alert == True:
                    delay += 1
                elif Devices.FieldService.Task18_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task19_End_Date:
                if Devices.FieldService.Task19_complete_date:
                    complete += 1
                elif Devices.FieldService.Task19_alert == True:
                    delay += 1
                elif Devices.FieldService.Task19_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.FieldService.Task20_End_Date:
                if Devices.FieldService.Task20_complete_date:
                    complete += 1
                elif Devices.FieldService.Task20_alert == True:
                    delay += 1
                elif Devices.FieldService.Task20_warning == True:
                    due += 1
                else:
                    ontime += 1
            Completed.append(complete)
            Delayed.append(delay)
            DueSoon.append(due)
            OnTime.append(ontime)
            complete = 0
            delay = 0
            due = 0
            ontime = 0 
            if Devices.TechSupport.Task1_End_Date:
                if Devices.TechSupport.Task1_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task1_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task1_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task2_End_Date:
                if Devices.TechSupport.Task2_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task2_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task2_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task3_End_Date:
                if Devices.TechSupport.Task3_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task3_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task3_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task4_End_Date:
                if Devices.TechSupport.Task4_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task4_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task4_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task5_End_Date:
                if Devices.TechSupport.Task5_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task5_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task5_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task6_End_Date:
                if Devices.TechSupport.Task6_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task6_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task6_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task7_End_Date:
                if Devices.TechSupport.Task7_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task7_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task7_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task8_End_Date:
                if Devices.TechSupport.Task8_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task8_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task8_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task9_End_Date:
                if Devices.TechSupport.Task9_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task9_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task9_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task10_End_Date:
                if Devices.TechSupport.Task10_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task10_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task10_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task11_End_Date:
                if Devices.TechSupport.Task11_complete_date:
                    complete += 1 
                elif Devices.TechSupport.Task11_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task11_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task12_End_Date:
                if Devices.TechSupport.Task12_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task12_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task12_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task13_End_Date:
                if Devices.TechSupport.Task13_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task13_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task13_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task14_End_Date:
                if Devices.TechSupport.Task14_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task14_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task14_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task15_End_Date:
                if Devices.TechSupport.Task15_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task15_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task15_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task16_End_Date:
                if Devices.TechSupport.Task16_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task16_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task16_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task17_End_Date:
                if Devices.TechSupport.Task17_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task17_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task17_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task18_End_Date:
                if Devices.TechSupport.Task18_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task18_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task18_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task19_End_Date:
                if Devices.TechSupport.Task19_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task19_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task19_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.TechSupport.Task20_End_Date:
                if Devices.TechSupport.Task20_complete_date:
                    complete += 1
                elif Devices.TechSupport.Task20_alert == True:
                    delay += 1
                elif Devices.TechSupport.Task20_warning == True:
                    due += 1
                else:
                    ontime += 1
            Completed.append(complete)
            Delayed.append(delay)
            DueSoon.append(due)
            OnTime.append(ontime)
            complete = 0
            delay = 0
            due = 0
            ontime = 0 
            if Devices.ServiceMarketing.Task1_End_Date:
                if Devices.ServiceMarketing.Task1_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task1_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task1_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task2_End_Date:
                if Devices.ServiceMarketing.Task2_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task2_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task2_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task3_End_Date:
                if Devices.ServiceMarketing.Task3_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task3_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task3_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task4_End_Date:
                if Devices.ServiceMarketing.Task4_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task4_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task4_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task5_End_Date:
                if Devices.ServiceMarketing.Task5_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task5_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task5_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task6_End_Date:
                if Devices.ServiceMarketing.Task6_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task6_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task6_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task7_End_Date:
                if Devices.ServiceMarketing.Task7_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task7_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task7_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task8_End_Date:
                if Devices.ServiceMarketing.Task8_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task8_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task8_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task9_End_Date:
                if Devices.ServiceMarketing.Task9_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task9_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task9_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task10_End_Date:
                if Devices.ServiceMarketing.Task10_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task10_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task10_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task11_End_Date:
                if Devices.ServiceMarketing.Task11_complete_date:
                    complete += 1 
                elif Devices.ServiceMarketing.Task11_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task11_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task12_End_Date:
                if Devices.ServiceMarketing.Task12_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task12_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task12_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task13_End_Date:
                if Devices.ServiceMarketing.Task13_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task13_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task13_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task14_End_Date:
                if Devices.ServiceMarketing.Task14_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task14_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task14_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task15_End_Date:
                if Devices.ServiceMarketing.Task15_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task15_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task15_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task16_End_Date:
                if Devices.ServiceMarketing.Task16_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task16_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task16_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task17_End_Date:
                if Devices.ServiceMarketing.Task17_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task17_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task17_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task18_End_Date:
                if Devices.ServiceMarketing.Task18_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task18_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task18_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task19_End_Date:
                if Devices.ServiceMarketing.Task19_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task19_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task19_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceMarketing.Task20_End_Date:
                if Devices.ServiceMarketing.Task20_complete_date:
                    complete += 1
                elif Devices.ServiceMarketing.Task20_alert == True:
                    delay += 1
                elif Devices.ServiceMarketing.Task20_warning == True:
                    due += 1
                else:
                    ontime += 1
            Completed.append(complete)
            Delayed.append(delay)
            DueSoon.append(due)
            OnTime.append(ontime)
            complete = 0
            delay = 0
            due = 0
            ontime = 0 
            if Devices.ServiceTraining.Task1_End_Date:
                if Devices.ServiceTraining.Task1_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task1_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task1_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task2_End_Date:
                if Devices.ServiceTraining.Task2_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task2_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task2_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task3_End_Date:
                if Devices.ServiceTraining.Task3_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task3_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task3_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task4_End_Date:
                if Devices.ServiceTraining.Task4_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task4_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task4_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task5_End_Date:
                if Devices.ServiceTraining.Task5_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task5_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task5_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task6_End_Date:
                if Devices.ServiceTraining.Task6_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task6_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task6_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task7_End_Date:
                if Devices.ServiceTraining.Task7_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task7_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task7_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task8_End_Date:
                if Devices.ServiceTraining.Task8_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task8_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task8_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task9_End_Date:
                if Devices.ServiceTraining.Task9_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task9_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task9_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task10_End_Date:
                if Devices.ServiceTraining.Task10_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task10_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task10_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task11_End_Date:
                if Devices.ServiceTraining.Task11_complete_date:
                    complete += 1 
                elif Devices.ServiceTraining.Task11_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task11_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task12_End_Date:
                if Devices.ServiceTraining.Task12_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task12_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task12_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task13_End_Date:
                if Devices.ServiceTraining.Task13_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task13_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task13_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task14_End_Date:
                if Devices.ServiceTraining.Task14_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task14_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task14_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task15_End_Date:
                if Devices.ServiceTraining.Task15_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task15_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task15_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task16_End_Date:
                if Devices.ServiceTraining.Task16_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task16_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task16_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task17_End_Date:
                if Devices.ServiceTraining.Task17_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task17_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task17_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task18_End_Date:
                if Devices.ServiceTraining.Task18_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task18_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task18_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task19_End_Date:
                if Devices.ServiceTraining.Task19_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task19_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task19_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.ServiceTraining.Task20_End_Date:
                if Devices.ServiceTraining.Task20_complete_date:
                    complete += 1
                elif Devices.ServiceTraining.Task20_alert == True:
                    delay += 1
                elif Devices.ServiceTraining.Task20_warning == True:
                    due += 1
                else:
                    ontime += 1
            Completed.append(complete)
            Delayed.append(delay)
            DueSoon.append(due)
            OnTime.append(ontime)
            complete = 0
            delay = 0
            due = 0
            ontime = 0 
            if Devices.Parts.Task1_End_Date:
                if Devices.Parts.Task1_complete_date:
                    complete += 1
                elif Devices.Parts.Task1_alert == True:
                    delay += 1
                elif Devices.Parts.Task1_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task2_End_Date:
                if Devices.Parts.Task2_complete_date:
                    complete += 1
                elif Devices.Parts.Task2_alert == True:
                    delay += 1
                elif Devices.Parts.Task2_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task3_End_Date:
                if Devices.Parts.Task3_complete_date:
                    complete += 1
                elif Devices.Parts.Task3_alert == True:
                    delay += 1
                elif Devices.Parts.Task3_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task4_End_Date:
                if Devices.Parts.Task4_complete_date:
                    complete += 1
                elif Devices.Parts.Task4_alert == True:
                    delay += 1
                elif Devices.Parts.Task4_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task5_End_Date:
                if Devices.Parts.Task5_complete_date:
                    complete += 1
                elif Devices.Parts.Task5_alert == True:
                    delay += 1
                elif Devices.Parts.Task5_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task6_End_Date:
                if Devices.Parts.Task6_complete_date:
                    complete += 1
                elif Devices.Parts.Task6_alert == True:
                    delay += 1
                elif Devices.Parts.Task6_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task7_End_Date:
                if Devices.Parts.Task7_complete_date:
                    complete += 1
                elif Devices.Parts.Task7_alert == True:
                    delay += 1
                elif Devices.Parts.Task7_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task8_End_Date:
                if Devices.Parts.Task8_complete_date:
                    complete += 1
                elif Devices.Parts.Task8_alert == True:
                    delay += 1
                elif Devices.Parts.Task8_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task9_End_Date:
                if Devices.Parts.Task9_complete_date:
                    complete += 1
                elif Devices.Parts.Task9_alert == True:
                    delay += 1
                elif Devices.Parts.Task9_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task10_End_Date:
                if Devices.Parts.Task10_complete_date:
                    complete += 1
                elif Devices.Parts.Task10_alert == True:
                    delay += 1
                elif Devices.Parts.Task10_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task11_End_Date:
                if Devices.Parts.Task11_complete_date:
                    complete += 1 
                elif Devices.Parts.Task11_alert == True:
                    delay += 1
                elif Devices.Parts.Task11_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task12_End_Date:
                if Devices.Parts.Task12_complete_date:
                    complete += 1
                elif Devices.Parts.Task12_alert == True:
                    delay += 1
                elif Devices.Parts.Task12_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task13_End_Date:
                if Devices.Parts.Task13_complete_date:
                    complete += 1
                elif Devices.Parts.Task13_alert == True:
                    delay += 1
                elif Devices.Parts.Task13_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task14_End_Date:
                if Devices.Parts.Task14_complete_date:
                    complete += 1
                elif Devices.Parts.Task14_alert == True:
                    delay += 1
                elif Devices.Parts.Task14_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task15_End_Date:
                if Devices.Parts.Task15_complete_date:
                    complete += 1
                elif Devices.Parts.Task15_alert == True:
                    delay += 1
                elif Devices.Parts.Task15_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task16_End_Date:
                if Devices.Parts.Task16_complete_date:
                    complete += 1
                elif Devices.Parts.Task16_alert == True:
                    delay += 1
                elif Devices.Parts.Task16_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task17_End_Date:
                if Devices.Parts.Task17_complete_date:
                    complete += 1
                elif Devices.Parts.Task17_alert == True:
                    delay += 1
                elif Devices.Parts.Task17_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task18_End_Date:
                if Devices.Parts.Task18_complete_date:
                    complete += 1
                elif Devices.Parts.Task18_alert == True:
                    delay += 1
                elif Devices.Parts.Task18_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task19_End_Date:
                if Devices.Parts.Task19_complete_date:
                    complete += 1
                elif Devices.Parts.Task19_alert == True:
                    delay += 1
                elif Devices.Parts.Task19_warning == True:
                    due += 1
                else:
                    ontime += 1
            if Devices.Parts.Task20_End_Date:
                if Devices.Parts.Task20_complete_date:
                    complete += 1
                elif Devices.Parts.Task20_alert == True:
                    delay += 1
                elif Devices.Parts.Task20_warning == True:
                    due += 1
                else:
                    ontime += 1
            Completed.append(complete)
            Delayed.append(delay)
            DueSoon.append(due)
            OnTime.append(ontime)

            return zip(Completed,Delayed,DueSoon,OnTime)

def activeTasksPR(device):
    ActiveTasks = 0
    if device.ProductReadiness.Task1_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task2_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task3_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task4_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task5_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task6_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task7_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task8_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task9_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task10_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task11_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task12_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task13_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task14_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task15_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task16_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task17_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task18_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task19_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductReadiness.Task20_Name:
        ActiveTasks = ActiveTasks + 1
    return ActiveTasks

def activeTasksDC(device):
    ActiveTasks = 0
    if device.DigitalContent.Task1_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task2_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task3_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task4_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task5_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task6_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task7_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task8_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task9_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task10_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task11_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task12_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task13_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task14_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task15_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task16_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task17_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task18_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task19_Name:
        ActiveTasks = ActiveTasks + 1
    if device.DigitalContent.Task20_Name:
        ActiveTasks = ActiveTasks + 1
    return ActiveTasks

def activeTasksVC(device):
    ActiveTasks = 0
    if device.VideoContent.Task1_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task2_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task3_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task4_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task5_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task6_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task7_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task8_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task9_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task10_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task11_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task12_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task13_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task14_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task15_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task16_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task17_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task18_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task19_Name:
        ActiveTasks = ActiveTasks + 1
    if device.VideoContent.Task20_Name:
        ActiveTasks = ActiveTasks + 1
    return ActiveTasks

def activeTasksCCT(device):
    ActiveTasks = 0
    if device.CallCenterTraining.Task1_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task2_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task3_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task4_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task5_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task6_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task7_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task8_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task9_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task10_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task11_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task12_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task13_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task14_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task15_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task16_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task17_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task18_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task19_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterTraining.Task20_Name:
        ActiveTasks = ActiveTasks + 1
    return ActiveTasks

def activeTasksCCO(device):
    ActiveTasks = 0
    if device.CallCenterOpertaions.Task1_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task2_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task3_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task4_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task5_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task6_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task7_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task8_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task9_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task10_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task11_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task12_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task13_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task14_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task15_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task16_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task17_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task18_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task19_Name:
        ActiveTasks = ActiveTasks + 1
    if device.CallCenterOpertaions.Task20_Name:
        ActiveTasks = ActiveTasks + 1
    return ActiveTasks

def activeTasksPS(device):
    ActiveTasks = 0
    if device.ProductSupport.Task1_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task2_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task3_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task4_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task5_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task6_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task7_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task8_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task9_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task10_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task11_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task12_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task13_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task14_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task15_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task16_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task17_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task18_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task19_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ProductSupport.Task20_Name:
        ActiveTasks = ActiveTasks + 1
    return ActiveTasks

def activeTasksW(device):
    ActiveTasks = 0
    if device.Warehouse.Task1_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task2_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task3_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task4_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task5_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task6_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task7_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task8_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task9_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task10_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task11_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task12_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task13_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task14_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task15_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task16_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task17_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task18_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task19_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Warehouse.Task20_Name:
        ActiveTasks = ActiveTasks + 1
    return ActiveTasks

def activeTasksFS(device):
    ActiveTasks = 0
    if device.FieldService.Task1_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task2_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task3_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task4_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task5_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task6_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task7_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task8_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task9_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task10_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task11_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task12_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task13_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task14_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task15_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task16_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task17_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task18_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task19_Name:
        ActiveTasks = ActiveTasks + 1
    if device.FieldService.Task20_Name:
        ActiveTasks = ActiveTasks + 1
    return ActiveTasks

def activeTasksTS(device):
    ActiveTasks = 0
    if device.TechSupport.Task1_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task2_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task3_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task4_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task5_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task6_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task7_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task8_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task9_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task10_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task11_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task12_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task13_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task14_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task15_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task16_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task17_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task18_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task19_Name:
        ActiveTasks = ActiveTasks + 1
    if device.TechSupport.Task20_Name:
        ActiveTasks = ActiveTasks + 1
    return ActiveTasks

def activeTasksSM(device):
    ActiveTasks = 0
    if device.ServiceMarketing.Task1_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task2_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task3_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task4_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task5_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task6_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task7_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task8_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task9_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task10_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task11_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task12_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task13_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task14_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task15_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task16_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task17_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task18_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task19_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceMarketing.Task20_Name:
        ActiveTasks = ActiveTasks + 1
    return ActiveTasks

def activeTasksST(device):
    ActiveTasks = 0
    if device.ServiceTraining.Task1_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task2_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task3_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task4_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task5_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task6_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task7_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task8_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task9_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task10_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task11_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task12_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task13_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task14_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task15_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task16_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task17_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task18_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task19_Name:
        ActiveTasks = ActiveTasks + 1
    if device.ServiceTraining.Task20_Name:
        ActiveTasks = ActiveTasks + 1
    return ActiveTasks

def activeTasksP(device):
    ActiveTasks = 0
    if device.Parts.Task1_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task2_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task3_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task4_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task5_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task6_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task7_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task8_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task9_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task10_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task11_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task12_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task13_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task14_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task15_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task16_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task17_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task18_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task19_Name:
        ActiveTasks = ActiveTasks + 1
    if device.Parts.Task20_Name:
        ActiveTasks = ActiveTasks + 1
    return ActiveTasks

def update_Warning():
    print ("I am here")
    z = Device.objects.all()

    for device in z:
      if device.Archive==False:
        # device = Device.objects.get(pk=i)
        y = activeTasksPR(device)

        x = 0
        if device.ProductReadiness.Task1_complete_date:
            x = x + 1
        if device.ProductReadiness.Task2_complete_date:
            x = x + 1
        if device.ProductReadiness.Task3_complete_date:
            x = x + 1
        if device.ProductReadiness.Task4_complete_date:
            x = x + 1
        if device.ProductReadiness.Task5_complete_date:
            x = x + 1
        if device.ProductReadiness.Task6_complete_date:
            x = x + 1
        if device.ProductReadiness.Task7_complete_date:
            x = x + 1
        if device.ProductReadiness.Task8_complete_date:
            x = x + 1
        if device.ProductReadiness.Task9_complete_date:
            x = x + 1
        if device.ProductReadiness.Task10_complete_date:
            x = x + 1
        if device.ProductReadiness.Task11_complete_date:
            x = x + 1
        if device.ProductReadiness.Task12_complete_date:
            x = x + 1
        if device.ProductReadiness.Task13_complete_date:
            x = x + 1
        if device.ProductReadiness.Task14_complete_date:
            x = x + 1
        if device.ProductReadiness.Task15_complete_date:
            x = x + 1
        if device.ProductReadiness.Task16_complete_date:
            x = x + 1
        if device.ProductReadiness.Task17_complete_date:
            x = x + 1
        if device.ProductReadiness.Task18_complete_date:
            x = x + 1
        if device.ProductReadiness.Task19_complete_date:
            x = x + 1
        if device.ProductReadiness.Task20_complete_date:
            x = x + 1
        percent = x / y * 100
        print(percent)
        device.ProductReadiness.completed = int(percent)

        device.ProductReadiness.Task1_alert = False
        device.ProductReadiness.Task1_warning = False
        device.ProductReadiness.Status = 'On_Time'
        device.ProductReadiness.Task2_alert = False
        device.ProductReadiness.Task2_warning = False

        device.ProductReadiness.Task3_alert = False
        device.ProductReadiness.Task3_warning = False

        device.ProductReadiness.Task4_alert = False
        device.ProductReadiness.Task4_warning = False

        device.ProductReadiness.Task5_alert = False
        device.ProductReadiness.Task5_warning = False

        device.ProductReadiness.Task6_alert = False
        device.ProductReadiness.Task6_warning = False

        device.ProductReadiness.Task7_alert = False
        device.ProductReadiness.Task7_warning = False

        device.ProductReadiness.Task8_alert = False
        device.ProductReadiness.Task8_warning = False

        device.ProductReadiness.Task9_alert = False
        device.ProductReadiness.Task9_warning = False

        device.ProductReadiness.Task10_alert = False
        device.ProductReadiness.Task10_warning = False

        device.ProductReadiness.Task11_alert = False
        device.ProductReadiness.Task11_warning = False

        device.ProductReadiness.Task12_alert = False
        device.ProductReadiness.Task12_warning = False

        device.ProductReadiness.Task13_alert = False
        device.ProductReadiness.Task13_warning = False

        device.ProductReadiness.Task14_alert = False
        device.ProductReadiness.Task14_warning = False

        device.ProductReadiness.Task15_alert = False
        device.ProductReadiness.Task15_warning = False

        device.ProductReadiness.Task16_alert = False
        device.ProductReadiness.Task16_warning = False

        device.ProductReadiness.Task17_alert = False
        device.ProductReadiness.Task17_warning = False

        device.ProductReadiness.Task18_alert = False
        device.ProductReadiness.Task18_warning = False

        device.ProductReadiness.Task19_alert = False
        device.ProductReadiness.Task19_warning = False

        device.ProductReadiness.Task20_alert = False
        device.ProductReadiness.Task20_warning = False


        # alerting logic
        today = datetime.date.today()
        if device.ProductReadiness.Task1_End_Date:
            Task1_delta = device.ProductReadiness.Task1_End_Date - today
        else:
            Task1_delta = None
        if device.ProductReadiness.Task2_End_Date:
            Task2_delta = device.ProductReadiness.Task2_End_Date - today
        else:
            Task2_delta = None
        if device.ProductReadiness.Task3_End_Date:
            Task3_delta = device.ProductReadiness.Task3_End_Date - today
        else:
            Task3_delta = None
        if device.ProductReadiness.Task4_End_Date:
            Task4_delta = device.ProductReadiness.Task4_End_Date - today
        else:
            Task4_delta = None
        if device.ProductReadiness.Task5_End_Date:
            Task5_delta = device.ProductReadiness.Task5_End_Date - today
        else:
            Task5_delta = None
        if device.ProductReadiness.Task6_End_Date:
            Task6_delta = device.ProductReadiness.Task6_End_Date - today
        else:
            Task6_delta = None
        if device.ProductReadiness.Task7_End_Date:
            Task7_delta = device.ProductReadiness.Task7_End_Date - today
        else:
            Task7_delta = None
        if device.ProductReadiness.Task8_End_Date:
            Task8_delta = device.ProductReadiness.Task8_End_Date - today
        else:
            Task8_delta = None
        if device.ProductReadiness.Task9_End_Date:
            Task9_delta = device.ProductReadiness.Task9_End_Date - today
        else:
            Task9_delta = None
        if device.ProductReadiness.Task10_End_Date:
            Task10_delta = device.ProductReadiness.Task10_End_Date - today
        else:
            Task10_delta = None
        if device.ProductReadiness.Task11_End_Date:
            Task11_delta = device.ProductReadiness.Task11_End_Date - today
        else:
            Task11_delta = None
        if device.ProductReadiness.Task12_End_Date:
            Task12_delta = device.ProductReadiness.Task12_End_Date - today
        else:
            Task12_delta = None
        if device.ProductReadiness.Task13_End_Date:
            Task13_delta = device.ProductReadiness.Task13_End_Date - today
        else:
            Task13_delta = None
        if device.ProductReadiness.Task14_End_Date:
            Task14_delta = device.ProductReadiness.Task14_End_Date - today
        else:
            Task14_delta = None
        if device.ProductReadiness.Task15_End_Date:
            Task15_delta = device.ProductReadiness.Task15_End_Date - today
        else:
            Task15_delta = None
        if device.ProductReadiness.Task16_End_Date:
            Task16_delta = device.ProductReadiness.Task16_End_Date - today
        else:
            Task16_delta = None
        if device.ProductReadiness.Task17_End_Date:
            Task17_delta = device.ProductReadiness.Task17_End_Date - today
        else:
            Task17_delta = None
        if device.ProductReadiness.Task18_End_Date:
            Task18_delta = device.ProductReadiness.Task18_End_Date - today
        else:
            Task18_delta = None
        if device.ProductReadiness.Task19_End_Date:
            Task19_delta = device.ProductReadiness.Task19_End_Date - today
        else:
            Task19_delta = None
        if device.ProductReadiness.Task20_End_Date:
            Task20_delta = device.ProductReadiness.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not device.ProductReadiness.Task1_complete_date:
            device.ProductReadiness.Task1_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not device.ProductReadiness.Task2_complete_date:
            device.ProductReadiness.Task2_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not device.ProductReadiness.Task3_complete_date:
            device.ProductReadiness.Task3_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not device.ProductReadiness.Task4_complete_date:
            device.ProductReadiness.Task4_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not device.ProductReadiness.Task5_complete_date:
            device.ProductReadiness.Task5_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not device.ProductReadiness.Task6_complete_date:
            device.ProductReadiness.Task6_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not device.ProductReadiness.Task7_complete_date:
            device.ProductReadiness.Task7_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not device.ProductReadiness.Task8_complete_date:
            device.ProductReadiness.Task8_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not device.ProductReadiness.Task9_complete_date:
            device.ProductReadiness.Task9_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not device.ProductReadiness.Task10_complete_date:
            device.ProductReadiness.Task10_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not device.ProductReadiness.Task11_complete_date:
            device.ProductReadiness.Task11_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not device.ProductReadiness.Task12_complete_date:
            device.ProductReadiness.Task12_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not device.ProductReadiness.Task13_complete_date:
            device.ProductReadiness.Task13_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not device.ProductReadiness.Task14_complete_date:
            device.ProductReadiness.Task14_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not device.ProductReadiness.Task15_complete_date:
            device.ProductReadiness.Task15_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not device.ProductReadiness.Task16_complete_date:
            device.ProductReadiness.Task16_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not device.ProductReadiness.Task17_complete_date:
            device.ProductReadiness.Task17_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not device.ProductReadiness.Task18_complete_date:
            device.ProductReadiness.Task18_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not device.ProductReadiness.Task19_complete_date:
            device.ProductReadiness.Task19_warning = True
            device.ProductReadiness.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(
                device.ProductReadiness.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not device.ProductReadiness.Task20_complete_date:
            device.ProductReadiness.Task20_warning = True
            device.ProductReadiness.Status = 'At Risk'

        if device.ProductReadiness.Task1_End_Date and Task1_delta < timedelta(
                0) and not device.ProductReadiness.Task1_complete_date:
            device.ProductReadiness.Task1_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task2_End_Date and Task2_delta < timedelta(
                0) and not device.ProductReadiness.Task2_complete_date:
            device.ProductReadiness.Task2_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task3_End_Date and Task3_delta < timedelta(
                0) and not device.ProductReadiness.Task3_complete_date:
            device.ProductReadiness.Task3_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task4_End_Date and Task4_delta < timedelta(
                0) and not device.ProductReadiness.Task4_complete_date:
            device.ProductReadiness.Task4_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task5_End_Date and Task5_delta < timedelta(
                0) and not device.ProductReadiness.Task5_complete_date:
            device.ProductReadiness.Task5_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task6_End_Date and Task6_delta < timedelta(
                0) and not device.ProductReadiness.Task6_complete_date:
            device.ProductReadiness.Task6_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task7_End_Date and Task7_delta < timedelta(
                0) and not device.ProductReadiness.Task7_complete_date:
            device.ProductReadiness.Task7_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task8_End_Date and Task8_delta < timedelta(
                0) and not device.ProductReadiness.Task8_complete_date:
            device.ProductReadiness.Task8_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task9_End_Date and Task9_delta < timedelta(
                0) and not device.ProductReadiness.Task9_complete_date:
            device.ProductReadiness.Task9_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task10_End_Date and Task10_delta < timedelta(
                0) and not device.ProductReadiness.Task10_complete_date:
            device.ProductReadiness.Task10_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task11_End_Date and Task11_delta < timedelta(
                0) and not device.ProductReadiness.Task11_complete_date:
            device.ProductReadiness.Task11_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task12_End_Date and Task12_delta < timedelta(
                0) and not device.ProductReadiness.Task12_complete_date:
            device.ProductReadiness.Task12_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task13_End_Date and Task13_delta < timedelta(
                0) and not device.ProductReadiness.Task13_complete_date:
            device.ProductReadiness.Task13_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task14_End_Date and Task14_delta < timedelta(
                0) and not device.ProductReadiness.Task14_complete_date:
            device.ProductReadiness.Task14_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task15_End_Date and Task15_delta < timedelta(
                0) and not device.ProductReadiness.Task15_complete_date:
            device.ProductReadiness.Task15_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task16_End_Date and Task16_delta < timedelta(
                0) and not device.ProductReadiness.Task16_complete_date:
            device.ProductReadiness.Task16_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task17_End_Date and Task17_delta < timedelta(
                0) and not device.ProductReadiness.Task17_complete_date:
            device.ProductReadiness.Task17_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task18_End_Date and Task18_delta < timedelta(
                0) and not device.ProductReadiness.Task18_complete_date:
            device.ProductReadiness.Task18_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task19_End_Date and Task19_delta < timedelta(
                0) and not device.ProductReadiness.Task19_complete_date:
            device.ProductReadiness.Task19_alert = True
            device.ProductReadiness.Status = 'Delayed'
        if device.ProductReadiness.Task20_End_Date and Task20_delta < timedelta(
                0) and not device.ProductReadiness.Task20_complete_date:
            device.ProductReadiness.Task20_alert = True
            device.ProductReadiness.Status = 'Delayed'

        device.ProductReadiness.save()

        device.DigitalContent.Task1_alert = False
        device.DigitalContent.Task1_warning = False
        device.DigitalContent.Status = 'On_Time'

        device.DigitalContent.Task2_alert = False
        device.DigitalContent.Task2_warning = False

        device.DigitalContent.Task3_alert = False
        device.DigitalContent.Task3_warning = False

        device.DigitalContent.Task4_alert = False
        device.DigitalContent.Task4_warning = False

        device.DigitalContent.Task5_alert = False
        device.DigitalContent.Task5_warning = False

        device.DigitalContent.Task6_alert = False
        device.DigitalContent.Task6_warning = False

        device.DigitalContent.Task7_alert = False
        device.DigitalContent.Task7_warning = False

        device.DigitalContent.Task8_alert = False
        device.DigitalContent.Task8_warning = False

        device.DigitalContent.Task9_alert = False
        device.DigitalContent.Task9_warning = False

        device.DigitalContent.Task10_alert = False
        device.DigitalContent.Task10_warning = False

        device.DigitalContent.Task11_alert = False
        device.DigitalContent.Task11_warning = False

        device.DigitalContent.Task12_alert = False
        device.DigitalContent.Task12_warning = False

        device.DigitalContent.Task13_alert = False
        device.DigitalContent.Task13_warning = False

        device.DigitalContent.Task14_alert = False
        device.DigitalContent.Task14_warning = False

        device.DigitalContent.Task15_alert = False
        device.DigitalContent.Task15_warning = False

        device.DigitalContent.Task16_alert = False
        device.DigitalContent.Task16_warning = False

        device.DigitalContent.Task17_alert = False
        device.DigitalContent.Task17_warning = False

        device.DigitalContent.Task18_alert = False
        device.DigitalContent.Task18_warning = False

        device.DigitalContent.Task19_alert = False
        device.DigitalContent.Task19_warning = False

        device.DigitalContent.Task20_alert = False
        device.DigitalContent.Task20_warning = False

        y = activeTasksDC(device)

        x = 0
        if device.DigitalContent.Task1_complete_date:
            x = x + 1
        if device.DigitalContent.Task2_complete_date:
            x = x + 1
        if device.DigitalContent.Task3_complete_date:
            x = x + 1
        if device.DigitalContent.Task4_complete_date:
            x = x + 1
        if device.DigitalContent.Task5_complete_date:
            x = x + 1
        if device.DigitalContent.Task6_complete_date:
            x = x + 1
        if device.DigitalContent.Task7_complete_date:
            x = x + 1
        if device.DigitalContent.Task8_complete_date:
            x = x + 1
        if device.DigitalContent.Task9_complete_date:
            x = x + 1
        if device.DigitalContent.Task10_complete_date:
            x = x + 1
        if device.DigitalContent.Task11_complete_date:
            x = x + 1
        if device.DigitalContent.Task12_complete_date:
            x = x + 1
        if device.DigitalContent.Task13_complete_date:
            x = x + 1
        if device.DigitalContent.Task14_complete_date:
            x = x + 1
        if device.DigitalContent.Task15_complete_date:
            x = x + 1
        if device.DigitalContent.Task16_complete_date:
            x = x + 1
        if device.DigitalContent.Task17_complete_date:
            x = x + 1
        if device.DigitalContent.Task18_complete_date:
            x = x + 1
        if device.DigitalContent.Task19_complete_date:
            x = x + 1
        if device.DigitalContent.Task20_complete_date:
            x = x + 1
        percent = x / y * 100
        device.DigitalContent.completed = int(percent)

        #alerting logic
        today = datetime.date.today()
        if device.DigitalContent.Task1_End_Date:
            Task1_delta =  device.DigitalContent.Task1_End_Date - today
        else:
            Task1_delta = None
        if device.DigitalContent.Task2_End_Date:
            Task2_delta = device.DigitalContent.Task2_End_Date - today
        else:
            Task2_delta = None
        if device.DigitalContent.Task3_End_Date:
            Task3_delta = device.DigitalContent.Task3_End_Date - today
        else:
            Task3_delta = None
        if device.DigitalContent.Task4_End_Date:
            Task4_delta = device.DigitalContent.Task4_End_Date - today
        else:
            Task4_delta = None
        if device.DigitalContent.Task5_End_Date:
            Task5_delta = device.DigitalContent.Task5_End_Date - today
        else:
            Task5_delta = None
        if device.DigitalContent.Task6_End_Date:
            Task6_delta = device.DigitalContent.Task6_End_Date - today
        else:
            Task6_delta = None
        if device.DigitalContent.Task7_End_Date:
            Task7_delta = device.DigitalContent.Task7_End_Date - today
        else:
            Task7_delta = None
        if device.DigitalContent.Task8_End_Date:
            Task8_delta = device.DigitalContent.Task8_End_Date - today
        else:
            Task8_delta = None
        if device.DigitalContent.Task9_End_Date:
            Task9_delta = device.DigitalContent.Task9_End_Date - today
        else:
            Task9_delta = None
        if device.DigitalContent.Task10_End_Date:
            Task10_delta =  device.DigitalContent.Task10_End_Date - today
        else:
            Task10_delta = None
        if device.DigitalContent.Task11_End_Date:
            Task11_delta =  device.DigitalContent.Task11_End_Date - today
        else:
            Task11_delta = None
        if device.DigitalContent.Task12_End_Date:
            Task12_delta = device.DigitalContent.Task12_End_Date - today
        else:
            Task12_delta = None
        if device.DigitalContent.Task13_End_Date:
            Task13_delta = device.DigitalContent.Task13_End_Date - today
        else:
            Task13_delta = None
        if device.DigitalContent.Task14_End_Date:
            Task14_delta = device.DigitalContent.Task14_End_Date - today
        else:
            Task14_delta = None
        if device.DigitalContent.Task15_End_Date:
            Task15_delta = device.DigitalContent.Task15_End_Date - today
        else:
            Task15_delta = None
        if device.DigitalContent.Task16_End_Date:
            Task16_delta = device.DigitalContent.Task16_End_Date - today
        else:
            Task16_delta = None
        if device.DigitalContent.Task17_End_Date:
            Task17_delta = device.DigitalContent.Task17_End_Date - today
        else:
            Task17_delta = None
        if device.DigitalContent.Task18_End_Date:
            Task18_delta = device.DigitalContent.Task18_End_Date - today
        else:
            Task18_delta = None
        if device.DigitalContent.Task19_End_Date:
            Task19_delta = device.DigitalContent.Task19_End_Date - today
        else:
            Task19_delta = None
        if device.DigitalContent.Task20_End_Date:
            Task20_delta = device.DigitalContent.Task20_End_Date - today
        else:
            Task20_delta = None


        if Task1_delta and Task1_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not device.DigitalContent.Task1_complete_date:
            device.DigitalContent.Task1_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not device.DigitalContent.Task2_complete_date:
            device.DigitalContent.Task2_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not device.DigitalContent.Task3_complete_date:
            device.DigitalContent.Task3_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not device.DigitalContent.Task4_complete_date:
            device.DigitalContent.Task4_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not device.DigitalContent.Task5_complete_date:
            device.DigitalContent.Task5_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not device.DigitalContent.Task6_complete_date:
            device.DigitalContent.Task6_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not device.DigitalContent.Task7_complete_date:
            device.DigitalContent.Task7_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not device.DigitalContent.Task8_complete_date:
            device.DigitalContent.Task8_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not device.DigitalContent.Task9_complete_date:
            device.DigitalContent.Task9_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not device.DigitalContent.Task10_complete_date:
            device.DigitalContent.Task10_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not device.DigitalContent.Task11_complete_date:
            device.DigitalContent.Task11_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not device.DigitalContent.Task12_complete_date:
            device.DigitalContent.Task12_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not device.DigitalContent.Task13_complete_date:
            device.DigitalContent.Task13_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not device.DigitalContent.Task14_complete_date:
            device.DigitalContent.Task14_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not device.DigitalContent.Task15_complete_date:
            device.DigitalContent.Task15_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not device.DigitalContent.Task16_complete_date:
            device.DigitalContent.Task16_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not device.DigitalContent.Task17_complete_date:
            device.DigitalContent.Task17_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not device.DigitalContent.Task18_complete_date:
            device.DigitalContent.Task18_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not device.DigitalContent.Task19_complete_date:
            device.DigitalContent.Task19_warning = True
            device.DigitalContent.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(device.DigitalContent.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not device.DigitalContent.Task20_complete_date:
            device.DigitalContent.Task20_warning = True
            device.DigitalContent.Status = 'At Risk'

        if device.DigitalContent.Task1_End_Date and Task1_delta < timedelta(0) and not device.DigitalContent.Task1_complete_date:
            device.DigitalContent.Task1_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task2_End_Date and Task2_delta < timedelta(0) and not device.DigitalContent.Task2_complete_date:
            device.DigitalContent.Task2_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task3_End_Date and Task3_delta < timedelta(0) and not device.DigitalContent.Task3_complete_date:
            device.DigitalContent.Task3_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task4_End_Date and Task4_delta < timedelta(0) and not device.DigitalContent.Task4_complete_date:
            device.DigitalContent.Task4_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task5_End_Date and Task5_delta < timedelta(0) and not device.DigitalContent.Task5_complete_date:
            device.DigitalContent.Task5_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task6_End_Date and Task6_delta < timedelta(0) and not device.DigitalContent.Task6_complete_date:
            device.DigitalContent.Task6_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task7_End_Date and Task7_delta < timedelta(0) and not device.DigitalContent.Task7_complete_date:
            device.DigitalContent.Task7_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task8_End_Date and Task8_delta < timedelta(0)and not device.DigitalContent.Task8_complete_date:
            device.DigitalContent.Task8_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task9_End_Date and Task9_delta < timedelta(0)and not device.DigitalContent.Task9_complete_date:
            device.DigitalContent.Task9_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task10_End_Date and Task10_delta < timedelta(0) and not device.DigitalContent.Task10_complete_date:
            device.DigitalContent.Task10_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task11_End_Date and Task11_delta < timedelta(0) and not device.DigitalContent.Task11_complete_date:
            device.DigitalContent.Task11_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task12_End_Date and Task12_delta < timedelta(0) and not device.DigitalContent.Task12_complete_date:
            device.DigitalContent.Task12_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task13_End_Date and Task13_delta < timedelta(0) and not device.DigitalContent.Task13_complete_date:
            device.DigitalContent.Task13_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task14_End_Date and Task14_delta < timedelta(0) and not device.DigitalContent.Task14_complete_date:
            device.DigitalContent.Task14_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task15_End_Date and Task15_delta < timedelta(0) and not device.DigitalContent.Task15_complete_date:
            device.DigitalContent.Task15_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task16_End_Date and Task16_delta < timedelta(0) and not device.DigitalContent.Task16_complete_date:
            device.DigitalContent.Task16_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task17_End_Date and Task17_delta < timedelta(0)and not device.DigitalContent.Task17_complete_date:
            device.DigitalContent.Task17_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task18_End_Date and Task18_delta < timedelta(0)and not device.DigitalContent.Task18_complete_date:
            device.DigitalContent.Task18_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task19_End_Date and Task19_delta < timedelta(0)and not device.DigitalContent.Task19_complete_date:
            device.DigitalContent.Task19_alert = True
            device.DigitalContent.Status = 'Delayed'
        if device.DigitalContent.Task20_End_Date and Task20_delta < timedelta(0)and not device.DigitalContent.Task20_complete_date:
            device.DigitalContent.Task20_alert = True
            device.DigitalContent.Status = 'Delayed'


        device.DigitalContent.save()

        device.VideoContent.Task1_alert = False
        device.VideoContent.Task1_warning = False
        device.VideoContent.Status = 'On_Time'

        device.VideoContent.Task2_alert = False
        device.VideoContent.Task2_warning = False

        device.VideoContent.Task3_alert = False
        device.VideoContent.Task3_warning = False

        device.VideoContent.Task4_alert = False
        device.VideoContent.Task4_warning = False

        device.VideoContent.Task5_alert = False
        device.VideoContent.Task5_warning = False

        device.VideoContent.Task6_alert = False
        device.VideoContent.Task6_warning = False

        device.VideoContent.Task7_alert = False
        device.VideoContent.Task7_warning = False

        device.VideoContent.Task8_alert = False
        device.VideoContent.Task8_warning = False

        device.VideoContent.Task9_alert = False
        device.VideoContent.Task9_warning = False

        device.VideoContent.Task10_alert = False
        device.VideoContent.Task10_warning = False

        device.VideoContent.Task11_alert = False
        device.VideoContent.Task11_warning = False

        device.VideoContent.Task12_alert = False
        device.VideoContent.Task12_warning = False

        device.VideoContent.Task13_alert = False
        device.VideoContent.Task13_warning = False

        device.VideoContent.Task14_alert = False
        device.VideoContent.Task14_warning = False

        device.VideoContent.Task15_alert = False
        device.VideoContent.Task15_warning = False

        device.VideoContent.Task16_alert = False
        device.VideoContent.Task16_warning = False

        device.VideoContent.Task17_alert = False
        device.VideoContent.Task17_warning = False

        device.VideoContent.Task18_alert = False
        device.VideoContent.Task18_warning = False

        device.VideoContent.Task19_alert = False
        device.VideoContent.Task19_warning = False

        device.VideoContent.Task20_alert = False
        device.VideoContent.Task20_warning = False

        y = activeTasksVC(device)

        x = 0
        if device.VideoContent.Task1_complete_date:
            x = x + 1
        if device.VideoContent.Task2_complete_date:
            x = x + 1
        if device.VideoContent.Task3_complete_date:
            x = x + 1
        if device.VideoContent.Task4_complete_date:
            x = x + 1
        if device.VideoContent.Task5_complete_date:
            x = x + 1
        if device.VideoContent.Task6_complete_date:
            x = x + 1
        if device.VideoContent.Task7_complete_date:
            x = x + 1
        if device.VideoContent.Task8_complete_date:
            x = x + 1
        if device.VideoContent.Task9_complete_date:
            x = x + 1
        if device.VideoContent.Task10_complete_date:
            x = x + 1
        if device.VideoContent.Task11_complete_date:
            x = x + 1
        if device.VideoContent.Task12_complete_date:
            x = x + 1
        if device.VideoContent.Task13_complete_date:
            x = x + 1
        if device.VideoContent.Task14_complete_date:
            x = x + 1
        if device.VideoContent.Task15_complete_date:
            x = x + 1
        if device.VideoContent.Task16_complete_date:
            x = x + 1
        if device.VideoContent.Task17_complete_date:
            x = x + 1
        if device.VideoContent.Task18_complete_date:
            x = x + 1
        if device.VideoContent.Task19_complete_date:
            x = x + 1
        if device.VideoContent.Task20_complete_date:
            x = x + 1
        percent = x / y * 100
        device.VideoContent.completed = int(percent)

        #alerting logic
        today = datetime.date.today()
        if device.VideoContent.Task1_End_Date:
            Task1_delta =  device.VideoContent.Task1_End_Date - today
        else:
            Task1_delta = None
        if device.VideoContent.Task2_End_Date:
            Task2_delta = device.VideoContent.Task2_End_Date - today
        else:
            Task2_delta = None
        if device.VideoContent.Task3_End_Date:
            Task3_delta = device.VideoContent.Task3_End_Date - today
        else:
            Task3_delta = None
        if device.VideoContent.Task4_End_Date:
            Task4_delta = device.VideoContent.Task4_End_Date - today
        else:
            Task4_delta = None
        if device.VideoContent.Task5_End_Date:
            Task5_delta = device.VideoContent.Task5_End_Date - today
        else:
            Task5_delta = None
        if device.VideoContent.Task6_End_Date:
            Task6_delta = device.VideoContent.Task6_End_Date - today
        else:
            Task6_delta = None
        if device.VideoContent.Task7_End_Date:
            Task7_delta = device.VideoContent.Task7_End_Date - today
        else:
            Task7_delta = None
        if device.VideoContent.Task8_End_Date:
            Task8_delta = device.VideoContent.Task8_End_Date - today
        else:
            Task8_delta = None
        if device.VideoContent.Task9_End_Date:
            Task9_delta = device.VideoContent.Task9_End_Date - today
        else:
            Task9_delta = None
        if device.VideoContent.Task10_End_Date:
            Task10_delta =  device.VideoContent.Task10_End_Date - today
        else:
            Task10_delta = None
        if device.VideoContent.Task11_End_Date:
            Task11_delta =  device.VideoContent.Task11_End_Date - today
        else:
            Task11_delta = None
        if device.VideoContent.Task12_End_Date:
            Task12_delta = device.VideoContent.Task12_End_Date - today
        else:
            Task12_delta = None
        if device.VideoContent.Task13_End_Date:
            Task13_delta = device.VideoContent.Task13_End_Date - today
        else:
            Task13_delta = None
        if device.VideoContent.Task14_End_Date:
            Task14_delta = device.VideoContent.Task14_End_Date - today
        else:
            Task14_delta = None
        if device.VideoContent.Task15_End_Date:
            Task15_delta = device.VideoContent.Task15_End_Date - today
        else:
            Task15_delta = None
        if device.VideoContent.Task16_End_Date:
            Task16_delta = device.VideoContent.Task16_End_Date - today
        else:
            Task16_delta = None
        if device.VideoContent.Task17_End_Date:
            Task17_delta = device.VideoContent.Task17_End_Date - today
        else:
            Task17_delta = None
        if device.VideoContent.Task18_End_Date:
            Task18_delta = device.VideoContent.Task18_End_Date - today
        else:
            Task18_delta = None
        if device.VideoContent.Task19_End_Date:
            Task19_delta = device.VideoContent.Task19_End_Date - today
        else:
            Task19_delta = None
        if device.VideoContent.Task20_End_Date:
            Task20_delta = device.VideoContent.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not device.VideoContent.Task1_complete_date:
            device.VideoContent.Task1_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not device.VideoContent.Task2_complete_date:
            device.VideoContent.Task2_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not device.VideoContent.Task3_complete_date:
            device.VideoContent.Task3_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not device.VideoContent.Task4_complete_date:
            device.VideoContent.Task4_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not device.VideoContent.Task5_complete_date:
            device.VideoContent.Task5_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not device.VideoContent.Task6_complete_date:
            device.VideoContent.Task6_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not device.VideoContent.Task7_complete_date:
            device.VideoContent.Task7_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not device.VideoContent.Task8_complete_date:
            device.VideoContent.Task8_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not device.VideoContent.Task9_complete_date:
            device.VideoContent.Task9_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not device.VideoContent.Task10_complete_date:
            device.VideoContent.Task10_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not device.VideoContent.Task11_complete_date:
            device.VideoContent.Task11_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not device.VideoContent.Task12_complete_date:
            device.VideoContent.Task12_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not device.VideoContent.Task13_complete_date:
            device.VideoContent.Task13_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not device.VideoContent.Task14_complete_date:
            device.VideoContent.Task14_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not device.VideoContent.Task15_complete_date:
            device.VideoContent.Task15_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not device.VideoContent.Task16_complete_date:
            device.VideoContent.Task16_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not device.VideoContent.Task17_complete_date:
            device.VideoContent.Task17_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not device.VideoContent.Task18_complete_date:
            device.VideoContent.Task18_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not device.VideoContent.Task19_complete_date:
            device.VideoContent.Task19_warning = True
            device.VideoContent.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(device.VideoContent.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not device.VideoContent.Task20_complete_date:
            device.VideoContent.Task20_warning = True
            device.VideoContent.Status = 'At Risk'

        if device.VideoContent.Task1_End_Date and Task1_delta < timedelta(0) and not device.VideoContent.Task1_complete_date:
            device.VideoContent.Task1_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task2_End_Date and Task2_delta < timedelta(0) and not device.VideoContent.Task2_complete_date:
            device.VideoContent.Task2_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task3_End_Date and Task3_delta < timedelta(0) and not device.VideoContent.Task3_complete_date:
            device.VideoContent.Task3_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task4_End_Date and Task4_delta < timedelta(0) and not device.VideoContent.Task4_complete_date:
            device.VideoContent.Task4_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task5_End_Date and Task5_delta < timedelta(0) and not device.VideoContent.Task5_complete_date:
            device.VideoContent.Task5_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task6_End_Date and Task6_delta < timedelta(0) and not device.VideoContent.Task6_complete_date:
            device.VideoContent.Task6_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task7_End_Date and Task7_delta < timedelta(0) and not device.VideoContent.Task7_complete_date:
            device.VideoContent.Task7_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task8_End_Date and Task8_delta < timedelta(0)and not device.VideoContent.Task8_complete_date:
            device.VideoContent.Task8_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task9_End_Date and Task9_delta < timedelta(0)and not device.VideoContent.Task9_complete_date:
            device.VideoContent.Task9_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task10_End_Date and Task10_delta < timedelta(0) and not device.VideoContent.Task10_complete_date:
            device.VideoContent.Task10_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task11_End_Date and Task11_delta < timedelta(0) and not device.VideoContent.Task11_complete_date:
            device.VideoContent.Task11_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task12_End_Date and Task12_delta < timedelta(0) and not device.VideoContent.Task12_complete_date:
            device.VideoContent.Task12_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task13_End_Date and Task13_delta < timedelta(0) and not device.VideoContent.Task13_complete_date:
            device.VideoContent.Task13_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task14_End_Date and Task14_delta < timedelta(0) and not device.VideoContent.Task14_complete_date:
            device.VideoContent.Task14_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task15_End_Date and Task15_delta < timedelta(0) and not device.VideoContent.Task15_complete_date:
            device.VideoContent.Task15_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task16_End_Date and Task16_delta < timedelta(0) and not device.VideoContent.Task16_complete_date:
            device.VideoContent.Task16_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task17_End_Date and Task17_delta < timedelta(0)and not device.VideoContent.Task17_complete_date:
            device.VideoContent.Task17_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task18_End_Date and Task18_delta < timedelta(0)and not device.VideoContent.Task18_complete_date:
            device.VideoContent.Task18_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task19_End_Date and Task19_delta < timedelta(0)and not device.VideoContent.Task19_complete_date:
            device.VideoContent.Task19_alert = True
            device.VideoContent.Status = 'Delayed'
        if device.VideoContent.Task20_End_Date and Task20_delta < timedelta(0)and not device.VideoContent.Task20_complete_date:
            device.VideoContent.Task20_alert = True
            device.VideoContent.Status = 'Delayed'

        device.VideoContent.save()

        device.CallCenterTraining.Task1_alert = False
        device.CallCenterTraining.Task1_warning = False
        device.CallCenterTraining.Status = 'On_Time'

        device.CallCenterTraining.Task2_alert = False
        device.CallCenterTraining.Task2_warning = False

        device.CallCenterTraining.Task3_alert = False
        device.CallCenterTraining.Task3_warning = False

        device.CallCenterTraining.Task4_alert = False
        device.CallCenterTraining.Task4_warning = False

        device.CallCenterTraining.Task5_alert = False
        device.CallCenterTraining.Task5_warning = False

        device.CallCenterTraining.Task6_alert = False
        device.CallCenterTraining.Task6_warning = False

        device.CallCenterTraining.Task7_alert = False
        device.CallCenterTraining.Task7_warning = False

        device.CallCenterTraining.Task8_alert = False
        device.CallCenterTraining.Task8_warning = False

        device.CallCenterTraining.Task9_alert = False
        device.CallCenterTraining.Task9_warning = False

        device.CallCenterTraining.Task10_alert = False
        device.CallCenterTraining.Task10_warning = False

        device.CallCenterTraining.Task11_alert = False
        device.CallCenterTraining.Task11_warning = False

        device.CallCenterTraining.Task12_alert = False
        device.CallCenterTraining.Task12_warning = False

        device.CallCenterTraining.Task13_alert = False
        device.CallCenterTraining.Task13_warning = False

        device.CallCenterTraining.Task14_alert = False
        device.CallCenterTraining.Task14_warning = False

        device.CallCenterTraining.Task15_alert = False
        device.CallCenterTraining.Task15_warning = False

        device.CallCenterTraining.Task16_alert = False
        device.CallCenterTraining.Task16_warning = False

        device.CallCenterTraining.Task17_alert = False
        device.CallCenterTraining.Task17_warning = False

        device.CallCenterTraining.Task18_alert = False
        device.CallCenterTraining.Task18_warning = False

        device.CallCenterTraining.Task19_alert = False
        device.CallCenterTraining.Task19_warning = False

        device.CallCenterTraining.Task20_alert = False
        device.CallCenterTraining.Task20_warning = False

        y = activeTasksCCT(device)

        x = 0
        if device.CallCenterTraining.Task1_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task2_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task3_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task4_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task5_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task6_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task7_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task8_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task9_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task10_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task11_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task12_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task13_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task14_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task15_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task16_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task17_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task18_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task19_complete_date:
            x = x + 1
        if device.CallCenterTraining.Task20_complete_date:
            x = x + 1
        percent = x / y * 100
        device.CallCenterTraining.completed = int(percent)

        #alerting logic
        today = datetime.date.today()
        if device.CallCenterTraining.Task1_End_Date:
            Task1_delta =  device.CallCenterTraining.Task1_End_Date - today
        else:
            Task1_delta = None
        if device.CallCenterTraining.Task2_End_Date:
            Task2_delta = device.CallCenterTraining.Task2_End_Date - today
        else:
            Task2_delta = None
        if device.CallCenterTraining.Task3_End_Date:
            Task3_delta = device.CallCenterTraining.Task3_End_Date - today
        else:
            Task3_delta = None
        if device.CallCenterTraining.Task4_End_Date:
            Task4_delta = device.CallCenterTraining.Task4_End_Date - today
        else:
            Task4_delta = None
        if device.CallCenterTraining.Task5_End_Date:
            Task5_delta = device.CallCenterTraining.Task5_End_Date - today
        else:
            Task5_delta = None
        if device.CallCenterTraining.Task6_End_Date:
            Task6_delta = device.CallCenterTraining.Task6_End_Date - today
        else:
            Task6_delta = None
        if device.CallCenterTraining.Task7_End_Date:
            Task7_delta = device.CallCenterTraining.Task7_End_Date - today
        else:
            Task7_delta = None
        if device.CallCenterTraining.Task8_End_Date:
            Task8_delta = device.CallCenterTraining.Task8_End_Date - today
        else:
            Task8_delta = None
        if device.CallCenterTraining.Task9_End_Date:
            Task9_delta = device.CallCenterTraining.Task9_End_Date - today
        else:
            Task9_delta = None
        if device.CallCenterTraining.Task10_End_Date:
            Task10_delta =  device.CallCenterTraining.Task10_End_Date - today
        else:
            Task10_delta = None
        if device.CallCenterTraining.Task11_End_Date:
            Task11_delta =  device.CallCenterTraining.Task11_End_Date - today
        else:
            Task11_delta = None
        if device.CallCenterTraining.Task12_End_Date:
            Task12_delta = device.CallCenterTraining.Task12_End_Date - today
        else:
            Task12_delta = None
        if device.CallCenterTraining.Task13_End_Date:
            Task13_delta = device.CallCenterTraining.Task13_End_Date - today
        else:
            Task13_delta = None
        if device.CallCenterTraining.Task14_End_Date:
            Task14_delta = device.CallCenterTraining.Task14_End_Date - today
        else:
            Task14_delta = None
        if device.CallCenterTraining.Task15_End_Date:
            Task15_delta = device.CallCenterTraining.Task15_End_Date - today
        else:
            Task15_delta = None
        if device.CallCenterTraining.Task16_End_Date:
            Task16_delta = device.CallCenterTraining.Task16_End_Date - today
        else:
            Task16_delta = None
        if device.CallCenterTraining.Task17_End_Date:
            Task17_delta = device.CallCenterTraining.Task17_End_Date - today
        else:
            Task17_delta = None
        if device.CallCenterTraining.Task18_End_Date:
            Task18_delta = device.CallCenterTraining.Task18_End_Date - today
        else:
            Task18_delta = None
        if device.CallCenterTraining.Task19_End_Date:
            Task19_delta = device.CallCenterTraining.Task19_End_Date - today
        else:
            Task19_delta = None
        if device.CallCenterTraining.Task20_End_Date:
            Task20_delta = device.CallCenterTraining.Task20_End_Date - today
        else:
            Task20_delta = None


        if Task1_delta and Task1_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not device.CallCenterTraining.Task1_complete_date:
            device.CallCenterTraining.Task1_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not device.CallCenterTraining.Task2_complete_date:
            device.CallCenterTraining.Task2_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not device.CallCenterTraining.Task3_complete_date:
            device.CallCenterTraining.Task3_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not device.CallCenterTraining.Task4_complete_date:
            device.CallCenterTraining.Task4_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not device.CallCenterTraining.Task5_complete_date:
            device.CallCenterTraining.Task5_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not device.CallCenterTraining.Task6_complete_date:
            device.CallCenterTraining.Task6_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not device.CallCenterTraining.Task7_complete_date:
            device.CallCenterTraining.Task7_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not device.CallCenterTraining.Task8_complete_date:
            device.CallCenterTraining.Task8_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not device.CallCenterTraining.Task9_complete_date:
            device.CallCenterTraining.Task9_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not device.CallCenterTraining.Task10_complete_date:
            device.CallCenterTraining.Task10_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not device.CallCenterTraining.Task11_complete_date:
            device.CallCenterTraining.Task11_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not device.CallCenterTraining.Task12_complete_date:
            device.CallCenterTraining.Task12_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not device.CallCenterTraining.Task13_complete_date:
            device.CallCenterTraining.Task13_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not device.CallCenterTraining.Task14_complete_date:
            device.CallCenterTraining.Task14_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not device.CallCenterTraining.Task15_complete_date:
            device.CallCenterTraining.Task15_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not device.CallCenterTraining.Task16_complete_date:
            device.CallCenterTraining.Task16_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not device.CallCenterTraining.Task17_complete_date:
            device.CallCenterTraining.Task17_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not device.CallCenterTraining.Task18_complete_date:
            device.CallCenterTraining.Task18_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not device.CallCenterTraining.Task19_complete_date:
            device.CallCenterTraining.Task19_warning = True
            device.CallCenterTraining.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(device.CallCenterTraining.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not device.CallCenterTraining.Task20_complete_date:
            device.CallCenterTraining.Task20_warning = True
            device.CallCenterTraining.Status = 'At Risk'

        if device.CallCenterTraining.Task1_End_Date and Task1_delta < timedelta(0) and not device.CallCenterTraining.Task1_complete_date:
            device.CallCenterTraining.Task1_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task2_End_Date and Task2_delta < timedelta(0) and not device.CallCenterTraining.Task2_complete_date:
            device.CallCenterTraining.Task2_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task3_End_Date and Task3_delta < timedelta(0) and not device.CallCenterTraining.Task3_complete_date:
            device.CallCenterTraining.Task3_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task4_End_Date and Task4_delta < timedelta(0) and not device.CallCenterTraining.Task4_complete_date:
            device.CallCenterTraining.Task4_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task5_End_Date and Task5_delta < timedelta(0) and not device.CallCenterTraining.Task5_complete_date:
            device.CallCenterTraining.Task5_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task6_End_Date and Task6_delta < timedelta(0) and not device.CallCenterTraining.Task6_complete_date:
            device.CallCenterTraining.Task6_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task7_End_Date and Task7_delta < timedelta(0) and not device.CallCenterTraining.Task7_complete_date:
            device.CallCenterTraining.Task7_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task8_End_Date and Task8_delta < timedelta(0)and not device.CallCenterTraining.Task8_complete_date:
            device.CallCenterTraining.Task8_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task9_End_Date and Task9_delta < timedelta(0)and not device.CallCenterTraining.Task9_complete_date:
            device.CallCenterTraining.Task9_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task10_End_Date and Task10_delta < timedelta(0) and not device.CallCenterTraining.Task10_complete_date:
            device.CallCenterTraining.Task10_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task11_End_Date and Task11_delta < timedelta(0) and not device.CallCenterTraining.Task11_complete_date:
            device.CallCenterTraining.Task11_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task12_End_Date and Task12_delta < timedelta(0) and not device.CallCenterTraining.Task12_complete_date:
            device.CallCenterTraining.Task12_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task13_End_Date and Task13_delta < timedelta(0) and not device.CallCenterTraining.Task13_complete_date:
            device.CallCenterTraining.Task13_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task14_End_Date and Task14_delta < timedelta(0) and not device.CallCenterTraining.Task14_complete_date:
            device.CallCenterTraining.Task14_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task15_End_Date and Task15_delta < timedelta(0) and not device.CallCenterTraining.Task15_complete_date:
            device.CallCenterTraining.Task15_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task16_End_Date and Task16_delta < timedelta(0) and not device.CallCenterTraining.Task16_complete_date:
            device.CallCenterTraining.Task16_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task17_End_Date and Task17_delta < timedelta(0)and not device.CallCenterTraining.Task17_complete_date:
            device.CallCenterTraining.Task17_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task18_End_Date and Task18_delta < timedelta(0)and not device.CallCenterTraining.Task18_complete_date:
            device.CallCenterTraining.Task18_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task19_End_Date and Task19_delta < timedelta(0)and not device.CallCenterTraining.Task19_complete_date:
            device.CallCenterTraining.Task19_alert = True
            device.CallCenterTraining.Status = 'Delayed'
        if device.CallCenterTraining.Task20_End_Date and Task20_delta < timedelta(0)and not device.CallCenterTraining.Task20_complete_date:
            device.CallCenterTraining.Task20_alert = True
            device.CallCenterTraining.Status = 'Delayed'


        device.CallCenterTraining.save()

        device.CallCenterOpertaions.Task1_alert = False
        device.CallCenterOpertaions.Task1_warning = False
        device.CallCenterOpertaions.Status = 'On_Time'

        device.CallCenterOpertaions.Task2_alert = False
        device.CallCenterOpertaions.Task2_warning = False

        device.CallCenterOpertaions.Task3_alert = False
        device.CallCenterOpertaions.Task3_warning = False

        device.CallCenterOpertaions.Task4_alert = False
        device.CallCenterOpertaions.Task4_warning = False

        device.CallCenterOpertaions.Task5_alert = False
        device.CallCenterOpertaions.Task5_warning = False

        device.CallCenterOpertaions.Task6_alert = False
        device.CallCenterOpertaions.Task6_warning = False

        device.CallCenterOpertaions.Task7_alert = False
        device.CallCenterOpertaions.Task7_warning = False

        device.CallCenterOpertaions.Task8_alert = False
        device.CallCenterOpertaions.Task8_warning = False

        device.CallCenterOpertaions.Task9_alert = False
        device.CallCenterOpertaions.Task9_warning = False

        device.CallCenterOpertaions.Task10_alert = False
        device.CallCenterOpertaions.Task10_warning = False

        device.CallCenterOpertaions.Task11_alert = False
        device.CallCenterOpertaions.Task11_warning = False

        device.CallCenterOpertaions.Task12_alert = False
        device.CallCenterOpertaions.Task12_warning = False

        device.CallCenterOpertaions.Task13_alert = False
        device.CallCenterOpertaions.Task13_warning = False

        device.CallCenterOpertaions.Task14_alert = False
        device.CallCenterOpertaions.Task14_warning = False

        device.CallCenterOpertaions.Task15_alert = False
        device.CallCenterOpertaions.Task15_warning = False

        device.CallCenterOpertaions.Task16_alert = False
        device.CallCenterOpertaions.Task16_warning = False

        device.CallCenterOpertaions.Task17_alert = False
        device.CallCenterOpertaions.Task17_warning = False

        device.CallCenterOpertaions.Task18_alert = False
        device.CallCenterOpertaions.Task18_warning = False

        device.CallCenterOpertaions.Task19_alert = False
        device.CallCenterOpertaions.Task19_warning = False

        device.CallCenterOpertaions.Task20_alert = False
        device.CallCenterOpertaions.Task20_warning = False

        y = activeTasksCCO(device)

        x = 0
        if device.CallCenterOpertaions.Task1_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task2_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task3_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task4_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task5_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task6_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task7_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task8_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task9_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task10_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task11_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task12_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task13_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task14_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task15_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task16_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task17_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task18_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task19_complete_date:
            x = x + 1
        if device.CallCenterOpertaions.Task20_complete_date:
            x = x + 1
        percent = x / y * 100
        device.CallCenterOpertaions.completed = int(percent)

        #alerting logic
        today = datetime.date.today()
        if device.CallCenterOpertaions.Task1_End_Date:
            Task1_delta =  device.CallCenterOpertaions.Task1_End_Date - today
        else:
            Task1_delta = None
        if device.CallCenterOpertaions.Task2_End_Date:
            Task2_delta = device.CallCenterOpertaions.Task2_End_Date - today
        else:
            Task2_delta = None
        if device.CallCenterOpertaions.Task3_End_Date:
            Task3_delta = device.CallCenterOpertaions.Task3_End_Date - today
        else:
            Task3_delta = None
        if device.CallCenterOpertaions.Task4_End_Date:
            Task4_delta = device.CallCenterOpertaions.Task4_End_Date - today
        else:
            Task4_delta = None
        if device.CallCenterOpertaions.Task5_End_Date:
            Task5_delta = device.CallCenterOpertaions.Task5_End_Date - today
        else:
            Task5_delta = None
        if device.CallCenterOpertaions.Task6_End_Date:
            Task6_delta = device.CallCenterOpertaions.Task6_End_Date - today
        else:
            Task6_delta = None
        if device.CallCenterOpertaions.Task7_End_Date:
            Task7_delta = device.CallCenterOpertaions.Task7_End_Date - today
        else:
            Task7_delta = None
        if device.CallCenterOpertaions.Task8_End_Date:
            Task8_delta = device.CallCenterOpertaions.Task8_End_Date - today
        else:
            Task8_delta = None
        if device.CallCenterOpertaions.Task9_End_Date:
            Task9_delta = device.CallCenterOpertaions.Task9_End_Date - today
        else:
            Task9_delta = None
        if device.CallCenterOpertaions.Task10_End_Date:
            Task10_delta =  device.CallCenterOpertaions.Task10_End_Date - today
        else:
            Task10_delta = None
        if device.CallCenterOpertaions.Task11_End_Date:
            Task11_delta =  device.CallCenterOpertaions.Task11_End_Date - today
        else:
            Task11_delta = None
        if device.CallCenterOpertaions.Task12_End_Date:
            Task12_delta = device.CallCenterOpertaions.Task12_End_Date - today
        else:
            Task12_delta = None
        if device.CallCenterOpertaions.Task13_End_Date:
            Task13_delta = device.CallCenterOpertaions.Task13_End_Date - today
        else:
            Task13_delta = None
        if device.CallCenterOpertaions.Task14_End_Date:
            Task14_delta = device.CallCenterOpertaions.Task14_End_Date - today
        else:
            Task14_delta = None
        if device.CallCenterOpertaions.Task15_End_Date:
            Task15_delta = device.CallCenterOpertaions.Task15_End_Date - today
        else:
            Task15_delta = None
        if device.CallCenterOpertaions.Task16_End_Date:
            Task16_delta = device.CallCenterOpertaions.Task16_End_Date - today
        else:
            Task16_delta = None
        if device.CallCenterOpertaions.Task17_End_Date:
            Task17_delta = device.CallCenterOpertaions.Task17_End_Date - today
        else:
            Task17_delta = None
        if device.CallCenterOpertaions.Task18_End_Date:
            Task18_delta = device.CallCenterOpertaions.Task18_End_Date - today
        else:
            Task18_delta = None
        if device.CallCenterOpertaions.Task19_End_Date:
            Task19_delta = device.CallCenterOpertaions.Task19_End_Date - today
        else:
            Task19_delta = None
        if device.CallCenterOpertaions.Task20_End_Date:
            Task20_delta = device.CallCenterOpertaions.Task20_End_Date - today
        else:
            Task20_delta = None


        if Task1_delta and Task1_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task1_complete_date:
            device.CallCenterOpertaions.Task1_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task2_complete_date:
            device.CallCenterOpertaions.Task2_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task3_complete_date:
            device.CallCenterOpertaions.Task3_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task4_complete_date:
            device.CallCenterOpertaions.Task4_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task5_complete_date:
            device.CallCenterOpertaions.Task5_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task6_complete_date:
            device.CallCenterOpertaions.Task6_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task7_complete_date:
            device.CallCenterOpertaions.Task7_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task8_complete_date:
            device.CallCenterOpertaions.Task8_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task9_complete_date:
            device.CallCenterOpertaions.Task9_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task10_complete_date:
            device.CallCenterOpertaions.Task10_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task11_complete_date:
            device.CallCenterOpertaions.Task11_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task12_complete_date:
            device.CallCenterOpertaions.Task12_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task13_complete_date:
            device.CallCenterOpertaions.Task13_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task14_complete_date:
            device.CallCenterOpertaions.Task14_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task15_complete_date:
            device.CallCenterOpertaions.Task15_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task16_complete_date:
            device.CallCenterOpertaions.Task16_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task17_complete_date:
            device.CallCenterOpertaions.Task17_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task18_complete_date:
            device.CallCenterOpertaions.Task18_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task19_complete_date:
            device.CallCenterOpertaions.Task19_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(device.CallCenterOpertaions.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not device.CallCenterOpertaions.Task20_complete_date:
            device.CallCenterOpertaions.Task20_warning = True
            device.CallCenterOpertaions.Status = 'At Risk'

        if device.CallCenterOpertaions.Task1_End_Date and Task1_delta < timedelta(0) and not device.CallCenterOpertaions.Task1_complete_date:
            device.CallCenterOpertaions.Task1_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task2_End_Date and Task2_delta < timedelta(0) and not device.CallCenterOpertaions.Task2_complete_date:
            device.CallCenterOpertaions.Task2_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task3_End_Date and Task3_delta < timedelta(0) and not device.CallCenterOpertaions.Task3_complete_date:
            device.CallCenterOpertaions.Task3_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task4_End_Date and Task4_delta < timedelta(0) and not device.CallCenterOpertaions.Task4_complete_date:
            device.CallCenterOpertaions.Task4_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task5_End_Date and Task5_delta < timedelta(0) and not device.CallCenterOpertaions.Task5_complete_date:
            device.CallCenterOpertaions.Task5_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task6_End_Date and Task6_delta < timedelta(0) and not device.CallCenterOpertaions.Task6_complete_date:
            device.CallCenterOpertaions.Task6_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task7_End_Date and Task7_delta < timedelta(0) and not device.CallCenterOpertaions.Task7_complete_date:
            device.CallCenterOpertaions.Task7_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task8_End_Date and Task8_delta < timedelta(0)and not device.CallCenterOpertaions.Task8_complete_date:
            device.CallCenterOpertaions.Task8_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task9_End_Date and Task9_delta < timedelta(0)and not device.CallCenterOpertaions.Task9_complete_date:
            device.CallCenterOpertaions.Task9_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task10_End_Date and Task10_delta < timedelta(0) and not device.CallCenterOpertaions.Task10_complete_date:
            device.CallCenterOpertaions.Task10_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task11_End_Date and Task11_delta < timedelta(0) and not device.CallCenterOpertaions.Task11_complete_date:
            device.CallCenterOpertaions.Task11_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task12_End_Date and Task12_delta < timedelta(0) and not device.CallCenterOpertaions.Task12_complete_date:
            device.CallCenterOpertaions.Task12_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task13_End_Date and Task13_delta < timedelta(0) and not device.CallCenterOpertaions.Task13_complete_date:
            device.CallCenterOpertaions.Task13_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task14_End_Date and Task14_delta < timedelta(0) and not device.CallCenterOpertaions.Task14_complete_date:
            device.CallCenterOpertaions.Task14_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task15_End_Date and Task15_delta < timedelta(0) and not device.CallCenterOpertaions.Task15_complete_date:
            device.CallCenterOpertaions.Task15_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task16_End_Date and Task16_delta < timedelta(0) and not device.CallCenterOpertaions.Task16_complete_date:
            device.CallCenterOpertaions.Task16_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task17_End_Date and Task17_delta < timedelta(0)and not device.CallCenterOpertaions.Task17_complete_date:
            device.CallCenterOpertaions.Task17_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task18_End_Date and Task18_delta < timedelta(0)and not device.CallCenterOpertaions.Task18_complete_date:
            device.CallCenterOpertaions.Task18_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task19_End_Date and Task19_delta < timedelta(0)and not device.CallCenterOpertaions.Task19_complete_date:
            device.CallCenterOpertaions.Task19_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'
        if device.CallCenterOpertaions.Task20_End_Date and Task20_delta < timedelta(0)and not device.CallCenterOpertaions.Task20_complete_date:
            device.CallCenterOpertaions.Task20_alert = True
            device.CallCenterOpertaions.Status = 'Delayed'

        device.CallCenterOpertaions.save()

        device.ProductSupport.Task1_alert = False
        device.ProductSupport.Task1_warning = False
        device.ProductSupport.Status = 'On_Time'

        device.ProductSupport.Task2_alert = False
        device.ProductSupport.Task2_warning = False

        device.ProductSupport.Task3_alert = False
        device.ProductSupport.Task3_warning = False

        device.ProductSupport.Task4_alert = False
        device.ProductSupport.Task4_warning = False

        device.ProductSupport.Task5_alert = False
        device.ProductSupport.Task5_warning = False

        device.ProductSupport.Task6_alert = False
        device.ProductSupport.Task6_warning = False

        device.ProductSupport.Task7_alert = False
        device.ProductSupport.Task7_warning = False

        device.ProductSupport.Task8_alert = False
        device.ProductSupport.Task8_warning = False

        device.ProductSupport.Task9_alert = False
        device.ProductSupport.Task9_warning = False

        device.ProductSupport.Task10_alert = False
        device.ProductSupport.Task10_warning = False

        device.ProductSupport.Task11_alert = False
        device.ProductSupport.Task11_warning = False

        device.ProductSupport.Task12_alert = False
        device.ProductSupport.Task12_warning = False

        device.ProductSupport.Task13_alert = False
        device.ProductSupport.Task13_warning = False

        device.ProductSupport.Task14_alert = False
        device.ProductSupport.Task14_warning = False

        device.ProductSupport.Task15_alert = False
        device.ProductSupport.Task15_warning = False

        device.ProductSupport.Task16_alert = False
        device.ProductSupport.Task16_warning = False

        device.ProductSupport.Task17_alert = False
        device.ProductSupport.Task17_warning = False

        device.ProductSupport.Task18_alert = False
        device.ProductSupport.Task18_warning = False

        device.ProductSupport.Task19_alert = False
        device.ProductSupport.Task19_warning = False

        device.ProductSupport.Task20_alert = False
        device.ProductSupport.Task20_warning = False

        y = activeTasksPS(device)

        x = 0
        if device.ProductSupport.Task1_complete_date:
            x = x + 1
        if device.ProductSupport.Task2_complete_date:
            x = x + 1
        if device.ProductSupport.Task3_complete_date:
            x = x + 1
        if device.ProductSupport.Task4_complete_date:
            x = x + 1
        if device.ProductSupport.Task5_complete_date:
            x = x + 1
        if device.ProductSupport.Task6_complete_date:
            x = x + 1
        if device.ProductSupport.Task7_complete_date:
            x = x + 1
        if device.ProductSupport.Task8_complete_date:
            x = x + 1
        if device.ProductSupport.Task9_complete_date:
            x = x + 1
        if device.ProductSupport.Task10_complete_date:
            x = x + 1
        if device.ProductSupport.Task11_complete_date:
            x = x + 1
        if device.ProductSupport.Task12_complete_date:
            x = x + 1
        if device.ProductSupport.Task13_complete_date:
            x = x + 1
        if device.ProductSupport.Task14_complete_date:
            x = x + 1
        if device.ProductSupport.Task15_complete_date:
            x = x + 1
        if device.ProductSupport.Task16_complete_date:
            x = x + 1
        if device.ProductSupport.Task17_complete_date:
            x = x + 1
        if device.ProductSupport.Task18_complete_date:
            x = x + 1
        if device.ProductSupport.Task19_complete_date:
            x = x + 1
        if device.ProductSupport.Task20_complete_date:
            x = x + 1
        percent = x / y * 100
        device.ProductSupport.completed = int(percent)

        #alerting logic
        today = datetime.date.today()
        if device.ProductSupport.Task1_End_Date:
            Task1_delta =  device.ProductSupport.Task1_End_Date - today
        else:
            Task1_delta = None
        if device.ProductSupport.Task2_End_Date:
            Task2_delta = device.ProductSupport.Task2_End_Date - today
        else:
            Task2_delta = None
        if device.ProductSupport.Task3_End_Date:
            Task3_delta = device.ProductSupport.Task3_End_Date - today
        else:
            Task3_delta = None
        if device.ProductSupport.Task4_End_Date:
            Task4_delta = device.ProductSupport.Task4_End_Date - today
        else:
            Task4_delta = None
        if device.ProductSupport.Task5_End_Date:
            Task5_delta = device.ProductSupport.Task5_End_Date - today
        else:
            Task5_delta = None
        if device.ProductSupport.Task6_End_Date:
            Task6_delta = device.ProductSupport.Task6_End_Date - today
        else:
            Task6_delta = None
        if device.ProductSupport.Task7_End_Date:
            Task7_delta = device.ProductSupport.Task7_End_Date - today
        else:
            Task7_delta = None
        if device.ProductSupport.Task8_End_Date:
            Task8_delta = device.ProductSupport.Task8_End_Date - today
        else:
            Task8_delta = None
        if device.ProductSupport.Task9_End_Date:
            Task9_delta = device.ProductSupport.Task9_End_Date - today
        else:
            Task9_delta = None
        if device.ProductSupport.Task10_End_Date:
            Task10_delta =  device.ProductSupport.Task10_End_Date - today
        else:
            Task10_delta = None
        if device.ProductSupport.Task11_End_Date:
            Task11_delta =  device.ProductSupport.Task11_End_Date - today
        else:
            Task11_delta = None
        if device.ProductSupport.Task12_End_Date:
            Task12_delta = device.ProductSupport.Task12_End_Date - today
        else:
            Task12_delta = None
        if device.ProductSupport.Task13_End_Date:
            Task13_delta = device.ProductSupport.Task13_End_Date - today
        else:
            Task13_delta = None
        if device.ProductSupport.Task14_End_Date:
            Task14_delta = device.ProductSupport.Task14_End_Date - today
        else:
            Task14_delta = None
        if device.ProductSupport.Task15_End_Date:
            Task15_delta = device.ProductSupport.Task15_End_Date - today
        else:
            Task15_delta = None
        if device.ProductSupport.Task16_End_Date:
            Task16_delta = device.ProductSupport.Task16_End_Date - today
        else:
            Task16_delta = None
        if device.ProductSupport.Task17_End_Date:
            Task17_delta = device.ProductSupport.Task17_End_Date - today
        else:
            Task17_delta = None
        if device.ProductSupport.Task18_End_Date:
            Task18_delta = device.ProductSupport.Task18_End_Date - today
        else:
            Task18_delta = None
        if device.ProductSupport.Task19_End_Date:
            Task19_delta = device.ProductSupport.Task19_End_Date - today
        else:
            Task19_delta = None
        if device.ProductSupport.Task20_End_Date:
            Task20_delta = device.ProductSupport.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not device.ProductSupport.Task1_complete_date:
            device.ProductSupport.Task1_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not device.ProductSupport.Task2_complete_date:
            device.ProductSupport.Task2_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not device.ProductSupport.Task3_complete_date:
            device.ProductSupport.Task3_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not device.ProductSupport.Task4_complete_date:
            device.ProductSupport.Task4_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not device.ProductSupport.Task5_complete_date:
            device.ProductSupport.Task5_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not device.ProductSupport.Task6_complete_date:
            device.ProductSupport.Task6_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not device.ProductSupport.Task7_complete_date:
            device.ProductSupport.Task7_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not device.ProductSupport.Task8_complete_date:
            device.ProductSupport.Task8_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not device.ProductSupport.Task9_complete_date:
            device.ProductSupport.Task9_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not device.ProductSupport.Task10_complete_date:
            device.ProductSupport.Task10_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not device.ProductSupport.Task11_complete_date:
            device.ProductSupport.Task11_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not device.ProductSupport.Task12_complete_date:
            device.ProductSupport.Task12_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not device.ProductSupport.Task13_complete_date:
            device.ProductSupport.Task13_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not device.ProductSupport.Task14_complete_date:
            device.ProductSupport.Task14_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not device.ProductSupport.Task15_complete_date:
            device.ProductSupport.Task15_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not device.ProductSupport.Task16_complete_date:
            device.ProductSupport.Task16_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not device.ProductSupport.Task17_complete_date:
            device.ProductSupport.Task17_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not device.ProductSupport.Task18_complete_date:
            device.ProductSupport.Task18_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not device.ProductSupport.Task19_complete_date:
            device.ProductSupport.Task19_warning = True
            device.ProductSupport.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(device.ProductSupport.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not device.ProductSupport.Task20_complete_date:
            device.ProductSupport.Task20_warning = True
            device.ProductSupport.Status = 'At Risk'


        if device.ProductSupport.Task1_End_Date and Task1_delta < timedelta(0) and not device.ProductSupport.Task1_complete_date:
            device.ProductSupport.Task1_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task2_End_Date and Task2_delta < timedelta(0) and not device.ProductSupport.Task2_complete_date:
            device.ProductSupport.Task2_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task3_End_Date and Task3_delta < timedelta(0) and not device.ProductSupport.Task3_complete_date:
            device.ProductSupport.Task3_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task4_End_Date and Task4_delta < timedelta(0) and not device.ProductSupport.Task4_complete_date:
            device.ProductSupport.Task4_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task5_End_Date and Task5_delta < timedelta(0) and not device.ProductSupport.Task5_complete_date:
            device.ProductSupport.Task5_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task6_End_Date and Task6_delta < timedelta(0) and not device.ProductSupport.Task6_complete_date:
            device.ProductSupport.Task6_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task7_End_Date and Task7_delta < timedelta(0) and not device.ProductSupport.Task7_complete_date:
            device.ProductSupport.Task7_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task8_End_Date and Task8_delta < timedelta(0)and not device.ProductSupport.Task8_complete_date:
            device.ProductSupport.Task8_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task9_End_Date and Task9_delta < timedelta(0)and not device.ProductSupport.Task9_complete_date:
            device.ProductSupport.Task9_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task10_End_Date and Task10_delta < timedelta(0) and not device.ProductSupport.Task10_complete_date:
            device.ProductSupport.Task10_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task11_End_Date and Task11_delta < timedelta(0) and not device.ProductSupport.Task11_complete_date:
            device.ProductSupport.Task11_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task12_End_Date and Task12_delta < timedelta(0) and not device.ProductSupport.Task12_complete_date:
            device.ProductSupport.Task12_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task13_End_Date and Task13_delta < timedelta(0) and not device.ProductSupport.Task13_complete_date:
            device.ProductSupport.Task13_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task14_End_Date and Task14_delta < timedelta(0) and not device.ProductSupport.Task14_complete_date:
            device.ProductSupport.Task14_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task15_End_Date and Task15_delta < timedelta(0) and not device.ProductSupport.Task15_complete_date:
            device.ProductSupport.Task15_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task16_End_Date and Task16_delta < timedelta(0) and not device.ProductSupport.Task16_complete_date:
            device.ProductSupport.Task16_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task17_End_Date and Task17_delta < timedelta(0)and not device.ProductSupport.Task17_complete_date:
            device.ProductSupport.Task17_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task18_End_Date and Task18_delta < timedelta(0)and not device.ProductSupport.Task18_complete_date:
            device.ProductSupport.Task18_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task19_End_Date and Task19_delta < timedelta(0)and not device.ProductSupport.Task19_complete_date:
            device.ProductSupport.Task19_alert = True
            device.ProductSupport.Status = 'Delayed'
        if device.ProductSupport.Task20_End_Date and Task20_delta < timedelta(0)and not device.ProductSupport.Task20_complete_date:
            device.ProductSupport.Task20_alert = True
            device.ProductSupport.Status = 'Delayed'

        device.ProductSupport.save()


        device.Warehouse.Task1_alert = False
        device.Warehouse.Task1_warning = False
        device.Warehouse.Status = 'On_Time'

        device.Warehouse.Task2_alert = False
        device.Warehouse.Task2_warning = False

        device.Warehouse.Task3_alert = False
        device.Warehouse.Task3_warning = False

        device.Warehouse.Task4_alert = False
        device.Warehouse.Task4_warning = False

        device.Warehouse.Task5_alert = False
        device.Warehouse.Task5_warning = False

        device.Warehouse.Task6_alert = False
        device.Warehouse.Task6_warning = False

        device.Warehouse.Task7_alert = False
        device.Warehouse.Task7_warning = False

        device.Warehouse.Task8_alert = False
        device.Warehouse.Task8_warning = False

        device.Warehouse.Task9_alert = False
        device.Warehouse.Task9_warning = False

        device.Warehouse.Task10_alert = False
        device.Warehouse.Task10_warning = False

        device.Warehouse.Task11_alert = False
        device.Warehouse.Task11_warning = False

        device.Warehouse.Task12_alert = False
        device.Warehouse.Task12_warning = False

        device.Warehouse.Task13_alert = False
        device.Warehouse.Task13_warning = False

        device.Warehouse.Task14_alert = False
        device.Warehouse.Task14_warning = False

        device.Warehouse.Task15_alert = False
        device.Warehouse.Task15_warning = False

        device.Warehouse.Task16_alert = False
        device.Warehouse.Task16_warning = False

        device.Warehouse.Task17_alert = False
        device.Warehouse.Task17_warning = False

        device.Warehouse.Task18_alert = False
        device.Warehouse.Task18_warning = False

        device.Warehouse.Task19_alert = False
        device.Warehouse.Task19_warning = False

        device.Warehouse.Task20_alert = False
        device.Warehouse.Task20_warning = False

        y = activeTasksW(device)

        x = 0
        if device.Warehouse.Task1_complete_date:
            x = x + 1
        if device.Warehouse.Task2_complete_date:
            x = x + 1
        if device.Warehouse.Task3_complete_date:
            x = x + 1
        if device.Warehouse.Task4_complete_date:
            x = x + 1
        if device.Warehouse.Task5_complete_date:
            x = x + 1
        if device.Warehouse.Task6_complete_date:
            x = x + 1
        if device.Warehouse.Task7_complete_date:
            x = x + 1
        if device.Warehouse.Task8_complete_date:
            x = x + 1
        if device.Warehouse.Task9_complete_date:
            x = x + 1
        if device.Warehouse.Task10_complete_date:
            x = x + 1
        if device.Warehouse.Task11_complete_date:
            x = x + 1
        if device.Warehouse.Task12_complete_date:
            x = x + 1
        if device.Warehouse.Task13_complete_date:
            x = x + 1
        if device.Warehouse.Task14_complete_date:
            x = x + 1
        if device.Warehouse.Task15_complete_date:
            x = x + 1
        if device.Warehouse.Task16_complete_date:
            x = x + 1
        if device.Warehouse.Task17_complete_date:
            x = x + 1
        if device.Warehouse.Task18_complete_date:
            x = x + 1
        if device.Warehouse.Task19_complete_date:
            x = x + 1
        if device.Warehouse.Task20_complete_date:
            x = x + 1
        percent = x / y * 100
        device.Warehouse.completed = int(percent)

        #alerting logic
        today = datetime.date.today()
        if device.Warehouse.Task1_End_Date:
            Task1_delta =  device.Warehouse.Task1_End_Date - today
        else:
            Task1_delta = None
        if device.Warehouse.Task2_End_Date:
            Task2_delta = device.Warehouse.Task2_End_Date - today
        else:
            Task2_delta = None
        if device.Warehouse.Task3_End_Date:
            Task3_delta = device.Warehouse.Task3_End_Date - today
        else:
            Task3_delta = None
        if device.Warehouse.Task4_End_Date:
            Task4_delta = device.Warehouse.Task4_End_Date - today
        else:
            Task4_delta = None
        if device.Warehouse.Task5_End_Date:
            Task5_delta = device.Warehouse.Task5_End_Date - today
        else:
            Task5_delta = None
        if device.Warehouse.Task6_End_Date:
            Task6_delta = device.Warehouse.Task6_End_Date - today
        else:
            Task6_delta = None
        if device.Warehouse.Task7_End_Date:
            Task7_delta = device.Warehouse.Task7_End_Date - today
        else:
            Task7_delta = None
        if device.Warehouse.Task8_End_Date:
            Task8_delta = device.Warehouse.Task8_End_Date - today
        else:
            Task8_delta = None
        if device.Warehouse.Task9_End_Date:
            Task9_delta = device.Warehouse.Task9_End_Date - today
        else:
            Task9_delta = None
        if device.Warehouse.Task10_End_Date:
            Task10_delta =  device.Warehouse.Task10_End_Date - today
        else:
            Task10_delta = None
        if device.Warehouse.Task11_End_Date:
            Task11_delta =  device.Warehouse.Task11_End_Date - today
        else:
            Task11_delta = None
        if device.Warehouse.Task12_End_Date:
            Task12_delta = device.Warehouse.Task12_End_Date - today
        else:
            Task12_delta = None
        if device.Warehouse.Task13_End_Date:
            Task13_delta = device.Warehouse.Task13_End_Date - today
        else:
            Task13_delta = None
        if device.Warehouse.Task14_End_Date:
            Task14_delta = device.Warehouse.Task14_End_Date - today
        else:
            Task14_delta = None
        if device.Warehouse.Task15_End_Date:
            Task15_delta = device.Warehouse.Task15_End_Date - today
        else:
            Task15_delta = None
        if device.Warehouse.Task16_End_Date:
            Task16_delta = device.Warehouse.Task16_End_Date - today
        else:
            Task16_delta = None
        if device.Warehouse.Task17_End_Date:
            Task17_delta = device.Warehouse.Task17_End_Date - today
        else:
            Task17_delta = None
        if device.Warehouse.Task18_End_Date:
            Task18_delta = device.Warehouse.Task18_End_Date - today
        else:
            Task18_delta = None
        if device.Warehouse.Task19_End_Date:
            Task19_delta = device.Warehouse.Task19_End_Date - today
        else:
            Task19_delta = None
        if device.Warehouse.Task20_End_Date:
            Task20_delta = device.Warehouse.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not device.Warehouse.Task1_complete_date:
            device.Warehouse.Task1_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not device.Warehouse.Task2_complete_date:
            device.Warehouse.Task2_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not device.Warehouse.Task3_complete_date:
            device.Warehouse.Task3_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not device.Warehouse.Task4_complete_date:
            device.Warehouse.Task4_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not device.Warehouse.Task5_complete_date:
            device.Warehouse.Task5_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not device.Warehouse.Task6_complete_date:
            device.Warehouse.Task6_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not device.Warehouse.Task7_complete_date:
            device.Warehouse.Task7_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not device.Warehouse.Task8_complete_date:
            device.Warehouse.Task8_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not device.Warehouse.Task9_complete_date:
            device.Warehouse.Task9_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not device.Warehouse.Task10_complete_date:
            device.Warehouse.Task10_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not device.Warehouse.Task11_complete_date:
            device.Warehouse.Task11_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not device.Warehouse.Task12_complete_date:
            device.Warehouse.Task12_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not device.Warehouse.Task13_complete_date:
            device.Warehouse.Task13_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not device.Warehouse.Task14_complete_date:
            device.Warehouse.Task14_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not device.Warehouse.Task15_complete_date:
            device.Warehouse.Task15_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not device.Warehouse.Task16_complete_date:
            device.Warehouse.Task16_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not device.Warehouse.Task17_complete_date:
            device.Warehouse.Task17_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not device.Warehouse.Task18_complete_date:
            device.Warehouse.Task18_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not device.Warehouse.Task19_complete_date:
            device.Warehouse.Task19_warning = True
            device.Warehouse.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(device.Warehouse.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not device.Warehouse.Task20_complete_date:
            device.Warehouse.Task20_warning = True
            device.Warehouse.Status = 'At Risk'


        if device.Warehouse.Task1_End_Date and Task1_delta < timedelta(0) and not device.Warehouse.Task1_complete_date:
            device.Warehouse.Task1_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task2_End_Date and Task2_delta < timedelta(0) and not device.Warehouse.Task2_complete_date:
            device.Warehouse.Task2_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task3_End_Date and Task3_delta < timedelta(0) and not device.Warehouse.Task3_complete_date:
            device.Warehouse.Task3_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task4_End_Date and Task4_delta < timedelta(0) and not device.Warehouse.Task4_complete_date:
            device.Warehouse.Task4_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task5_End_Date and Task5_delta < timedelta(0) and not device.Warehouse.Task5_complete_date:
            device.Warehouse.Task5_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task6_End_Date and Task6_delta < timedelta(0) and not device.Warehouse.Task6_complete_date:
            device.Warehouse.Task6_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task7_End_Date and Task7_delta < timedelta(0) and not device.Warehouse.Task7_complete_date:
            device.Warehouse.Task7_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task8_End_Date and Task8_delta < timedelta(0)and not device.Warehouse.Task8_complete_date:
            device.Warehouse.Task8_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task9_End_Date and Task9_delta < timedelta(0)and not device.Warehouse.Task9_complete_date:
            device.Warehouse.Task9_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task10_End_Date and Task10_delta < timedelta(0) and not device.Warehouse.Task10_complete_date:
            device.Warehouse.Task10_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task11_End_Date and Task11_delta < timedelta(0) and not device.Warehouse.Task11_complete_date:
            device.Warehouse.Task11_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task12_End_Date and Task12_delta < timedelta(0) and not device.Warehouse.Task12_complete_date:
            device.Warehouse.Task12_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task13_End_Date and Task13_delta < timedelta(0) and not device.Warehouse.Task13_complete_date:
            device.Warehouse.Task13_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task14_End_Date and Task14_delta < timedelta(0) and not device.Warehouse.Task14_complete_date:
            device.Warehouse.Task14_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task15_End_Date and Task15_delta < timedelta(0) and not device.Warehouse.Task15_complete_date:
            device.Warehouse.Task15_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task16_End_Date and Task16_delta < timedelta(0) and not device.Warehouse.Task16_complete_date:
            device.Warehouse.Task16_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task17_End_Date and Task17_delta < timedelta(0)and not device.Warehouse.Task17_complete_date:
            device.Warehouse.Task17_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task18_End_Date and Task18_delta < timedelta(0)and not device.Warehouse.Task18_complete_date:
            device.Warehouse.Task18_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task19_End_Date and Task19_delta < timedelta(0)and not device.Warehouse.Task19_complete_date:
            device.Warehouse.Task19_alert = True
            device.Warehouse.Status = 'Delayed'
        if device.Warehouse.Task20_End_Date and Task20_delta < timedelta(0)and not device.Warehouse.Task20_complete_date:
            device.Warehouse.Task20_alert = True
            device.Warehouse.Status = 'Delayed'

        device.Warehouse.save()

        device.FieldService.Task1_alert = False
        device.FieldService.Task1_warning = False
        device.FieldService.Status = 'On_Time'

        device.FieldService.Task2_alert = False
        device.FieldService.Task2_warning = False

        device.FieldService.Task3_alert = False
        device.FieldService.Task3_warning = False

        device.FieldService.Task4_alert = False
        device.FieldService.Task4_warning = False

        device.FieldService.Task5_alert = False
        device.FieldService.Task5_warning = False

        device.FieldService.Task6_alert = False
        device.FieldService.Task6_warning = False

        device.FieldService.Task7_alert = False
        device.FieldService.Task7_warning = False

        device.FieldService.Task8_alert = False
        device.FieldService.Task8_warning = False

        device.FieldService.Task9_alert = False
        device.FieldService.Task9_warning = False

        device.FieldService.Task10_alert = False
        device.FieldService.Task10_warning = False

        device.FieldService.Task11_alert = False
        device.FieldService.Task11_warning = False

        device.FieldService.Task12_alert = False
        device.FieldService.Task12_warning = False

        device.FieldService.Task13_alert = False
        device.FieldService.Task13_warning = False

        device.FieldService.Task14_alert = False
        device.FieldService.Task14_warning = False

        device.FieldService.Task15_alert = False
        device.FieldService.Task15_warning = False

        device.FieldService.Task16_alert = False
        device.FieldService.Task16_warning = False

        device.FieldService.Task17_alert = False
        device.FieldService.Task17_warning = False

        device.FieldService.Task18_alert = False
        device.FieldService.Task18_warning = False

        device.FieldService.Task19_alert = False
        device.FieldService.Task19_warning = False

        device.FieldService.Task20_alert = False
        device.FieldService.Task20_warning = False

        y = activeTasksFS(device)

        x = 0
        if device.FieldService.Task1_complete_date:
            x = x + 1
        if device.FieldService.Task2_complete_date:
            x = x + 1
        if device.FieldService.Task3_complete_date:
            x = x + 1
        if device.FieldService.Task4_complete_date:
            x = x + 1
        if device.FieldService.Task5_complete_date:
            x = x + 1
        if device.FieldService.Task6_complete_date:
            x = x + 1
        if device.FieldService.Task7_complete_date:
            x = x + 1
        if device.FieldService.Task8_complete_date:
            x = x + 1
        if device.FieldService.Task9_complete_date:
            x = x + 1
        if device.FieldService.Task10_complete_date:
            x = x + 1
        if device.FieldService.Task11_complete_date:
            x = x + 1
        if device.FieldService.Task12_complete_date:
            x = x + 1
        if device.FieldService.Task13_complete_date:
            x = x + 1
        if device.FieldService.Task14_complete_date:
            x = x + 1
        if device.FieldService.Task15_complete_date:
            x = x + 1
        if device.FieldService.Task16_complete_date:
            x = x + 1
        if device.FieldService.Task17_complete_date:
            x = x + 1
        if device.FieldService.Task18_complete_date:
            x = x + 1
        if device.FieldService.Task19_complete_date:
            x = x + 1
        if device.FieldService.Task20_complete_date:
            x = x + 1
        percent = x / y * 100
        device.FieldService.completed = int(percent)

        #alerting logic
        today = datetime.date.today()
        if device.FieldService.Task1_End_Date:
            Task1_delta =  device.FieldService.Task1_End_Date - today
        else:
            Task1_delta = None
        if device.FieldService.Task2_End_Date:
            Task2_delta = device.FieldService.Task2_End_Date - today
        else:
            Task2_delta = None
        if device.FieldService.Task3_End_Date:
            Task3_delta = device.FieldService.Task3_End_Date - today
        else:
            Task3_delta = None
        if device.FieldService.Task4_End_Date:
            Task4_delta = device.FieldService.Task4_End_Date - today
        else:
            Task4_delta = None
        if device.FieldService.Task5_End_Date:
            Task5_delta = device.FieldService.Task5_End_Date - today
        else:
            Task5_delta = None
        if device.FieldService.Task6_End_Date:
            Task6_delta = device.FieldService.Task6_End_Date - today
        else:
            Task6_delta = None
        if device.FieldService.Task7_End_Date:
            Task7_delta = device.FieldService.Task7_End_Date - today
        else:
            Task7_delta = None
        if device.FieldService.Task8_End_Date:
            Task8_delta = device.FieldService.Task8_End_Date - today
        else:
            Task8_delta = None
        if device.FieldService.Task9_End_Date:
            Task9_delta = device.FieldService.Task9_End_Date - today
        else:
            Task9_delta = None
        if device.FieldService.Task10_End_Date:
            Task10_delta =  device.FieldService.Task10_End_Date - today
        else:
            Task10_delta = None
        if device.FieldService.Task11_End_Date:
            Task11_delta =  device.FieldService.Task11_End_Date - today
        else:
            Task11_delta = None
        if device.FieldService.Task12_End_Date:
            Task12_delta = device.FieldService.Task12_End_Date - today
        else:
            Task12_delta = None
        if device.FieldService.Task13_End_Date:
            Task13_delta = device.FieldService.Task13_End_Date - today
        else:
            Task13_delta = None
        if device.FieldService.Task14_End_Date:
            Task14_delta = device.FieldService.Task14_End_Date - today
        else:
            Task14_delta = None
        if device.FieldService.Task15_End_Date:
            Task15_delta = device.FieldService.Task15_End_Date - today
        else:
            Task15_delta = None
        if device.FieldService.Task16_End_Date:
            Task16_delta = device.FieldService.Task16_End_Date - today
        else:
            Task16_delta = None
        if device.FieldService.Task17_End_Date:
            Task17_delta = device.FieldService.Task17_End_Date - today
        else:
            Task17_delta = None
        if device.FieldService.Task18_End_Date:
            Task18_delta = device.FieldService.Task18_End_Date - today
        else:
            Task18_delta = None
        if device.FieldService.Task19_End_Date:
            Task19_delta = device.FieldService.Task19_End_Date - today
        else:
            Task19_delta = None
        if device.FieldService.Task20_End_Date:
            Task20_delta = device.FieldService.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not device.FieldService.Task1_complete_date:
            device.FieldService.Task1_warning = True
            device.FieldService.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not device.FieldService.Task2_complete_date:
            device.FieldService.Task2_warning = True
            device.FieldService.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not device.FieldService.Task3_complete_date:
            device.FieldService.Task3_warning = True
            device.FieldService.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not device.FieldService.Task4_complete_date:
            device.FieldService.Task4_warning = True
            device.FieldService.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not device.FieldService.Task5_complete_date:
            device.FieldService.Task5_warning = True
            device.FieldService.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not device.FieldService.Task6_complete_date:
            device.FieldService.Task6_warning = True
            device.FieldService.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not device.FieldService.Task7_complete_date:
            device.FieldService.Task7_warning = True
            device.FieldService.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not device.FieldService.Task8_complete_date:
            device.FieldService.Task8_warning = True
            device.FieldService.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not device.FieldService.Task9_complete_date:
            device.FieldService.Task9_warning = True
            device.FieldService.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not device.FieldService.Task10_complete_date:
            device.FieldService.Task10_warning = True
            device.FieldService.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not device.FieldService.Task11_complete_date:
            device.FieldService.Task11_warning = True
            device.FieldService.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not device.FieldService.Task12_complete_date:
            device.FieldService.Task12_warning = True
            device.FieldService.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not device.FieldService.Task13_complete_date:
            device.FieldService.Task13_warning = True
            device.FieldService.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not device.FieldService.Task14_complete_date:
            device.FieldService.Task14_warning = True
            device.FieldService.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not device.FieldService.Task15_complete_date:
            device.FieldService.Task15_warning = True
            device.FieldService.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not device.FieldService.Task16_complete_date:
            device.FieldService.Task16_warning = True
            device.FieldService.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not device.FieldService.Task17_complete_date:
            device.FieldService.Task17_warning = True
            device.FieldService.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not device.FieldService.Task18_complete_date:
            device.FieldService.Task18_warning = True
            device.FieldService.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not device.FieldService.Task19_complete_date:
            device.FieldService.Task19_warning = True
            device.FieldService.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(device.FieldService.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not device.FieldService.Task20_complete_date:
            device.FieldService.Task20_warning = True
            device.FieldService.Status = 'At Risk'


        if device.FieldService.Task1_End_Date and Task1_delta < timedelta(0) and not device.FieldService.Task1_complete_date:
            device.FieldService.Task1_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task2_End_Date and Task2_delta < timedelta(0) and not device.FieldService.Task2_complete_date:
            device.FieldService.Task2_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task3_End_Date and Task3_delta < timedelta(0) and not device.FieldService.Task3_complete_date:
            device.FieldService.Task3_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task4_End_Date and Task4_delta < timedelta(0) and not device.FieldService.Task4_complete_date:
            device.FieldService.Task4_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task5_End_Date and Task5_delta < timedelta(0) and not device.FieldService.Task5_complete_date:
            device.FieldService.Task5_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task6_End_Date and Task6_delta < timedelta(0) and not device.FieldService.Task6_complete_date:
            device.FieldService.Task6_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task7_End_Date and Task7_delta < timedelta(0) and not device.FieldService.Task7_complete_date:
            device.FieldService.Task7_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task8_End_Date and Task8_delta < timedelta(0)and not device.FieldService.Task8_complete_date:
            device.FieldService.Task8_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task9_End_Date and Task9_delta < timedelta(0)and not device.FieldService.Task9_complete_date:
            device.FieldService.Task9_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task10_End_Date and Task10_delta < timedelta(0) and not device.FieldService.Task10_complete_date:
            device.FieldService.Task10_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task11_End_Date and Task11_delta < timedelta(0) and not device.FieldService.Task11_complete_date:
            device.FieldService.Task11_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task12_End_Date and Task12_delta < timedelta(0) and not device.FieldService.Task12_complete_date:
            device.FieldService.Task12_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task13_End_Date and Task13_delta < timedelta(0) and not device.FieldService.Task13_complete_date:
            device.FieldService.Task13_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task14_End_Date and Task14_delta < timedelta(0) and not device.FieldService.Task14_complete_date:
            device.FieldService.Task14_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task15_End_Date and Task15_delta < timedelta(0) and not device.FieldService.Task15_complete_date:
            device.FieldService.Task15_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task16_End_Date and Task16_delta < timedelta(0) and not device.FieldService.Task16_complete_date:
            device.FieldService.Task16_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task17_End_Date and Task17_delta < timedelta(0)and not device.FieldService.Task17_complete_date:
            device.FieldService.Task17_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task18_End_Date and Task18_delta < timedelta(0)and not device.FieldService.Task18_complete_date:
            device.FieldService.Task18_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task19_End_Date and Task19_delta < timedelta(0)and not device.FieldService.Task19_complete_date:
            device.FieldService.Task19_alert = True
            device.FieldService.Status = 'Delayed'
        if device.FieldService.Task20_End_Date and Task20_delta < timedelta(0)and not device.FieldService.Task20_complete_date:
            device.FieldService.Task20_alert = True
            device.FieldService.Status = 'Delayed'

        device.FieldService.save()

        device.TechSupport.Task1_alert = False
        device.TechSupport.Task1_warning = False
        device.TechSupport.Status = 'On_Time'

        device.TechSupport.Task2_alert = False
        device.TechSupport.Task2_warning = False

        device.TechSupport.Task3_alert = False
        device.TechSupport.Task3_warning = False

        device.TechSupport.Task4_alert = False
        device.TechSupport.Task4_warning = False

        device.TechSupport.Task5_alert = False
        device.TechSupport.Task5_warning = False

        device.TechSupport.Task6_alert = False
        device.TechSupport.Task6_warning = False

        device.TechSupport.Task7_alert = False
        device.TechSupport.Task7_warning = False

        device.TechSupport.Task8_alert = False
        device.TechSupport.Task8_warning = False

        device.TechSupport.Task9_alert = False
        device.TechSupport.Task9_warning = False

        device.TechSupport.Task10_alert = False
        device.TechSupport.Task10_warning = False

        device.TechSupport.Task11_alert = False
        device.TechSupport.Task11_warning = False

        device.TechSupport.Task12_alert = False
        device.TechSupport.Task12_warning = False

        device.TechSupport.Task13_alert = False
        device.TechSupport.Task13_warning = False

        device.TechSupport.Task14_alert = False
        device.TechSupport.Task14_warning = False

        device.TechSupport.Task15_alert = False
        device.TechSupport.Task15_warning = False

        device.TechSupport.Task16_alert = False
        device.TechSupport.Task16_warning = False

        device.TechSupport.Task17_alert = False
        device.TechSupport.Task17_warning = False

        device.TechSupport.Task18_alert = False
        device.TechSupport.Task18_warning = False

        device.TechSupport.Task19_alert = False
        device.TechSupport.Task19_warning = False

        device.TechSupport.Task20_alert = False
        device.TechSupport.Task20_warning = False

        y = activeTasksTS(device)

        x = 0
        if device.TechSupport.Task1_complete_date:
            x = x + 1
        if device.TechSupport.Task2_complete_date:
            x = x + 1
        if device.TechSupport.Task3_complete_date:
            x = x + 1
        if device.TechSupport.Task4_complete_date:
            x = x + 1
        if device.TechSupport.Task5_complete_date:
            x = x + 1
        if device.TechSupport.Task6_complete_date:
            x = x + 1
        if device.TechSupport.Task7_complete_date:
            x = x + 1
        if device.TechSupport.Task8_complete_date:
            x = x + 1
        if device.TechSupport.Task9_complete_date:
            x = x + 1
        if device.TechSupport.Task10_complete_date:
            x = x + 1
        if device.TechSupport.Task11_complete_date:
            x = x + 1
        if device.TechSupport.Task12_complete_date:
            x = x + 1
        if device.TechSupport.Task13_complete_date:
            x = x + 1
        if device.TechSupport.Task14_complete_date:
            x = x + 1
        if device.TechSupport.Task15_complete_date:
            x = x + 1
        if device.TechSupport.Task16_complete_date:
            x = x + 1
        if device.TechSupport.Task17_complete_date:
            x = x + 1
        if device.TechSupport.Task18_complete_date:
            x = x + 1
        if device.TechSupport.Task19_complete_date:
            x = x + 1
        if device.TechSupport.Task20_complete_date:
            x = x + 1
        percent = x / y * 100
        device.TechSupport.completed = int(percent)

        #alerting logic
        today = datetime.date.today()
        if device.TechSupport.Task1_End_Date:
            Task1_delta =  device.TechSupport.Task1_End_Date - today
        else:
            Task1_delta = None
        if device.TechSupport.Task2_End_Date:
            Task2_delta = device.TechSupport.Task2_End_Date - today
        else:
            Task2_delta = None
        if device.TechSupport.Task3_End_Date:
            Task3_delta = device.TechSupport.Task3_End_Date - today
        else:
            Task3_delta = None
        if device.TechSupport.Task4_End_Date:
            Task4_delta = device.TechSupport.Task4_End_Date - today
        else:
            Task4_delta = None
        if device.TechSupport.Task5_End_Date:
            Task5_delta = device.TechSupport.Task5_End_Date - today
        else:
            Task5_delta = None
        if device.TechSupport.Task6_End_Date:
            Task6_delta = device.TechSupport.Task6_End_Date - today
        else:
            Task6_delta = None
        if device.TechSupport.Task7_End_Date:
            Task7_delta = device.TechSupport.Task7_End_Date - today
        else:
            Task7_delta = None
        if device.TechSupport.Task8_End_Date:
            Task8_delta = device.TechSupport.Task8_End_Date - today
        else:
            Task8_delta = None
        if device.TechSupport.Task9_End_Date:
            Task9_delta = device.TechSupport.Task9_End_Date - today
        else:
            Task9_delta = None
        if device.TechSupport.Task10_End_Date:
            Task10_delta =  device.TechSupport.Task10_End_Date - today
        else:
            Task10_delta = None
        if device.TechSupport.Task11_End_Date:
            Task11_delta =  device.TechSupport.Task11_End_Date - today
        else:
            Task11_delta = None
        if device.TechSupport.Task12_End_Date:
            Task12_delta = device.TechSupport.Task12_End_Date - today
        else:
            Task12_delta = None
        if device.TechSupport.Task13_End_Date:
            Task13_delta = device.TechSupport.Task13_End_Date - today
        else:
            Task13_delta = None
        if device.TechSupport.Task14_End_Date:
            Task14_delta = device.TechSupport.Task14_End_Date - today
        else:
            Task14_delta = None
        if device.TechSupport.Task15_End_Date:
            Task15_delta = device.TechSupport.Task15_End_Date - today
        else:
            Task15_delta = None
        if device.TechSupport.Task16_End_Date:
            Task16_delta = device.TechSupport.Task16_End_Date - today
        else:
            Task16_delta = None
        if device.TechSupport.Task17_End_Date:
            Task17_delta = device.TechSupport.Task17_End_Date - today
        else:
            Task17_delta = None
        if device.TechSupport.Task18_End_Date:
            Task18_delta = device.TechSupport.Task18_End_Date - today
        else:
            Task18_delta = None
        if device.TechSupport.Task19_End_Date:
            Task19_delta = device.TechSupport.Task19_End_Date - today
        else:
            Task19_delta = None
        if device.TechSupport.Task20_End_Date:
            Task20_delta = device.TechSupport.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not device.TechSupport.Task1_complete_date:
            device.TechSupport.Task1_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not device.TechSupport.Task2_complete_date:
            device.TechSupport.Task2_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not device.TechSupport.Task3_complete_date:
            device.TechSupport.Task3_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not device.TechSupport.Task4_complete_date:
            device.TechSupport.Task4_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not device.TechSupport.Task5_complete_date:
            device.TechSupport.Task5_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not device.TechSupport.Task6_complete_date:
            device.TechSupport.Task6_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not device.TechSupport.Task7_complete_date:
            device.TechSupport.Task7_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not device.TechSupport.Task8_complete_date:
            device.TechSupport.Task8_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not device.TechSupport.Task9_complete_date:
            device.TechSupport.Task9_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not device.TechSupport.Task10_complete_date:
            device.TechSupport.Task10_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not device.TechSupport.Task11_complete_date:
            device.TechSupport.Task11_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not device.TechSupport.Task12_complete_date:
            device.TechSupport.Task12_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not device.TechSupport.Task13_complete_date:
            device.TechSupport.Task13_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not device.TechSupport.Task14_complete_date:
            device.TechSupport.Task14_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not device.TechSupport.Task15_complete_date:
            device.TechSupport.Task15_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not device.TechSupport.Task16_complete_date:
            device.TechSupport.Task16_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not device.TechSupport.Task17_complete_date:
            device.TechSupport.Task17_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not device.TechSupport.Task18_complete_date:
            device.TechSupport.Task18_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not device.TechSupport.Task19_complete_date:
            device.TechSupport.Task19_warning = True
            device.TechSupport.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(device.TechSupport.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not device.TechSupport.Task20_complete_date:
            device.TechSupport.Task20_warning = True
            device.TechSupport.Status = 'At Risk'

        if device.TechSupport.Task1_End_Date and Task1_delta < timedelta(0) and not device.TechSupport.Task1_complete_date:
            device.TechSupport.Task1_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task2_End_Date and Task2_delta < timedelta(0) and not device.TechSupport.Task2_complete_date:
            device.TechSupport.Task2_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task3_End_Date and Task3_delta < timedelta(0) and not device.TechSupport.Task3_complete_date:
            device.TechSupport.Task3_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task4_End_Date and Task4_delta < timedelta(0) and not device.TechSupport.Task4_complete_date:
            device.TechSupport.Task4_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task5_End_Date and Task5_delta < timedelta(0) and not device.TechSupport.Task5_complete_date:
            device.TechSupport.Task5_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task6_End_Date and Task6_delta < timedelta(0) and not device.TechSupport.Task6_complete_date:
            device.TechSupport.Task6_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task7_End_Date and Task7_delta < timedelta(0) and not device.TechSupport.Task7_complete_date:
            device.TechSupport.Task7_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task8_End_Date and Task8_delta < timedelta(0)and not device.TechSupport.Task8_complete_date:
            device.TechSupport.Task8_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task9_End_Date and Task9_delta < timedelta(0)and not device.TechSupport.Task9_complete_date:
            device.TechSupport.Task9_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task10_End_Date and Task10_delta < timedelta(0) and not device.TechSupport.Task10_complete_date:
            device.TechSupport.Task10_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task11_End_Date and Task11_delta < timedelta(0) and not device.TechSupport.Task11_complete_date:
            device.TechSupport.Task11_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task12_End_Date and Task12_delta < timedelta(0) and not device.TechSupport.Task12_complete_date:
            device.TechSupport.Task12_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task13_End_Date and Task13_delta < timedelta(0) and not device.TechSupport.Task13_complete_date:
            device.TechSupport.Task13_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task14_End_Date and Task14_delta < timedelta(0) and not device.TechSupport.Task14_complete_date:
            device.TechSupport.Task14_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task15_End_Date and Task15_delta < timedelta(0) and not device.TechSupport.Task15_complete_date:
            device.TechSupport.Task15_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task16_End_Date and Task16_delta < timedelta(0) and not device.TechSupport.Task16_complete_date:
            device.TechSupport.Task16_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task17_End_Date and Task17_delta < timedelta(0)and not device.TechSupport.Task17_complete_date:
            device.TechSupport.Task17_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task18_End_Date and Task18_delta < timedelta(0)and not device.TechSupport.Task18_complete_date:
            device.TechSupport.Task18_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task19_End_Date and Task19_delta < timedelta(0)and not device.TechSupport.Task19_complete_date:
            device.TechSupport.Task19_alert = True
            device.TechSupport.Status = 'Delayed'
        if device.TechSupport.Task20_End_Date and Task20_delta < timedelta(0)and not device.TechSupport.Task20_complete_date:
            device.TechSupport.Task20_alert = True
            device.TechSupport.Status = 'Delayed'

        device.TechSupport.save()


        device.ServiceMarketing.Task1_alert = False
        device.ServiceMarketing.Task1_warning = False
        device.ServiceMarketing.Status = 'On_Time'

        device.ServiceMarketing.Task2_alert = False
        device.ServiceMarketing.Task2_warning = False

        device.ServiceMarketing.Task3_alert = False
        device.ServiceMarketing.Task3_warning = False

        device.ServiceMarketing.Task4_alert = False
        device.ServiceMarketing.Task4_warning = False

        device.ServiceMarketing.Task5_alert = False
        device.ServiceMarketing.Task5_warning = False

        device.ServiceMarketing.Task6_alert = False
        device.ServiceMarketing.Task6_warning = False

        device.ServiceMarketing.Task7_alert = False
        device.ServiceMarketing.Task7_warning = False

        device.ServiceMarketing.Task8_alert = False
        device.ServiceMarketing.Task8_warning = False

        device.ServiceMarketing.Task9_alert = False
        device.ServiceMarketing.Task9_warning = False

        device.ServiceMarketing.Task10_alert = False
        device.ServiceMarketing.Task10_warning = False

        device.ServiceMarketing.Task11_alert = False
        device.ServiceMarketing.Task11_warning = False

        device.ServiceMarketing.Task12_alert = False
        device.ServiceMarketing.Task12_warning = False

        device.ServiceMarketing.Task13_alert = False
        device.ServiceMarketing.Task13_warning = False

        device.ServiceMarketing.Task14_alert = False
        device.ServiceMarketing.Task14_warning = False

        device.ServiceMarketing.Task15_alert = False
        device.ServiceMarketing.Task15_warning = False

        device.ServiceMarketing.Task16_alert = False
        device.ServiceMarketing.Task16_warning = False

        device.ServiceMarketing.Task17_alert = False
        device.ServiceMarketing.Task17_warning = False

        device.ServiceMarketing.Task18_alert = False
        device.ServiceMarketing.Task18_warning = False

        device.ServiceMarketing.Task19_alert = False
        device.ServiceMarketing.Task19_warning = False

        device.ServiceMarketing.Task20_alert = False
        device.ServiceMarketing.Task20_warning = False

        y = activeTasksSM(device)

        x = 0
        if device.ServiceMarketing.Task1_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task2_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task3_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task4_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task5_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task6_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task7_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task8_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task9_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task10_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task11_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task12_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task13_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task14_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task15_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task16_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task17_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task18_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task19_complete_date:
            x = x + 1
        if device.ServiceMarketing.Task20_complete_date:
            x = x + 1
        percent = x / y * 100
        device.ServiceMarketing.completed = int(percent)

        #alerting logic
        today = datetime.date.today()
        if device.ServiceMarketing.Task1_End_Date:
            Task1_delta =  device.ServiceMarketing.Task1_End_Date - today
        else:
            Task1_delta = None
        if device.ServiceMarketing.Task2_End_Date:
            Task2_delta = device.ServiceMarketing.Task2_End_Date - today
        else:
            Task2_delta = None
        if device.ServiceMarketing.Task3_End_Date:
            Task3_delta = device.ServiceMarketing.Task3_End_Date - today
        else:
            Task3_delta = None
        if device.ServiceMarketing.Task4_End_Date:
            Task4_delta = device.ServiceMarketing.Task4_End_Date - today
        else:
            Task4_delta = None
        if device.ServiceMarketing.Task5_End_Date:
            Task5_delta = device.ServiceMarketing.Task5_End_Date - today
        else:
            Task5_delta = None
        if device.ServiceMarketing.Task6_End_Date:
            Task6_delta = device.ServiceMarketing.Task6_End_Date - today
        else:
            Task6_delta = None
        if device.ServiceMarketing.Task7_End_Date:
            Task7_delta = device.ServiceMarketing.Task7_End_Date - today
        else:
            Task7_delta = None
        if device.ServiceMarketing.Task8_End_Date:
            Task8_delta = device.ServiceMarketing.Task8_End_Date - today
        else:
            Task8_delta = None
        if device.ServiceMarketing.Task9_End_Date:
            Task9_delta = device.ServiceMarketing.Task9_End_Date - today
        else:
            Task9_delta = None
        if device.ServiceMarketing.Task10_End_Date:
            Task10_delta =  device.ServiceMarketing.Task10_End_Date - today
        else:
            Task10_delta = None
        if device.ServiceMarketing.Task11_End_Date:
            Task11_delta =  device.ServiceMarketing.Task11_End_Date - today
        else:
            Task11_delta = None
        if device.ServiceMarketing.Task12_End_Date:
            Task12_delta = device.ServiceMarketing.Task12_End_Date - today
        else:
            Task12_delta = None
        if device.ServiceMarketing.Task13_End_Date:
            Task13_delta = device.ServiceMarketing.Task13_End_Date - today
        else:
            Task13_delta = None
        if device.ServiceMarketing.Task14_End_Date:
            Task14_delta = device.ServiceMarketing.Task14_End_Date - today
        else:
            Task14_delta = None
        if device.ServiceMarketing.Task15_End_Date:
            Task15_delta = device.ServiceMarketing.Task15_End_Date - today
        else:
            Task15_delta = None
        if device.ServiceMarketing.Task16_End_Date:
            Task16_delta = device.ServiceMarketing.Task16_End_Date - today
        else:
            Task16_delta = None
        if device.ServiceMarketing.Task17_End_Date:
            Task17_delta = device.ServiceMarketing.Task17_End_Date - today
        else:
            Task17_delta = None
        if device.ServiceMarketing.Task18_End_Date:
            Task18_delta = device.ServiceMarketing.Task18_End_Date - today
        else:
            Task18_delta = None
        if device.ServiceMarketing.Task19_End_Date:
            Task19_delta = device.ServiceMarketing.Task19_End_Date - today
        else:
            Task19_delta = None
        if device.ServiceMarketing.Task20_End_Date:
            Task20_delta = device.ServiceMarketing.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not device.ServiceMarketing.Task1_complete_date:
            device.ServiceMarketing.Task1_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not device.ServiceMarketing.Task2_complete_date:
            device.ServiceMarketing.Task2_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not device.ServiceMarketing.Task3_complete_date:
            device.ServiceMarketing.Task3_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not device.ServiceMarketing.Task4_complete_date:
            device.ServiceMarketing.Task4_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not device.ServiceMarketing.Task5_complete_date:
            device.ServiceMarketing.Task5_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not device.ServiceMarketing.Task6_complete_date:
            device.ServiceMarketing.Task6_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not device.ServiceMarketing.Task7_complete_date:
            device.ServiceMarketing.Task7_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not device.ServiceMarketing.Task8_complete_date:
            device.ServiceMarketing.Task8_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not device.ServiceMarketing.Task9_complete_date:
            device.ServiceMarketing.Task9_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not device.ServiceMarketing.Task10_complete_date:
            device.ServiceMarketing.Task10_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not device.ServiceMarketing.Task11_complete_date:
            device.ServiceMarketing.Task11_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not device.ServiceMarketing.Task12_complete_date:
            device.ServiceMarketing.Task12_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not device.ServiceMarketing.Task13_complete_date:
            device.ServiceMarketing.Task13_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not device.ServiceMarketing.Task14_complete_date:
            device.ServiceMarketing.Task14_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not device.ServiceMarketing.Task15_complete_date:
            device.ServiceMarketing.Task15_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not device.ServiceMarketing.Task16_complete_date:
            device.ServiceMarketing.Task16_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not device.ServiceMarketing.Task17_complete_date:
            device.ServiceMarketing.Task17_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not device.ServiceMarketing.Task18_complete_date:
            device.ServiceMarketing.Task18_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not device.ServiceMarketing.Task19_complete_date:
            device.ServiceMarketing.Task19_warning = True
            device.ServiceMarketing.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(device.ServiceMarketing.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not device.ServiceMarketing.Task20_complete_date:
            device.ServiceMarketing.Task20_warning = True
            device.ServiceMarketing.Status = 'At Risk'

        if device.ServiceMarketing.Task1_End_Date and Task1_delta < timedelta(0) and not device.ServiceMarketing.Task1_complete_date:
            device.ServiceMarketing.Task1_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task2_End_Date and Task2_delta < timedelta(0) and not device.ServiceMarketing.Task2_complete_date:
            device.ServiceMarketing.Task2_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task3_End_Date and Task3_delta < timedelta(0) and not device.ServiceMarketing.Task3_complete_date:
            device.ServiceMarketing.Task3_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task4_End_Date and Task4_delta < timedelta(0) and not device.ServiceMarketing.Task4_complete_date:
            device.ServiceMarketing.Task4_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task5_End_Date and Task5_delta < timedelta(0) and not device.ServiceMarketing.Task5_complete_date:
            device.ServiceMarketing.Task5_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task6_End_Date and Task6_delta < timedelta(0) and not device.ServiceMarketing.Task6_complete_date:
            device.ServiceMarketing.Task6_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task7_End_Date and Task7_delta < timedelta(0) and not device.ServiceMarketing.Task7_complete_date:
            device.ServiceMarketing.Task7_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task8_End_Date and Task8_delta < timedelta(0)and not device.ServiceMarketing.Task8_complete_date:
            device.ServiceMarketing.Task8_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task9_End_Date and Task9_delta < timedelta(0)and not device.ServiceMarketing.Task9_complete_date:
            device.ServiceMarketing.Task9_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task10_End_Date and Task10_delta < timedelta(0) and not device.ServiceMarketing.Task10_complete_date:
            device.ServiceMarketing.Task10_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task11_End_Date and Task11_delta < timedelta(0) and not device.ServiceMarketing.Task11_complete_date:
            device.ServiceMarketing.Task11_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task12_End_Date and Task12_delta < timedelta(0) and not device.ServiceMarketing.Task12_complete_date:
            device.ServiceMarketing.Task12_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task13_End_Date and Task13_delta < timedelta(0) and not device.ServiceMarketing.Task13_complete_date:
            device.ServiceMarketing.Task13_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task14_End_Date and Task14_delta < timedelta(0) and not device.ServiceMarketing.Task14_complete_date:
            device.ServiceMarketing.Task14_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task15_End_Date and Task15_delta < timedelta(0) and not device.ServiceMarketing.Task15_complete_date:
            device.ServiceMarketing.Task15_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task16_End_Date and Task16_delta < timedelta(0) and not device.ServiceMarketing.Task16_complete_date:
            device.ServiceMarketing.Task16_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task17_End_Date and Task17_delta < timedelta(0)and not device.ServiceMarketing.Task17_complete_date:
            device.ServiceMarketing.Task17_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task18_End_Date and Task18_delta < timedelta(0)and not device.ServiceMarketing.Task18_complete_date:
            device.ServiceMarketing.Task18_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task19_End_Date and Task19_delta < timedelta(0)and not device.ServiceMarketing.Task19_complete_date:
            device.ServiceMarketing.Task19_alert = True
            device.ServiceMarketing.Status = 'Delayed'
        if device.ServiceMarketing.Task20_End_Date and Task20_delta < timedelta(0)and not device.ServiceMarketing.Task20_complete_date:
            device.ServiceMarketing.Task20_alert = True
            device.ServiceMarketing.Status = 'Delayed'

        device.ServiceMarketing.save()

        device.ServiceTraining.Task1_alert = False
        device.ServiceTraining.Task1_warning = False
        device.ServiceTraining.Status = 'On_Time'

        device.ServiceTraining.Task2_alert = False
        device.ServiceTraining.Task2_warning = False

        device.ServiceTraining.Task3_alert = False
        device.ServiceTraining.Task3_warning = False

        device.ServiceTraining.Task4_alert = False
        device.ServiceTraining.Task4_warning = False

        device.ServiceTraining.Task5_alert = False
        device.ServiceTraining.Task5_warning = False

        device.ServiceTraining.Task6_alert = False
        device.ServiceTraining.Task6_warning = False

        device.ServiceTraining.Task7_alert = False
        device.ServiceTraining.Task7_warning = False

        device.ServiceTraining.Task8_alert = False
        device.ServiceTraining.Task8_warning = False

        device.ServiceTraining.Task9_alert = False
        device.ServiceTraining.Task9_warning = False

        device.ServiceTraining.Task10_alert = False
        device.ServiceTraining.Task10_warning = False

        device.ServiceTraining.Task11_alert = False
        device.ServiceTraining.Task11_warning = False

        device.ServiceTraining.Task12_alert = False
        device.ServiceTraining.Task12_warning = False

        device.ServiceTraining.Task13_alert = False
        device.ServiceTraining.Task13_warning = False

        device.ServiceTraining.Task14_alert = False
        device.ServiceTraining.Task14_warning = False

        device.ServiceTraining.Task15_alert = False
        device.ServiceTraining.Task15_warning = False

        device.ServiceTraining.Task16_alert = False
        device.ServiceTraining.Task16_warning = False

        device.ServiceTraining.Task17_alert = False
        device.ServiceTraining.Task17_warning = False

        device.ServiceTraining.Task18_alert = False
        device.ServiceTraining.Task18_warning = False

        device.ServiceTraining.Task19_alert = False
        device.ServiceTraining.Task19_warning = False

        device.ServiceTraining.Task20_alert = False
        device.ServiceTraining.Task20_warning = False

        y = activeTasksST(device)

        x = 0
        if device.ServiceTraining.Task1_complete_date:
            x = x + 1
        if device.ServiceTraining.Task2_complete_date:
            x = x + 1
        if device.ServiceTraining.Task3_complete_date:
            x = x + 1
        if device.ServiceTraining.Task4_complete_date:
            x = x + 1
        if device.ServiceTraining.Task5_complete_date:
            x = x + 1
        if device.ServiceTraining.Task6_complete_date:
            x = x + 1
        if device.ServiceTraining.Task7_complete_date:
            x = x + 1
        if device.ServiceTraining.Task8_complete_date:
            x = x + 1
        if device.ServiceTraining.Task9_complete_date:
            x = x + 1
        if device.ServiceTraining.Task10_complete_date:
            x = x + 1
        if device.ServiceTraining.Task11_complete_date:
            x = x + 1
        if device.ServiceTraining.Task12_complete_date:
            x = x + 1
        if device.ServiceTraining.Task13_complete_date:
            x = x + 1
        if device.ServiceTraining.Task14_complete_date:
            x = x + 1
        if device.ServiceTraining.Task15_complete_date:
            x = x + 1
        if device.ServiceTraining.Task16_complete_date:
            x = x + 1
        if device.ServiceTraining.Task17_complete_date:
            x = x + 1
        if device.ServiceTraining.Task18_complete_date:
            x = x + 1
        if device.ServiceTraining.Task19_complete_date:
            x = x + 1
        if device.ServiceTraining.Task20_complete_date:
            x = x + 1
        percent = x / y * 100
        device.ServiceTraining.completed = int(percent)

        #alerting logic
        today = datetime.date.today()
        if device.ServiceTraining.Task1_End_Date:
            Task1_delta =  device.ServiceTraining.Task1_End_Date - today
        else:
            Task1_delta = None
        if device.ServiceTraining.Task2_End_Date:
            Task2_delta = device.ServiceTraining.Task2_End_Date - today
        else:
            Task2_delta = None
        if device.ServiceTraining.Task3_End_Date:
            Task3_delta = device.ServiceTraining.Task3_End_Date - today
        else:
            Task3_delta = None
        if device.ServiceTraining.Task4_End_Date:
            Task4_delta = device.ServiceTraining.Task4_End_Date - today
        else:
            Task4_delta = None
        if device.ServiceTraining.Task5_End_Date:
            Task5_delta = device.ServiceTraining.Task5_End_Date - today
        else:
            Task5_delta = None
        if device.ServiceTraining.Task6_End_Date:
            Task6_delta = device.ServiceTraining.Task6_End_Date - today
        else:
            Task6_delta = None
        if device.ServiceTraining.Task7_End_Date:
            Task7_delta = device.ServiceTraining.Task7_End_Date - today
        else:
            Task7_delta = None
        if device.ServiceTraining.Task8_End_Date:
            Task8_delta = device.ServiceTraining.Task8_End_Date - today
        else:
            Task8_delta = None
        if device.ServiceTraining.Task9_End_Date:
            Task9_delta = device.ServiceTraining.Task9_End_Date - today
        else:
            Task9_delta = None
        if device.ServiceTraining.Task10_End_Date:
            Task10_delta =  device.ServiceTraining.Task10_End_Date - today
        else:
            Task10_delta = None
        if device.ServiceTraining.Task11_End_Date:
            Task11_delta =  device.ServiceTraining.Task11_End_Date - today
        else:
            Task11_delta = None
        if device.ServiceTraining.Task12_End_Date:
            Task12_delta = device.ServiceTraining.Task12_End_Date - today
        else:
            Task12_delta = None
        if device.ServiceTraining.Task13_End_Date:
            Task13_delta = device.ServiceTraining.Task13_End_Date - today
        else:
            Task13_delta = None
        if device.ServiceTraining.Task14_End_Date:
            Task14_delta = device.ServiceTraining.Task14_End_Date - today
        else:
            Task14_delta = None
        if device.ServiceTraining.Task15_End_Date:
            Task15_delta = device.ServiceTraining.Task15_End_Date - today
        else:
            Task15_delta = None
        if device.ServiceTraining.Task16_End_Date:
            Task16_delta = device.ServiceTraining.Task16_End_Date - today
        else:
            Task16_delta = None
        if device.ServiceTraining.Task17_End_Date:
            Task17_delta = device.ServiceTraining.Task17_End_Date - today
        else:
            Task17_delta = None
        if device.ServiceTraining.Task18_End_Date:
            Task18_delta = device.ServiceTraining.Task18_End_Date - today
        else:
            Task18_delta = None
        if device.ServiceTraining.Task19_End_Date:
            Task19_delta = device.ServiceTraining.Task19_End_Date - today
        else:
            Task19_delta = None
        if device.ServiceTraining.Task20_End_Date:
            Task20_delta = device.ServiceTraining.Task20_End_Date - today
        else:
            Task20_delta = None


        if Task1_delta and Task1_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not device.ServiceTraining.Task1_complete_date:
            device.ServiceTraining.Task1_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not device.ServiceTraining.Task2_complete_date:
            device.ServiceTraining.Task2_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not device.ServiceTraining.Task3_complete_date:
            device.ServiceTraining.Task3_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not device.ServiceTraining.Task4_complete_date:
            device.ServiceTraining.Task4_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not device.ServiceTraining.Task5_complete_date:
            device.ServiceTraining.Task5_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not device.ServiceTraining.Task6_complete_date:
            device.ServiceTraining.Task6_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not device.ServiceTraining.Task7_complete_date:
            device.ServiceTraining.Task7_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not device.ServiceTraining.Task8_complete_date:
            device.ServiceTraining.Task8_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not device.ServiceTraining.Task9_complete_date:
            device.ServiceTraining.Task9_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not device.ServiceTraining.Task10_complete_date:
            device.ServiceTraining.Task10_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not device.ServiceTraining.Task11_complete_date:
            device.ServiceTraining.Task11_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not device.ServiceTraining.Task12_complete_date:
            device.ServiceTraining.Task12_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not device.ServiceTraining.Task13_complete_date:
            device.ServiceTraining.Task13_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not device.ServiceTraining.Task14_complete_date:
            device.ServiceTraining.Task14_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not device.ServiceTraining.Task15_complete_date:
            device.ServiceTraining.Task15_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not device.ServiceTraining.Task16_complete_date:
            device.ServiceTraining.Task16_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not device.ServiceTraining.Task17_complete_date:
            device.ServiceTraining.Task17_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not device.ServiceTraining.Task18_complete_date:
            device.ServiceTraining.Task18_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not device.ServiceTraining.Task19_complete_date:
            device.ServiceTraining.Task19_warning = True
            device.ServiceTraining.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(device.ServiceTraining.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not device.ServiceTraining.Task20_complete_date:
            device.ServiceTraining.Task20_warning = True
            device.ServiceTraining.Status = 'At Risk'

        if device.ServiceTraining.Task1_End_Date and Task1_delta < timedelta(0) and not device.ServiceTraining.Task1_complete_date:
            device.ServiceTraining.Task1_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task2_End_Date and Task2_delta < timedelta(0) and not device.ServiceTraining.Task2_complete_date:
            device.ServiceTraining.Task2_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task3_End_Date and Task3_delta < timedelta(0) and not device.ServiceTraining.Task3_complete_date:
            device.ServiceTraining.Task3_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task4_End_Date and Task4_delta < timedelta(0) and not device.ServiceTraining.Task4_complete_date:
            device.ServiceTraining.Task4_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task5_End_Date and Task5_delta < timedelta(0) and not device.ServiceTraining.Task5_complete_date:
            device.ServiceTraining.Task5_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task6_End_Date and Task6_delta < timedelta(0) and not device.ServiceTraining.Task6_complete_date:
            device.ServiceTraining.Task6_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task7_End_Date and Task7_delta < timedelta(0) and not device.ServiceTraining.Task7_complete_date:
            device.ServiceTraining.Task7_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task8_End_Date and Task8_delta < timedelta(0)and not device.ServiceTraining.Task8_complete_date:
            device.ServiceTraining.Task8_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task9_End_Date and Task9_delta < timedelta(0)and not device.ServiceTraining.Task9_complete_date:
            device.ServiceTraining.Task9_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task10_End_Date and Task10_delta < timedelta(0) and not device.ServiceTraining.Task10_complete_date:
            device.ServiceTraining.Task10_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task11_End_Date and Task11_delta < timedelta(0) and not device.ServiceTraining.Task11_complete_date:
            device.ServiceTraining.Task11_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task12_End_Date and Task12_delta < timedelta(0) and not device.ServiceTraining.Task12_complete_date:
            device.ServiceTraining.Task12_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task13_End_Date and Task13_delta < timedelta(0) and not device.ServiceTraining.Task13_complete_date:
            device.ServiceTraining.Task13_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task14_End_Date and Task14_delta < timedelta(0) and not device.ServiceTraining.Task14_complete_date:
            device.ServiceTraining.Task14_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task15_End_Date and Task15_delta < timedelta(0) and not device.ServiceTraining.Task15_complete_date:
            device.ServiceTraining.Task15_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task16_End_Date and Task16_delta < timedelta(0) and not device.ServiceTraining.Task16_complete_date:
            device.ServiceTraining.Task16_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task17_End_Date and Task17_delta < timedelta(0)and not device.ServiceTraining.Task17_complete_date:
            device.ServiceTraining.Task17_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task18_End_Date and Task18_delta < timedelta(0)and not device.ServiceTraining.Task18_complete_date:
            device.ServiceTraining.Task18_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task19_End_Date and Task19_delta < timedelta(0)and not device.ServiceTraining.Task19_complete_date:
            device.ServiceTraining.Task19_alert = True
            device.ServiceTraining.Status = 'Delayed'
        if device.ServiceTraining.Task20_End_Date and Task20_delta < timedelta(0)and not device.ServiceTraining.Task20_complete_date:
            device.ServiceTraining.Task20_alert = True
            device.ServiceTraining.Status = 'Delayed'

        device.ServiceTraining.save()

        device.Parts.Task1_alert = False
        device.Parts.Task1_warning = False
        device.Parts.Status = 'On_Time'

        device.Parts.Task2_alert = False
        device.Parts.Task2_warning = False

        device.Parts.Task3_alert = False
        device.Parts.Task3_warning = False

        device.Parts.Task4_alert = False
        device.Parts.Task4_warning = False

        device.Parts.Task5_alert = False
        device.Parts.Task5_warning = False

        device.Parts.Task6_alert = False
        device.Parts.Task6_warning = False

        device.Parts.Task7_alert = False
        device.Parts.Task7_warning = False

        device.Parts.Task8_alert = False
        device.Parts.Task8_warning = False

        device.Parts.Task9_alert = False
        device.Parts.Task9_warning = False

        device.Parts.Task10_alert = False
        device.Parts.Task10_warning = False

        device.Parts.Task11_alert = False
        device.Parts.Task11_warning = False

        device.Parts.Task12_alert = False
        device.Parts.Task12_warning = False

        device.Parts.Task13_alert = False
        device.Parts.Task13_warning = False

        device.Parts.Task14_alert = False
        device.Parts.Task14_warning = False

        device.Parts.Task15_alert = False
        device.Parts.Task15_warning = False

        device.Parts.Task16_alert = False
        device.Parts.Task16_warning = False

        device.Parts.Task17_alert = False
        device.Parts.Task17_warning = False

        device.Parts.Task18_alert = False
        device.Parts.Task18_warning = False

        device.Parts.Task19_alert = False
        device.Parts.Task19_warning = False

        device.Parts.Task20_alert = False
        device.Parts.Task20_warning = False

        y = activeTasksP(device)

        x = 0
        if device.Parts.Task1_complete_date:
            x = x + 1
        if device.Parts.Task2_complete_date:
            x = x + 1
        if device.Parts.Task3_complete_date:
            x = x + 1
        if device.Parts.Task4_complete_date:
            x = x + 1
        if device.Parts.Task5_complete_date:
            x = x + 1
        if device.Parts.Task6_complete_date:
            x = x + 1
        if device.Parts.Task7_complete_date:
            x = x + 1
        if device.Parts.Task8_complete_date:
            x = x + 1
        if device.Parts.Task9_complete_date:
            x = x + 1
        if device.Parts.Task10_complete_date:
            x = x + 1
        if device.Parts.Task11_complete_date:
            x = x + 1
        if device.Parts.Task12_complete_date:
            x = x + 1
        if device.Parts.Task13_complete_date:
            x = x + 1
        if device.Parts.Task14_complete_date:
            x = x + 1
        if device.Parts.Task15_complete_date:
            x = x + 1
        if device.Parts.Task16_complete_date:
            x = x + 1
        if device.Parts.Task17_complete_date:
            x = x + 1
        if device.Parts.Task18_complete_date:
            x = x + 1
        if device.Parts.Task19_complete_date:
            x = x + 1
        if device.Parts.Task20_complete_date:
            x = x + 1
        percent = x / y * 100
        device.Parts.completed = int(percent)

        #alerting logic
        today = datetime.date.today()
        if device.Parts.Task1_End_Date:
            Task1_delta =  device.Parts.Task1_End_Date - today
        else:
            Task1_delta = None
        if device.Parts.Task2_End_Date:
            Task2_delta = device.Parts.Task2_End_Date - today
        else:
            Task2_delta = None
        if device.Parts.Task3_End_Date:
            Task3_delta = device.Parts.Task3_End_Date - today
        else:
            Task3_delta = None
        if device.Parts.Task4_End_Date:
            Task4_delta = device.Parts.Task4_End_Date - today
        else:
            Task4_delta = None
        if device.Parts.Task5_End_Date:
            Task5_delta = device.Parts.Task5_End_Date - today
        else:
            Task5_delta = None
        if device.Parts.Task6_End_Date:
            Task6_delta = device.Parts.Task6_End_Date - today
        else:
            Task6_delta = None
        if device.Parts.Task7_End_Date:
            Task7_delta = device.Parts.Task7_End_Date - today
        else:
            Task7_delta = None
        if device.Parts.Task8_End_Date:
            Task8_delta = device.Parts.Task8_End_Date - today
        else:
            Task8_delta = None
        if device.Parts.Task9_End_Date:
            Task9_delta = device.Parts.Task9_End_Date - today
        else:
            Task9_delta = None
        if device.Parts.Task10_End_Date:
            Task10_delta =  device.Parts.Task10_End_Date - today
        else:
            Task10_delta = None
        if device.Parts.Task11_End_Date:
            Task11_delta =  device.Parts.Task11_End_Date - today
        else:
            Task11_delta = None
        if device.Parts.Task12_End_Date:
            Task12_delta = device.Parts.Task12_End_Date - today
        else:
            Task12_delta = None
        if device.Parts.Task13_End_Date:
            Task13_delta = device.Parts.Task13_End_Date - today
        else:
            Task13_delta = None
        if device.Parts.Task14_End_Date:
            Task14_delta = device.Parts.Task14_End_Date - today
        else:
            Task14_delta = None
        if device.Parts.Task15_End_Date:
            Task15_delta = device.Parts.Task15_End_Date - today
        else:
            Task15_delta = None
        if device.Parts.Task16_End_Date:
            Task16_delta = device.Parts.Task16_End_Date - today
        else:
            Task16_delta = None
        if device.Parts.Task17_End_Date:
            Task17_delta = device.Parts.Task17_End_Date - today
        else:
            Task17_delta = None
        if device.Parts.Task18_End_Date:
            Task18_delta = device.Parts.Task18_End_Date - today
        else:
            Task18_delta = None
        if device.Parts.Task19_End_Date:
            Task19_delta = device.Parts.Task19_End_Date - today
        else:
            Task19_delta = None
        if device.Parts.Task20_End_Date:
            Task20_delta = device.Parts.Task20_End_Date - today
        else:
            Task20_delta = None

        if Task1_delta and Task1_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task1_delta > timedelta(0) \
                and not device.Parts.Task1_complete_date:
            device.Parts.Task1_warning = True
            device.Parts.Status = 'At Risk'
        if Task2_delta and Task2_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task2_delta > timedelta(0) \
                and not device.Parts.Task2_complete_date:
            device.Parts.Task2_warning = True
            device.Parts.Status = 'At Risk'
        if Task3_delta and Task3_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task3_delta > timedelta(0) \
                and not device.Parts.Task3_complete_date:
            device.Parts.Task3_warning = True
            device.Parts.Status = 'At Risk'
        if Task4_delta and Task4_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task4_delta > timedelta(0) \
                and not device.Parts.Task4_complete_date:
            device.Parts.Task4_warning = True
            device.Parts.Status = 'At Risk'
        if Task5_delta and Task5_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task5_delta > timedelta(0) \
                and not device.Parts.Task5_complete_date:
            device.Parts.Task5_warning = True
            device.Parts.Status = 'At Risk'
        if Task6_delta and Task6_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task6_delta > timedelta(0) \
                and not device.Parts.Task6_complete_date:
            device.Parts.Task6_warning = True
            device.Parts.Status = 'At Risk'
        if Task7_delta and Task7_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task7_delta > timedelta(0) \
                and not device.Parts.Task7_complete_date:
            device.Parts.Task7_warning = True
            device.Parts.Status = 'At Risk'
        if Task8_delta and Task8_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task8_delta > timedelta(0) \
                and not device.Parts.Task8_complete_date:
            device.Parts.Task8_warning = True
            device.Parts.Status = 'At Risk'
        if Task9_delta and Task9_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task9_delta > timedelta(0) \
                and not device.Parts.Task9_complete_date:
            device.Parts.Task9_warning = True
            device.Parts.Status = 'At Risk'
        if Task10_delta and Task10_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task10_delta > timedelta(0) \
                and not device.Parts.Task10_complete_date:
            device.Parts.Task10_warning = True
            device.Parts.Status = 'At Risk'
        if Task11_delta and Task11_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task11_delta > timedelta(0) \
                and not device.Parts.Task11_complete_date:
            device.Parts.Task11_warning = True
            device.Parts.Status = 'At Risk'
        if Task12_delta and Task12_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task12_delta > timedelta(0) \
                and not device.Parts.Task12_complete_date:
            device.Parts.Task12_warning = True
            device.Parts.Status = 'At Risk'
        if Task13_delta and Task13_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task13_delta > timedelta(0) \
                and not device.Parts.Task13_complete_date:
            device.Parts.Task13_warning = True
            device.Parts.Status = 'At Risk'
        if Task14_delta and Task14_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task14_delta > timedelta(0) \
                and not device.Parts.Task14_complete_date:
            device.Parts.Task14_warning = True
            device.Parts.Status = 'At Risk'
        if Task15_delta and Task15_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task15_delta > timedelta(0) \
                and not device.Parts.Task15_complete_date:
            device.Parts.Task15_warning = True
            device.Parts.Status = 'At Risk'
        if Task16_delta and Task16_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task16_delta > timedelta(0) \
                and not device.Parts.Task16_complete_date:
            device.Parts.Task16_warning = True
            device.Parts.Status = 'At Risk'
        if Task17_delta and Task17_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task17_delta > timedelta(0) \
                and not device.Parts.Task17_complete_date:
            device.Parts.Task17_warning = True
            device.Parts.Status = 'At Risk'
        if Task18_delta and Task18_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task18_delta > timedelta(0) \
                and not device.Parts.Task18_complete_date:
            device.Parts.Task18_warning = True
            device.Parts.Status = 'At Risk'
        if Task19_delta and Task19_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task19_delta > timedelta(0) \
                and not device.Parts.Task19_complete_date:
            device.Parts.Task19_warning = True
            device.Parts.Status = 'At Risk'
        if Task20_delta and Task20_delta < timedelta(device.Parts.Time_Delta_For_Warning) and Task20_delta > timedelta(0) \
                and not device.Parts.Task20_complete_date:
            device.Parts.Task20_warning = True
            device.Parts.Status = 'At Risk'

        if device.Parts.Task1_End_Date and Task1_delta < timedelta(0) and not device.Parts.Task1_complete_date:
            device.Parts.Task1_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task2_End_Date and Task2_delta < timedelta(0) and not device.Parts.Task2_complete_date:
            device.Parts.Task2_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task3_End_Date and Task3_delta < timedelta(0) and not device.Parts.Task3_complete_date:
            device.Parts.Task3_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task4_End_Date and Task4_delta < timedelta(0) and not device.Parts.Task4_complete_date:
            device.Parts.Task4_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task5_End_Date and Task5_delta < timedelta(0) and not device.Parts.Task5_complete_date:
            device.Parts.Task5_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task6_End_Date and Task6_delta < timedelta(0) and not device.Parts.Task6_complete_date:
            device.Parts.Task6_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task7_End_Date and Task7_delta < timedelta(0) and not device.Parts.Task7_complete_date:
            device.Parts.Task7_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task8_End_Date and Task8_delta < timedelta(0)and not device.Parts.Task8_complete_date:
            device.Parts.Task8_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task9_End_Date and Task9_delta < timedelta(0)and not device.Parts.Task9_complete_date:
            device.Parts.Task9_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task10_End_Date and Task10_delta < timedelta(0) and not device.Parts.Task10_complete_date:
            device.Parts.Task10_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task11_End_Date and Task11_delta < timedelta(0) and not device.Parts.Task11_complete_date:
            device.Parts.Task11_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task12_End_Date and Task12_delta < timedelta(0) and not device.Parts.Task12_complete_date:
            device.Parts.Task12_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task13_End_Date and Task13_delta < timedelta(0) and not device.Parts.Task13_complete_date:
            device.Parts.Task13_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task14_End_Date and Task14_delta < timedelta(0) and not device.Parts.Task14_complete_date:
            device.Parts.Task14_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task15_End_Date and Task15_delta < timedelta(0) and not device.Parts.Task15_complete_date:
            device.Parts.Task15_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task16_End_Date and Task16_delta < timedelta(0) and not device.Parts.Task16_complete_date:
            device.Parts.Task16_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task17_End_Date and Task17_delta < timedelta(0)and not device.Parts.Task17_complete_date:
            device.Parts.Task17_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task18_End_Date and Task18_delta < timedelta(0)and not device.Parts.Task18_complete_date:
            device.Parts.Task18_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task19_End_Date and Task19_delta < timedelta(0)and not device.Parts.Task19_complete_date:
            device.Parts.Task19_alert = True
            device.Parts.Status = 'Delayed'
        if device.Parts.Task20_End_Date and Task20_delta < timedelta(0)and not device.Parts.Task20_complete_date:
            device.Parts.Task20_alert = True
            device.Parts.Status = 'Delayed'

        device.Parts.save()
        overallpercent = int ((device.ProductReadiness.completed + device.DigitalContent.completed + device.VideoContent.completed
                   + device.CallCenterTraining.completed + device.CallCenterOpertaions.completed + device.ProductSupport.completed
                    + device.Warehouse.completed + device.FieldService.completed + device.TechSupport.completed +
                    device.ServiceMarketing.completed + device.ServiceTraining.completed + device.Parts.completed)/12)
        device.completed = overallpercent
        device.save()
