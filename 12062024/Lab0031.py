# need to calculate the grade


score = int(input("Enter the score"))

if score >= 90 and score <= 100:
    print("Grade is A")
elif score >= 80 and score <= 89:
    print("Grade is B")
elif score >= 70 and score <= 79:
    print("Grade is C")
elif score >= 60 and score <= 69:
    print("Grade is D")
elif score >= 0 and score <= 59:
    print("Fail")
else:
    print("invalid score")
