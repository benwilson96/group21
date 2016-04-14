from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import pymysql
#from Login import *

LARGE_FONT=("Verdana", 12)



def verify_details(Page,UN,PW):
    db = pymysql.connect(host="csmysql.cs.cf.ac.uk", user="c1531722", passwd="pE9zby3j", db="c1531722")
    cursor = db.cursor()
    cursor.execute("SELECT Username, Password, Admin FROM Accounts")

    InputUN = UN.get()
    InputPW = PW.get()
    for UN, PW, ADM in cursor:
        if UN == InputUN and PW == InputPW:
            app.show_frame("student_homepage")	#needs to distinguish between lecturers/students

            break
    if not(UN == InputUN and PW == InputPW):
        Page.unsuccessful_login()

    db.close()

def insert_account(UN,PW,Admin):
    db = pymysql.connect(host="csmysql.cs.cf.ac.uk", user="c1531722", passwd="pE9zby3j", db="c1531722")
    cursor = db.cursor()
    cursor.execute("SELECT ID FROM Accounts ORDER BY ID DESC")
    ID = cursor.fetchone()
    InputUN = UN.get()
    InputPW = PW.get()
    cursor.execute('''INSERT INTO `c1531722`.`Accounts` (`ID`, `Username`, `Password`, `Admin`) VALUES (%s, %s, %s, %s);''',(ID[0]+1,InputUN,InputPW,Admin))
    db.commit()
    db.close()





rights = 0
User = ""
class SampleApp(Tk):

	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		Tk.wm_title(self, "Learn Interactive 2016")

		container = Frame(self)

		container.pack(side="top", fill="both", expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (student_homepage, lessonPage, StartPage, binaryTestPage, SetsPage, ResultsStore, LoginPage, Register, setsTestPage):
			page_name = F.__name__
			frame = F(container, self)
			self.frames[page_name] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("LoginPage")

	def show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.frames[page_name]
		frame.tkraise()


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        l1 = ttk.Label(self, text="Login", font=LARGE_FONT)
        l1.pack(pady=10,padx=10)

        l2 = ttk.Label(self, text="User Name")
        l2.pack(side=LEFT)

        l3 = ttk.Label(self, text="Password ")
        l3.pack(side=LEFT)

        UserN_input = ttk.Entry(self, width=20)
        UserN_input.pack(side=RIGHT)

        PW_input = ttk.Entry(self, width=20)
        PW_input.pack(side=RIGHT)

        LoginBtn = ttk.Button(self, text="Login", command= lambda: verify_details(self, UserN_input, PW_input))
        LoginBtn.pack(side = BOTTOM)

        RegBtn = ttk.Button(self, text="Register", command= lambda: controller.show_frame("Register"))
        RegBtn.pack(side = BOTTOM)

    def unsuccessful_login():
        l4 = ttk.Label(self, text="Inccorect login credentials")
        l4.pack(side=BOTTOM)


class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        l1 = ttk.Label(self, text="Register", font=LARGE_FONT)
        l1.pack(pady=10,padx=10)

        l2 = ttk.Label(self, text="User Name")
        l2.pack(side=LEFT)

        l3 = ttk.Label(self, text="Password ")
        l3.pack(side=LEFT)

        UserN_input = ttk.Entry(self, width=20)
        UserN_input.pack(side=RIGHT)

        PW_input = ttk.Entry(self, width=20)
        PW_input.pack(side=RIGHT)

        RegBtn = ttk.Button(self, text="Register", command= lambda: insert_account(UserN_input,PW_input,1))
        RegBtn.pack(side = BOTTOM)

        button4 = ttk.Button(self, text="Back", command=lambda: controller.show_frame("LoginPage"))
        button4.pack(side = RIGHT)

######################################################################################
#currently, a successful login goes to the student_homepage, regardless of who logs in. We still need to add some some of way to distinguish between lecturers and students so we can load the correct page after a login.

# class LoggedIn(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)

#         label = ttk.Label(self, text="Login Successful", font=LARGE_FONT)
#         label.pack(pady=10,padx=10)
######################################################################################


class student_homepage(Frame):

	def __init__(self, parent, controller):

		Frame.__init__(self, parent)
		self.controller = controller


		self.grid()
		self.Title()
		self.TopicSelect()
		self.LayoutPadding()
		# self.LogoutButton()

		button1 = Button(self, text="Binary Conversion Lesson", command=lambda: controller.show_frame("StartPage"))
		button1.grid(row = 3, column = 4, columnspan = 1, sticky = W)

		button2 = Button(self, text="Sets & Probability Lesson", command=lambda: controller.show_frame("SetsPage"))
		button2.grid(row = 3, column = 3, columnspan = 1, sticky = E)

		button3 = Button(self, text="View Results", command=lambda: controller.show_frame("ResultsStore"))
		button3.grid(row = 5, column = 3, columnspan = 1, sticky = E)

		button4 = Button(self, text="Logout", command=lambda: controller.show_frame("LoginPage"))
		button4.grid(row = 6, column = 3, columnspan = 1, sticky = W)

		
	def Title(self):

		lblHomepageTitle = Label(self, text = 'Learn Interactive 2016               \n', font = ('calibri', 22, 'bold'))
		lblHomepageTitle.grid(row = 1, column = 4, columnspan = 2, sticky = N)


	def TopicSelect(self):

		lblChooseTopic = Label(self, text = 'Choose Topic \n \n', font = ('calibri', 12, 'bold'))
		lblChooseTopic.grid(row = 2, column = 2, columnspan = 1, sticky = N)


	def createLessonTitle(self):

		lblLessonTitle = Label(self, text='"Binary Conversion" \n', font=('MS', 22, 'bold'))
		lblLessonTitle.grid(row=1, column=6, columnspan=3, sticky=N)


	def LayoutPadding(self):

		lblResultsPadding = Label(self, text = '')
		lblResultsPadding.grid(row = 4, column = 4, columnspan = 1)

		lblBottomLogoutPadding = Label(self, text = '')
		lblBottomLogoutPadding.grid(row = 8, column = 5, columnspan = 1)

		lblTopLogoutPadding = Label(self, text = '')
		lblTopLogoutPadding.grid(row = 6, column = 5, columnspan = 1)


	# def LogoutButton(self):

	# 	buttonLogout = Button(self, text = 'Logout', font = ('calibri', 12, 'bold'))
	# 	buttonLogout.grid(row = 7, column = 5, columnspan = 1, sticky = N)

		


class lessonPage(Frame):								#why is this class here?

	def __init__(self, parent, controller):


		Frame.__init__(self, parent)
		self.controller = controller

		self.grid()
		self.createLessonTitle()


	def createLessonTitle(self):

		lblLessonTitle = Label(self, text='"Binary Conversion" \n', font=('MS', 22, 'bold'))
		lblLessonTitle.grid(row=1, column=6, columnspan=3, sticky=N)


class StartPage(Frame): 								#change name to binaryLesson

	def __init__(self, parent, controller):

		Frame.__init__(self, parent)
		self.controller = controller


		self.grid()
		self.createLessonTitle()
		self.createLessonDescription()
		self.createLessonObjectives()
		self.createLessonContent()

		button1 = Button(self, text="Take Test",
							command=lambda: controller.show_frame("binaryTestPage"))
		button1.grid(row=23, column=19, columnspan=1, sticky=W)

		button2 = Button(self, text="Back", command=lambda: controller.show_frame("student_homepage"))
		button2.grid(row = 23, column = 4, columnspan = 1, sticky = W)



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


class binaryTestPage(Frame):

	def __init__(self, parent, controller):

		Frame.__init__(self, parent)
		self.controller = controller
		self.grid()
		self.Binary_Title()
		self.setQuestions()
		self.studentNumEntry()
		self.addButtons()
		self.storeResult


	def Binary_Title(self):
		theTitle = Label(self, text="Binary Test", font=('MS', 22, 'bold'))
		theTitle.grid(row=0, column=5, columnspan=2)

	def setQuestions(self):

		lblDesc1 = Label(self, text='Multiple Choice Questions:', font=('MS', 10,'bold'))
		lblDesc1.grid(row=3, column = 3)

		lblDesc2 = Label(self, text='For each of the following, convert the decimal numbers (base 10) into octal (base 8) and choose an answer:', font=('MS', 10))
		lblDesc2.grid(row=3, column = 4, columnspan=5, sticky=W)

		#Start Of Question 1

		lblQ1 = Label(self, text='\nQuestion 1): ', font=('MS', 10,'bold'))
		lblQ1.grid(row=6, column = 4)

		lblQ1_Question = Label(self, text='\nWhat is 18 (10) in octal?', font=('MS', 10))
		lblQ1_Question.grid(row=6, column = 5, columnspan=2, sticky=W)

		lblQ1_ChoiceA = Label(self, text='A) 19 (8)', font=('MS', 10))
		lblQ1_ChoiceA.grid(row=7, column = 5, columnspan=1, sticky=W)

		lblQ1_ChoiceB = Label(self, text='B) 20 (8)', font=('MS', 10))
		lblQ1_ChoiceB.grid(row=8, column = 5, columnspan=1, sticky=W)

		lblQ1_ChoiceC = Label(self, text='C) 21 (8)', font=('MS', 10))
		lblQ1_ChoiceC.grid(row=9, column = 5, columnspan=1, sticky=W)

		lblQ1_ChoiceD = Label(self, text='D) 22 (8)', font=('MS', 10))
		lblQ1_ChoiceD.grid(row=10, column = 5, columnspan=1, sticky=W)

		self.varQ1 = IntVar()
		R1Q1 = Radiobutton(self, variable=self.varQ1, value=4)
		R1Q1.grid(row=7, column= 6)
		R2Q1 = Radiobutton(self, variable= self.varQ1, value=3)
		R2Q1.grid(row=8, column= 6)
		R3Q1 = Radiobutton(self, variable= self.varQ1, value=2)
		R3Q1.grid(row=9, column= 6)
		R4Q1 = Radiobutton(self, variable= self.varQ1, value=1)
		R4Q1.grid(row=10, column= 6)

		#End of Question 1

		#----------------------------------------------------------------------------------------------------------------------------#

		#Start of Question 2

		lblQ2 = Label(self, text='\nQuestion 2): ', font=('MS', 10,'bold'))
		lblQ2.grid(row=11, column = 4)

		lblQ2_Question = Label(self, text='\nWhat is 156 (10) in octal?', font=('MS', 10))
		lblQ2_Question.grid(row=11, column = 5, columnspan=2, sticky=W)

		lblQ2_ChoiceA = Label(self, text='A) 212 (8)', font=('MS', 10))
		lblQ2_ChoiceA.grid(row=12, column = 5, columnspan=1, sticky=W)

		lblQ2_ChoiceB = Label(self, text='B) 220 (8)', font=('MS', 10))
		lblQ2_ChoiceB.grid(row=13, column = 5, columnspan=1, sticky=W)

		lblQ2_ChoiceC = Label(self, text='C) 234 (8)', font=('MS', 10))
		lblQ2_ChoiceC.grid(row=14, column = 5, columnspan=1, sticky=W)

		lblQ2_ChoiceD = Label(self, text='D) 242 (8)', font=('MS', 10))
		lblQ2_ChoiceD.grid(row=15, column = 5, columnspan=1, sticky=W)

		self.varQ2 = IntVar()
		R1Q2 = Radiobutton(self, variable=self.varQ2, value=4)
		R1Q2.grid(row=12, column= 6)
		R2Q2 = Radiobutton(self, variable= self.varQ2, value=3)
		R2Q2.grid(row=13, column= 6)
		R3Q2 = Radiobutton(self, variable= self.varQ2, value=2)
		R3Q2.grid(row=14, column= 6)
		R4Q2 = Radiobutton(self, variable= self.varQ2, value=1)
		R4Q2.grid(row=15, column= 6)

		#End of Question 2

		#----------------------------------------------------------------------------------------------------------------------------#

		#Start of Question 3

		lblQ3 = Label(self, text='\nQuestion 3): ', font=('MS', 10,'bold'))
		lblQ3.grid(row=16, column = 4)

		lblQ3_Question = Label(self, text='\nWhat is 1267 (10) in octal?', font=('MS', 10))
		lblQ3_Question.grid(row=16, column = 5, columnspan=2, sticky=W)

		lblQ3_ChoiceA = Label(self, text='A) 2109 (8)', font=('MS', 10))
		lblQ3_ChoiceA.grid(row=17, column = 5, columnspan=1, sticky=W)

		lblQ3_ChoiceB = Label(self, text='B) 2163 (8)', font=('MS', 10))
		lblQ3_ChoiceB.grid(row=18, column = 5, columnspan=1, sticky=W)

		lblQ3_ChoiceC = Label(self, text='C) 2363 (8)', font=('MS', 10))
		lblQ3_ChoiceC.grid(row=19, column = 5, columnspan=1, sticky=W)

		lblQ3_ChoiceD = Label(self, text='D) 2451 (8)', font=('MS', 10))
		lblQ3_ChoiceD.grid(row=20, column = 5, columnspan=1, sticky=W)

		self.varQ3 = IntVar()
		R1Q3 = Radiobutton(self, variable=self.varQ3, value=4)
		R1Q3.grid(row=17, column= 6)
		R2Q3 = Radiobutton(self, variable= self.varQ3, value=3)
		R2Q3.grid(row=18, column= 6)
		R3Q3 = Radiobutton(self, variable= self.varQ3, value=2)
		R3Q3.grid(row=19, column= 6)
		R4Q3 = Radiobutton(self, variable= self.varQ3, value=1)
		R4Q3.grid(row=20, column= 6)

		#End of Question 3

		#----------------------------------------------------------------------------------------------------------------------------#

		#Start of Question 4

		lblQ4 = Label(self, text='\nQuestion 4): ', font=('MS', 10,'bold'))
		lblQ4.grid(row=21, column = 4)

		lblQ4_Question = Label(self, text='\nWhat is 4000 (8) in decimal?', font=('MS', 10))
		lblQ4_Question.grid(row=21, column = 5, columnspan=2, sticky=W)

		lblQ4_ChoiceA = Label(self, text='A) 2048 (10)', font=('MS', 10))
		lblQ4_ChoiceA.grid(row=22, column = 5, columnspan=1, sticky=W)

		lblQ4_ChoiceB = Label(self, text='B) 2060 (10)', font=('MS', 10))
		lblQ4_ChoiceB.grid(row=23, column = 5, columnspan=1, sticky=W)

		lblQ4_ChoiceC = Label(self, text='C) 2084 (10)', font=('MS', 10))
		lblQ4_ChoiceC.grid(row=24, column = 5, columnspan=1, sticky=W)

		lblQ4_ChoiceD = Label(self, text='D) 2101 (10)', font=('MS', 10))
		lblQ4_ChoiceD.grid(row=25, column = 5, columnspan=1, sticky=W)

		self.varQ4 = IntVar()
		R1Q4 = Radiobutton(self, variable=self.varQ4, value=4)
		R1Q4.grid(row=22, column= 6)
		R2Q4 = Radiobutton(self, variable= self.varQ4, value=3)
		R2Q4.grid(row=23, column= 6)
		R3Q4 = Radiobutton(self, variable= self.varQ4, value=2)
		R3Q4.grid(row=24, column= 6)
		R4Q4 = Radiobutton(self, variable= self.varQ4, value=1)
		R4Q4.grid(row=25, column= 6)

		#End of Question 4

		#----------------------------------------------------------------------------------------------------------------------------#

		#Start of Question 5

		lblQ5 = Label(self, text='\nQuestion 5): ', font=('MS', 10,'bold'))
		lblQ5.grid(row=26, column = 4)

		lblQ5_Question = Label(self, text='\nWhat is 127 (8) in decimal?', font=('MS', 10))
		lblQ5_Question.grid(row=26, column = 5, columnspan=2, sticky=W)

		lblQ5_ChoiceA = Label(self, text='A) 87 (10)', font=('MS', 10))
		lblQ5_ChoiceA.grid(row=27, column = 5, columnspan=2, sticky=W)

		lblQ5_ChoiceB = Label(self, text='B) 94 (10)', font=('MS', 10))
		lblQ5_ChoiceB.grid(row=28, column = 5, columnspan=2, sticky=W)

		lblQ5_ChoiceC = Label(self, text='C) 96 (10)', font=('MS', 10))
		lblQ5_ChoiceC.grid(row=29, column = 5, columnspan=2, sticky=W)

		lblQ5_ChoiceD = Label(self, text='D) 88 (10)', font=('MS', 10))
		lblQ5_ChoiceD.grid(row=30, column = 5, columnspan=1, sticky=W)

		self.varQ5 = IntVar()
		R1Q5 = Radiobutton(self, variable=self.varQ5, value=4)
		R1Q5.grid(row=27, column= 6)
		R2Q5 = Radiobutton(self, variable= self.varQ5, value=3)
		R2Q5.grid(row=28, column= 6)
		R3Q5 = Radiobutton(self, variable= self.varQ5, value=2)
		R3Q5.grid(row=29, column= 6)
		R4Q5 = Radiobutton(self, variable= self.varQ5, value=1)
		R4Q5.grid(row=30, column= 6)

		#End of Question 5

		#----------------------------------------------------------------------------------------------------------------------------#

	def studentNumEntry(self):

		#Start of Student ID text box

		lbl_blank1 = Label(self, text=' ', font=('MS', 10,'bold'))
		lbl_blank1.grid(row=31, column = 1)

		lbl_ID = Label(self, text='Enter your student number:', font=('MS', 10,'bold'))
		lbl_ID.grid(row=32, column = 5, sticky=W)

		self.entName = Entry(self)
		self.entName.grid(row=32, column=5, columnspan=2, sticky=E) 

		#End of Student ID text box

		#----------------------------------------------------------------------------------------------------------------------------#

	def addButtons(self):

		#Start of Buttons Method

		lbl_blank2 = Label(self, text=' ', font=('MS', 10,'bold'))
		lbl_blank2.grid(row=33, column = 5)

		butSubmit = Button(self, text='Submit',font=('MS', 8,'bold'))
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
		q1answer = "0"
		q2answer = "0"
		q3answer = "0"
		q4answer = "0"
		q5answer = "0"

		if (self.varQ1.get() == 1):
			theScore = theScore + 1
			q1answer = "1"
		if (self.varQ2.get() == 2):
			theScore = theScore + 1
			q2answer = "1"
		if (self.varQ3.get() == 2):
			theScore = theScore + 1
			q3answer = "1"
		if (self.varQ4.get() == 4):
			theScore = theScore + 1
			q4answer = "1"
		if (self.varQ5.get() == 4):
			theScore = theScore + 1
			q5answer = "1"
		if strMsg == "":

			messagebox.showinfo("Test", "Your test has been saved and you have scored " + str(theScore) + "/5")
			with open("Results.txt", "a") as ifile:
				ifile.write("\nB," + theUser + ","+q1answer + "," + q2answer + ","+q3answer+","+q4answer+","+q5answer+","+str(theScore))

		else:

			messagebox.showwarning("Entry Error", strMsg)





#SETS LESSON
#change content of lesson and test to sets.


class SetsPage(Frame):

	def __init__(self, parent, controller):

		Frame.__init__(self, parent)
		self.controller = controller

		self.grid()
		self.lTitle()
		self.LessonDescription()
		self.LOutline()
		self.Content()
		self.Objectives()
		


		TakeTest = Button(self, text="Take Test",
							command=lambda: controller.show_frame("setsTestPage"))
		TakeTest.grid(row=23, column=19, columnspan=1, sticky=W)

		button2 = Button(self, text="Back ", command=lambda: controller.show_frame("student_homepage"))
		button2.grid(row = 24, column = 6, columnspan = 1, sticky = W)


		# TakeTest = Button(self, text='Take Test', font=('MS', 10, 'bold'))
		# TakeTest['command']=self.GoToTest
		# TakeTest.grid(row=24, column= 24)


	def lTitle(self):
		Title = Label(self, text='"Sets"', font=('MS', 22, 'bold'))
		Title.grid(row=1, column=13, columnspan=2, sticky=N)

	def LessonDescription(self):
		description = Label(self, text='Lesson description', font=('MS', 12, 'bold'))
		description.grid(row=2, column=5, columnspan=1, sticky=N)

		des = Label(self, text='This lesson aims to Introduce the consept of Sets', font=('MS', 9, 'bold'))
		des.grid(row=3, column=4,columnspan=4, sticky=N)

	def LOutline(self):
		OL = Label(self, text='Lesson Outline', font=('MS', 12, 'bold'))
		OL.grid(row=2, column= 23, columnspan=1, sticky=E)

		outline = Label(self, text='1. What is "Set theory"? And how to write sets? \n 2. Special sets \n 3. Subsets, Universal and empty sets. \n 4. Operations on sets.', font=('MS', 9, 'bold'))
		outline.grid(row=3, column= 21, columnspan=4, sticky=E)		


	def Content(self):

		con1 = Label(self, text='What is "Set theory"? And how to write sets?', font=('MS', 11, 'bold'))
		con1.grid(row=9, column= 13)
		lessonCon1 = Label(self, text='Set theory is a formal way of dealing with collections of things. A set is a collection of distinguishable objects called elements.', font=('MS', 10))
		lessonCon1.grid(row=10, column= 13)
		example = Label(self, text='Example of a set: The set of letters: s = {a, b, c,…, y, z}. (Note:objects in a set cannot be repeated.) ', font=('MS', 10))
		example.grid(row=11, column= 13)
		ways = Label(self, text='Two ways to write sets:', font=('MS', 10, 'bold'))
		ways.grid(row=12, column= 13)
		ways2 = Label(self, text='1. Enumeration: {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}. \n 2. Set builder notation: {x : 1 < x < 20 and x is even}.' , font=('MS', 10))
		ways2.grid(row=13, column= 13)

		con2 = Label(self, text='Special sets', font=('MS', 11, 'bold'))
		con2.grid(row=14, column= 13)
		lessonCon2 = Label(self, text='N= {0, 1, 2, 3, . . .}, set of rational numbers. \n Z= {. . . , −3, −2, −1, 0, 1, 2, 3, . . .},set of integers. \n  Q= {x ∈ R : x = p\q such that p, q ∈ Z}, set of rational numbers. \n R=the set of all real numbers- all decimal numbers.', font=('MS', 10))
		lessonCon2.grid(row=15, column= 13)

		con3 = Label(self, text='Subsets, Universal and empty sets', font=('MS', 11, 'bold'))
		con3.grid(row=16, column= 13)
		lessonCon3 = Label(self, text='Subset:(A ⊆ B).means every element of A is an element of B.             Equality:(A = B) if they have exactly the same elements. \n Proper subset:(A ⊂ B) A is a subset of B but not equal to B. \n \n Cardinality: the number of elements in a set.        Empty set({} or ∅): the set with zero elements. \n Universal set(U): set of all possible elements.            Power set(P(S)): the set of all subsets of S.', font=('MS', 10))
		lessonCon3.grid(row=17, column= 13)

		con4 = Label(self, text='Operations on sets', font=('MS', 11, 'bold'))
		con4.grid(row=18, column= 13)
		lessonCon4 = Label(self, text='-Union of sets(A∪B)= {x : x ∈ A or x ∈ B}.        -Intersection of sets(A∩B)= {x : x ∈ A and x ∈ B}. \n   -Difference  of sets(A-B)= {x : x ∈ A and x ̸∈ B}.       -complement of sets(A(or A C))= A = U − A = {x : x ∈ U and x ̸∈ A}.', font=('MS', 10))
		lessonCon4.grid(row=19, column= 13)

		con5 = Label(self, text='\n Disjoint sets: If two sets have no common elements, they are disjoint.', font=('MS', 10, 'bold'))
		con5.grid(row=20, column= 13)
		lessonCon5 = Label(self, text='{1, 2, 3}, {x, y} are disjoint, but {1, 2, 3}, {2, x, y} are not disjoint (they share a common element).', font=('MS', 10))
		lessonCon5.grid(row=21, column= 13)

		con6 = Label(self, text='Inclusion-exclusion principle: ', font=('MS', 11, 'bold'))
		con6.grid(row=22, column= 13)
		lessonCon6 = Label(self, text=' For two (finite) sets A and B:  |A ∪ B| = |A| + |B| − |A ∩ B|. \n For three sets A, B and C:  |A ∪B∪ C| = |A|+|B|+|C|−|A ∩B|−|A ∩ C|−|B∩ C|+|A ∩B∩ C|.', font=('MS', 10))
		lessonCon6.grid(row=23, column= 13)

	def Objectives(self):

		o = Label(self, text='Lesson Objectives: ', font=('MS', 11, 'bold'))
		o.grid(row=22, column=5)

		O1 = Label(self, text=" -Represent collections of objects as sets. \n -Use set operations to express the relationships between sets. ")
		O1.grid(row=23, column=5)

	# def TakeTest(self):

	# 	TakeTest = Button(self, text='Take Test', font=('MS', 10, 'bold'))
	# 	TakeTest['command']=self.GoToTest
	# 	TakeTest.grid(row=24, column= 24)

	# def GoToTest(self):

	# 	test= Toplevel(self)
	# 	test.title("Sets Test")


class setsTestPage(Frame):

	def __init__(self, parent, controller):

		Frame.__init__(self, parent)
		self.controller = controller
		self.grid()
		self.Sets_Title()
		self.setQuestions()
		#self.studentNumEntry()
		self.addButtons()
		self.storeResult


	def Sets_Title(self):
		theTitle = Label(self, text="Sets Test", font=('MS', 22, 'bold'))
		theTitle.grid(row=0, column=5, columnspan=2)

	def setQuestions(self):

		lblDesc1 = Label(self, text='Multiple Choice Questions:', font=('MS', 10,'bold'))
		lblDesc1.grid(row=3, column = 3)


		#Start Of Question 1

		lblQ1 = Label(self, text='\nQuestion 1): ', font=('MS', 9,'bold'))
		lblQ1.grid(row=6, column = 4)

		lblQ1_Question = Label(self, text='\nWhat is the cardinality of the set S= {3, 6, 9, 12}?', font=('MS', 9))
		lblQ1_Question.grid(row=6, column = 5, columnspan=2, sticky=W)

		lblQ1_ChoiceA = Label(self, text='A) One')
		lblQ1_ChoiceA.grid(row=7, column = 5, columnspan=1, sticky=W)

		lblQ1_ChoiceB = Label(self, text='B) Two')
		lblQ1_ChoiceB.grid(row=8, column = 5, columnspan=1, sticky=W)

		lblQ1_ChoiceC = Label(self, text='C) Three')
		lblQ1_ChoiceC.grid(row=9, column = 5, columnspan=1, sticky=W)

		lblQ1_ChoiceD = Label(self, text='D) Four')
		lblQ1_ChoiceD.grid(row=10, column = 5, columnspan=1, sticky=W)

		self.varQ1 = IntVar()
		R1Q1 = Radiobutton(self, variable=self.varQ1, value=4)
		R1Q1.grid(row=7, column= 6)
		R2Q1 = Radiobutton(self, variable= self.varQ1, value=3)
		R2Q1.grid(row=8, column= 6)
		R3Q1 = Radiobutton(self, variable= self.varQ1, value=2)
		R3Q1.grid(row=9, column= 6)
		R4Q1 = Radiobutton(self, variable= self.varQ1, value=1)
		R4Q1.grid(row=10, column= 6)

		#End of Question 1

		#----------------------------------------------------------------------------------------------------------------------------#

		#Start of Question 2

		lblQ2 = Label(self, text='\nQuestion 2): ', font=('MS', 9,'bold'))
		lblQ2.grid(row=11, column = 4)

		lblQ2_Question = Label(self, text='\nThe set of all rational numbers is denoted by:', font=('MS', 9))
		lblQ2_Question.grid(row=11, column = 5, columnspan=2, sticky=W)

		lblQ2_ChoiceA = Label(self, text='A) ℕ')
		lblQ2_ChoiceA.grid(row=12, column = 5, columnspan=1, sticky=W)

		lblQ2_ChoiceB = Label(self, text='B) ℝ')
		lblQ2_ChoiceB.grid(row=13, column = 5, columnspan=1, sticky=W)

		lblQ2_ChoiceC = Label(self, text='C) ℕ')
		lblQ2_ChoiceC.grid(row=14, column = 5, columnspan=1, sticky=W)

		lblQ2_ChoiceD = Label(self, text='D) ℝ')
		lblQ2_ChoiceD.grid(row=15, column = 5, columnspan=1, sticky=W)

		self.varQ2 = IntVar()
		R1Q2 = Radiobutton(self, variable=self.varQ2, value=4)
		R1Q2.grid(row=12, column= 6)
		R2Q2 = Radiobutton(self, variable= self.varQ2, value=3)
		R2Q2.grid(row=13, column= 6)
		R3Q2 = Radiobutton(self, variable= self.varQ2, value=2)
		R3Q2.grid(row=14, column= 6)
		R4Q2 = Radiobutton(self, variable= self.varQ2, value=1)
		R4Q2.grid(row=15, column= 6)

		#End of Question 2

		#----------------------------------------------------------------------------------------------------------------------------#

		#Start of Question 3

		lblQ3 = Label(self, text='\nQuestion 3): ', font=('MS', 9,'bold'))
		lblQ3.grid(row=16, column = 4)

		lblQ3_Question = Label(self, text='\nThe notation x ∈ S means :', font=('MS', 9))
		lblQ3_Question.grid(row=16, column = 5, columnspan=2, sticky=W)

		lblQ3_ChoiceA = Label(self, text='A) “x is an element of S”')
		lblQ3_ChoiceA.grid(row=17, column = 5, columnspan=1, sticky=W)

		lblQ3_ChoiceB = Label(self, text='B) “x is not an element of S”')
		lblQ3_ChoiceB.grid(row=18, column = 5, columnspan=1, sticky=W)

		lblQ3_ChoiceC = Label(self, text='C) “x is a subset of S”')
		lblQ3_ChoiceC.grid(row=19, column = 5, columnspan=1, sticky=W)

		lblQ3_ChoiceD = Label(self, text='D) x is a Proper set of S')
		lblQ3_ChoiceD.grid(row=20, column = 5, columnspan=1, sticky=W)

		self.varQ3 = IntVar()
		R1Q3 = Radiobutton(self, variable=self.varQ3, value=4)
		R1Q3.grid(row=17, column= 6)
		R2Q3 = Radiobutton(self, variable= self.varQ3, value=3)
		R2Q3.grid(row=18, column= 6)
		R3Q3 = Radiobutton(self, variable= self.varQ3, value=2)
		R3Q3.grid(row=19, column= 6)
		R4Q3 =Radiobutton(self, variable= self.varQ3, value=1)
		R4Q3.grid(row=20, column= 6)

		#End of Question 3

		#----------------------------------------------------------------------------------------------------------------------------#

		#Start of Question 4

		lblQ4 = Label(self, text='\nQuestion 4): ', font=('MS', 9,'bold'))
		lblQ4.grid(row=21, column = 4)

		lblQ4_Question =Label(self, text='\nThe power set is:', font=('MS', 9))
		lblQ4_Question.grid(row=21, column = 5, columnspan=2, sticky=W)

		lblQ4_ChoiceA = Label(self, text='The set of all possible elements.')
		lblQ4_ChoiceA.grid(row=22, column = 5, columnspan=1, sticky=W)

		lblQ4_ChoiceB = Label(self, text='The set with zero elements.')
		lblQ4_ChoiceB.grid(row=23, column = 5, columnspan=1, sticky=W)

		lblQ4_ChoiceC = Label(self, text='C) The set of all subsets.')
		lblQ4_ChoiceC.grid(row=24, column = 5, columnspan=1, sticky=W)

		lblQ4_ChoiceD = Label(self, text='D) None of the above.')
		lblQ4_ChoiceD.grid(row=25, column = 5, columnspan=1, sticky=W)

		self.varQ4 = IntVar()
		R1Q4 = Radiobutton(self, variable=self.varQ4, value=4)
		R1Q4.grid(row=22, column= 6)
		R2Q4 = Radiobutton(self, variable= self.varQ4, value=3)
		R2Q4.grid(row=23, column= 6)
		R3Q4 = Radiobutton(self, variable= self.varQ4, value=2)
		R3Q4.grid(row=24, column= 6)
		R4Q4 = Radiobutton(self, variable= self.varQ4, value=1)
		R4Q4.grid(row=25, column= 6)

		#End of Question 4

		#----------------------------------------------------------------------------------------------------------------------------#

		#Start of Question 5

		lblQ5 = Label(self, text='\nQuestion 5): ', font=('MS', 9,'bold'))
		lblQ5.grid(row=26, column = 4)

		lblQ5_Question = Label(self, text='\n{x : x ∈ A or x ∈ B} means:', font=('MS', 9))
		lblQ5_Question.grid(row=26, column = 5, columnspan=2, sticky=W)

		lblQ5_ChoiceA = Label(self, text='A) Intersection of sets A,B.')
		lblQ5_ChoiceA.grid(row=27, column = 5, columnspan=2, sticky=W)

		lblQ5_ChoiceB = Label(self, text='B) Difference  of sets A,B.')
		lblQ5_ChoiceB.grid(row=28, column = 5, columnspan=2, sticky=W)

		lblQ5_ChoiceC = Label(self, text='C) complement of sets A,B.')
		lblQ5_ChoiceC.grid(row=29, column = 5, columnspan=2, sticky=W)

		lblQ5_ChoiceD = Label(self, text='D)Union of sets A,B.')
		lblQ5_ChoiceD.grid(row=30, column = 5, columnspan=1, sticky=W)

		self.varQ5 = IntVar()
		R1Q5 = Radiobutton(self, variable=self.varQ5, value=4)
		R1Q5.grid(row=27, column= 6)
		R2Q5 = Radiobutton(self, variable= self.varQ5, value=3)
		R2Q5.grid(row=28, column= 6)
		R3Q5 = Radiobutton(self, variable= self.varQ5, value=2)
		R3Q5.grid(row=29, column= 6)
		R4Q5 = Radiobutton(self, variable= self.varQ5, value=1)
		R4Q5.grid(row=30, column= 6)

		#End of Question 5

		#----------------------------------------------------------------------------------------------------------------------------#

	#def studentNumEntry(self):

		#Start of Student ID text box

		#lbl_blank1 = Label(self, text=' ', font=('MS', 10,'bold'))
		#lbl_blank1.grid(row=31, column = 1)

		#lbl_ID = Label(self, text='Enter your student number:', font=('MS', 10,'bold'))
		#lbl_ID.grid(row=32, column = 5, sticky=W)

		#self.entName = Entry(self)
		#self.entName.grid(row=32, column=5, columnspan=2, sticky=E) 

		#End of Student ID text box

		#----------------------------------------------------------------------------------------------------------------------------#

	def addButtons(self):

		#Start of Buttons Method

		lbl_blank2 = Label(self, text=' ', font=('MS', 10,'bold'))
		lbl_blank2.grid(row=33, column = 5)

		butSubmit = Button(self, text='Submit',font=('MS', 8,'bold'))
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

		#if (self.entName.get() == ""):
			#strMsg = strMsg + "\nPlease enter your student number!"

		answer_q1 = 1
		answer_q2 = 4
		answer_q3 = 4
		answer_q4 = 2
		answer_q5 = 1
		q1answer = "0"
		q2answer = "0"
		q3answer = "0"
		q4answer = "0"
		q5answer = "0"

		if (self.varQ1.get() == 1):
			theScore = theScore + 1
			q1answer = "1"
		if (self.varQ2.get() == 2):
			theScore = theScore + 1
			q2answer = "1"
		if (self.varQ3.get() == 2):
			theScore = theScore + 1
			q3answer = "1"
		if (self.varQ4.get() == 4):
			theScore = theScore + 1
			q4answer = "1"
		if (self.varQ5.get() == 4):
			theScore = theScore + 1
			q5answer = "1"
		if strMsg == "":

			messagebox.showinfo("Test", "Your test has been saved and you have scored " + str(theScore) + "/5")
			with open("Results.txt", "a") as ifile:
				ifile.write("\nS," + theUser + ","+q1answer + "," + q2answer + ","+q3answer+","+q4answer+","+q5answer+","+str(theScore))


		else:

			messagebox.showwarning("Entry Error", strMsg)

class ResultsStore(Frame):
	
	
	def __init__(self, parent, controller):
		User = "1"
		Frame.__init__(self, parent)
		self.controller = controller
		self.grid()

		button2 = Button(self, text="Back ", command=lambda: controller.show_frame("student_homepage"))
		button2.grid(row = 24, column = 6, columnspan = 1, sticky = W)

		if rights == "1":
			self.Title()
			self.Topic()
		else:
			self.LTitle()
			self.LTopic()
		


	def Title(self):
		StudentTitle = Label(self, text = "Student Results", font = ("calibri", 22, "bold"))
		StudentTitle.grid(row = 1, column = 10, columnspan = 2, padx= 150, pady = 10, sticky = N)
	
	def Topic(self):
		listbox = Listbox(self)
		listbox.grid(row=5,column = 10,sticky =E)
		def Results(var):
			res = []
			listbox.delete(0,20)
			goal = ""
			student = User
			turns = 0
			f = open("Results.txt", "r")
			doc = f.readlines()
			for lines in doc:
				seg = lines.split(",")
				if var == "Binary":
					goal = "B"
				elif var == "Sets":
					goal = "S"
				if seg[0] == goal:
					if seg[1] == User:
						if var == "Binary":
							res.append("Binary")
						else:
							res.append("Sets")
						info = doc[turns].split(",")
						res.append("ID: " + info[1])
						res.append("Q1: " + info[2])
						res.append("Q2: " + info[3])
						res.append("Q3: " + info[4])
						res.append("Q4: " + info[5])
						res.append("Q5: " + info[6])
						res.append("Overall: " + info[7])
						break
					else:
						turns += 1
				else:
					turns +=1
			
			for item in res:
				listbox.insert(END, item)

		var = StringVar()
		var.set("Topic")
		button = Button(self, text="Select")
		button.grid(row = 3, column = 11)
		button['command'] = lambda:Results(var.get())
		drop = OptionMenu(self, var, "Binary", "Sets")
		drop.grid(row = 3, column = 10, columnspan = 2, padx = 150,pady = 10, sticky = N)
	


	def LTitle(self):
		LecturerTitle = Label(self, text = "Lecturer Page", font = ("calibri", 22, "bold"))
		LecturerTitle.grid(row = 1, column = 10, columnspan = 2, padx= 150, pady = 10, sticky = N)

	def LTopic(self):
		
		options = []
		
		listbox = Listbox(self)
		listbox.grid(row = 5, column =10)
		f = open("Results.txt", "r")
		doc = f.readlines()
		for lines in doc:
				seg = lines.split(",")

				options.append(seg[1])
			
		def Results(var):
			User = var
			turns = 0
			res = []
			listbox.delete(0,20)
			for lines in doc:
				seg = lines.split(",")
				if seg[1] == User:
					print("Yes")
					if seg[0] == "B":
						info = doc[turns].split(",")
						res.append("Binary")
						res.append("ID: " + info[1])
						res.append("Q1: " + info[2])
						res.append("Q2: " + info[3])
						res.append("Q3: " + info[4])
						res.append("Q4: " + info[5])
						res.append("Q5: " + info[6])
						res.append("Overall: " + info[7])
						turns += 1
					elif seg[0] == "S":
						info = doc[turns].split(",")
						res.append("Sets")
						res.append("ID: " + info[1])
						res.append("Q1: " + info[2])
						res.append("Q2: " + info[3])
						res.append("Q3: " + info[4])
						res.append("Q4: " + info[5])
						res.append("Q5: " + info[6])
						res.append("Overall: " + info[7])
						turns +=1
				else:
					turns += 1
			
			for item in res:
				listbox.insert(END, item)
		var = StringVar()
		var.set("Students")
		button = Button(self, text="Select")
		button.grid(row = 3, column = 11)
		button['command'] = lambda:Results(var.get())
		
		drop = OptionMenu(self, var, *list(set(options)))
		drop.grid(row = 3, column = 10, columnspan = 2, padx = 150,pady = 10, sticky = N)

		Feedback = Label(self, text = "Feedback:", font = "calibri")
		area = Entry(self,width = 40, textvariable = StringVar(),xscrollcommand = Y)
		area.grid(row = 17, column = 9,columnspan = 3, rowspan=3)
		FButton = Button(self, text = "Give Feedback")
		FButton.grid(row = 17 , column = 11)


if __name__ == "__main__":


	app = SampleApp()
	app.mainloop()