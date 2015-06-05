#
# Simple python wrapper for Weather Underground API
#   You need API key to use it. You can get it for free http://www.wunderground.com/weather/api/
#
# Returns the current temperature, weather condition, humidity, wind, 'feels like' temperature, barometric pressure, and visibility.
#
import requests
import sys
import cmath
import datetime
import time

class Conditions(object):
    def __init__(self,key,location):
        self.key = key
        self.location = location 

               
            
        self.data = parse_data(self.key,"conditions",self.location)
        self.rjecnik  = {}
            
        if 'error' in self.data["response"]:
            print "Error! Check your API key or PWS"

        else:

            try:

                self.rjecnik['location'] = self.data["current_observation"]["display_location"]["full"]
                self.rjecnik['observation location'] = self.data["current_observation"]["observation_location"]["full"]
                self.rjecnik['weather'] = self.data["current_observation"]["weather"]
                self.rjecnik['local time'] = self.data["current_observation"]["local_time_rfc822"]
                self.rjecnik['temperature(C)'] = self.data["current_observation"]["temp_c"]
                self.rjecnik['temperature(F)'] = self.data["current_observation"]["temp_f"]
                self.rjecnik['humidity'] = self.data["current_observation"]["relative_humidity"]
                self.rjecnik['wind direction'] = self.data["current_observation"]["wind_dir"]
                self.rjecnik['wind speed(kph)'] = self.data["current_observation"]["wind_kph"]
                self.rjecnik['pressure'] = self.data["current_observation"]["pressure_mb"]
                self.rjecnik['precipitation(mm)'] = self.data["current_observation"]["precip_today_metric"]

            except  (ValueError, KeyError, TypeError) as e:
                print type(e)
                print "Check is data for that city available"
 
        
  
    def weather_test(self,period):
        if location in self.rjecnik.keys():
            return self.rjecnik['location']
        else:
            return "location $s does't exist!" %location

    def weather(self):
        for k,v in self.rjecnik.items():
            print k,':',v
            
    def condition(self):
        return self.rjecnik['weather']
    
    def date(self):
        return self.rjecnik['local time']
        
    def wind_direction(self):
        return self.rjecnik['wind direction']

    def temperature_celsius(self):
        return self.rjecnik['temperature(C)']

    def temperature_fahrenheit(self):
        return self.rjecnik['temperature(F)']

    def wind_speed(self):
        return self.rjecnik['wind speed(kph)']

    def pressure(self):
        return self.rjecnik['pressure']
    
    def humidity(self):
        return self.rjecnik['humidity']
    
    def precipitation(self):
        return self.rjecnik['precipitation(mm)']

    def location(self):
        return self.rjecnik['location']

    def observation_location(self):
        return self.rjecnik['observation location']

#
# Returns a summary of the weather for the next 3 days. This includes high and low temperatures,
# a string text forecast and the conditions.
#
class Forecast(object):
    def __init__(self,key,location):
        self.key = key
        self.location = location
    
            
        self.data = parse_data(self.key,"forecast",self.location)
        self.rjecnik = {}
            
        if 'error' in self.data["response"]:
              print "Error! Check your API key or city/state name"

        else:
            
#            try:
#
#                for period in self.data['forecast']['txt_forecast']['forecastday']:
#		    if 'period' in period['forecastday']:
#                        x=period['period']
#                        self.rjecnik[x]=[period['title']]
#                        self.rjecnik[x].append(peroid['fcttext'])
#
#            except  (ValueError, KeyError, TypeError) as e:
#                print type(e)
#                print "Forcast text: Check is data for that city available"

            try:

                for day in self.data['forecast']['simpleforecast']['forecastday']:
                    if 'day' in day['date']:
                        x=day['period'] 
                        self.rjecnik[x] = {}
			self.rjecnik[x]['epoch']=day['date']['epoch']						
                        self.rjecnik[x]['pretty']=day['date']['pretty']
                        self.rjecnik[x]['day']=day['date']['day']
                        self.rjecnik[x]['month']=day['date']['month']
                        self.rjecnik[x]['year']=day['date']['year']
                        self.rjecnik[x]['yday']=day['date']['yday']
                        self.rjecnik[x]['hour']=day['date']['hour']
                        self.rjecnik[x]['min']=day['date']['min']
                        self.rjecnik[x]['sec']=day['date']['sec']
                        self.rjecnik[x]['isdst']=day['date']['isdst']
                        self.rjecnik[x]['monthname']=day['date']['monthname']
                        self.rjecnik[x]['monthname_short']=day['date']['monthname_short']
                        self.rjecnik[x]['weekday_short']=day['date']['weekday_short']
                        self.rjecnik[x]['weekday']=day['date']['weekday']
                        self.rjecnik[x]['ampm']=day['date']['ampm']
                        self.rjecnik[x]['tz_short']=day['date']['tz_short']
                        self.rjecnik[x]['tz_long']=day['date']['tz_long']
                        self.rjecnik[x]['tz_long']=day['high']
                        self.rjecnik[x]['tz_long']=day['low']
                        self.rjecnik[x]['conditions']=day['conditions']
                        self.rjecnik[x]['icom']=day['icon']
                        self.rjecnik[x]['icon_url']=day['icon_url']
                        self.rjecnik[x]['skyicon']=day['skyicon']
                        self.rjecnik[x]['pop']=day['pop']
                        self.rjecnik[x]['high_celsius']=day['high']['celsius']
                        self.rjecnik[x]['high_fahrenheit']=day['high']['fahrenheit']
                        self.rjecnik[x]['low_celsius']=day['low']['celsius']
                        self.rjecnik[x]['low_fahrenheit']=day['low']['fahrenheit']
                        self.rjecnik[x]['qpf_allday_in']=day['qpf_allday']['in']
                        self.rjecnik[x]['qpf_allday_mm']=day['qpf_allday']['mm']
                        self.rjecnik[x]['qpf_day_in']=day['qpf_day']['in']
                        self.rjecnik[x]['qpf_day_mm']=day['qpf_day']['mm']
                        self.rjecnik[x]['qpf_night_in']=day['qpf_night']['in']
                        self.rjecnik[x]['qpf_night_mm']=day['qpf_night']['mm']
                        self.rjecnik[x]['snow_allday_in']=day['snow_allday']['in']
                        self.rjecnik[x]['snow_allday_cm']=day['snow_allday']['cm']
                        self.rjecnik[x]['snow_day_in']=day['snow_day']['in']
                        self.rjecnik[x]['snow_day_cm']=day['snow_day']['cm']
                        self.rjecnik[x]['snow_night_in']=day['snow_night']['in']
                        self.rjecnik[x]['snow_night_cm']=day['snow_night']['cm']
                        self.rjecnik[x]['maxwind_mph']=day['maxwind']['mph']
                        self.rjecnik[x]['maxwind_kph']=day['maxwind']['kph']
                        self.rjecnik[x]['maxwind_dir']=day['maxwind']['dir']
                        self.rjecnik[x]['maxwind_degrees']=day['maxwind']['degrees']
                        self.rjecnik[x]['avewind_mph']=day['avewind']['mph']
                        self.rjecnik[x]['avewind_kph']=day['avewind']['kph']
                        self.rjecnik[x]['avewind_dir']=day['avewind']['dir']
                        self.rjecnik[x]['avewind_degrees']=day['avewind']['degrees']
                        self.rjecnik[x]['avehumidity']=day['avehumidity']
                        self.rjecnik[x]['maxhumidity']=day['maxhumidity']
                        self.rjecnik[x]['minhumidity']=day['minhumidity']

                            
            except  (ValueError, KeyError, TypeError) as e:
                print type(e)
                print "Forecast data: Check is data for that city available"
                
       
    def forcast_test(self,period):
        if period in self.rjecnik.keys():
            return self.rjecnik[period][1]
        else:
            return "Period $s does't exist!" %period

    def forecast(self):
        for p in self.rjecnik.items():
            print 'Period:', p[0]
            for k,v in p[1].items():
                print '    ',k,':',v
            
    def date_pretty(self,period):
	if period in self.rjecnik.keys():
	    return self.rjecnik[period]['pretty']
	else:
	    print "Period %s doesn't exist!" %period
 
    def day_short(self,period):
	if period in self.rjecnik.keys():
	    return self.rjecnik[period]['weekday']+' '+self.rjecnik[period]['monthname']+' '+str(self.rjecnik[period]['day'])+' '
	else:
	    print "Period %s doesn't exist!" %period
 
    def condition(self,period):
        if period in self.rjecnik.keys():
            return self.rjecnik[period]['conditions']
        else:
            print "Period %s doesn't exist!" %period
                
    def temperature(self,period):
        if period in self.rjecnik.keys():
            temperature = {}
            temperature['celsius high']=self.rjecnik[period]['high_celsius']
            temperature['celsius low']=self.rjecnik[period]['low_celsius']
            temperature['fahrenheit high']=self.rjecnik[period]['high_fahrenheit']
            temperature['fahrenheit low']=self.rjecnik[period]['low_fahrenheit']
            return temperature
        else:
            print "Day %s doesn't exist!" %period


    def humidity(self,period):
        if period in self.rjecnik.keys():
            humidity = {}
            humidity['humidity ave']=self.rjecnik[period]['avehumidity']
            humidity['humidity max']=self.rjecnik[period]['maxhumidity']
            humidity['humidity min']=self.rjecnik[period]['minhumidity']
            return humidity
        else:
            print "Day doesn't exist!"
        
    def wind_mph(self,period):
        if period in self.rjecnik.keys():
            wind = {}
            wind['direction']=self.rjecnik[period]['avewind_degrees']
            wind['speed']=self.rjecnik[period]['avewind_mph']
            return wind
        else:
            print "Day %s doesn't exist!" %period

    def high_wind_mph(self,period):
        if period in self.rjecnik.keys():
            wind = {}
            wind['direction']=self.rjecnik[period]['maxwind_degrees']
            wind['speed']=self.rjecnik[period]['maxwind_mph']
            return wind
        else:
            print "Day %s doesn't exist!" %period

    def precipitation_in(self,period):
        if period in self.rjecnik.keys():
            return self.rjecnik[period]['qpf_allday_in']
        else:
            print "Day %s doesn't exist!" %period

    def precipitation_mm(self,period):
        if period in self.rjecnik.keys():
            return self.rjecnik[period]['qpf_allday_mm']
        else:
            print "Day %s doesn't exist!" %period

    def precipitation_pop(self,period):
        if period in self.rjecnik.keys():
            return self.rjecnik[period]['pop']
        else:
            print "Day %s doesn't exist!" %period

    #just for testing purposes to see is it period in dictionary        
    def weekperiod(self,period):
        if period in self.rjecnik.keys():
            return self.rjecnik[period][9]
        else:
            print "Day %s doesn't exist!" %period


#
# 10 day Hourly forecast
#
class Hourly10day(object):
    def __init__(self,key,location):
        self.key = key
        self.location = location

        self.data = parse_data(self.key,"hourly10day",self.location)
        self.rjecnik  = {}

        if 'error' in self.data["response"]:
            print "Error! Check your API key or PWS"

        else:

            try:
                x = 0
                for time in self.data['hourly_forecast']:
                    x += 1
                    self.rjecnik[x] = {}
                    self.rjecnik[x]['hour'] = time['FCTTIME']['hour']
                    self.rjecnik[x]['hour_padded'] = time['FCTTIME']['hour_padded']
                    self.rjecnik[x]['min'] = time['FCTTIME']['min']
                    self.rjecnik[x]['sec'] = time['FCTTIME']['sec']
                    self.rjecnik[x]['year'] = time['FCTTIME']['year']
                    self.rjecnik[x]['mon'] = time['FCTTIME']['mon']
                    self.rjecnik[x]['mon_padded'] = time['FCTTIME']['mon_padded']
                    self.rjecnik[x]['mon_abbrev'] = time['FCTTIME']['mon_abbrev']
                    self.rjecnik[x]['mday'] = time['FCTTIME']['mday']
                    self.rjecnik[x]['mday_padded'] = time['FCTTIME']['mday_padded']
                    self.rjecnik[x]['yday'] = time['FCTTIME']['yday']
                    self.rjecnik[x]['epoch'] = time['FCTTIME']['epoch']
                    self.rjecnik[x]['pretty'] = time['FCTTIME']['pretty']
                    self.rjecnik[x]['civil'] = time['FCTTIME']['civil']
                    self.rjecnik[x]['month_name'] = time['FCTTIME']['month_name']
                    self.rjecnik[x]['month_name_abbrev'] = time['FCTTIME']['month_name_abbrev']
                    self.rjecnik[x]['weekday_name'] = time['FCTTIME']['weekday_name']
                    self.rjecnik[x]['weekday_name_night'] = time['FCTTIME']['weekday_name_night']
                    self.rjecnik[x]['weekday_name_abbrev'] = time['FCTTIME']['weekday_name_abbrev']
                    self.rjecnik[x]['weekday_name_unlang'] = time['FCTTIME']['weekday_name_unlang']
                    self.rjecnik[x]['weekday_name_night_unlang'] = time['FCTTIME']['weekday_name_night_unlang']
                    self.rjecnik[x]['ampm'] = time['FCTTIME']['ampm']
                    self.rjecnik[x]['tz'] = time['FCTTIME']['tz']
                    self.rjecnik[x]['age'] = time['FCTTIME']['age']
                    self.rjecnik[x]['UTCDATE'] = time['FCTTIME']['UTCDATE']
                    self.rjecnik[x]['temp_english'] = time['temp']['english']
                    self.rjecnik[x]['temp_metric'] = time['temp']['metric']
                    self.rjecnik[x]['dewpoint_english'] = time['dewpoint']['english']
                    self.rjecnik[x]['condition'] = time['condition']
                    self.rjecnik[x]['con'] = time['icon']
                    self.rjecnik[x]['icon_url'] = time['icon_url']
                    self.rjecnik[x]['fctcode'] = time['fctcode']
                    self.rjecnik[x]['sky'] = time['sky']
                    self.rjecnik[x]['wspd_english'] = time['wspd']['english']
                    self.rjecnik[x]['wspd_metric'] = time['wspd']['metric']
                    self.rjecnik[x]['wdir_dir'] = time['wdir']['dir']
                    self.rjecnik[x]['wdir_degrees'] = time['wdir']['degrees']
                    self.rjecnik[x]['wx'] = time['wx']
                    self.rjecnik[x]['uvi'] = time['uvi']
                    self.rjecnik[x]['humidity'] = time['humidity']
                    self.rjecnik[x]['windchill_english'] = time['windchill']['english']
                    self.rjecnik[x]['windchill_metric'] = time['windchill']['metric']
		    self.rjecnik[x]['heatindex_english'] = time['heatindex']['english']
		    self.rjecnik[x]['heatindex_metric'] = time['heatindex']['metric']
                    self.rjecnik[x]['feelslike_english'] = time['feelslike']['english']
                    self.rjecnik[x]['feelslike_metric'] = time['feelslike']['metric']
                    self.rjecnik[x]['qpf_english'] = time['qpf']['english']
                    self.rjecnik[x]['qpf_metric'] = time['qpf']['metric']
                    self.rjecnik[x]['snow_english'] = time['snow']['english']
                    self.rjecnik[x]['pop'] = time['pop']
                    self.rjecnik[x]['mslp_english'] = time['mslp']['english']
                    self.rjecnik[x]['mslp_metric'] = time['mslp']['metric']

            except  (ValueError, KeyError, TypeError) as e:
                print type(e)
                print "Check is data for that city available"

    def hourly10day(self):
        for k,v in self.rjecnik.items():
            print 'Hour:', k
            print '    ',k,':',v

    def pop(self,hour):
        if hour in self.rjecnik.keys():
            return self.rjecnik[hour]['pop']
        else:
            print "Hour %s doesn't exist!" %hour

    def weekdayName(self,hour):
        if hour in self.rjecnik.keys():
            return self.rjecnik[hour]['weekday_name']
        else:
            print "Hour %s doesn't exist!" %hour

    def sky(self,hour):
        if hour in self.rjecnik.keys():
            return self.rjecnik[hour]['sky']
        else:
            print "Hour %s doesn't exist!" %hour

    def wspdEnglish(self,hour):
        if hour in self.rjecnik.keys():
            return self.rjecnik[hour]['wspd_english']
        else:
            print "Hour %s doesn't exist!" %hour

    def tempEnglish(self,hour):
        if hour in self.rjecnik.keys():
            return self.rjecnik[hour]['temp_english']
        else:
            print "Hour %s doesn't exist!" %hour

    def wdirDegrees(self,hour):
        if hour in self.rjecnik.keys():
            return self.rjecnik[hour]['wdir_degrees']
        else:
            print "Hour %s doesn't exist!" %hour


#
# Returns the moon phase, sunrise and sunset times.
#
class Astronomy(object):
    def __init__(self,key,location):
        self.key = key
        self.location = location 

        
        self.data = parse_data(self.key,"astronomy",self.location)
        self.rjecnik  = {}
        if 'error' in self.data["response"]:
            print "Error! Check your API key or city/state name"

        else:
            try:
                sunrise = self.data["sun_phase"]["sunrise"]["hour"] + ':' + self.data["sun_phase"]["sunrise"]["minute"]
                sunset = self.data["sun_phase"]["sunset"]["hour"] + ':' + self.data["sun_phase"]["sunset"]["minute"]
                self.rjecnik['sunrise'] = sunrise
                self.rjecnik['sunset'] = sunset
                
            except  (ValueError, KeyError, TypeError) as e:
                print type(e)
                print "Check is data for that city available"
                
    def astronomy(self):
	print 'Sunrise is at', self.rjecnik['sunrise']
        print 'Sunset is at', self.rjecnik['sunset']
  
    def sunrise(self):
        return self.rjecnik['sunrise']

    def sunset(self):
        return self.rjecnik['sunset']

    def sunriseHour(self):
        return self.data["sun_phase"]["sunrise"]["hour"]

    def sunriseMinute(self):
        return self.data["sun_phase"]["sunrise"]["minute"]

    def sunsetHour(self):
        return self.data["sun_phase"]["sunset"]["hour"]

    def sunsetMinute(self):
        return self.data["sun_phase"]["sunset"]["minute"]

#
#
#
def parse_data(key, forecast, location):
    
    try:
            
        json_data = requests.get("http://api.wunderground.com/api/"+key+"/"+forecast+"/q/"+location+".json")
        json = json_data.json()
        return json
    
    except requests.exceptions.ConnectionError as e:
        print type(e)
        print "Check your network connection!"
        sys.exit(1)

#end
