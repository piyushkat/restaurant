import math
import random
import re
import haversine as hs
from datetime import date
from rest_framework.response import Response



def email_otp():
  r1 = random.randint(100000,999999)
  return r1


def Validate_Password(password):
    try:
    
        regex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        if (re.fullmatch(regex, password)):
            return True
        return False
    except:
        return Response({"msg": "Password is empty"})
        

def get_distance(x1,y1,x2,y2):
  """
  :return: To find the distance between the latitude and longitude
  """
  loc1 = (x1,y1)
  loc2 = (x2,y2)
  return hs.haversine(loc1, loc2)
  
def calculateAge(dob):
    today = date.today()
    age = today.year - \
        int(dob[:4]) - ((today.month, today.day)
                        < (int(dob[5:7]), int(dob[8:10])))
    return age





#given coordinates
x1 = 10
y1 = 10
# radius of 10km
radius = 10

# calculate all the coordinates in radius of 10km 
for x in range(x1-radius,x1+radius+1):
  for y in range(y1-radius,y1+radius+1):
    if math.sqrt((x-x1)**2 + (y-y1)**2)<=radius:
      print(x,y)