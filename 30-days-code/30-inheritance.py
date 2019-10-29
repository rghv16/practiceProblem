

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
    def __init__(self, fname, lname, id1, scores):
        self.firstName = fname
        self.lastName = lname
        self.idNumber = id1
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        x = sum(self.scores) / len(self.scores)
        if x >= 90:
            return 'O'
        elif x >= 80:
            return 'E'
        elif x >= 70:
            return 'A'
        elif x >= 55:
            return 'P'
        elif x >= 40:
            return 'D'
        else:
            return 'T'



