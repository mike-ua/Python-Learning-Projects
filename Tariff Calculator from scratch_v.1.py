finished = False
while finished == False:
    print("Let's calculate the delivery tariff based on two zones")

    pickup_zone = int(input("Pick-up zone is:  "))
    delivery_zone = int(input("Drop-off zone is: "))
        
    zone1 = 30
    zone2 = 60
    zone3 = 90

    def find_highest_zone():
        if pickup_zone > delivery_zone and pickup_zone <=4:
            return pickup_zone
        elif delivery_zone > pickup_zone and delivery_zone <=4:
            return delivery_zone
        elif delivery_zone == pickup_zone and delivery_zone <=4:
            return delivery_zone
#        elif delivery_zone or pickup_zone >=4:
#            return "Sorry, you entered an incorrect zone"
        else:
            return "Sorry, you entered an incorrect zone"
               
    def calculate_rate():
        if find_highest_zone() == 1:
            print("Your rate is: " + str(zone1))
        elif find_highest_zone() == 2:
            print("Your rate is: " + str(zone2))
        elif find_highest_zone() == 3:
            print("Your rate is: " + str(zone3))
            finished = True
        else:
            print("Sorry, that's not a correct zone, try again.")
              
    print(calculate_rate())





                    
        #finished = True
