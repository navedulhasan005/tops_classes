# Book Appointment:
# ● Prompt for patient name, age, mobile number, and preferred doctor.
# ● Show time slots (10am, 11am, 12pm, 2pm, 3pm).
# ● Check slot availability and confirm booking.
#  View/Cancel Appointment:
# ● Allow patient to view or cancel their appointment using mobile number

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
            print("This time slot is not valid....")

        else:   
            k = []
            for i in db.values():
                k.append(i["slot"])
            if slot in k:
                print("This time slot is already taken...")

            else:
                db.update({mobile: {"name": name, "doctor": doctor, "slot": slot}})
                print("Appoinment Booked successfully.....")

    if choice == 2:
        mobile = int(input("Enter your Mobile Number:"))
        if mobile in db:
            del db[mobile]
            print("Appoinment Cancelled successfully.....")
        else:
            print("No appoinment found with this mobile number...")

    if choice == 3:
        mobile = int(input("Enter your Mobile Number:"))
        if mobile in db:
            appointment = db[mobile]
            print(f"Name: {appointment['name']}")
            print(f"Doctor: Dr. {appointment['doctor']}")
            print(f"Slot: {appointment['slot']}am")
        else:
            print("No appoinment found with this mobile number...")

    c = input("Do you want to book another appointment? (y/n): ")