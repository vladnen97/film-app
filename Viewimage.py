import tkinter as tk
import tkinter.font as TkFont
import KinopoiskAPI
from PIL import ImageTk, Image
from io import BytesIO



class ViewImage():
    def __init__(self, name, year):
        root = tk.Tk()
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.title(f'{name}, {year}  v1.5')
        
        self.main_frame = tk.Frame(root, bg='white')
        self.main_frame.grid(row=0, column=0, padx=0, pady=0, sticky=tk.S+tk.E+tk.W+tk.N)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0,weight=1)
        try:
            kinopoisk = KinopoiskAPI.KinopoiskAPI(name, year)
            
            image_open= Image.open(BytesIO(kinopoisk.get_image()))
            image_open= image_open.resize([x//2 for x in image_open.size])                   
            self.img= ImageTk.PhotoImage(image_open, master=root)
            self.canvas=tk.Label(self.main_frame,image=self.img)
            self.canvas.grid(row=0, column=0)

            self.film_font = TkFont.Font(root=root,family = 'Comic Sans MS', size=16)
            description_message = tk.Message(self.main_frame,text=kinopoisk.get_description()
                                             ,justify=tk.LEFT,aspect=150,highlightthickness=0,bg='white')
            description_message.config(font = self.film_font)
            description_message.grid(row=0,column=1)

        except:
            root.geometry("500x200")
            self.error_label=tk.Label(self.main_frame, text='Фильм не найден.')
            self.error_label.grid(row=0, column=0)

        root.mainloop()
            
        
        
        
        
        

        
        


