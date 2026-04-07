import json
import requests

time = [10,11,12,1,2]
db = {}

c = 'y'
while c != 'n':

    choice = int(input(""""Enter your choice:
    1. Book Appoinment
    2. cencel Appoinment
    3.view Appoinment
    
    """))

    if choice == 1:
        name = input("Enter patient name: ")
        mobile = input("Enter mobile number: ")
        doctor = input("Enter preferred doctor: ")
        slot = int(input("Select a time slot (10, 11, 12, 1, 2): "))

        if slot not in time:
            print("This time slot is not valid !!!!!!")

        else:   
            k = []
            for i in db.values():
                k.append(i["slot"])
            if slot in k:
                print("This time slot is already taken!!!!!!!")

            else:
                 with open("data.json","r") as f:
                    db = json.load(f)
                    
                    db.update({mobile: {"name": name, "doctor": doctor, "slot": slot}})
                    print("Appoinment Booked successfully.....")
                    with open("data.json","r") as f:
                        json.dump(db,f)

    elif choice == 2:
            mobile = int(input("Enter your Mobile Number:"))
            if mobile in db:
                db.pop(mobile)
                print("Appoinment Cancelled Successfully.....")
            else:
                print("This Number is not available......")
        
    elif choice == 3:
        with open("data.json","r") as f:
            data = json.load(f)
            print(data)
            
       
    else:
            print("This Choice is not valid!!!!!!!!!")

    c = input("Do you want to book another appointment? (y/n): ")

    