student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# using python sum
total_exam_score = sum(student_scores)
print(total_exam_score)

# using a loop to add them all
total_sum = 0
for score in student_scores:
    total_sum += score

print(total_sum)

# Find the highest score
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(highest_score)
