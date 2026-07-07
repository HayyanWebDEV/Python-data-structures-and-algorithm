class Student:
    def __init__(self , name , marks_list):
        self.name = name
        self.mlist = marks_list

    def average(self):
        n = 0
        total = 0
        for mark in self.mlist:
            n += 1
            total += mark
        return total / n


abdullah_marks = [100 , 49 ,98 ,30 , 100, 70, 90, 81]
abdullah = Student("abdullah", abdullah_marks)
print(abdullah.average())