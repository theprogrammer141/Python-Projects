#Interface
print("\n\n")

print("-" * 20)
print("Welcome to the Quiz!")
print("Please answer the following questions to achieve score!")
print("Note : Every answer has four choices, choose the correct one!")
print("-" * 20)
print("\n")

#Question to be asked
print("-" * 20)
print("Question # 1:")
print("-" * 20)
print("Who invented the World Wide Web?")
a = "Tim Berners-Lee"
print("a.", a)
b = "Michael Faraday"
print("b.", b)
c = "John F.Kennedy"
print("c.", c)
d = "Bjarne Stroustrup"
print("d.", d)
print("-" * 20)

answer = str(input("Ans: "))

#Score to be incremented
score = 0

#Answer validation
if answer == "a":
    print("Correct!")
    score = score + 1       #Increment score if answer is correct
    print("-" * 20)
else:
    print("Incorrect")
    print("-" * 20)

print("-" * 20)
print("Question # 2:")
print("-" * 20)
print("Why was java invented?")
a = "To overcome syntax difficulty"
print("a.", a)
b = "To achieve more flexibility"
print("b.", b)
c = "To focus on software design"
print("c.", c)
d = "To achieve cross-platform compatibility"
print("d.", d)
print("-" * 20)

answer = str(input("Ans: "))

#Answer validation
if answer == "d":
    print("Correct!")
    score = score + 1
    print("-" * 20)
else:
    print("Incorrect!")
    print("-" * 20)


print("-" * 20)
print("Question # 3: ")
print("-" * 20)
print("When was Python invented?")
a = 1990
print("a.", a)
b = 1989
print("b.", b)
c = 1979
print("c.", c)
d = 1980
print("d.", d)
print("-" * 20)

answer = str(input("Ans: "))

#Answer Validation
if answer == "a":
    print("Correct!")
    score = score + 1
    print("-" * 20)
else:
    print("Incorrect!")
    print("-" * 20)


print("-" * 20)
print("Question # 4: ")
print("-" * 20)
print("Why Python is considered a powerful language?")
a = "Because of quick execution times"
print("a.", a)
b = "Because of less memory usage"
print("b.", b)
c = "Because of low-level memory interaction"
print("c.", c)
d = "Because of large libraries availability"
print("d.", d)
print("-" * 20)

answer = str(input("Ans: "))

#Answer validation
if answer == "d":
    print("Correct!")
    score = score + 1
    print("-" * 20)
else:
    print("Incorrect!")
    print("-" * 20)

print("-" * 20)
print("Question # 5: ")
print("-" * 20)
print("For what purpose, Python is used largely now-a-days?")
a = "Data Structures and Algorithms"
print("a.", a)
b = "Artificial Intelligence/Data Science"
print("b.", b)
c = "Robotics"
print("c.", c)
d = "Economics and Management"
print("d.", d)
print("-" * 20)

answer = str(input("Ans: "))

#Answer validation
if answer == "b":
    print("Correct!")
    score = score + 1
    print("-" * 20)
else:
    print("Incorrect!")
    print("-" * 20)

print("-" * 20)
print("Quiz Over, thank you!")
print("-" * 20)

print("\n")
print("Total Score: ", score)



