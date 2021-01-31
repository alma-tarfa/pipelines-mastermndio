import requests
import csv 

#This is where we will extract 
def get_launch_data(url):
    launch_data = requests.get(url)
    return launch_data.json()

#This is where we will transfrom 
def transform_data(launch_data):
    mission_names =[]
    missions_image = []
    mission_id = []
    
    for launch in launch_data:
        mission_names.append(launch["mission_name"])
        missions_image.append(launch["links"]["mission_patch"])
        mission_id.append(launch["flight_number"])
        
    #This is where we will load 
    # loads data to csv        
    with open('flightData.csv', 'w', newline='') as f:
        for a, b, c in zip(mission_id, mission_names, missions_image):   
            writer = csv.writer(f)
            writer.writerow([a,b,c])

    print(len(mission_names))
    print(len(missions_image))
    print(len(mission_id))



#This is where we run the code
result = get_launch_data("https://api.spacexdata.com/v3/launches")
#print(len(result))

transform_data(result)