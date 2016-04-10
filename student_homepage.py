from tkinter import *

class student_homepage(Frame):

	def __init__(self, master):

		Frame.__init__(self, master)
		self.grid()
		self.Title()
		self.TopicSelect()
		self.TakeTestButton()
		self.TestWindow
		self.ViewLessonButton()
		self.LessonWindow
		self.TestResultsButton()
		self.LayoutPadding()
		self.ResultsWindow
		self.LogoutButton()


	def Title(self):

		lblHomepageTitle = Label(self, text = 'Learn Interactive 2016               \n', font = ('calibri', 22, 'bold'))
		lblHomepageTitle.grid(row = 1, column = 4, columnspan = 2, sticky = N)


	def TopicSelect(self):

		lblChooseTopic = Label(self, text = 'Choose Topic \n \n', font = ('calibri', 12, 'bold'))
		lblChooseTopic.grid(row = 2, column = 2, columnspan = 1, sticky = N)

		#how to make drop down menu

		# menuDefault = StringVar(root)
		# menuDefault.set("Sets & Probability")

		# menu = OptionMenu(root, menuDefault, "Sets & Probability", "Binary Conversion")
		# menu.pack

		lblMenuPlaceholder = Label(self, text = 'dropdown menu placeholder', font = ('calibri', 12, 'bold'))
		lblMenuPlaceholder.grid(row = 2, column = 4, columnspan = 1, sticky	= NE)


	def TakeTestButton(self):

		buttonTakeTest = Button(self, text = 'Take Test', font = ('calibri', 12, 'bold'))
		buttonTakeTest.grid(row = 3, column = 2, columnspan = 1, sticky = E)
		buttonTakeTest['command'] = self.TestWindow


	def TestWindow(self):

		#need to limit to 1 window max
		
		testWindow = Toplevel(self)
		testWindow.title("whichever test is selected")
		testLabel = Label(testWindow, text = "whichever test is selected")
		testLabel.pack(side = "top", fill = "both", expand = True, padx = 100, pady = 100)


	def ViewLessonButton(self):

		buttonViewLesson = Button(self, text = 'View Lesson', font = ('calibri', 12, 'bold'))
		buttonViewLesson['command'] = self.LessonWindow
		buttonViewLesson.grid(row = 3, column = 4, columnspan = 1, sticky = E)
		

	def LessonWindow(self):

		#need to limit to 1 window max

		lessonWindow = Toplevel(self)
		lessonWindow.title("whichever lesson is selected")
		lessonLabel = Label(lessonWindow, text = "whichever lesson is selected")
		lessonLabel.pack(side = "top", fill = "both", expand = True, padx = 100, pady = 100)


	def TestResultsButton(self):

		buttonTestResults = Button(self, text = 'View My Test Results', font = ('calibri', 12, 'bold'))
		buttonTestResults['command'] = self.ResultsWindow
		buttonTestResults.grid(row = 5, column = 3, columnspan = 2, sticky = N)


	def ResultsWindow(self):

		#need to limit to 1 window max

		resultsWindow = Toplevel(self)
		resultsWindow.title("Test Results")
		resultsLabel = Label(resultsWindow, text = "results for student who is logged in")
		resultsLabel.pack(side = "top", fill = "both", expand = True, padx = 100, pady = 100)


	def LayoutPadding(self):

		lblResultsPadding = Label(self, text = '')
		lblResultsPadding.grid(row = 4, column = 4, columnspan = 1)

		lblBottomLogoutPadding = Label(self, text = '')
		lblBottomLogoutPadding.grid(row = 8, column = 5, columnspan = 1)

		lblTopLogoutPadding = Label(self, text = '')
		lblTopLogoutPadding.grid(row = 6, column = 5, columnspan = 1)

		lblPlaceholderPadding = Label(self, text = 'functionality needs to be added and layout changed, \n but basic window is created for studnet homepage. \n When this message isn\'t here the layout fits better')
		lblPlaceholderPadding.grid(row = 8, column = 2, columnspan = 1)


	def LogoutButton(self):

		buttonLogout = Button(self, text = 'Logout', font = ('calibri', 12, 'bold'))

		# logout functionality needed for button command
		# buttonLogout['command'] = ??

		buttonLogout.grid(row = 7, column = 5, columnspan = 1, sticky = N)


if __name__ == "__main__":


	root = Tk()
	root.title("Learn Interactive 2016")
	main = student_homepage(root)
	main.pack(side = "top", fill = "both", expand = True)
	root.config(background = 'white')
	root.mainloop()
