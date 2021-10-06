from canvasapi import Canvas
# from getpass import getpass

class Canvareum(object):

	def __init__(self, key):
		self.api_url = "https://canvas.instructure.com/"
		self.key = key
		self.canvas = Canvas(self.api_url, key)
		self.courses = {}

	def get_courses(self):
		courses = self.canvas.get_courses()
		for course in courses:
			self.courses[course.name] = course.id


if __name__ == '__main__':
	auth = input("Please enter API Key:> ")
	inst = Canvareum(auth)
	inst.get_courses()
	print(inst.courses)