# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

def main():
  
  length = 0
  heights_total = 0
  for heights in student_heights:
    length += 1
    heights_total += heights

  average = heights_total / length
  average = round(average)
  print(f"total height = {heights_total}")
  print(f"number of students = {length}")
  print(f"average height = {average}")

if __name__ == "__main__":
  main()