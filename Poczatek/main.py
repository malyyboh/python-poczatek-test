import speed_calculator

running_daistance = float(input("Ile km przebiegles? "))
running_time = float(input("Ile godzin Ci to zajelo? "))

avg_speed = speed_calculator.avg_speed(running_daistance, running_time)
print(f"Twoja srednia przedkosc biegu to {avg_speed:.2f}km/h")