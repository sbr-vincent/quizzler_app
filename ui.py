from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self. quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text="Some Question Text",
                                                fill=THEME_COLOR, font=("Ariel", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        green_image = PhotoImage(file="./images/true.png")
        self.green_button = Button(image=green_image, highlightthickness=0, command=self.answer_true)
        self.green_button.grid(column=0, row=2)

        red_image = PhotoImage(file="./images/false.png")
        self.red_button = Button(image=red_image, highlightthickness=0, command=self.answer_false)
        self.red_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz")
            self.green_button.config(state="disabled")
            self.red_button.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")

        self.window.after(1000, self.get_next_question)


