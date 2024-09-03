import RPi.GPIO as GPIO
import urllib3
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)

while(1):
  URL="https://api.thingspeak.com/channels/2306806/feeds.json?api_key=U54U1ZONQ4V27KRZ&results=1"
  http = urllib3.PoolManager()
  resp = http.request("GET", URL)
  r = str(resp.data)
  s = r [r.find("start2:")+7:r.find(":end2")]
  check = int(s)
  while(check):
    r = r [r.find("D_START:")+8:r.find(":D_END")]
    print(r)
    v1=r[1:2]
    v2=r[4:5]
    v=r[7:8]
    v1=int(v1)
    v2=int(v2)
    v=int(v)

    if(v==1):
      print("Water pump on")
      GPIO.output(17,GPIO.LOW)
      GPIO.output(7, GPIO.HIGH)
      time.sleep(5)
      print("Water pump off")
      GPIO.output(17,GPIO.HIGH)
      GPIO.output(7, GPIO.LOW)
      if(v2==1):
        print("Fertilizer pump on")
        GPIO.output(27,GPIO.LOW)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(5)
        print("Fertilizer pump off")
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(7, GPIO.LOW)
    elif(v==2):
        print("Fertilizer pump on")
        GPIO.output(27,GPIO.LOW)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(5)
        print("Fertilizer pump off")
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(7, GPIO.LOW)`
        if(v1==1):
          print("Water pump on")
          GPIO.output(17,GPIO.LOW)
          GPIO.output(7, GPIO.HIGH)
          time.sleep(5)
          print("Water pump off")
          GPIO.output(17,GPIO.HIGH)
          GPIO.output(7, GPIO.LOW)
    elif(v1==1 and v2==1):
        print("Both are getting on")
        GPIO.output(17,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(5)
        print("Both are getting off")
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(7, GPIO.LOW)
    elif(v1==1):
        print("Water pump on")
        GPIO.output(17,GPIO.LOW)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(5)
        print("Water pump off")
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(7, GPIO.LOW)
    elif(v2==1):
        print("Fertilizer pump on")
        GPIO.output(27,GPIO.LOW)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(5)
        print("Fertilizer pump off")
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(7, GPIO.LOW)
    else:
        print("No need of water")
        GPIO.output(7, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(7, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(7, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(7, GPIO.LOW)
    time.sleep(10)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(7, GPIO.LOW)
    check=0
    print("waiting for instruction")
    api_key="WPP6IT1CUULUHPJI"
    URL="http://api.thingspeak.com/update?api_key="+api_key+"&field1=D_START:"+r+":D_END&field2=start1:1:end1&field3=start2:0:end2"
    # Creating a PoolManager instance for sending requests.
    http = urllib3.PoolManager()
    # Sending a GET request and getting back response as HTTPResponse object.
    resp = http.request("GET", URL)
    # Print the returned data.
    #print(resp.data)



