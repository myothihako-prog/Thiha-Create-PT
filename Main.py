import turtle as trtl

writer = trtl.Turtle()
writer.hideturtle()
writer.speed(0)
writer.goto(0,0)#location of written text 
font = ("Arial", 20, "normal")#font
#List for Algebra 1 and Spanish 1
#If user chooses Algebra 1 then assign Algebra 1 to subject
#Else choose Spanish 1 then assign Spanish 1 to subject

#SPANISH QUESTIONS
def spanish1():
  writer.clear()#Makes sure there won't be a overlap
  writer.write("What does El mean?", font=font)#font is Arial, 8, and normal.
  #I want to use answer as a variable to get answer so I have to put within the function so that other functions wouldn't use the variable here
  answer = input("1. He  \n2.Him \n3.Her \n4.The\n")#User Input to ask for answer
  if answer == "1" or answer == "2" or answer == "3" or answer == "He" or answer == "Him" or answer == "Her":#wrong answers
    print("You got it wrong! El actually means The, with the accent is He.")
    writer.write("You got it wrong!", font=font)
  elif answer == "4" or answer == "The":
    print("You got it right!")
    writer.clear()#removes overlap from last written font.
    writer.write("You got it right!")
  else:
    print("Please only answer with the corresponding number or word.")
    writer.clear()#removes overlap from last written font.
    writer.write("Please only answer with the corresponding number or word.")
    spanish1()#repeats the function if unvalid input is an answer
    
def spanish2():
  writer.clear()#clears any text that was inputted in writer
  writer.write("What does cama mean?")
  answer = input("1.House \n2.Bed \n3. Wall \n4. Shower\n")
  if answer == "1" or answer == "3" or answer == "4" or answer=="House" or answer=="Wall" or answer == "Shower":#wrong answers
    print("You got it wrong! Cama actually means Bed.")
    writer.write("You got it wrong! Cama actually means Bed.")
  elif answer == "2" or answer == "Cama":
    print("You got it right!")
    writer.clear()#removes overlap from last written font.
    writer.write("You got it right!")
  else:
    print("Please only answer with the corresponding number or word.")
    writer.clear()#removes overlap from last written font.
    writer.write("Please only answer with the corresponding number or word.")
    spanish2()
  
def spanish3():
  writer.clear()
  writer.write("What does tener mean?")
  answer = input("1.To have \n 2.To make \n3.To run \n4. To read\n")
  if answer == "2" or answer == "3" or answer == "4" or answer == "To make" or answer == "To run" or answer == "To read":
    print("You got it wrong! Tener means to have.")
    writer.clear()
    writer.write("You got it wrong! Tener means to have.")
  elif answer == "1" or answer == "To Have":
    print("You got it right!")
    writer.clear()#removes overlap from last written font.
    writer.write("You got it right!")
  else:#if input isn't in the if or elif.
    print("Please only answer with the corresponding number or word.")
    writer.clear()#removes overlap from last written font.
    writer.write("Please only answer with the corresponding number or word.")
    spanish3()#restarts function
#Less complex and simpified way to make questions using lists.
#I got this idea from my teacher, note that this code is still what I created though. 
def spanish4():
  right_answers = ["hola",4]
  writer.clear()
  writer.write("What does hello mean in spanish?")
  print("What does hello mean in spanish?")
  answer = input("1.Amigo \n 2.Ella \n 3.El \n 4.Hola")
  if answer in right_answers:
    writer.clear()
    writer.write("You got it right!")
    print("You got it right!")
  else:
    writer.clear()
    writer.write("You got it wrong! Hello means Hola in spanish.")
    print("You got it wrong! Hello means Hola in spanish.")
def spanish5():
  right_answers = ["Buenos días", 3]
  writer.clear()
  writer.write("How do you say good morning in spanish?")
  print("How do you say good morning in spanish?")
  

#ALGEBRA QUESTIONS
def algebra1():
  writer.clear()
  writer.write("What is the slope of y=5x+1?")
  answer = input("1.1/1 \n2.4/3 \n3.5/1 \n4.-5/1")
  if answer == "1" or answer == "2" or answer == "4" or answer == "1/1" or answer == "4/3" or answer == "-5/1":
    print("You got it wrong! In a equation of y=mx+b, m stands for slope.")
    writer.clear()
    writer.write("You got it wrong! In a equation of y=mx+b, m stands for slope.", algin="center", font=font)
  elif answer == "2" or answer == "5/1":
    print("You got it right!")
    writer.clear()
    writer.write("You got it right!")
  else:
    print("Please onmly answer with the corresponding number or word.")
    writer.clear()#removes overlap from last written font.
    writer.write("Please only answer with the corresponding number or word.")

#Less complex and simpified way to make questions using lists.
#I got this idea from my teacher, note that this code is still what I created though. 
def algebra2():
  right_answers = [1, 8]
  writer.clear()
  writer.write("What is the y-intercept of y=5x+8?")
  answer = input("1.8 \n 2.5\n 3.1\n 4.5\n")
  if answer in right_answers:
    writer.clear()
    writer.write("You got it right!")
    print("You got it right!")
  else:
    writer.clear()
    writer.write("You got it wrong! The y-intercept is 8.")
    print("You got it wrong! The y-intercept is 8.")

def algebra3():
  right_answers = [3, 8]
  writer.clear()
  writer.write("Find x in x + 12 = 20")
  answer = input("1.-8 \n2.12 \n3.8 \n 4.20 \n")
  if answer in right_answers:
    writer.clear()
    writer.write("You got it right!")
    print("You got it right!")
  else:
    writer.clear()
    writer.write("You got it wrong! x is 8")
    print("You got it wrong! x is 8")

def algebra4():
  right_answers = [-3/-5,1]
  writer.clear()
  writer.write("Find the slope of (3,5) and (8,8)")
  answer = input("1.3/5 \n2.5/3 \n 3.5/-3 \n 3/8\n")
  if answer in right_answers:
    writer.clear()
    writer.write("You got it right!")
    print("You got it right!")
  else:
    writer.clear()
    writer.write("You got it wrong! m is 3/5")
    print("You got it wrong! m is 3/5")
#Create list of right answer within function
#if the input isn't in right answer, say you got it wrong
def algebra5():
  right_answers = [5,4]
  writer.clear()
  writer.write("Find the hyptenuse of a right triangle that has sides of 3 and 4.,", font=font)
  answer = input("1.3\n 2.4\n 3.7 \n 4.5\n")
  if answer in right_answers:
    writer.clear()
    writer.write("You got it right!")
    print("You got it right!")
  else:
    writer.clear()
    writer.write("You got it wrong! The hyptenuse is 5.", font=font)
    print("You got it wrong! The hyptenuse is 5.")
  
#LISTS for questions 
# I am using these functions that generate questions in a list to use when iterrating these questions for a spanish quiz
spanish_questions = [spanish1, spanish2, spanish3]
algebra_questions = []
#EXECUTION
#Ask User_Input if they want a Spanish 1 or Algebra 1 quiz.
def ask_subject():
  writer.clear()#makes sure there isn't an overlap
  subject = input("Do you want to have to quiz of Spanish 1 or Algebra 1? Say S or A")
  
  #if subject isn't S or A then ask again
  if not subject == "A" or not subject =="S":
    print("Please input only S or A")
    writer.clear()#makes sure there isn't am overlap
    writer.write("Please input only S or A")
    print("Try again.")
    ask_subject()

ask_subject()
    

def user_chosen_subject(subject):#uses input of subject to determine if subject is Algebra or Spanish
  if subject == "S":
    for question in spanish_questions():#iterate through each question in spanish_questions
      #calls the function within spanish_questions list by using question() 
      question()#1.spanish1() 2. spanish2() 3.spanish3()
      
  elif subject == "A":     
    for question in algebra_questions():
      question()
      
  else:#if it is not working somehow, make a loop for user_chosen_subject
    print("Try again.")
    user_chosen_subject(subject)
   


trtl.mainloop()