marks = []
total_marks = 0
for i in range(5):
 subject = input(f"Enter marks for subject {i+1}: ")
 marks.append(int(subject))
 total_marks += int(subject)
percentage = (total_marks/500)*100
if percentage >= 90:
 grade = 'A'
elif percentage >= 80:
 grade = 'B'
elif percentage >= 70:
 grade = 'C'
elif percentage >= 60:
 grade = 'D'
elif percentage >= 40:
 grade = 'E'
else:
 grade = 'F'
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}") 