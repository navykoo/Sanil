#-*-coding:utf-8-*-
from   Tkinter import *
import Pmw
import os
import AppShell
from   datadictionary2 import *
from w import *
from calendar import *

import io
import urllib
import urllib2
import base64
import tkFont

class SanilDetail(AppShell.AppShell):
    usecommandarea = 1
    appname        = 'Next'        
    dictionary     = 'crewmembers'
    frameWidth     = 435
    frameHeight    = 520
    
    def createButtons(self):
        self.buttonAdd('刷新',
              helpMessage='Return to main menu',
              statusMessage='refreshed',
              command=self.update_display)
        self.buttonAdd('退出',
              helpMessage='Reload the pages',
              statusMessage='quit',
               command=self.close)
        
    def createNotebook(self):
        self.notebook = self.createcomponent('notebook', (), None,
                                         Pmw.NoteBook, (self.interior(),),)
        self.notebook.pack(side=TOP, expand=YES, fill=BOTH, padx=5, pady=5)
        self.formwidth = self.root.winfo_width()
        
    def addPage(self, dictionary,pageIdx):
        table, top, anchor, incr, fields, \
            title, keylist = dataDict[dictionary]
        #self.notebook.add(table, label=title)
        self.notebook.add(title)
        self.current = 0
        ypos = top
        idx = 0
        for label, field, width, proc, valid, nonblank in fields:
            pstr = 'Label(self.notebook.page(pageIdx),'\
                   'text="%s").place(relx=%f,rely=%f, anchor=E)\n' % \
                   (label, (anchor-0.02), ypos)
            if idx == keylist[0]:
                pstr = '%sself.%s=Entry(self.notebook.page(pageIdx),'\
                       'text="",insertbackground="yellow", width=%d+1,'\
                       'highlightthickness=1)\n' % (pstr,field,width)
            else:
                pstr = '%sself.%s=Entry(self.notebook.page(pageIdx),'\
                       'text="", insertbackground="yellow",'\
                       'width=%d+1)\n' % (pstr,field,width)
            pstr = '%sself.%s.place(relx=%f, rely=%f,'\
                   'anchor=W)\n' % (pstr,field,(anchor+0.02),ypos)
            exec '%sself.%sV=StringVar()\n'\
                 'self.%s["textvariable"] = self.%sV' % \
                                          (pstr,field,field,field)
            ypos = ypos + incr
            idx = idx + 1

    def addWeatherReport(self,page):
	  weaInfo = getWeatherInfo2()
	  lblFont = tkFont.Font(family='Fixdsys',size=24)
	  relTime = " (发布时间: "+ weaInfo['date_y'].encode('utf-8')+" "+weaInfo['fchh'].encode('utf-8')+"时)"

	# need to split the data into a Day and Night sequence
	# image pattern: 
	# day: http://www.weather.com.cn/m2/i/icon_weather/29x20/d07.gif
	# night: http://www.weather.com.cn/m2/i/icon_weather/29x20/n07.gif
	# weaInfo['imgx']

	  imgIDs=['d','n']
	  imgIDIdx=0
	  dateStr=""
	  fetchHour = weaInfo['fchh']
	  if int(fetchHour) >= 18:
		imgIDIdx=1
	  j=1
	  self.img = {}
	  for i in range(1,7): 
	    if j == 1: dateStr1="今天"
	    if j == 2: dateStr1="明天"
	    if j == 3: dateStr1="后天"
	    if j >= 4: dateStr1="第"+str(j)+"天"
	    if imgIDIdx==1 :
		dateStr= dateStr1+" (夜间): "
		j = j+1
	    else:
		dateStr= dateStr1+" (白天): "

	    weaText = dateStr+weaInfo['temp'+str(i)].encode('utf-8')+";"+weaInfo['weather'+str(i)].encode('utf-8')+"; "+weaInfo['wind'+str(i)].encode('utf-8')
	    imgRemoteID = int(weaInfo['img'+str(i)])
	    if imgRemoteID == 99: imgRemoteID=0
            imgURL = '{0}{1}{2:02d}.gif'.format('http://www.weather.com.cn/m2/i/icon_weather/29x20/',imgIDs[imgIDIdx],imgRemoteID)
	    imgByte = urllib2.urlopen(imgURL).read()
	    imgB64  = base64.encodestring(imgByte)
	    self.img[i] = PhotoImage(data=imgB64)
	    Label(self.notebook.page(0),image=self.img[i]).grid(row=i,column=1)
	    Label(self.notebook.page(0),text=weaText,font=lblFont).grid(row=i,column=2,sticky=W)
	    imgIDIdx=1-imgIDIdx

	  Label(self.notebook.page(0),text=relTime).grid(row=7,column=2,sticky=E)

    def addSPage(self,title):
        self.notebook.add(title)

    def createPages(self):
        p1 = self.addSPage('Weather')
        self.addWeatherReport(p1)
        self.addSPage('Calendar')
	try:
	        displayCalendar(self.notebook.page(1))
	except:
		print "Unexpected error:", sys.exc_info()[0]
		pass
        self.addSPage('Education')
        #self.update_display()

    def update_display(self):
        pass
	self.notebook.delete('Weather')
	self.notebook.delete('Calendar')
	self.notebook.delete('Education')
	self.createPages()
    
    def save(self):
        pass
    def close(self):
        self.quit()

    def createInterface(self):
        AppShell.AppShell.createInterface(self)
        self.createButtons()
        self.createNotebook()
        self.createPages()
        
if __name__ == '__main__':
    sanildetail = SanilDetail()
    sanildetail.run()
