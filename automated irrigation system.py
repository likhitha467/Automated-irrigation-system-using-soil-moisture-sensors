
def irrigation_system(moisture):

    if moisture <= 400:
        condition = "DRY"
        pump = "ON"
        red_led = "ON"
        green_led = "OFF"

    elif moisture <= 700:
        condition = "MEDIUM"
        pump = "OFF"
        red_led = "OFF"
        green_led = "OFF"

    else:
        condition = "WET"
        pump = "OFF"
        red_led = "OFF"
        green_led = "ON"

    print("Moisture Value:", moisture)
    print("Soil Condition:", condition)
    print("Water Pump:", pump)
    print("Red LED:", red_led)
    print("Green LED:", green_led)
    print("--------------------------")


test_values = [120,300,450,600,780,900,1100]

for value in test_values:
    irrigation_system(value)
