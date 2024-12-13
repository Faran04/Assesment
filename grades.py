while True:
    mark = int(input("Enter student's mark: "))
    if mark > 100:
        print("Error: Mark cannot be greater than 100. Please enter a valid mark.")
    elif mark < 0:
        print("Error: Mark cannot be negative. Please enter a valid mark.")
    else:
        if mark >= 70:
            print("Grade: A")
            break
        elif mark >= 60:
            print("Grade: B")
            break
        elif mark >= 50:
            print("Grade: C")
            break
        elif mark >= 40:
            print("Grade: D")
            break
        elif mark >= 30:
            print("Grade: E")
            break
        elif mark >= 20:
            print("Grade: F")
            break
        else:
            print("Invalid mark")

