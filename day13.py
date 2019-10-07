class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName,lastName,idNumber, scores = []):
        self.firstName = firstName
        self.lastName=lastName
        self.idNumber = idNumber
        self.scores = scores
        self.grades = ['O','E','A','P','D','T']
    
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def  calculate(self):
       
        if(len(self.scores)> 0):
             media =  sum(self.scores)/len(self.scores)

        else:
            media = 0
        
        if(media>=90 and media <=100):
            return 'O'
        elif (media>=80 and  media <90):
            return 'E'
        elif (media>=70 and media <80):
            return 'A'
        elif (media>=55 and media <70):
            return 'P'
        elif (media>=40 and media <55): 
            return 'D'
        elif(media<40 ):
            return 'T'  
        
   
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())