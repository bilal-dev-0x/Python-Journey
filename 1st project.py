marks = int(input("Enter obtained number : "))
total = int(input("Enter total numbers : "))

divide = marks / total
percentage = divide * 100

if marks > total or marks < 0:
    print("⚠️ You are entering wrong figures")
    print("Please check it before entering")

else:
    print("Percentage : ",percentage,"%")
    

    if percentage >= 90:
        print("Your Grade is A+\U0001F600")

    elif percentage >= 80:
        print("Your Grade is A\U0001F600")

    elif percentage >= 70:
        print("Grade: B")

    elif percentage >= 60:
        print("Grade: C")

    elif percentage >= 50:
        print("Grade : D")

    elif percentage >= 40:
       print("Grade : E")

    else:
        print("Fail")