import tkinter as tk
import DataBase
import time
import tkinter.font as TkFont
import Viewimage

##created by vlad

class ViewFrame():
    db = DataBase.Database()
    
    def __init__(self, down_frame):
        self.root = down_frame
        self.root.rowconfigure(0, weight = 1)
        self.root.columnconfigure(0, weight = 1)
        
        self.view_frame = tk.Frame(down_frame, bg = "green")
        self.view_frame.grid(row = 0,sticky=tk.S+tk.E+tk.W+tk.N)
        self.view_frame.rowconfigure(0, weight = 0)
        self.view_frame.rowconfigure(1, weight = 1)
        self.view_frame.columnconfigure(0, weight = 1)
        self.view_frame.columnconfigure(1, weight = 1)
        
        self.time_label = tk.Label(self.root, text='time')
        self.time_label.grid(row=2, column=0, sticky=tk.E+tk.S, padx=0, pady=0)

        photo_image=tk.PhotoImage(file ='windows_gif.gif')
        self.photo_image = photo_image.subsample(15, 14)

        start_button=tk.Button(self.root, image = self.photo_image, bd=0)
        start_button.grid(row=2, column=0, sticky=tk.W)
              
        self.create_lf()
        self.create_rf()
        self.create_bf()
        self.updatetime() 

    def create_lf(self):
        self.left_frame = tk.Frame(self.view_frame, bg ='grey')
        self.left_frame.grid(row = 0, column = 0,sticky=tk.E+tk.W+tk.N)
        self.left_frame.rowconfigure(0, weight = 1)
        self.left_frame.columnconfigure(0, weight = 1)

        name_label = tk.Label(self.left_frame, text='Add Название', bg='grey')
        name_label.grid(row=0, column=0, sticky=tk.N, padx=5, pady=5)
        self.name_entry = tk.Entry(self.left_frame)
        self.name_entry.grid(row=0, column =1, sticky=tk.N, padx=5, pady=5)
        
        genre1_label = tk.Label(self.left_frame, text='Add Жанр-1', bg='grey')
        genre1_label.grid(row=1, column =0,sticky=tk.N, padx=5, pady=5)
        self.genre1_entry=tk.Entry(self.left_frame)
        self.genre1_entry.grid(row=1, column =1,sticky=tk.N, padx=5, pady=5)

        genre2_label = tk.Label(self.left_frame, text='Add Жанр-2', bg='grey')
        genre2_label.grid(row=2, column =0,sticky=tk.N, padx=5, pady=5)
        self.genre2_entry=tk.Entry(self.left_frame)
        self.genre2_entry.grid(row=2, column=1,sticky=tk.N, padx=5, pady=5)

        self.add_year_label = tk.Label(self.left_frame, text='Add Год', bg='grey')
        self.add_year_label.grid(row=3, column=0,sticky=tk.N, padx=5, pady=5)
        self.add_year_entry=tk.Entry(self.left_frame)
        self.add_year_entry.grid(row=3, column=1,sticky=tk.N, padx=5, pady=5)

        append_button = tk.Button(self.left_frame, text ='Добавить',borderwidth = 5)
        append_button.grid(row = 4, column = 0, padx = 20, pady=20, ipady=10,
                           ipadx=15)

        remove_button = tk.Button(self.left_frame, text ='Удалить',borderwidth = 5)
        remove_button.grid(row = 4, column = 1, padx = 20, pady=20, ipady=10,
                           ipadx=15)
    
        remove_button.bind('<Button-1>', self.remove)
        append_button.bind('<Button-1>', self.dobavit)

    def updatetime(self):
        self.time_label.config(text=time.strftime('%X'))
        self.root.after(1000, self.updatetime)

    def remove(self, event):
        name = self.name_entry.get()
        year = self.add_year_entry.get()

        self.db.delete(name, year)
    
    def dobavit(self, event):
        name = self.name_entry.get()
        genre1 = self.genre1_entry.get()
        genre2 = self.genre2_entry.get()
        year = self.add_year_entry.get()
        
        self.db.append(name, genre1, genre2, year)
          
    def create_rf(self):
        self.right_frame = tk.Frame(self.view_frame, bg = 'white')
        self.right_frame.grid(row=0, column= 1, sticky=tk.E+tk.W+tk.N)
        self.right_frame.rowconfigure(0, weight = 1)
        self.right_frame.columnconfigure(0, weight = 1)

        right_label = tk.Label(self.right_frame, text='Жанр-1', bg='white')
        right_label.grid(row=0, column =0, sticky=tk.N, padx=5, pady=5)
        self.right_entry=tk.Entry(self.right_frame)
        self.right_entry.grid(row=0, column =1, sticky=tk.N, padx=5, pady=5)
        
        right1_label = tk.Label(self.right_frame, text='Жанр-2', bg='white')
        right1_label.grid(row=1, column =0, sticky=tk.N, padx=5, pady=5)       
        self.right1_entry=tk.Entry(self.right_frame)
        self.right1_entry.grid(row=1, column=1, sticky=tk.N, padx=5, pady=5)

        self.from_year_label=tk.Label(self.right_frame, text='Год от', bg='white')
        self.from_year_label.grid(row=2, column=0, sticky=tk.N, padx=5, pady=5)
        self.from_year_entry=tk.Entry(self.right_frame)
        self.from_year_entry.grid(row=2, column=1, sticky=tk.N, padx=5, pady=5)

        self.to_year_label = tk.Label(self.right_frame, text='Год до', bg='white')
        self.to_year_label.grid(row=3, column=0, sticky=tk.N, padx=5, pady=5)
        self.to_year_entry=tk.Entry(self.right_frame)
        self.to_year_entry.grid(row=3, column=1, sticky=tk.N, padx=5, pady=5)

        find_button = tk.Button(self.right_frame, text ='Поиск',borderwidth = 5)
        find_button.grid(row = 4, column = 0, padx = 20, pady=20, ipady=10,
                           ipadx=15)
        find_button.bind('<Button-1>', self.find)

        shutdown_image=tk.PhotoImage(file ='poweroff.png')
        self.shutdown_image = shutdown_image.subsample(11, 11)

        shutdown_button=tk.Button(self.right_frame, image = self.shutdown_image, bd=0,
                                  highlightthickness=0)
        shutdown_button.grid(row=4, column=1, padx = 20, pady=20)
        
    def create_bf(self):
        bottom_frame = tk.Frame(self.view_frame, bg = 'white', bd= 0)
        bottom_frame.grid(row=1, column= 0,columnspan=2, sticky=tk.S+tk.E+tk.W+tk.N)
        bottom_frame.rowconfigure(0, weight = 1)
        bottom_frame.columnconfigure(0, weight = 1)

        scroll_bar = tk.Scrollbar(bottom_frame, orient=tk.VERTICAL)
        scroll_bar.grid(row=0,column=1,sticky=tk.S+tk.N)

        self.text_font = TkFont.Font(family = 'Comic Sans MS', size=16)
        self.answer = tk.Listbox(bottom_frame, yscrollcommand = scroll_bar.set,
                                 font = self.text_font)
        self.answer.grid(row=0,column=0, sticky=tk.S+tk.E+tk.W+tk.N)
        scroll_bar.config(command=self.answer.yview)
        
        self.answer.bind('<<ListboxSelect>>', self.openwindow)

    def openwindow(self,event):
        index = event.widget.curselection()[0]
        film = event.widget.get(index).split()
        year = film[-1]
        film_name = ' '.join(film[1:-3])
        view_image = Viewimage.ViewImage(film_name, year)
        
    def find(self, event):
        genre1 = self.right_entry.get()
        genre2 = self.right1_entry.get()
        yearot = self.from_year_entry.get()
        yeardo = self.to_year_entry.get()

        result = self.db.poisk(genre1, genre2, yearot, yeardo)

        self.botframe(result)
        
    def botframe(self, result):
        self.answer.delete(0, tk.END)
        count = 1
        for i in result:
            self.answer.insert(tk.END, f"{count} {' '.join(str(el) for el in i)}")
            count+=1


root = tk.Tk()
root.title("App 1.2.0 release")
var = ViewFrame(root)
root.mainloop()
        
