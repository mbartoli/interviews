"""
@author mbartoli

Calculate the angle between the hour and minutes hands
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
