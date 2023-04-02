# from pydictionary import Dictionary
# dict = Dictionary("fix",15)

# meanings_list = dict.meanings()

# synonyms_list = dict.synonyms()

# antonyms_list = dict.antonyms()

# dict.print_meanings()

# dict.print_synonyms()

# dict.print_antonyms()

# dict.print_meanings("red")

# dict.print_synonyms("green")

# dict.print_antonyms("blue")

#module imported
from tkinter import *
from tkinter import messagebox 
from pydictionary import Dictionary 
from googletrans import Translator 

#Idea is: input :english
# output: meaning,synonym,antonym & bangla translated

def meaning():
    dictionary=Dictionary()
    translator=Translator()
    word=txt_input.get()
    d=dictionary.meaning(word)    

    if word=="" or d is None:
        messagebox.showerror('Dictionary','Please enter a valid word')
    else:
        meaning.delete("1.0","end")
        synonyms.delete("1.0","end")
        antonyms.delete("1.0","end")
        bangla.delete("1.0","end")

        meaning.insert('end',d)
        s=dictionary.synonym(word)
        synonyms.insert('end',s)
        a=dictionary.antonym(word)
        antonyms.insert('end',a)
       
        tran=translator.translate(word,dest='tran')
        bangla.insert('end',tran.text)


def refresh():
    meaning.delete("1.0","end")
    synonyms.delete("1.0","end")
    antonyms.delete("1.0","end")
    bangla.delete("1.0","end")
    txt_input.delete(0,"end")


#frame
root=Tk()
root.title("Dictionary App")
root.geometry("990x750+100+0")
root.resizable(False,False)
root.configure(bg="green")


#buttons
lbl_word=Label(root,text="Enter Word",font=("Times New Roman",16,"bold"),bg="green")
txt_input=Entry(root,width=25,bd="2",font="18")
btn_search=Button(root,text='Search',width=6,command=meaning,font=("Times New Roman",16,"bold"))
f1=Frame(root,bg="green")
f1.grid(row=7,column=1)
btn_refresh=Button(f1,text='Refresh',width=6,command=refresh,font=("Times New Roman",16,"bold"))
btn_exit=Button(f1,text='Exit',width=6,command=root.destroy,font=("Times New Roman",16,"bold"))

lbl_means=Label(root,text="Meaning",font=("Verdana",13,'bold'),bg="green",fg="white",width=12)
meaning=Text(root,width=70,height=4,relief=GROOVE,bd=4,font=("Times New Roman",16,"bold"),wrap=WORD)

lbl_syn=Label(root,text="Synonyms",font=("Verdana",13,'bold'),bg="green",fg="white",width=12)
synonyms=Text(root,width=70,height=4,relief=GROOVE,bd=4,font=("Times New Roman",16,"bold"),wrap=WORD)

lbl_ant=Label(root,text="Antonyms",font=("Verdana",13,'bold'),bg="green",fg="white",width=12)
antonyms=Text(root,width=70,height=4,relief=GROOVE,bd=4,font=("Times New Roman",16,"bold"),wrap=WORD)

lbl_bangla=Label(root,text="Bangla",font=("Verdana",13,'bold'),bg="green",fg="white",width=12)
bangla=Text(root,width=70,height=4,relief=GROOVE,bd=4,font=("Times New Roman",16,"bold"))


lbl_word.grid(row=0,column=1,padx=10,pady=10)
txt_input.grid(row=1,column=1,padx=10,pady=10)
btn_search.grid(row=2,column=1,padx=10,pady=10)
lbl_means.grid(row=3,column=0,padx=10,pady=10)
meaning.grid(row=3,column=1,padx=10,pady=10)
lbl_syn.grid(row=4,column=0,padx=10,pady=10)
synonyms.grid(row=4,column=1,padx=10,pady=10)
lbl_ant.grid(row=5,column=0,padx=10,pady=10)
antonyms.grid(row=5,column=1,padx=10,pady=10)
lbl_bangla.grid(row=6,column=0,padx=10,pady=10)
bangla.grid(row=6,column=1,padx=10,pady=10)

btn_refresh.pack(side=LEFT,padx=10,pady=20)
btn_exit.pack(side=LEFT,padx=10,pady=20)

vsb=Scrollbar(root,orient="vertical")

root.mainloop()