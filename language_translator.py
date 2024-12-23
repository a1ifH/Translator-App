from tkinter import *
from tkinter import ttk, messagebox
import googletrans 
import textblob

# getting Google translator from computer
root = Tk()
root.title("Language Translator")
root.geometry("1080x400")



#function to change country names in labels
def label_change():
	c = combo1.get()
	c1 = combo2.get()
	label1.configure(text = c)
	label2.configure(text = c1)
	root.after(1000,label_change)

# function to translate language for button
def translate_now():
	global language
	try:
		text_ = text1.get(1.0, END)
		c2 = combo1.get()
		c3 = combo2.get()
		if(text_):
			words=textblob.TextBlob(text_)
			lan=words.detect_language()
			for i,j in language.items():
				if(j==c3):
					lan_=i
			words=words.translate(from_lang=lan,to=str(lan_))
			text2.delete(1.0,END)
			text2.insert(END,words)
	except Exception as e:
		messagebox.showerror("googletrans","please try again")






#icon
image_icon = PhotoImage(file="trans_pic.png")
root.iconphoto(False,image_icon)

#arrow
arrow_image = PhotoImage(file="bl.png")
image_label=Label(root, image=arrow_image,width=55, height=50)
image_label.place(x=510, y=150)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

#Left side language slection bar
combo1 = ttk.Combobox(root, values = languageV, font= "Roboto 14", state="r")
combo1.place(x = 110, y = 20)
combo1.set("English")


#Label Under selection Bar
label1 = Label(root, text = "English", font="ComicSansMS 30 bold", bg = "skyblue", width = 18, bd = 5, 
				relief = GROOVE)
label1.place(x=10, y=50)


#Frame to display input language
f = Frame(root, bg= "Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

#adding textbox
text1 = Text(f,font="Robote 20", bg = "white", relief = GROOVE, wrap=WORD)
text1.place(x=0, y=0, width = 430, height= 200)


#adding Scrollbar
scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)



#Right side language selection bar
combo2 = ttk.Combobox(root, values = languageV, font= "Roboto 14", state="r")
combo2.place(x = 730, y = 20)
combo2.set("Select Language")


#Label Under selection Bar
label2 = Label(root, text = "English", font="segoe 30 bold", bg = "skyblue", width = 18, bd = 5, 
				relief = GROOVE)
label2.place(x=620, y=50)


#Frame to display input language
f1= Frame(root, bg= "Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

#adding textbox
text2 = Text(f1,font="Robote 20", bg = "white", relief = GROOVE, wrap=WORD)
text2.place(x=0, y=0, width = 430, height= 200)


#adding Scrollbar
scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#translate button
translate = Button(root,text = "Translate",font = "Roboto 15 bold italic",
					activebackground = "purple", cursor="hand2", bd=5,
					bg="orange",fg="black", command=translate_now)

translate.place(x = 480, y =250)



# calling function
label_change()


root.configure(bg = "lightblue")
root.mainloop()
