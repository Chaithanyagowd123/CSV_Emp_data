from django.shortcuts import render
import csv
from django.http import HttpResponse
# Create your views here.
from app.models import *


def business_employment_data(self):
    with open('C:\\Users\\CHAITHANYA\\OneDrive\\Desktop\\Django projects\\hanuman\\Scripts\\project42\\app\\Business-employment-data-september-2022-quarter-csv.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            series_reference=i[0]
            Period=i[1]
            Datavalue=i[2]
            Suppressed=i[3]
            Status=i[4]
            Units=i[5]
            Magnitude=i[6]
            Subject=i[7]
            Group=i[8]
            Series_title_1=i[9]
            Series_title_2=i[10]
            Series_title_3=i[11]
            Series_title_4=i[12]
            Series_title_5=i[13]
            DO=Business_Employment_Data(series_reference=series_reference,period=Period,data_value=Datavalue,suppressed=Suppressed,status=Status,units=Units,magnitude=Magnitude,subject=Subject,group=Group,series_title_1=Series_title_1,series_title_2=Series_title_2,series_title_3=Series_title_3,series_title_4=Series_title_4,series_title_5=Series_title_5)
            DO.save()

    return HttpResponse(' Business Employement data is inserted successfully')









            


