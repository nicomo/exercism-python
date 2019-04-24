class Garden(object):
    plantsDict = {
        "C": "Clover",
        "G": "Grass",
        "R": "Radishes",
        "V": "Violets",
    }

    def __init__(self, diagram, students = 
            ['Alice', 'Bob', 'Charlie', 'David',
            'Eve', 'Fred','Ginny','Harriet',
            'Ileana','Joseph', 'Kincaid','Larry']):
        self.rows = diagram.split("\n")
        self.students = sorted(students)
    
    def plants(self,student):
        i = self.students.index(student) * 2
        res = []
        for row in self.rows:
            res.append(self.plantsDict.get(row[i]))
            res.append(self.plantsDict.get(row[i+1]))
        return res

