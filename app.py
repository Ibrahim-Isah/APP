command = ""
started = False
#  making the car engine
while command != "quit":
    command = input("Car :")
    command = command.lower()
    #  commands given to the engine that makes the car know what to do
    if command == "start":
        if started:
            print("Car has started already")
        else:
            started = True
            print("Engine has started")
            

    elif command == "stop":
        if not started:
            print("car is stopped already")
        else:
            started = False
            print("Engine has stopped")

    elif command == "help":
        print("""
        start - to start engine
        stop - to stop engine
        quit - to get out of car
        """)
    elif command == "quit":
        break
    else:
        print("I dont know what you enter, type help for assitance")
else:
    print("")
