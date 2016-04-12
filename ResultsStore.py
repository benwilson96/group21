from tkinter import *

class ResultsStore(Frame):
	
	
	def __init__(self, root):
		User = "1"
		Frame.__init__(self, root)
		self.grid()
		if User == "1":
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
			User = "c1535751"
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
		#button['command'] = 


root = Tk()
root.title("Results")
root.minsize(500,500)
root.geometry("500x500")
main = ResultsStore(root)
root.mainloop()