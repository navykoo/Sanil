import urllib
import urllib2
from ntlm import HTTPNtlmAuthHandler
import os
import sys
import re
import simplejson
import codecs

def getHtml2(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getHtml(url):
	user = 'org\name'
	password = 'password'
    
	passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
	passman.add_password(None, url, user, password)
	    # create the NTLM authentication handler
	auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)
	    
	    # create and install the opener
	opener = urllib2.build_opener(auth_NTLM)
	urllib2.install_opener(opener)
	   
	    # retrieve the result
	response = urllib2.urlopen(url)
	html = response.read()
	#print(html)
	return html

def getWeather(html):
    #reg='<a title=.*?>(.*?)</a>.*?<span>(.*?)</span>.*?<b>(.*?)</b>'
    reg='<a title=.*?>(.*?)</a>'
    weatherList=re.compile(reg).findall(html)
    return weatherList

def printWeatherFromJSON(html):
	#print(html)
	ddata = simplejson.loads(html)

	#if isinstance(ddata['weatherinfo']['date_y'],unicode):
	#	d_str = ddata['weatherinfo']['date_y'].encode('utf-8')
	#print d_str
	print ddata['weatherinfo']['city'].encode('utf-8')
	print ddata['weatherinfo']['date_y'].encode('utf-8')
	print ddata['weatherinfo']['temp1'].encode('utf-8')

def getWeatherReport2():
	data = simplejson.loads(getHtml2(sz_url))
	return data['weatherinfo']['date_y'].encode('utf-8') + data['weatherinfo']['temp1'].encode('utf-8')

def getWeatherReport():
	data = simplejson.loads(getHtml(sz_url))
	return data['weatherinfo']['date_y'].encode('utf-8') + data['weatherinfo']['temp1'].encode('utf-8')
#China weather center JSON request
#	Suzhou - http://m.weather.com.cn/data/101190401.html
#	Sample return -
#{"weatherinfo":{"city":"..","city_en":"suzhou","date_y":"2013.2.19.","date":"","week":"...","fchh":"11","cityid":"101190401","temp1":"3.~-2.","temp2":"5.~-1.","temp3":"6.~2.","temp4":"9.~2.","temp5":"10.~3.","temp6":"14.~5.","tempF1":"37.4.~28.4.","tempF2":"41.~30.2.","tempF3":"42.8.~35.6.","tempF4":"48.2.~35.6.","tempF5":"50.~37.4.","tempF6":"57.2.~41.","weather1":".....","weather2":"....","weather3":"..","weather4":".","weather5":"....","weather6":"....","img1":"14","img2":"1","img3":"1","img4":"2","img5":"7","img6":"99","img7":"0","img8":"99","img9":"0","img10":"1","img11":"1","img12":"0","img_single":"14","img_title1":"..","img_title2":"..","img_title3":"..","img_title4":".","img_title5":"..","img_title6":"..","img_title7":".","img_title8":".","img_title9":".","img_title10":"..","img_title11":"..","img_title12":".","img_title_single":"..","wind1":"......4-5.","wind2":"...3-4.","wind3":"......3-4.","wind4":"..3-4.","wind5":"...3-4.","wind6":"...4-5.","fx1":"..","fx2":"...","fl1":"4-5.","fl2":"3-4.","fl3":"3-4.","fl4":"3-4.","fl5":"3-4.","fl6":"4-5.","index":".","index_d":"...............................................","index48":".","index48_d":"...............................................","index_uv":"..","index48_uv":"..","index_xc":"..","index_tr":"..","index_co":"....","st1":"3","st2":"-5","st3":"4","st4":"-5","st5":"5","st6":"0","index_cl":"..","index_ls":"..","index_ag":"...."}}
sz_url = 'http://m.weather.com.cn/data/101190401.html'
#sz_url = 'http://www.weather.com.cn/weather/101190401.shtml'
#printWeatherFromJSON(getHtml(sz_url))
#weatherList=getWeather(getHtml(sz_url))
#for weather in weatherList:
#    print weather
