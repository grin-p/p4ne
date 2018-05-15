from matplotlib import pyplot
from openpyxl import load_workbook

def getvalue(x):
    return x.value

wb=load_workbook('data_analysis_lab.xlsx')
sheet=wb['Data']

Years_list = list(map(getvalue, sheet['A'][1:]))
Temp_list = list(map(getvalue, sheet['C'][1:]))
SunAct_list = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(Years_list, Temp_list, label="График температуры по годам")
pyplot.plot(Years_list, SunAct_list, label="График температуры по годам")
pyplot.show()
