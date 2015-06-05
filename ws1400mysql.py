#!/usr/bin/python
# -*- coding: utf-8 -*- 

import subprocess
import re
import time
import MySQLdb as mdb
import sys

re.DOTALL # cause re matching for entire string, rather than just per line

IP_address_of_server = "192.168.2.99"

web_page_name_for_data = "http://"+IP_address_of_server+"/"+"livedata.htm"
delay_between_web_page_fetches = 15

vars = ('inTemp','inHumi','AbsPress','RelPress','outTemp','outHumi','windir',
      'avgwind','gustspeed','solarrad','uv','uvi','rainofhourly','rainofdaily',
      'rainofweekly','rainofmonthly','rainofyearly') # tags for data scraped from the web page

list = {} # contains key: values for web page data
old_list = {} # used to compair previous web page data values (only print when they differ)

try:
    con = mdb.connect('localhost', 'root', 'wXg00d2fLy', 'obs')

except mdb.Error, e:

    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)


def get_data_from_webpage(): # return dict of (data tags : values)
   readings = {}
   
   try:
      webpage =subprocess.check_output(["curl","-s","-m 3",web_page_name_for_data])
      # curl needs -m flag to prevent auto page refresh
   except subprocess.CalledProcessError, e:
      return "" # web page fetch failed

   for var in vars:
      match=re.search(var+r'.*value=\"([0123456789\.]+)',webpage)
      
      if match is None:
         return "" # on the tage or its value not found
      else:
         readings[var]=match.group(1)
         
   return readings

def print_file_header_columns():
   print "\"date\"",
   print ",\"time\"",
   for var in vars:
      print ",\""+var+"\"",
   print "\n"
   

#let's go

#print_file_header_columns()

while (True):
   list = get_data_from_webpage()
   
   if cmp(old_list,list) and (list != ""): #only perform if readings have changed or webpage returned ""
      old_list = list
      tmp = "INSERT INTO ws1400(datetime,inTemp,inHumi,AbsPress,RelPress,outTemp,outHumi,windir,avgwind,gustspeed,solarrad,uv,uvi,rainofhourly,rainofdaily,rainofweekly,rainofmonthly,rainofyearly) VALUES("
      tmp = tmp+ time.strftime("\"%Y/%m/%d ",time.gmtime())
      tmp = tmp+ time.strftime("%H:%M:%S\"",time.gmtime())
      for var in vars:
         tmp = tmp+','+list[var]
      tmp = tmp+ ")"

   try:
      con = mdb.connect('localhost', 'root', 'wXg00d2fLy', 'obs')
      cur = con.cursor()
      cur.execute(tmp)
      con.commit()

   except mdb.Error, e:
      print "Error %d: %s" % (e.args[0], e.args[1])
      if e.args[0] != 1062 :
          sys.exit(1)

   finally:
      if con:
#         print tmp
         con.close()
   
   time.sleep(delay_between_web_page_fetches)


