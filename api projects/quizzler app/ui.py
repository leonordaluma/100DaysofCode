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
                                         fill=THEME_COLOR,
                                         width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        self.score_text = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_text.grid(row=0, column=1, padx=50)
        
        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")
        
        self.true_button = Button(true_image, highlightthickness=0, bg=THEME_COLOR)
        self.true_button.grid(row=2, column=0)
        
        self.false_button = Button(false_image, highlightthickness=0, bg=THEME_COLOR)
        self.false_button.grid(row=2, column=1)
        
        
        self.window.mainloop()

