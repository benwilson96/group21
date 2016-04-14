from tkinter import*



class sets_Lesson(Frame):

	def __init__(self, master):

		Frame.__init__(self, master)
		self.grid()
		self.lTitle()
		self.LessonDescription()
		self.LOutline()
		self.Content()
		self.TakeTest()
		self.Objectives()
		self.GoToTest



	def lTitle(self):
		Title = Label(self, text='"Sets"', font=('MS', 22, 'bold'))
		Title.grid(row=1, column=13, columnspan=2, sticky=N)

	def LessonDescription(self):
		description = Label(self, text='Lesson description', font=('MS', 12, 'bold'))
		description.grid(row=2, column=5, columnspan=1, sticky=N)

		des = Label(self, text='This lessom aims to Introduce the consept of Sets', font=('MS', 9, 'bold'))
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
		o.grid(row=23, column=5)

		O1 = Label(self, text=" -Represent collections of objects as sets. \n -Use set operations to express the relationships between sets. ")
		O1.grid(row=24, column=5)

	def TakeTest(self):

		TakeTest = Button(self, text='Take Test', font=('MS', 10, 'bold'))
		TakeTest['command']=self.GoToTest
		TakeTest.grid(row=24, column= 24)

	def GoToTest(self):

		test= Toplevel(self)
		test.title("Sets Test")

#main
root = Tk()
root.title("Interactive Lesson - Sets")

#create a toplevel menu
menu = Menu(root)
root.config(menu=menu) #display the menu
submenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=submenu)
submenu.add_command(label="Homepage")
submenu.add_command(label="Help")
submenu.add_separator()
submenu.add_command(label="LOGOUT")

app = sets_Lesson(root)
root.mainloop()
