import tkinter as tk
from pydictionary import Dictionary

window = tk.Tk()
window.title("Dictionary App")

label_word = tk.Label(window, text="Enter a word:")
label_word.grid(row=0, column=0, padx=5, pady=5)

entry_word = tk.Entry(window)
entry_word.grid(row=0, column=1, padx=5, pady=5)

dictionary = Dictionary(entry_word.get())

def search_word():
    word = entry_word.get()
    
    synonyms = dictionary.synonym(word)
    antonyms = dictionary.antonym(word)
    
    if synonyms:
        text_synonyms.delete('1.0', tk.END)
        text_synonyms.insert(tk.END, str(synonyms))
    else:
        text_synonyms.delete('1.0', tk.END)
        text_synonyms.insert(tk.END, "Synonyms not found.")
    if antonyms:
        text_antonyms.delete('1.0', tk.END)
        text_antonyms.insert(tk.END, str(antonyms))
    else:
        text_antonyms.delete('1.0', tk.END)
        text_antonyms.insert(tk.END, "Antonyms not found.")



button_search = tk.Button(window, text="Search", command=search_word)
button_search.grid(row=1, column=0, padx=5, pady=5)



label_synonyms = tk.Label(window, text="Synonyms:")
label_synonyms.grid(row=4, column=0, padx=5, pady=5)

text_synonyms = tk.Text(window, height=2, width=50)
text_synonyms.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

label_antonyms = tk.Label(window, text="Antonyms:")
label_antonyms.grid(row=6, column=0, padx=5, pady=5)

text_antonyms = tk.Text(window, height=2, width=50)
text_antonyms.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()