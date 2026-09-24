# conditional tests:


name = "Mario"

if name == "Mario":
    print("Test 1 passed")
else:
    print("Test 1 failed")

if name != "Sonic":
    print("Test 2 passed")
else:
    print("Test 2 failed")


color = "Red"

if color.lower() == "Red":
    print("Test 3 passed")
else:
    print("Test 3 failed")


age = 18

if age == 18:
    print("Test 4 passed")
else:
    print("Test 4 failed")

if age != 20:
    print("Test 5 passed")
else:
    print("Test 5 failed")

if age > 16:
    print("Test 6 passed")
else:
    print("Test 6 failed")

if age < 21:
    print("Test 7 passed")
else:
    print("Test 7 failed")

if age >= 18:
    print("Test 8 passed")
else:
    print("Test 8 failed")

if age <= 18:
    print("Test 9 passed")
else:
    print("Test 9 failed")



age = 20
has_id = True

if age >= 18 and has_id:
    print("Test 10 passed")
else:
    print("Test 10 failed")



day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Test 11 passed")
else:
    print("Test 11 failed")



foods = ["pizza", "burgers", "tacos"]

if "pizza" in foods:
    print("Test 12 passed")
else:
    print("Test 12 failed")



if "sushi" not in foods:
    print("Test 13 passed")
else:
    print("Test 13 failed")