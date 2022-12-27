###########################################
# Yaesu FT-991A UTC time and date setting #
###########################################

import serial
from datetime import datetime,date,timezone

ser = serial.Serial(port='COM3',baudrate=38400)  # set YOUR radio's enhanced serial port and rate

###########################################
# Set the FT-991A time zone to UTC        #
###########################################
cat = "DT2+0000;"
yaesu_cat_code = bytes(cat, 'utf-8')
ser.write(yaesu_cat_code)



##########################################
# Set the FT-991A system date            #
##########################################

today = date.today()
now_date = today.strftime("%Y%m%d")
cat = "DT0" + now_date + ";"
yaesu_cat_code = bytes(cat, 'utf-8')
ser.write(yaesu_cat_code)


############################################
# Set the FT-991A systems time             #
############################################

utctime = datetime.now(timezone.utc)
time_now = utctime.strftime("%H%M%S")
cat = "DT1" + time_now + ";"
yaesu_cat_code = bytes(cat, 'utf-8')
ser.write(yaesu_cat_code)

ser.close()