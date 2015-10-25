"""
@author mbartoli

Calculate the angle between the hour and minutes hands for a valid time
of the format HOUR:MIN. example 2:20 or 15:24.

@usage python clock.py HOUR:MIN
example: python clock.py 8:12
"""
import sys

def get_angle(time):
	time = time.split(":")
	hours = float(time[0])
	minutes = float(time[1])
	
	hour_hand = (hours % 12)/12*360+(360/12)*(minutes/60)
	minute_hand = minutes/60*360
	
	if hour_hand > minute_hand: 
		angle = abs(hour_hand-minute_hand)
	else:
		angle = abs(minute_hand-hour_hand)
	return angle

def main(time):
	time = str(time)
	print get_angle(time)

if __name__ == "__main__":
	main(sys.argv[1])
