import tkinter as tk
root = tk.Tk()

#List for Algebra 1 and Spanish 1
#If user chooses Algebra 1 then assign Algebra 1 to subject
#Else choose Spanish 1 then assign Spanish 1 to subject

spanish_questions = []
algebra_questions = []
#Ask User_Input if they want a Spanish 1 or Algebra 1 quiz.

# subject = input("Do you want to have to quiz of Spanish 1 or Algebra 1? Say S or A")
root.title("Quiz")
root.geometry("500x300")
frame_label = tk.Frame(root, pady=10)

def spanish_quiz():
    #create root geometric box and write Questions
    #Window
    root.title("Spanish 1")
    root.geometry("500x300")
    #Question labeling and clicking right button
    label = tk.Label(frame_label, text = "What is different between El and el?")
    tk.Button()
    
label = tk.Label(root, text="Do you want to have to quiz of Spanish 1 or Algebra 1? Click S or A")
label.pack(pady=10)
#Create box for Spanish 1 and Algebra 1 quizs 
btn_algebra1 = tk.Button(root, text="Algebra 1", command = spanish_quiz)

    
def user_chosen_subject(subject):
    
       
     if subject == "A":
       spanish_quiz()
     elif subject == "S":
       
     else:
         print("Try Again")
   



root.mainloop()