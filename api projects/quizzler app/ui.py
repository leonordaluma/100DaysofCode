from tkinter import *
THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "Italic")
class QuizInterface:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        
        self.score_text = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_text.grid(row=0, column=1)
        
        
        self.window.mainloop()

