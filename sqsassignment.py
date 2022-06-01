def parkingsystem(input_path : str, output_path : str) :
    """In this We created one dictionary called Slots which have two keys Available and UnAvailable
    Whenever Slot is occupied by vehicle then that slot number is poped out and move to UnAvailable
     dictionary which helps us in managing the slots records easily"""
    file1 = open(input_path, 'r')
    file2 = open(output_path,'w')
    ParkandLeave = file1.readlines() # read lines from input text file
    Slots = {}
    for parkandleave in ParkandLeave :
        if "Create_parking_lot" in parkandleave:
            parkandleave= parkandleave.split(" ")
            totalSlots = int(parkandleave[1])
            Slots = {"Available": {idx: {"vehicle_Number": "", "age": 0} for idx in range(1, totalSlots + 1)},
                     "UnAvailable": {}}
            file2.write(f"Created parking of {totalSlots} slots\n")
        else :
            if Slots :
                if "Park" in parkandleave:
                    parkandleave= parkandleave.split(" ")
                    first_key = list(Slots["Available"].keys())[0]
                    occuping_space = Slots["Available"].pop(first_key)
                    occuping_space["vehicle_Number"] = parkandleave[1]
                    occuping_space["age"] = int(parkandleave[3])
                    Slots["UnAvailable"].update({first_key:occuping_space})
                    file2.write(f"Car with vehicle registration number {parkandleave[1]} has been parked at slot number {first_key}\n")

                elif "Slot_numbers_for_driver_of_age" in parkandleave:
                    slots = ""
                    parkandleave = parkandleave.split(" ")
                    for slotNo, car_detail in Slots["UnAvailable"].items():
                        if  car_detail.get("age") == int(parkandleave[1]) :
                            slots += f"{slotNo} "
                    file2.write(f"{slots.strip().replace(' ',', ')}\n")

                elif "Slot_number_for_car_with_number" in parkandleave:
                    parkandleave = parkandleave.split(" ")
                    for slotNo, car_detail in Slots["UnAvailable"].items():
                        if car_detail.get("vehicle_Number") == parkandleave[1].strip("\n"):
                            file2.write(f"{slotNo}\n")
                            break
                else :
                    parkandleave = parkandleave.split(" ")
                    for slotNo, car_detail in Slots["UnAvailable"].items():
                        if slotNo == int(parkandleave[1]) :
                            released_space=Slots["UnAvailable"].pop(slotNo)
                            Slots["Available"].update({slotNo: {"vehicle_Number" :"" , "age" : 0}})
                            file2.write(f"Slot number {slotNo} vacated, the car with vehicle registration number {released_space['vehicle_Number']} left the space, the driver of the car was of age {int(released_space['age'])}\n")
                            break
            else :
                file2.write("Total number of slots are not given\n")
    file1.close()
    file2.close()


input_path = "input.txt"
output_path = "output.txt"
parkingsystem(input_path,output_path)




