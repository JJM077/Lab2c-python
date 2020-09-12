#author Joshua McIntyre jjm7410@psu.edu
#collaborator: Kushal Mandavia kqm5921@psu.edu
#collaborator: Lynn Francis jtf5383@psu.edu
#collaborator: Linghe Du lpd5243@psu.edu
#section 4
#breakout: 8



def getLetterGrade(grade):
  grade = float(grade)
  if(grade >= 90.00):
    return "A"
  elif(grade >= 87.00):
    return "B+"
  elif(grade >= 84.00):
    return "B"
  elif(grade >= 80.00):
    return "B-"
  elif(grade >= 77.00):
    return "C+"
  elif(grade >= 70.00): 
    return "C"
  elif(grade >=60):
    return "D"
  else: 
    return "F"
def run():

  grade = input("Enter your grade: ") 
  lettergrade = getLetterGrade(grade)
  print(f"Your letter grade for CMPSC 131 is {lettergrade}." )


if __name__=="__main__":
  run() 

