#author Joshua McIntyre jjm7410@psu.edu
#collaborator: Kushal Mandavia kqm5921@psu.edu
#collaborator: Lynn Francis jtf5383@psu.edu
#collaborator: Linghe Du lpd5243@psu.edu
#section 4
#breakout: 8



def getLetterGrade(grade):
  grade = float(grade)
  if(grade >= 90.00):
    print("Your letter grade for CMPSC 131 is " + lettergrade + ".")
  elif(grade >= 87.00):
    print("Your letter grade for CMPSC 131 is " + lettergrade + ".")
  elif(grade >= 84.00):
    print("Your letter grade for CMPSC 131 is " + lettergrade + ".")
  elif(grade >= 80.00):
    print("Your letter grade for CMPSC 131 is " + lettergrade + ".")
  elif(grade >= 77.00):
    print("Your letter grade for CMPSC 131 is " + lettergrade + ".")
  elif(grade >= 70.00): 
    print("Your letter grade for CMSC 131 is " + lettergrade + ".")
  elif(grade >=60):
    print("Your letter grade for CMPSC 131 is " + lettergrade + ".")
  else: 
    print("You have an F.")

grade = input("Enter your grade: ")
lettergrade = str() 
getLetterGrade(85)

