import time
import webbrowser


print "What time do you want to wake up?"
print "Please enter in military time in the following format example: 06:25"
alarm = raw_input(">")

Time = time.strftime("%H:%M")

while Time != alarm:
    sec_time = time.strftime("%H:%M:%S")
    
    print "The time is:" + sec_time 
    Time = time.strftime("%H:%M")
    time.sleep(1)
    
    if Time == alarm:
        webbrowser.open("https://www.youtube.com/watch?v=dIoILN_KrhU")
    


