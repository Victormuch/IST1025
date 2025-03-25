import tkinter as tk
from tkinter import font

#  We create a list of flashcards using lists of tuples
flashcards = [
    # IST1025 (Intro to Programming) Questions
    ("What does 'IDE' stand for in programming?", "Integrated Development Environment"),
    ("What is the main purpose of a compiler?", "To convert source code into machine code"),
    ("Which programming language is often used for web development?", "JavaScript"),
    ("What is a variable in programming?", "A storage location with a name and a value"),
    ("What is an algorithm?", "A step-by-step procedure to solve a problem"),
    
    # Web Design Questions
    ("What does HTML stand for?", "HyperText Markup Language"),
    ("What is the purpose of CSS in web development?", "To style and layout web pages"),
    ("Which tag is used to create a hyperlink in HTML?", "<a> tag"),
    ("What is responsive web design?", "A design approach that makes web pages look good on all devices"),
    ("What does 'SEO' stand for?", "Search Engine Optimization"),
    
    # Fun Questions
    ("What is the largest organ in the human body?", "The skin"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("What is the chemical symbol for gold?", "Au"),
    ("Who developed the theory of relativity?", "Albert Einstein"),
    ("What is the longest river in the world?", "The Nile River"),
]
print(len(flashcards))
#  We create a global variable that track the index of the cards which starts from 0 
current_index = 0
#  We set the default value of flipped to false
flipped = False

# We create the function of the flipping logic 
def flip_card():
    # We create a global variable that tracks of the card shows the answer or the question 
    global flipped
    # We use if statements to check if the card is flipped or not
    if flipped:  
        flipped = False  
    else:
        flipped = True   
        # We update the card regarding to the condition of the card 
    update_card()

# We create the function of the next flash card 
def next_card():
    # We need to modify the current_index and flipped variables that were defined outside this function.
    # current_index Keeps track of which flashcard is currently displayed.
    # Flipped keeps track whether the card is flipped or not
    global current_index, flipped
    # If not at the last card, move to the next one
    if current_index + 1 < len(flashcards):  
        # len() is a built-in function that returns the number of items in a list. For example:
        # if theres a list of tuples ("question", "answer") then len(flashcards) will return the number of tuples in the above its 15
        # If the questions were only in tuples not in both tuples and lists the output would be 30 
         # Move to the next card
        current_index = current_index + 1 
    # Always show the question first
    flipped = False  
    # update the status of the card
    update_card()  
    
# We create a function that moves to the next flash card 
def prev_card():
    # We need to modify the current_index and flipped variables that were defined outside this function.
    # current_index Keeps track of which flashcard is currently displayed.
    # Flipped keeps track whether the card is flipped or not
    global current_index, flipped
    # We use the if condition to check if the current index of the card is grater than 0 and if yes We minus the current index by 1
    if current_index > 0:
        current_index = current_index -1 
         # Always show the question first
        flipped = False
         # update the status of the card
        update_card()

# This is a function that updates the current display of the function 
def update_card():
     # Get the current question-answer pair
    current_card = flashcards[current_index]
    if flipped:
        # Show the answer
        text = current_card[1]  
    else:
        # show text
        text = current_card[0] 
        # card_canvas.itemconfig() Updates the text displayed on the flashcard.
        # card_text is the text object inside the canvas.
    card_canvas.itemconfig(card_text, text=text)


#  From here we now we create the graphical user interface of how the cards will look like
#  using the tkinter lib as tk to shorten the word 
# GUI Setup
root = tk.Tk()
root.title("Flashcards Innt")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Custom font for the card 
card_font = font.Font(family="Times roman ", size=16, weight="bold")

# we Create the Flashcard Frame
card_frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.RIDGE)
card_frame.pack(pady=30, padx=20, fill=tk.BOTH, expand=True)

# We create Flashcard Canvas
card_canvas = tk.Canvas(card_frame, width=400, height=200, bg="white", highlightthickness=2)
card_canvas.pack(pady=20)
card_text = card_canvas.create_text(200, 100, text=flashcards[0][0], font=card_font, width=350)

# We create the Button Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

# We now style the buttons here 
prev_button = tk.Button(button_frame, text="◀ Back", command=prev_card, font=("Arial", 12), bg="#2196F3", fg="white", padx=10, pady=5, relief=tk.GROOVE)
prev_button.grid(row=0, column=0, padx=10)

flip_button = tk.Button(button_frame, text="🔄 Flip", command=flip_card, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5, relief=tk.GROOVE)
flip_button.grid(row=0, column=1, padx=10)

next_button = tk.Button(button_frame, text="Next ▶", command=next_card, font=("Arial", 12), bg="#FF5722", fg="white", padx=10, pady=5, relief=tk.GROOVE)
next_button.grid(row=0, column=2, padx=10)

# Start GUI
root.mainloop()