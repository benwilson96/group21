from tkinter import*

class binary_lesson(Frame):

	def __init__(self, master):

		Frame.__init__(self, master)
		self.grid()
		self.createLessonTitle()
		self.createLessonDescription()
		self.createLessonObjectives()
		self.createLessonContent()
		self.createTakeTestButton()
		self.createTestWindow


	def createLessonTitle(self):

		lblLessonTitle = Label(self, text='Binary Conversion', font=('MS', 12, 'bold'))
		lblLessonTitle.grid(row=3, column=3, columnspan=2)


	def createLessonDescription(self):

		lblLessonDescription = Label(self, text='Lesson Description', font=('MS', 10, 'bold'))
		lblLessonDescription.grid(row=5, column=1, columnspan=2, sticky=W)

		lblDescription = Label(self, text='This lesson relates to binary conversion, more specifically, \n converting from decimal to octal numbers.', font=('MS', 10))
		lblDescription.grid(row=7, column=1, columnspan=3, sticky=W)


	def createLessonObjectives(self):

		lblLessonOutcomes = Label(self, text='Lesson Objectives: ', font=('MS', 10, 'bold'))
		lblLessonOutcomes.grid(row=5, column=5, columnspan=2)

		lblCompletedOutcomes = Label(self, text='Tick achieved lesson objectives', font=('MS', 10))
		lblCompletedOutcomes.grid(row=5, column=7, columnspan=3, sticky=W)

		self.varCB1 = IntVar()
		CB1 = Checkbutton(self, text=" Understand how decimal numbers are converted into octal numbers", variable=self.varCB1)
		CB1.grid(row=7, column=5, columnspan=5, sticky=W)

		self.varCB2 = IntVar()
		CB2 = Checkbutton(self, text=" Understand the concept of binary conversion and why it is useful for programmers", variable=self.varCB2)
		CB2.grid(row=8, column=5, columnspan=5, sticky=W)


	def createLessonContent(self):

		lblLessonContentTitle = Label(self, text='Binary Conversion - Decimal to Octal', font=('MS', 10, 'bold'))
		lblLessonContentTitle.grid(row=9, column=4, sticky=N)

		lblLessonContent = Label(self, text='The second short lesson will be on how to convert \n decimal to octal in binary. I will show a guide on \n how to convert decimal numbers into octal. \n \n Firstly, the digits used in octal (base 8) system \n are 0, 1, …, 7. Knowing this will allow us to convert \n from decimal to binary as shown below. \n \n Example: 83(10) in binary is 1010011(2) \n \n Secondly, we want to group the number in binary into \n threes, starting from the right hand side and \n pad to the left with 0’s where needed.\n \n Example: For the number above, grouping \n would look like the following: \n \n Group into threes starting from the right hand side: \n \n 1     0 1 0     0 1 1 \n \n Pad to the left with 0’s: \n \n 0 0 1     0 1 0     0 1 1 \n \n Translate each group of three bits into an octal digit: \n \n 1     2     3 \n \n This gives the final octal digit. 83(10) = 123(8) ', font=('MS', 10))
		lblLessonContent.grid(row=11, column=4, sticky=W)


	def createTakeTestButton(self):

		buttonTakeTest = Button(self, text='Take Test', font=('MS', 8, 'bold'))
		buttonTakeTest['command']=self.createTestWindow
		buttonTakeTest.grid(row=13, column=2, columnspan=2)


	def createTestWindow(self):
		
		testWindow= Toplevel(self)
		testWindow.title("Test - Binary Conversion")
		l = Label(testWindow, text="Kieren - Add binary test conent")
		l.pack(side="top", fill="both", expand=True, padx=100, pady=100)



root = Tk()

menu = Menu(root, tearoff = False)
root.config(menu = menu)
root.config(background = 'white') #not sure why this doesnt work

subMenu = Menu(menu, tearoff = False)

menu.add_cascade(label = "Menu", menu = subMenu)

subMenu.add_command(label = "Homepage - no functionality yet")
subMenu.add_command(label = "Help - no functionality yet")
subMenu.add_separator()
subMenu.add_command(label = "Logout - no functionality yet") 



if __name__ == "__main__":

	root.title("Interactive Lesson - Binary Conversions")
	main = binary_lesson(root)
	main.pack(side="top", fill="both", expand=True)
	root.mainloop()
