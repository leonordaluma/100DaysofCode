from tkinter import *
THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 14, "italic")
class QuizInterface:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.q_text = self.canvas.create_text(150,125, 
                                         text="Amazon acquired Twitch in August 2014 for $970 million dollars.", 
                                         font=QUESTION_FONT,
                                         width=280)
        self.canvas.grid(row=1, column=0, columnspan=2)
        
        self.score_text = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_text.grid(row=0, column=1)
        
        
        self.window.mainloop()

