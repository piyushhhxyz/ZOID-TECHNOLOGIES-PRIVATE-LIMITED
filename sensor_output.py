
import random
import time
import threading


#Do not change the following block of code
sensor_data = {
}
def data_generator():
    global sensor_data
    number_of_objects = 10
    object_list = ["Human", "Car", "Tool"]
    state_list = ["Active", "Inactive"]

    while True:
        for i in range(0, number_of_objects):
            sensor_data[i] =  {
                "Status":random.choice(state_list),
                "Properties":{
                    "Class":random.choice(object_list),
                    "Location": [random.randint(0,242354),random.randint(0,242354)],
                    "DetectionTime":random.randint(0,23244)
                    }
            }
        time.sleep(3)
data_thread = threading.Thread(target=data_generator)
data_thread.start()



#Make your changes from here 
#The global variable 'sensor_data' contains all the relvant information. 
#Make a copy of the variable and convert it to JSON formating 


while True:
    print(str(sensor_data)+"\n")
    time.sleep(1)
sensor_information.py
Displaying sensor_information.py.