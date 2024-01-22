# Input a list of student scores
#student_scores = input().split()
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

def score_calc(student_scores):
  highest_score = 0
  for score in student_scores:
    if score > highest_score:
      highest_score = score
  return highest_score

def main():
  highest_score = score_calc(student_scores)
  print(f"The highest score in the class is: {highest_score}")


if __name__ == "__main__":
  main()