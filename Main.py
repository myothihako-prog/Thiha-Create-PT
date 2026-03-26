import turtle as trtl
import time
writer = trtl.Turtle()
writer.hideturtle()
writer.speed(0)
writer.penup()
question_font = ("Arial", 13, "bold")#font
title_font = ("Arial", 15, "bold" )
#writer.goto simplification to keep in mind which question's positions are
title_pos = (-300, 300)
ask_que_pos = (-150, 300)
que_pos1 = (-250,00)
que_pos2 = (-100,00)
que_pos3 = (50,-00)
que_pos4 = (200,00)
#SPANISH QUESTIONS
def spanish1():
  writer.clear()#Makes sure there won't be a overlap
  writer.goto(ask_que_pos)
  writer.write("What does El mean?", font=title_font)
  print("What does El mean?")
  #I want to use answer as a variable to get answer so I have to put within the function so that other functions wouldn't use the variable here
  #writing in window
  writer.goto(que_pos1)
  writer.write("1.He", font=question_font)
  writer.goto(que_pos2)
  writer.write("2.Him", font=question_font)
  writer.goto(que_pos3)
  writer.write("3.Her", font=question_font)
  writer.goto(que_pos4)
  writer.write("4.The", font=question_font)
  #
  answer = input("1.He  \n2.Him \n3.Her \n4.The\n")#User Input to ask for answer
  if answer == "1" or answer == "2" or answer == "3" or answer == "He" or answer == "Him" or answer == "Her":#wrong answers
    print("You got it wrong! El actually means The, with the accent is He.")
    writer.goto(ask_que_pos)
    writer.write("You got it wrong!", font=title_font)
    time.sleep(3)
  elif answer == "4" or answer == "The" or answer == "the":
    print("You got it right!")
    writer.clear()#removes overlap from last written font.
    writer.goto(ask_que_pos)
    writer.write("You got it right!")
    
    #Unnessary
  else:
    print("Please only answer with the corresponding number or word.")
    writer.clear()#removes overlap from last written font.
    writer.goto(ask_que_pos)
    writer.write("Please only answer with the corresponding number or word.", font=title_font)
    return spanish1()#repeats the function if unvalid input is an answer
    
def spanish2():
  writer.clear()#clears any text that was inputted in writer
  writer.goto(ask_que_pos)
  writer.write("What does cama mean?", font=title_font)
  print("What does cama mean?")
  #writing in window
  writer.goto(que_pos1)
  writer.write("1.House", font=question_font)
  writer.goto(que_pos2)
  writer.write("2.Bed", font=question_font)
  writer.goto(que_pos3)
  writer.write("3.Wall", font=question_font)
  writer.goto(que_pos4)
  writer.write("4.Shower", font=question_font)
  #
  answer = input("1.House \n2.Bed \n3. Wall \n4. Shower\n")
  if answer == "1" or answer == "3" or answer == "4" or answer=="House" or answer=="Wall" or answer == "Shower":#wrong answers
    print("You got it wrong! Cama actually means Bed.")
    writer.goto(ask_que_pos)
    writer.write("You got it wrong! Cama actually means Bed.", font=title_font)
    time.sleep(3)
  elif answer == "2" or answer == "Bed" or answer == "bed":
    print("You got it right!")
    writer.clear()#removes overlap from last written font.
    writer.goto(ask_que_pos)
    writer.write("You got it right!",font=title_font)
    time.sleep(3)
    
    #Unnessary
  else:
    print("Please only answer with the corresponding number or word.")
    writer.clear()#removes overlap from last written font.
    writer.goto(ask_que_pos)
    writer.write("Please only answer with the corresponding number or word.",font=title_font)
    time.sleep(3)
    return spanish2()
  
def spanish3():
  writer.clear()
  writer.goto(ask_que_pos)
  writer.write("What does tener mean?",font=title_font)
  print("What does tener mean?")
  #writing in window
  writer.goto(que_pos1)
  writer.write("1.To have", font=question_font)
  writer.goto(que_pos2)
  writer.write("2.To make", font=question_font)
  writer.goto(que_pos3)
  writer.write("3.To run", font=question_font)
  writer.goto(que_pos4)
  writer.write("4.To read", font=question_font)
  #
  answer = input("1.To have \n 2.To make \n3.To run \n4. To read\n")
  if answer == "2" or answer == "3" or answer == "4" or answer == "To make" or answer == "To run" or answer == "To read":
    print("You got it wrong! Tener means to have.")
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it wrong! Tener means to have.",font=title_font)
  elif answer == "1" or answer == "To Have":
    print("You got it right!")
    writer.clear()#removes overlap from last written font.
    writer.goto(ask_que_pos)
    writer.write("You got it right!",font=title_font)
    
    #Unnessary
  else:#if input isn't in the if or elif.
    print("Please only answer with the corresponding number or word.")
    writer.clear()#removes overlap from last written font.
    writer.goto(ask_que_pos)
    writer.write("Please only answer with the corresponding number or word.",font=title_font)
    return spanish3()#restarts function
#Less complex and simpified way to make questions using lists.
#I got this idea from my teacher, note that this code is still what I created though. 
def spanish4():
  right_answers = ["hola","4", "Hola"]
  writer.clear()
  writer.goto(ask_que_pos)
  writer.write("What does hello mean in spanish?",font=title_font)
  print("What does hello mean in spanish?")
  #writing in window
  writer.goto(que_pos1)
  writer.write("1.Amigo", font=question_font)
  writer.goto(que_pos2)
  writer.write("2.Ella", font=question_font)
  writer.goto(que_pos3)
  writer.write("3.El", font=question_font)
  writer.goto(que_pos4)
  writer.write("4.Hola", font=question_font)
  #
  answer = input("1.Amigo \n 2.Ella \n 3.El \n 4.Hola\n")
  if answer in right_answers:
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it right!",font=title_font)
    print("You got it right!")
  else:
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it wrong! Hello means Hola in spanish.",font=title_font)
    print("You got it wrong! Hello means Hola in spanish.")
def spanish5():
  right_answers = ["Buenas día", "1"]
  writer.clear()
  writer.goto(ask_que_pos)
  writer.write("How do you say good morning in spanish?",font=title_font)
  print("How do you say good morning in spanish?")
  #writing in window
  writer.goto(que_pos1)
  writer.write("1.Buen día", font=question_font)
  writer.goto(que_pos2)
  writer.write("2.Buenas noches", font=question_font)
  writer.goto(que_pos3)
  writer.write("3.mala noche", font=question_font)
  writer.goto(que_pos4)
  writer.write("4.mala", font=question_font)
  #
  answer = input("1.Buen día \n2.Buenas noches \n3.mala noche \n4.mala día\n")
  if answer in right_answers:
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it right!",font=title_font)
    print("You got it right!")
  else:
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it wrong! Good morning means Buen día.",font=title_font)
    print("You got it wrong! Good morning means Buen día.")
    
#ALGEBRA QUESTIONS
def algebra1():
  writer.clear()
  writer.goto(ask_que_pos)
  writer.write("What is the slope of y=5x+1?",font=title_font)
  print("What is the slope of y=5x+1?")
  #writing in window
  writer.goto(que_pos1)
  writer.write("1.1/1", font=question_font)
  writer.goto(que_pos2)
  writer.write("2.4/3", font=question_font)
  writer.goto(que_pos3)
  writer.write("3.5/1", font=question_font)
  writer.goto(que_pos4)
  writer.write("4.-5/1", font=question_font)
  #
  answer = input("1.1/1 \n2.4/3 \n3.5/1 \n4.-5/1\n")
  if answer == "1" or answer == "2" or answer == "4" or answer == "1/1" or answer == "4/3" or answer == "-5/1":
    print("You got it wrong! In a equation of y=mx+b, m stands for slope.")
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it wrong! In a equation of y=mx+b, m stands for slope.", algin="center", font=title_font)
  elif answer == "3" or answer == "5/1" or answer =="5":
    print("You got it right!")
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it right!")
  else:
    print("Please only answer with the corresponding number or word.")
    writer.clear()#removes overlap from last written font.
    writer.goto(ask_que_pos)
    writer.write("Please only answer with the corresponding number or word.")

#Less complex and simpified way to make questions using lists.
#I got this idea from my teacher, note that this code is still what I created though. 
def algebra2():
  right_answers = ["1","8"]
  writer.clear()
  writer.goto(ask_que_pos)
  writer.write("What is the y-intercept of y=5x+8?",font=title_font)
  #writing in window
  writer.goto(que_pos1)
  writer.write("1.8", font=question_font)
  writer.goto(que_pos2)
  writer.write("2.5", font=question_font)
  writer.goto(que_pos3)
  writer.write("3.1", font=question_font)
  writer.goto(que_pos4)
  writer.write("4.5", font=question_font)
  #
  print("What is the y-intercept of y=5x+8?")
  answer = input("1.8\n2.5\n3.1\n4.5\n")
  if answer in right_answers:
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it right!",font=title_font)
    print("You got it right!")
  else:
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it wrong! The y-intercept is 8.",font=title_font)
    print("You got it wrong! The y-intercept is 8.")

def algebra3():
  right_answers = ["3", "8"]
  writer.clear()
  writer.goto(ask_que_pos)
  writer.write("Find x in x + 12 = 20",font=title_font)
  #writing in window
  writer.goto(que_pos1)
  writer.write("1.-8", font=question_font)
  writer.goto(que_pos2)
  writer.write("2.12", font=question_font)
  writer.goto(que_pos3)
  writer.write("3.8", font=question_font)
  writer.goto(que_pos4)
  writer.write("4.20", font=question_font)
  #
  print("Find x in x + 12 = 20")
  answer = input("1.-8 \n2.12 \n3.8 \n 4.20 \n")
  if answer in right_answers:
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it right!",font=title_font)
    print("You got it right!")
  else:
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it wrong! x is 8",font=title_font)
    print("You got it wrong! x is 8")

def algebra4():
  right_answers = ["-3/-5","1"]
  writer.clear()
  writer.goto(ask_que_pos)
  writer.write("Find the slope of (3,5) and (8,8)",font=title_font)
  #writing in window
  writer.goto(que_pos1)
  writer.write("1.3/5.", font=question_font)
  writer.goto(que_pos2)
  writer.write("2.5/3", font=question_font)
  writer.goto(que_pos3)
  writer.write("3.5/-3", font=question_font)
  writer.goto(que_pos4)
  writer.write("4.3/8", font=question_font)
  #
  print("Find the slope of (3,5) and (8,8)")
  answer = input("1.3/5 \n2.5/3 \n 3.5/-3 \n 3/8\n")
  if answer in right_answers:
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it right!",font=title_font)
    print("You got it right!")
  else:
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it wrong! m is 3/5",font=title_font)
    print("You got it wrong! m is 3/5")
#Create list of right answer within function
#if the input isn't in right answer, say you got it wrong
def algebra5():
  right_answers = ["5","4"]
  writer.clear()
  writer.goto(ask_que_pos)
  writer.write("Find the hyptenuse of a right triangle that has sides of 3 and 4.,", font=title_font)
  #writing in window
  writer.goto(que_pos1)
  writer.write("1.3", font=question_font)
  writer.goto(que_pos2)
  writer.write("2.4", font=question_font)
  writer.goto(que_pos3)
  writer.write("3.7", font=question_font)
  writer.goto(que_pos4)
  writer.write("4.5", font=question_font)
  #
  print("Find the hyptenuse of a right triangle that has sides of 3 and 4.")
  answer = input("1.3\n 2.4\n 3.7 \n 4.5\n")
  if answer in right_answers:
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it right!",font=title_font)
    print("You got it right!")
  else:
    writer.clear()
    writer.goto(ask_que_pos)
    writer.write("You got it wrong! The hyptenuse is 5.", font=title_font)
    print("You got it wrong! The hyptenuse is 5.")
  
#LISTS for questions 
# I am using these functions that generate questions in a list to use when iterrating these questions for a spanish/algebra quiz
spanish_questions = [spanish1, spanish2, spanish3, spanish4, spanish5]
algebra_questions = [algebra1, algebra2, algebra3, algebra4, algebra5]
#EXECUTION
#Ask User_Input if they want a Spanish 1 or Algebra 1 quiz.
def ask_subject():
  writer.goto(title_pos)
  writer.write("Do you want to have to quiz of Spanish 1 or Algebra 1? (Say S or A)", font=title_font)
  subject = input("Do you want to have to quiz of Spanish 1 or Algebra 1? Say S or A\n")
  writer.clear()#clears writing after user answers
  #if subject isn't S or A then ask again
  if subject != "A" and subject !="S" and subject != "s" and subject != "a":
    print("Please input only S or A")
    writer.clear()#makes sure there isn't an overlap
    writer.goto(ask_que_pos)
    writer.write("Please input only S or A", font= title_font)
    print("Try again.")
    time.sleep(3)
    return ask_subject()#restarts the function
  else:
    return subject #puts the value outside of function#Note: this ends the function of ask_subject as well with the else statement

subject = ask_subject()#Assigns subject as a variable from ask_subject data. 

def user_chosen_subject(subject):#uses input of subject to determine if subject is Algebra or Spanish
  if subject == "S" or subject =="s":
    for question in spanish_questions:#iterate through each question in spanish_questions
      #calls the function within spanish_questions list by using question() 
      question()
      #1.spanish1() 2.spanish2() 3.spanish3()...
      
  elif subject == "A" or subject == "a":     
    for question in algebra_questions:
      question()
      
  else:#if it is not working somehow, make a loop for user_chosen_subject
    print("Try again.")
    # subject = ask_subject()
    # user_chosen_subject(subject)
    
user_chosen_subject(subject)
trtl.mainloop()