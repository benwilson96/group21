from tkinter import *
import tkinter as tk
from tkinter import messagebox


TITLE_FONT = ("Helvetica", 18, "bold")

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, testPage):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		self.controller = controller


		self.grid()
		self.createLessonTitle()
		self.createLessonDescription()
		self.createLessonObjectives()
		self.createLessonContent()

		button1 = tk.Button(self, text="Take Test",
							command=lambda: controller.show_frame("testPage"))
		button1.grid(row=23, column=19, columnspan=1, sticky=tk.W)



	def createLessonTitle(self):

		lblLessonTitle = tk.Label(self, text='"Binary Conversion" \n', font=('MS', 22, 'bold'))
		lblLessonTitle.grid(row=1, column=6, columnspan=3, sticky=tk.N)

	def createLessonDescription(self):

		lblLessonDescription = tk.Label(self, text='  Lesson Description', font=('MS', 10, 'bold'))
		lblLessonDescription.grid(row=5, column=2, columnspan=1, sticky=tk.N)

		lblDescription = tk.Label(self, text='  This lesson relates to binary conversion, more specifically, \n converting from decimal to octal numbers.', font=('MS', 10))
		lblDescription.grid(row=6, column=2, columnspan=1, sticky=tk.N)


	def createLessonObjectives(self):

		lblLessonOutcomes = tk.Label(self, text='Lesson Objectives: ', font=('MS', 10, 'bold'))
		lblLessonOutcomes.grid(row=5, column=16, columnspan=2, sticky=tk.N)

		lblCompletedOutcomes = tk.Label(self, text='Tick achieved lesson objectives    ', font=('MS', 10))
		lblCompletedOutcomes.grid(row=5, column=18, columnspan=2, sticky=tk.N)

		self.varCB1 = tk.IntVar()
		CB1 = tk.Checkbutton(self, text=" Understand how decimal numbers are converted \n into octal numbers    ", variable=self.varCB1)
		CB1.grid(row=6, column=16, columnspan=3, sticky=tk.W)

		self.varCB2 = tk.IntVar()
		CB2 = tk.Checkbutton(self, text=" Understand the concept of binary conversion \n and why it is useful for programmers", variable=self.varCB2)
		CB2.grid(row=7, column=16, columnspan=3, sticky=tk.W)


	def createLessonContent(self):

		lblLessonContentTitle = tk.Label(self, text='Binary Conversion - Decimal to Octal \n', font=('MS', 12, 'bold'))
		lblLessonContentTitle.grid(row=12, column=6, columnspan=3)

		lblLessonContent1 = tk.Label(self, text='The second short lesson will be on how to convert decimal to octal in binary. \n I will show a guide on how to convert decimal numbers into octal. \n', font=('MS', 10))
		lblLessonContent1.grid(row=13, column=6, columnspan=3)

		lblLessonContent2 = tk.Label(self, text='Bases', font=('MS', 11, 'bold'))
		lblLessonContent2.grid(row=15, column=6, columnspan=3)

		lblLessonContent3 = tk.Label(self, text='Firstly, the digits used in octal (base 8) system  are 0, 1, …, 7. \n Knowing this will allow us to convert from decimal to binary as shown below: \n', font=('MS', 10))
		lblLessonContent3.grid(row=16, column=6, columnspan=3)

		lblLessonContent4 = tk.Label(self, text='Example: 83(10) in binary is 1010011(2) \n', font=('MS', 10))
		lblLessonContent4.grid(row=17, column=6, columnspan=3)

		lblLessonContent5 = tk.Label(self, text='Grouping', font=('MS', 11, 'bold'))
		lblLessonContent5.grid(row=18, column=6, columnspan=3)

		lblLessonContent6 = tk.Label(self, text='Secondly, we want to group the number in binary into threes, starting \n from the right hand side and pad to the left with 0’s where needed. \n \n Example: For the number above, grouping would look like the following:', font=('MS', 10))
		lblLessonContent6.grid(row=19, column=6, columnspan=3)

		lblLessonContent7 = tk.Label(self, text='Group into threes starting from the right hand side: \n \n 1     0 1 0     0 1 1 \n \n Pad to the left with 0’s: \n \n  0 0 1     0 1 0     0 1 1 \n', font=('MS', 10))
		lblLessonContent7.grid(row=20, column=6, columnspan=3)

		lblLessonContent8 = tk.Label(self, text='Translation', font=('MS', 11, 'bold'))
		lblLessonContent8.grid(row=21, column=6, columnspan=3)

		lblLessonContent9 = tk.Label(self, text='Translate each group of three bits into an octal digit: \n \n 1     2     3  \n \nThis gives the final octal digit: \n \n 83(10) = 123(8)', font=('MS', 10))
		lblLessonContent9.grid(row=22, column=6, columnspan=3)


class testPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.grid()
		self.Binary_Title()
		self.setQuestions()
		self.studentNumEntry()
		self.addButtons()
		self.storeResult


	def Binary_Title(self):
		theTitle = tk.Label(self, text="Binary Test", font=('MS', 22, 'bold'))
		theTitle.grid(row=0, column=5, columnspan=2)

	def setQuestions(self):

		lblDesc1 = tk.Label(self, text='Multiple Choice Questions:', font=('MS', 10,'bold'))
		lblDesc1.grid(row=3, column = 3)

		lblDesc2 = tk.Label(self, text='For each of the following, convert the decimal numbers (base 10) into octal (base 8) and choose an answer:', font=('MS', 10))
		lblDesc2.grid(row=3, column = 4, columnspan=5, sticky=tk.W)

		#Start Of Question 1

		lblQ1 = tk.Label(self, text='\nQuestion 1): ', font=('MS', 10,'bold'))
		lblQ1.grid(row=6, column = 4)

		lblQ1_Question = tk.Label(self, text='\nWhat is 18 (10) in octal?', font=('MS', 10))
		lblQ1_Question.grid(row=6, column = 5, columnspan=2, sticky=tk.W)

		lblQ1_ChoiceA = tk.Label(self, text='A) 19 (8)', font=('MS', 10))
		lblQ1_ChoiceA.grid(row=7, column = 5, columnspan=1, sticky=tk.W)

		lblQ1_ChoiceB = tk.Label(self, text='B) 20 (8)', font=('MS', 10))
		lblQ1_ChoiceB.grid(row=8, column = 5, columnspan=1, sticky=tk.W)

		lblQ1_ChoiceC = tk.Label(self, text='C) 21 (8)', font=('MS', 10))
		lblQ1_ChoiceC.grid(row=9, column = 5, columnspan=1, sticky=tk.W)

		lblQ1_ChoiceD = tk.Label(self, text='D) 22 (8)', font=('MS', 10))
		lblQ1_ChoiceD.grid(row=10, column = 5, columnspan=1, sticky=tk.W)

		self.varQ1 = tk.IntVar()
		R1Q1 = tk.Radiobutton(self, variable=self.varQ1, value=4)
		R1Q1.grid(row=7, column= 6)
		R2Q1 = tk.Radiobutton(self, variable= self.varQ1, value=3)
		R2Q1.grid(row=8, column= 6)
		R3Q1 = tk.Radiobutton(self, variable= self.varQ1, value=2)
		R3Q1.grid(row=9, column= 6)
		R4Q1 = tk.Radiobutton(self, variable= self.varQ1, value=1)
		R4Q1.grid(row=10, column= 6)

		#End of Question 1

		#----------------------------------------------------------------------------------------------------------------------------#

		#Start of Question 2

		lblQ2 = tk.Label(self, text='\nQuestion 2): ', font=('MS', 10,'bold'))
		lblQ2.grid(row=11, column = 4)

		lblQ2_Question = tk.Label(self, text='\nWhat is 156 (10) in octal?', font=('MS', 10))
		lblQ2_Question.grid(row=11, column = 5, columnspan=2, sticky=tk.W)

		lblQ2_ChoiceA = tk.Label(self, text='A) 212 (8)', font=('MS', 10))
		lblQ2_ChoiceA.grid(row=12, column = 5, columnspan=1, sticky=tk.W)

		lblQ2_ChoiceB = tk.Label(self, text='B) 220 (8)', font=('MS', 10))
		lblQ2_ChoiceB.grid(row=13, column = 5, columnspan=1, sticky=tk.W)

		lblQ2_ChoiceC = tk.Label(self, text='C) 234 (8)', font=('MS', 10))
		lblQ2_ChoiceC.grid(row=14, column = 5, columnspan=1, sticky=tk.W)

		lblQ2_ChoiceD = tk.Label(self, text='D) 242 (8)', font=('MS', 10))
		lblQ2_ChoiceD.grid(row=15, column = 5, columnspan=1, sticky=tk.W)

		self.varQ2 = tk.IntVar()
		R1Q2 = tk.Radiobutton(self, variable=self.varQ2, value=4)
		R1Q2.grid(row=12, column= 6)
		R2Q2 = tk.Radiobutton(self, variable= self.varQ2, value=3)
		R2Q2.grid(row=13, column= 6)
		R3Q2 = tk.Radiobutton(self, variable= self.varQ2, value=2)
		R3Q2.grid(row=14, column= 6)
		R4Q2 = tk.Radiobutton(self, variable= self.varQ2, value=1)
		R4Q2.grid(row=15, column= 6)

		#End of Question 2

		#----------------------------------------------------------------------------------------------------------------------------#

		#Start of Question 3

		lblQ3 = tk.Label(self, text='\nQuestion 3): ', font=('MS', 10,'bold'))
		lblQ3.grid(row=16, column = 4)

		lblQ3_Question = tk.Label(self, text='\nWhat is 1267 (10) in octal?', font=('MS', 10))
		lblQ3_Question.grid(row=16, column = 5, columnspan=2, sticky=tk.W)

		lblQ3_ChoiceA = tk.Label(self, text='A) 2109 (8)', font=('MS', 10))
		lblQ3_ChoiceA.grid(row=17, column = 5, columnspan=1, sticky=tk.W)

		lblQ3_ChoiceB = tk.Label(self, text='B) 2163 (8)', font=('MS', 10))
		lblQ3_ChoiceB.grid(row=18, column = 5, columnspan=1, sticky=tk.W)

		lblQ3_ChoiceC = tk.Label(self, text='C) 2363 (8)', font=('MS', 10))
		lblQ3_ChoiceC.grid(row=19, column = 5, columnspan=1, sticky=tk.W)

		lblQ3_ChoiceD = tk.Label(self, text='D) 2451 (8)', font=('MS', 10))
		lblQ3_ChoiceD.grid(row=20, column = 5, columnspan=1, sticky=tk.W)

		self.varQ3 = tk.IntVar()
		R1Q3 = tk.Radiobutton(self, variable=self.varQ3, value=4)
		R1Q3.grid(row=17, column= 6)
		R2Q3 = tk.Radiobutton(self, variable= self.varQ3, value=3)
		R2Q3.grid(row=18, column= 6)
		R3Q3 = tk.Radiobutton(self, variable= self.varQ3, value=2)
		R3Q3.grid(row=19, column= 6)
		R4Q3 = tk.Radiobutton(self, variable= self.varQ3, value=1)
		R4Q3.grid(row=20, column= 6)

		#End of Question 3

		#----------------------------------------------------------------------------------------------------------------------------#

		#Start of Question 4

		lblQ4 = tk.Label(self, text='\nQuestion 4): ', font=('MS', 10,'bold'))
		lblQ4.grid(row=21, column = 4)

		lblQ4_Question = tk.Label(self, text='\nWhat is 4000 (8) in decimal?', font=('MS', 10))
		lblQ4_Question.grid(row=21, column = 5, columnspan=2, sticky=tk.W)

		lblQ4_ChoiceA = tk.Label(self, text='A) 2048 (10)', font=('MS', 10))
		lblQ4_ChoiceA.grid(row=22, column = 5, columnspan=1, sticky=tk.W)

		lblQ4_ChoiceB = tk.Label(self, text='B) 2060 (10)', font=('MS', 10))
		lblQ4_ChoiceB.grid(row=23, column = 5, columnspan=1, sticky=tk.W)

		lblQ4_ChoiceC = tk.Label(self, text='C) 2084 (10)', font=('MS', 10))
		lblQ4_ChoiceC.grid(row=24, column = 5, columnspan=1, sticky=tk.W)

		lblQ4_ChoiceD = tk.Label(self, text='D) 2101 (10)', font=('MS', 10))
		lblQ4_ChoiceD.grid(row=25, column = 5, columnspan=1, sticky=tk.W)

		self.varQ4 = tk.IntVar()
		R1Q4 = tk.Radiobutton(self, variable=self.varQ4, value=4)
		R1Q4.grid(row=22, column= 6)
		R2Q4 = tk.Radiobutton(self, variable= self.varQ4, value=3)
		R2Q4.grid(row=23, column= 6)
		R3Q4 = tk.Radiobutton(self, variable= self.varQ4, value=2)
		R3Q4.grid(row=24, column= 6)
		R4Q4 = tk.Radiobutton(self, variable= self.varQ4, value=1)
		R4Q4.grid(row=25, column= 6)

		#End of Question 4

		#----------------------------------------------------------------------------------------------------------------------------#

		#Start of Question 5

		lblQ5 = tk.Label(self, text='\nQuestion 5): ', font=('MS', 10,'bold'))
		lblQ5.grid(row=26, column = 4)

		lblQ5_Question = tk.Label(self, text='\nWhat is 127 (8) in decimal?', font=('MS', 10))
		lblQ5_Question.grid(row=26, column = 5, columnspan=2, sticky=tk.W)

		lblQ5_ChoiceA = tk.Label(self, text='A) 87 (10)', font=('MS', 10))
		lblQ5_ChoiceA.grid(row=27, column = 5, columnspan=2, sticky=tk.W)

		lblQ5_ChoiceB = tk.Label(self, text='B) 94 (10)', font=('MS', 10))
		lblQ5_ChoiceB.grid(row=28, column = 5, columnspan=2, sticky=tk.W)

		lblQ5_ChoiceC = tk.Label(self, text='C) 96 (10)', font=('MS', 10))
		lblQ5_ChoiceC.grid(row=29, column = 5, columnspan=2, sticky=tk.W)

		lblQ5_ChoiceD = tk.Label(self, text='D) 88 (10)', font=('MS', 10))
		lblQ5_ChoiceD.grid(row=30, column = 5, columnspan=1, sticky=tk.W)

		self.varQ5 = tk.IntVar()
		R1Q5 = tk.Radiobutton(self, variable=self.varQ5, value=4)
		R1Q5.grid(row=27, column= 6)
		R2Q5 = tk.Radiobutton(self, variable= self.varQ5, value=3)
		R2Q5.grid(row=28, column= 6)
		R3Q5 = tk.Radiobutton(self, variable= self.varQ5, value=2)
		R3Q5.grid(row=29, column= 6)
		R4Q5 = tk.Radiobutton(self, variable= self.varQ5, value=1)
		R4Q5.grid(row=30, column= 6)

		#End of Question 5

		#----------------------------------------------------------------------------------------------------------------------------#

	def studentNumEntry(self):

		#Start of Student ID text box

		lbl_blank1 = tk.Label(self, text=' ', font=('MS', 10,'bold'))
		lbl_blank1.grid(row=31, column = 1)

		lbl_ID = tk.Label(self, text='Enter your student number:', font=('MS', 10,'bold'))
		lbl_ID.grid(row=32, column = 5, sticky=tk.W)

		self.entName = tk.Entry(self)
		self.entName.grid(row=32, column=5, columnspan=2, sticky=tk.E) 

		#End of Student ID text box

		#----------------------------------------------------------------------------------------------------------------------------#

	def addButtons(self):

		#Start of Buttons Method

		lbl_blank2 = tk.Label(self, text=' ', font=('MS', 10,'bold'))
		lbl_blank2.grid(row=33, column = 5)

		butSubmit = tk.Button(self, text='Submit',font=('MS', 8,'bold'))
		butSubmit['command']=self.storeResult
		butSubmit.grid(row=34, column=5, columnspan=2)

		#End of Buttons Method

		#----------------------------------------------------------------------------------------------------------------------------#

	def storeResult(self):

		#Start of Response Method

		theScore = 0
		strMsg=""

		if (self.varQ1.get()== 0) or (self.varQ2.get() == 0) or (self.varQ3.get() == 0) or (self.varQ4.get() == 0) or (self.varQ5.get() == 0):
			strMsg = strMsg + "You need to answer all questions! "

		if (self.entName.get() == ""):
			strMsg = strMsg + "\nPlease enter your student number!"

		answer_q1 = 1
		answer_q2 = 2
		answer_q3 = 2
		answer_q4 = 4
		answer_q5 = 4


		if (self.varQ1.get() == 1):
			theScore = theScore + 1

		if (self.varQ2.get() == 2):
			theScore = theScore + 1

		if (self.varQ3.get() == 2):
			theScore = theScore + 1

		if (self.varQ4.get() == 4):
			theScore = theScore + 1

		if (self.varQ5.get() == 4):
			theScore = theScore + 1

		if strMsg == "":

			messagebox.showinfo("Test", "Your test has been saved and you have scored " + str(theScore) + "/5")

		else:

			messagebox.showwarning("Entry Error", strMsg)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()