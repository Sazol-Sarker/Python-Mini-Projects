from tkinter import * 
import googletrans 
import textblob 
from tkinter import ttk,messagebox 

root=Tk() 
root.title("Language Translator")
root.geometry("1050x400+200+120")


def translate():
    translated_text.delete(1.0,END)
    try:
        for key,value in languages.items():
            if value==original_combo.get():
                from_language_key=key 
        
        for key,value in languages.items():
            if value==translated_combo.get():
                to_language_key=key 

        words=textblob.TextBlob(original_text.get(1.0,END))
        words=words.translate(from_lang=from_language_key,to=to_language_key)
        translated_text.insert(1.0,words)
    except Exception as e:
        messagebox.showerror("Translator",e)


def clear():
    original_text.delete(1.0,END)
    translated_text.delete(1.0,END)


languages=googletrans.LANGUAGES 
language_list=list(languages.values())

#original text lanugage option combo box
original_combo=ttk.Combobox(root,width=50,value=language_list) 
original_combo.current(20)
original_combo.grid(row=0,column=0)

# original_text box
original_text=Text(root,height=10,width=50)
original_text.grid(row=1,column=0,pady=20,padx=10)

#translated text lanugage option combo box
translated_combo=ttk.Combobox(root,width=50,value=language_list)
translated_combo.current(25)
translated_combo.grid(row=0,column=2)

# translated_text box
translated_text=Text(root,height=10,width=50)
translated_text.grid(row=1,column=2,pady=20,padx=10)

#buttons
translate_btn=Button(root,text="Translate",font=("Consolas",22),bg="green",command=translate)
translate_btn.grid(row=0,column=1,pady=20,padx=10)

clear_button=Button(root,text="Clear",font=("Consolas",22),bg="red",command=clear)
clear_button.grid(row=1,column=1,pady=20,padx=10)


root.mainloop()