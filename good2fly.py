#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# good2fly.fy - Version 2.0 - 2015/06/03
#  by  Mark Grennan {mark@grennan.com}
#
# This app read weather prodictors from WeatherUnderground.com.
#
#
# Cardinal	Degree
# N		348.75 - 11.25
# NNE		11.25 - 33.75
# #NE		33.75 - 56.25
# ENE		56.25 - 78.75
# E		78.75 - 101.25
# ESE		101.25 - 123.75
# SE		123.75 - 146.25
# SSE		146.25 - 168.75
# S		168.75 - 191.25
# SSW		191.25 - 213.75
# SW		213.75 - 236.25
# WSW		236.25 - 258.75
# W		258.75 - 281.25
# WNW		281.25 - 303.75
# NW		303.75 - 326.25
# NNW		326.25 - 348.75

import wunderground
import urllib2
import json
import datetime
import math
from optparse import OptionParser

wukey = 'Your WG KEY HERE'			# Your WounderGround Key

#
# http://www.wunderground.com/weather/api/d/docs?d=data/index
#
#location = '35.548836,-97.589470'		# Your location Longatude and Latatude
location = 'pws:KOKOKLAH101'			# Personal Weather Station	
#location = 'OK/Okalhoma_City'			# US State / City
#location = '73122'				# Zip Code
#location = 'US/Oklahoma_City'			# Country / City
#location = 'KOKC'				# Airport Code
#location = 'autoip'				# Automatic IP location
#location = 'autoip.json?geo_ip=70.169.95.77'	# specific IP address location

#
# Start
#
parser = OptionParser()

parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="Explain the output")

(options, args) = parser.parse_args()

now = datetime.datetime.now()
hour = now.hour
tomorrow = (24 - hour) + 10

forecast = wunderground.Hourly10day(wukey,location)
astronomy = wunderground.Astronomy(wukey,location)

sunset = astronomy.sunset()

if not options.verbose:
    print '<!DOCTYPE html> <html> <body><p><b>'
    print '</b><p><object width="290" height="130"><param name="movie" value="http://www.wunderground.com/swf/pws_mini_rf_nc.swf?station=KOKOKLAH101&freq=&units=english&lang=EN" /><embed src="http://www.wunderground.com/swf/pws_mini_rf_nc.swf?station=KOKOKLAH101&freq=&units=english&lang=EN" type="application/x-shockwave-flash" width="290" height="130" /></object> <p>'

#
# Todays forecast
#
if (hour < 15):
    print '<p><b>Today\'s forcast is:</b><p>'

# Morning
NumStars = 0
Stars = ""
if hour < 10:
# Precent of Percep
    pop = 0
    for y in range(1, 12 - hour):
        pop = pop + int(forecast.pop(hour + y))
    pop = pop / (y + 1)
    if pop <= 10:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Morning chance of precep is ', pop, Stars
# WIND
    wind = 0
    for y in range(1, 12 - hour):
        wind = wind + int(forecast.wspdEnglish(hour + y))
    wind = wind / (y + 1)
    if wind <= 10:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Morning wind speed is ', wind, Stars
# wdirDegrees
    sumDir = 0
    for y in range(1, 12 - hour):
        sumDir=sumDir+int(forecast.wdirDegrees(hour + y))
    winddir = sumDir / (y + 1)
    if (winddir > 235 or winddir < 35) or (winddir > 145 and winddir < 215):
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Morning wind direction is ', winddir, Stars
# TEMP
    temp = 0
    for y in range(1, 12 - hour):
        temp = temp + int(forecast.tempEnglish(hour + y))
    temp = temp / (y + 1)
    if temp >= 65 and temp <= 85:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Morning temp is ', temp, Stars
# SKY
    sky = 0
    for y in range(1, 12 - hour):
        sky = sky + int(forecast.sky(hour + y))
    sky = sky / (y + 1)
    if sky < 60:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Morning sky is ', sky, Stars

    print '  The morning will be {0:5} ({1}) starts for flying.<br>'.format(Stars,NumStars)


# Afternoon
NumStars = 0
Stars = ""
# Precent of Percep
if hour < 15:
    pop = 0
    for y in range(1, int(astronomy.sunsetHour()) - 11):
        pop = pop + int(forecast.pop(hour + y))
    pop = pop / (y + 1)
    if pop <= 10:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Afternoon chance of precep is ', pop, Stars
# WIND
    wind = 0
    for y in range(1, int(astronomy.sunsetHour()) - 11):
        wind = wind + int(forecast.wspdEnglish(hour + y))
    wind = wind / (y + 1)
    if wind <= 10:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Afternoon wind speed is ', wind, Stars
# wdirDegrees
    sumDir = 0
    for y in range(1, int(astronomy.sunsetHour()) - 11):
        sumDir=sumDir+int(forecast.wdirDegrees(hour + y))
    winddir = sumDir / (y + 1)
    if (winddir > 235 or winddir < 35) or (winddir > 145 and winddir < 215):
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Afternoon wind direction is ', winddir, Stars
# TEMP
    temp = 0
    for y in range(1, int(astronomy.sunsetHour()) - 11):
        temp = temp + int(forecast.tempEnglish(hour + y))
    temp = temp / (y + 1)
    if temp >= 65 and temp <= 85:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Afternoon temp is ', temp, Stars
# SKY
    sky = 0
    for y in range(1, int(astronomy.sunsetHour()) - 11):
        sky = sky + int(forecast.sky(hour + y))
    sky = sky / (y + 1)
    if sky < 60:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Afternoon sky is ', sky, Stars


    print '  The afternoon will be {0:5} ({1}) starts for flying.'.format(Stars,NumStars)


#
#
#
print "<p><B>Your five day flying forecast is:</B><p>"
for x in range(0,5):

    dayname = forecast.weekdayName(tomorrow + (x * 24))

#
# The five day forecast
#
# MORNING
#
    NumStars = 0
    Stars = ""
# Precent of Percep
    pop = 0
    for y in range(0,5):
        pop = pop + int(forecast.pop(tomorrow + (x * 24) + y))
    pop = pop / 6
    if pop <= 10:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Morning chance of precep is ', pop, Stars
# WIND
    wind = 0
    for y in range(0,5):
        wind = wind + int(forecast.wspdEnglish(tomorrow + (x * 24) + y))
    wind = wind / 6
    if wind <= 10:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Morning wind speed is ', wind, Stars
# wdirDegrees
    sumDir = 0
    for y in range(0,5):
        sumDir=sumDir+int(forecast.wdirDegrees(tomorrow + (x * 24) + y))
    winddir = sumDir / 6
    if (winddir > 235 or winddir < 35) or (winddir > 145 and winddir < 215):
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Morning wind direction is ', winddir, Stars
# TEMP
    temp = 0
    for y in range(0,5):
        temp = temp + int(forecast.tempEnglish(tomorrow + (x * 24) + y))
    temp = temp / 6
    if temp >= 65 and temp <= 85:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Morning temp is ', temp, Stars
# SKY
    sky = 0
    for y in range(0,5):
        sky = sky + int(forecast.sky(tomorrow + (x * 24) + y))
    sky = sky / 6
    if sky < 60:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Morning sky is ', sky, Stars


    print '{0} morning   will be a {1:5} ({2}) star day to fly.<br>'.format(dayname,Stars,NumStars)

#
# AFTERNOON
#
# Precent of Percep
    NumStars = 0
    Stars = ""
    pop = 0
    for y in range(5,11):
        pop += int(forecast.pop(tomorrow + (x * 24) + y))
    pop = pop / 6
    if pop <= 10:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Afternoon chance of precep is ', pop, Stars
# WIND
    wind = 0
    for y in range(5,11):
        wind = wind + int(forecast.wspdEnglish(tomorrow + (x * 24) + y))
    wind = wind / 6
    if wind <= 10:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Afternoon wind speed is ', wind, Stars
# wdirDegrees
    sumDir = 0
    for y in range(5,11):
        sumDir=sumDir+int(forecast.wdirDegrees(tomorrow + (x * 24) + y))
    winddir = sumDir / 6
    if (winddir > 235 or winddir < 35) or (winddir > 145 and winddir < 215):
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Afternoon wind direction is ', winddir, Stars
# TEMP
    temp = 0
    for y in range(5,11):
        temp = temp + int(forecast.tempEnglish(tomorrow + (x * 24) + y))
    temp = temp / 6
    if temp >= 65 and temp <= 85:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Afternoon temp is ', temp, Stars
# SKY
    sky = 0
    for y in range(5,11):
        sky = sky + int(forecast.sky(tomorrow + (x * 24) + y))
    sky = sky / 6
    if sky < 60:
        NumStars = NumStars +1
        Stars = Stars+ "*"
    if options.verbose:
        print '    Afternoon sky is ', sky, Stars

    print '{0} afternoon will be a {1:5} ({2}) star day to fly.<br>'.format(dayname,Stars,NumStars)
    print '<br>'

   
if not options.verbose:
  print '<a href="about.html">About this page.</a>'
  print '<p><img src="http://grennan.com/wxcam.jpg" alt="At the field now"'
  print '<p><p> For information on flying at the TORKS RC Air Field please go to <a href="http://torks.org/">TORKS.org</a>.  </body> </html>'

# end
