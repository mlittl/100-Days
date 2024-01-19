age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

aged = int(age) * 52 # This is the number of weeks wasted
totaltime = 90 * 52 # this is the number of weeks we have
timeremaining = totaltime - aged
print(f"You have {timeremaining} weeks left.")