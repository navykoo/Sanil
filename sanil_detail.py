#-*-coding:utf-8-*-
from   Tkinter import *
import Pmw
import os
import AppShell
from   datadictionary2 import *
from w import *
from calendar import *

class SanilDetail(AppShell.AppShell):
    usecommandarea = 1
    appname        = 'Next'        
    dictionary     = 'crewmembers'
    frameWidth     = 435
    frameHeight    = 520
    
    def createButtons(self):
        self.buttonAdd('Return',
              helpMessage='Return to main menu',
              statusMessage='...',
              command=self.save)
        self.buttonAdd('Refresh',
              helpMessage='Reload the pages',
              statusMessage='Refresh',
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
	  weaText = "发布时间: "+ weaInfo['date_y'].encode('utf-8')+" "+weaInfo['fchh'].encode('utf-8')
	  for i in range(1,7): 
	    weaText += "\r\n"+"第"+str(i)+"天: "+weaInfo['temp'+str(i)].encode('utf-8')+";"+weaInfo['weather'+str(i)].encode('utf-8')+"; "+weaInfo['wind'+str(i)].encode('utf-8')
	  Label(self.notebook.page(0),text=weaText).pack(pady=10)

    def addSPage(self,title):
        self.notebook.add(title)

    def createPages(self):
        p1 = self.addSPage('Weather')
        self.addWeatherReport(p1)
        self.addSPage('Calendar')
        displayCalendar(self.notebook.page(1))
        self.addSPage('Education')
        self.update_display()

    def update_display(self):
        pass
    
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
