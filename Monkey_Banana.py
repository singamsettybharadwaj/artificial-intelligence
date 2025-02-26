monkey_position = "Door"
chair_position = "Corner"
banana_position = "Ceiling"
monkey_on_chair = False
banana_grabbed = False
if monkey_position != chair_position:
    print("Monkey moves to the chair.")
    monkey_position = chair_position
if monkey_position == chair_position and not monkey_on_chair:
    print("Monkey climbs the chair.")
    monkey_on_chair = True
if monkey_on_chair and not banana_grabbed:
    print("Monkey grabs the banana!")
    banana_grabbed = True
if banana_grabbed:
    print("Task complete: The monkey has the banana!")
else:
    print("Task failed: The monkey couldn't grab the banana.")
