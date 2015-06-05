TORKS Air Field Weather Station 

These are files used to run the TORKS Weather Station.

See torks.ws

The weather station is a Ambent Weather 1400IP. This uses the 
AW-1400 and the AM-Observer module.

The Observer module connects via IP to a Raspberry Pi.

The Raspberry Pi connest to a APRS-Pi to transmit weather 
observations via APRS. To do this the ws1400aprs.py program
scrapes the data off the Observer module's webpage and formats
it for APRS. 

The weather station also uses a Raspberry Pi Camera to send
pictures back to a public webpage. The program wxcam2.py is 
used to do this.

For more information on the weather stations or TORKS, please
email Mark at Grennan dot com.





