#-*-coding:utf-8-*-
import time
import tkFont
from Tkinter import *
class Calendar:
    pass
AppCal = Calendar()

def calcFirstDayOfMonth(year,month,day):
    months = (0,31,59,90,120,151,181,212,243,273,304,334)
    if 0 <= month <= 12:
        sum = months[month - 1]
    else:
        print 'data error'
    # ...............................
    if year < 0 or month < 0 or month > 11 or day < 0 or day >31:
        import os
        os._exit(1)
        
    sum += day
    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if (leap == 1) and (month > 2):
        sum += 1
    # .............
    # (year + (year - 1)/4 - (year - 1)/100 + (year -1)/400)% 7
    return  (sum % 7 - 1 + (year + (year - 1)/4 - (year - 1)/100 + (year -1)/400))% 7
def createMonth(master):
    for i in range(6):
        for j in range(7):
            Label(master,text = '').grid(row = i + 2,column = j)
def updateDate(self):
    ft1 = tkFont.Font(weight=tkFont.BOLD)
    ft2 = tkFont.Font()
    #.........
    year = int(AppCal.vYear.get())
    month = int(AppCal.vMonth.get())
    day = int(AppCal.vDay.get())
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    # ......
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        months[1] += 1
    fd = calcFirstDayOfMonth(year,month,1)
    for i in range(6):
	#print i
        for j in range(7):
            self.grid_slaves(i +2,j)[0]['text'] = ''

    #print fd
    for i in range(1,months[month - 1] + 1):
	#print i
	if (i == day):
	        self.grid_slaves((i + fd - 1)/7 + 2,(i + fd -1)%7)[0]['text'] = str(i)
	        self.grid_slaves((i + fd - 1)/7 + 2,(i + fd -1)%7)[0]['font'] = ft1
	else:
	        self.grid_slaves((i + fd - 1)/7 + 2,(i + fd -1)%7)[0]['text'] = str(i)
	        self.grid_slaves((i + fd - 1)/7 + 2,(i + fd -1)%7)[0]['font'] = ft2
    
def drawHeader(master):
    # ..............
    now = time.localtime(time.time())
    col_idx = 0
    
    # ......
    AppCal.vYear = StringVar()
    AppCal.vYear.set(now[0])
    Label(master,text = '年').grid(row = 0,column = col_idx);col_idx += 1
    omYear = apply(OptionMenu,(master,AppCal.vYear) + tuple(range(2010,2020)))
    omYear.grid(row = 0,column = col_idx);col_idx += 1

    # ......
    AppCal.vMonth = StringVar()
    AppCal.vMonth.set(now[1])
    Label(master,text = '月').grid(row = 0,column = col_idx);col_idx += 1
    omMonth = apply(OptionMenu,(master,AppCal.vMonth) + tuple(range(1,12)))
    omMonth.grid(row = 0,column = col_idx);col_idx += 1

    # ......
    AppCal.vDay = StringVar()
    AppCal.vDay.set(now[2])
    Label(master,text = '日').grid(row = 0,column = col_idx);col_idx += 1
    omDay = apply(OptionMenu,(master,AppCal.vDay) + tuple(range(1,32)))
    omDay.grid(row = 0,column = col_idx);col_idx += 1

    # ......
    #btUpdate = Button(master,text = '更新',command = updateCalendar)
    #btUpdate.grid(row = 0,column = col_idx);
		#col_idx += 1

    # ......
    weeks = ['日','一','二','三','四','五','六']
    for week in weeks:
        Label(master,text = week).grid(row = 1,column = weeks.index(week))

def displayCalendar(root):
		drawHeader(root)
		createMonth(root)
		updateDate(root)
    
#from Tkinter import *
#root = Tk()
#display(root)
#drawHeader(root)
#createMonth(root)
#updateDate()

#root.mainloop()
