# Build a counter from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1

count = 1
while count <= 10:
    print(count)
    count += 2

# While Condition e.g. - Write a program that keep asking "Do You Agree" until the user type "Yes"

answer = ''
while answer != "yes":
    answer = input("Do You Agree?(yes/no): ")
print("Thank You")

# While True e.g. - 

while True:
    answer = input("Do You Agree?(yes/no): ")
    if answer == "yes":
        break
print("Thank You")

# Challenge - below loop with new requirements like 
# Allow upto 3 attempts if the user type yes in 3 attempt , print "Glad we are on same page"
# Otherwise, print "3 Strikes, You are Out"

attempt = 0
while attempt < 3:
    answer = input("DO you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we are on same page")
        break
    attempt += 1
else:
    print("3 Strikes, You are Out")

