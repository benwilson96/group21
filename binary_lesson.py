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

		lblLessonTitle = Label(self, text='"Binary Conversion" \n', font=('MS', 22, 'bold'))
		lblLessonTitle.grid(row=1, column=6, columnspan=3, sticky=N)


	def createLessonDescription(self):

		lblLessonDescription = Label(self, text='  Lesson Description', font=('MS', 10, 'bold'))
		lblLessonDescription.grid(row=5, column=2, columnspan=1, sticky=N)

		lblDescription = Label(self, text='  This lesson relates to binary conversion, more specifically, \n converting from decimal to octal numbers.', font=('MS', 10))
		lblDescription.grid(row=6, column=2, columnspan=1, sticky=N)


	def createLessonObjectives(self):

		lblLessonOutcomes = Label(self, text='Lesson Objectives: ', font=('MS', 10, 'bold'))
		lblLessonOutcomes.grid(row=5, column=16, columnspan=2, sticky=N)

		lblCompletedOutcomes = Label(self, text='Tick achieved lesson objectives    ', font=('MS', 10))
		lblCompletedOutcomes.grid(row=5, column=18, columnspan=2, sticky=N)

		self.varCB1 = IntVar()
		CB1 = Checkbutton(self, text=" Understand how decimal numbers are converted \n into octal numbers    ", variable=self.varCB1)
		CB1.grid(row=6, column=16, columnspan=3, sticky=W)

		self.varCB2 = IntVar()
		CB2 = Checkbutton(self, text=" Understand the concept of binary conversion \n and why it is useful for programmers", variable=self.varCB2)
		CB2.grid(row=7, column=16, columnspan=3, sticky=W)


	def createLessonContent(self):

		lblLessonContentTitle = Label(self, text='Binary Conversion - Decimal to Octal \n', font=('MS', 12, 'bold'))
		lblLessonContentTitle.grid(row=12, column=6, columnspan=3)

		lblLessonContent1 = Label(self, text='The second short lesson will be on how to convert decimal to octal in binary. \n I will show a guide on how to convert decimal numbers into octal. \n', font=('MS', 10))
		lblLessonContent1.grid(row=13, column=6, columnspan=3)

		lblLessonContent2 = Label(self, text='Bases', font=('MS', 11, 'bold'))
		lblLessonContent2.grid(row=15, column=6, columnspan=3)

		lblLessonContent3 = Label(self, text='Firstly, the digits used in octal (base 8) system  are 0, 1, …, 7. \n Knowing this will allow us to convert from decimal to binary as shown below: \n', font=('MS', 10))
		lblLessonContent3.grid(row=16, column=6, columnspan=3)

		lblLessonContent4 = Label(self, text='Example: 83(10) in binary is 1010011(2) \n', font=('MS', 10))
		lblLessonContent4.grid(row=17, column=6, columnspan=3)

		lblLessonContent5 = Label(self, text='Grouping', font=('MS', 11, 'bold'))
		lblLessonContent5.grid(row=18, column=6, columnspan=3)

		lblLessonContent6 = Label(self, text='Secondly, we want to group the number in binary into threes, starting \n from the right hand side and pad to the left with 0’s where needed. \n \n Example: For the number above, grouping would look like the following:', font=('MS', 10))
		lblLessonContent6.grid(row=19, column=6, columnspan=3)

		lblLessonContent7 = Label(self, text='Group into threes starting from the right hand side: \n \n 1     0 1 0     0 1 1 \n \n Pad to the left with 0’s: \n \n  0 0 1     0 1 0     0 1 1 \n', font=('MS', 10))
		lblLessonContent7.grid(row=20, column=6, columnspan=3)

		lblLessonContent8 = Label(self, text='Translation', font=('MS', 11, 'bold'))
		lblLessonContent8.grid(row=21, column=6, columnspan=3)

		lblLessonContent9 = Label(self, text='Translate each group of three bits into an octal digit: \n \n 1     2     3  \n \nThis gives the final octal digit: \n \n 83(10) = 123(8)', font=('MS', 10))
		lblLessonContent9.grid(row=22, column=6, columnspan=3)


	def createTakeTestButton(self): 

		buttonTakeTest = Button(self, text='Take Test', font=('MS', 8, 'bold'))
		buttonTakeTest['command']=self.createTestWindow
		buttonTakeTest.grid(row=23, column=19, columnspan=1, sticky=W)

		buttonPadding1 = Label(self, text='')
		buttonPadding1.grid(row=23, column=21, columnspan=1)

		buttonPadding2 = Label(self, text='')
		buttonPadding2.grid(row=24, column=19, columnspan=1)


	def createTestWindow(self):
		
		testWindow= Toplevel(self)
		testWindow.title("Test - Binary Conversion")
		l = Label(testWindow, text="Kieren - Add binary test conent")
		l.pack(side="top", fill="both", expand=True, padx=100, pady=100)



root = Tk()
root.config(background = 'white')

menu = Menu(root, tearoff = False)
root.config(menu = menu)

subMenu = Menu(menu, tearoff = False)

menu.add_cascade(label = "Menu", menu = subMenu)

subMenu.add_command(label = "Homepage - no functionality yet")
subMenu.add_command(label = "Help - no functionality yet")
subMenu.add_separator()
subMenu.add_command(label = "Logout - no functionality yet") 



if __name__ == "__main__":

	root.title("Interactive Lesson - Binary Conversion")
	main = binary_lesson(root)
	main.pack(side="top", fill="both", expand=True)
	root.mainloop()
