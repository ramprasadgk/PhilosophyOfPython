class SimpleGradeBook(object):
	def __init__(self):
		self._grades = {}
	
	def add_student(self,name):
		self._grades[name]=[]
	
	def report_grade(self,name,score):
		self._grades[name].append(score)

	def average_grade(self,name):
		grades = self._grades[name]
		return sum(grades)/ len(grades)

if __name__=="__main__":
	print("inside main")
	book=SimpleGradeBook()
	book.add_student("Ram")
	book.report_grade("Ram",60)
	print(book.average_grade("Ram"))

