#task 02
#ticket price 
age=int(input("Enter your Age:"))
if age <= 0:
 print("Invaild")
elif age <= 12:
    print("You are a child and you get a discount. Ticket price: $10")
elif age >= 18:
    is_student = input("Are you a student? (True/False): ").lower() == "true","yes"
    if is_student:
        print("You are a student. Ticket price: $18")
    else:
        print("You are an adult. Ticket price: $20")
else:
    print("You are a teenager. Ticket price: $15")