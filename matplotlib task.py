import matplotlib.pyplot as plt

days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
temperatures = [29,31,30,32,34,33,35]

plt.plot(days, temperatures, marker='o', linestyle="-", color="k")
plt.title("Temperature Variation Over a Week")
plt.xlabel("Days of the week")
plt.ylabel("Temperature in degrees Celsius")
plt.show()