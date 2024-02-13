# python code to suggest automatically activates for you 
import random


activities = {
    'A' : {
        "activity":"Have a paper airplane contest with some friends",
        "type":"social",
        "participants":4,
        "price":0.02,
        "link":"",
        "key":"8557562",
        "accessibility":0.05
    },
    'B' : {
        "activity":"Learn woodworking",
        "type":"diy",
        "participants":1,
        "price":0.3,
        "link":"",
        "key":"9216391",
        "accessibility":0.3
        },
    'C' : {
        "activity":"Go to an escape room",
        "type":"social",
        "participants":4,
        "price":0.5,
        "link":"",
        "key":"5585829",
        "accessibility":0.3
    },
    'D' : {
        "activity":"Have a picnic with some friends",
        "type":"social",
        "participants":3,
        "price":0.1,
        "link":"",
        "key":"6813070",
        "accessibility":0.1
    },
    'E':{
        "activity":"Plan a trip to another country",
        "type":"recreational",
        "participants":1,
        "price":0,
        "link":"",
        "key":"5554727",
        "accessibility":0
    } 

}




def suggested_activities():
    random_key = random.choice(list(activities.keys()))
    suggested_activity = activities[random_key]
    print(f"Suggested activity: {suggested_activity['activity']}")
    print(f"Type: {suggested_activity['type']}")
    print(f"Participants: {suggested_activity['participants']}")
    print(f"Price: {suggested_activity['price']}")
    print(f"link: {suggested_activity['link']}")
    print(f"key: {suggested_activity['key']}")
    print(f"Accessibility: {suggested_activity['accessibility']}")




if __name__ == "__main__":
    suggested_activities()