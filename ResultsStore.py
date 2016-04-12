from tkinter import *

class ResultsStore(Frame):
	
	
	def __init__(self, root):
		User = "0"
		Frame.__init__(self, root)
		self.pack()
		if User == "1":
			self.Title()
			self.Topic()
		else:
			self.LTitle()
			self.LTopic()
		


	def Title(self):
		StudentTitle = Label(self, text = "Student Results", font = ("calibri", 22, "bold"))
		StudentTitle.pack(fill=X)#row = 1, column = 10, columnspan = 2, padx= 150, pady = 10, sticky = N)
	
	def Topic(self):
		
		def Results(var):
			res = []
			goal = ""
			User = "c2345678"
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
			listbox = Listbox(self)
			listbox.pack(side=LEFT)
			for item in res:
				listbox.insert(END, item)

		var = StringVar()
		var.set("Topic")
		button = Button(self, text="Select")
		button.pack()#row = 3, column = 11)
		button['command'] = lambda:Results(var.get())
		drop = OptionMenu(self, var, "Binary", "Sets")
		drop.pack()#row = 3, column = 10, columnspan = 2, padx = 150,pady = 10, sticky = N)
	


	def LTitle(self):
		LecturerTitle = Label(self, text = "Lecturer Page", font = ("calibri", 22, "bold"))
		LecturerTitle.pack()#row = 1, column = 10, columnspan = 2, padx= 150, pady = 10, sticky = N)

	def LTopic(self):
		
		options = []
		res = []
		f = open("Results.txt", "r")
		doc = f.readlines()
		for lines in doc:
				seg = lines.split(",")

				options.append(seg[1])
			
		def Results(var):
			User = var
			turns = 0
			for lines in doc:
				seg = lines.split(",")
				if seg[1] == User:
					print("Yes")
					if seg[0] == "B":
						print(seg)
						print("Y")
						print(turns)
					#	binary = Label(self, text="Binary", font = "calibri")
					#	binary.pack(anchor=W)#row = 4, column = 10)
						info = doc[turns].split(",")
						res.append("Binary")
						res.append("ID: " + info[1])
						res.append("Q1: " + info[2])
						res.append("Q2: " + info[3])
						res.append("Q3: " + info[4])
						res.append("Q4: " + info[5])
						res.append("Q5: " + info[6])
						res.append("Overall: " + info[7])
					#	result1b = Label(self, text = "Id: " + info[1])
					#	result2b = Label(self, text = "Q1: " + info[2]+ "\tQ2: " + info[3])
					#	result3b = Label(self, text = "Q3: " + info[4]+ "\tQ4: " + info[5])
					#	result4b = Label(self, text = "Q5: " + info[6])
					#	result5b = Label(self, text = "Overall: " + info[7])
					#	result1b.pack(anchor=W)#row = 5, column= 10, columnspan =5)
					#	result2b.pack(anchor=W)#row = 6, column= 10, columnspan =5)
					#	result3b.pack(anchor=W)#row = 7, column= 10, columnspan =5)
					#	result4b.pack(anchor=W)#row = 8, column= 10, columnspan =5)
					#	result5b.pack(anchor=W)#row = 9, column= 10, columnspan =5)
						turns += 1
					elif seg[0] == "S":
						print("y")
						print(turns)
					#	sets = Label(self, text="Sets", font = "calibri")
					#	sets.pack(anchor=E, side = RIGHT)#row = 10, column = 10)
						info = doc[turns].split(",")
						res.append("Sets")
						res.append("ID: " + info[1])
						res.append("Q1: " + info[2])
						res.append("Q2: " + info[3])
						res.append("Q3: " + info[4])
						res.append("Q4: " + info[5])
						res.append("Q5: " + info[6])
						res.append("Overall: " + info[7])
					#	result1s = Label(self, text = "Id: " + info[1])
					#	result2s= Label(self, text = "Q1: " + info[2]+ "\tQ2: " + info[3])
					#	result3s = Label(self, text = "Q3: " + info[4]+ "\tQ4: " + info[5])
					#	result4s= Label(self, text = "Q5: " + info[6])
					#	result5s = Label(self, text = "Overall: " + info[7])
					#	result1s.pack(anchor=E)#row = 11, column= 10, columnspan =5)
					#	result2s.pack(anchor=E)#row = 12, column= 10, columnspan =5)
					#	result3s.pack(anchor=E)#row = 13, column= 10, columnspan =5)
					#	result4s.pack(anchor=E)#row = 14, column= 10, columnspan =5)
					#	result5s.pack(anchor=E)#row = 15, column= 10, columnspan =5)
						turns +=1
				else:
					print("No")
					turns += 1
			listbox = Listbox(self)
			listbox.pack(side=LEFT)
			for item in res:
				listbox.insert(END, item)
		var = StringVar()
		var.set("Students")
		button = Button(self, text="Select")
		button.pack(side=RIGHT)#row = 3, column = 11)
		button['command'] = lambda:Results(var.get())
		
		drop = OptionMenu(self, var, *list(set(options)))
		drop.pack()#row = 3, column = 10, columnspan = 2, padx = 150,pady = 10, sticky = N)

		Feedback = Label(self, text = "Feedback:", font = "calibri")
		area = Entry(self,width = 40, textvariable = StringVar(),xscrollcommand = Y)
		area.pack(side = BOTTOM)#row = 17, column = 9,columnspan = 3, rowspan=3)
		FButton = Button(self, text = "Give Feedback")
		FButton.pack(side = BOTTOM)#row = 17 , column = 11)
		#button['command'] = 


root = Tk()
root.title("Results")
root.minsize(500,500)
root.geometry("500x500")
main = ResultsStore(root)
root.mainloop()