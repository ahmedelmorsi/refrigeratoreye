import time
import random 
class Sensor(object):
    
    def gettemp(self):
        try:
            mytemp = ''
            filename = 'w1_slave'
            f = open('/sys/bus/w1/devices/' + '28-0014154fb8ff'+ '/' + filename, 'r')
            line = f.readline() # read 1st line
            crc = line.rsplit(' ',1)
            crc = crc[1].replace('\n', '')
            if crc=='YES':
                line = f.readline() # read 2nd line
                mytemp = line.rsplit('t=',1)
            else:
                mytemp = random.randint(10, 24)
                f.close()
            return int(mytemp[1])
        except:
            return random.randint(10, 24)
    def getdist(self):
        try:
            import RPi.GPIO as GPIO
            GPIO.setmode(GPIO.BCM)
            GPIO_trig = 23
            GPIO_echo = 24
            print "Ultrasonic Measurement"
            GPIO.setup(GPIO_trig,GPIO.OUT)  # trig
            GPIO.output(GPIO_trig, False)
            GPIO.setup(GPIO_echo,GPIO.IN)      # echo
            time.sleep(0.5)
            # Send 10us pulse to trig
            GPIO.output(GPIO_trig, True)
            time.sleep(0.00001)
            GPIO.output(GPIO_trig, False)
            start = time.time()
            while GPIO.input(GPIO_echo)==0:
              start = time.time()
            while GPIO.input(GPIO_echo)==1:
              stop = time.time()
            # Calculate time 
            T = stop-start
            distance = T * 17000
            print "Distance : " , distance , "cm"
            GPIO.cleanup()
        except:
            distance=random.randint(2, 20)
        return distance
