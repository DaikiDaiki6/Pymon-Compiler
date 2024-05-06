from PIL import ImageTk
from customtkinter import *
import PIL
import Lexer as lex
import Syntax
import Semantic
from tkinter import *

def centerLoginReg(wid, heig):
    x = y = 0
    width = wid  # Width
    height = heig  # Height

    screenWidth = root.winfo_screenwidth()  # ScreenWidth
    screenHeight = root.winfo_screenheight()  # ScreenHeight

    # Calculation
    x = (screenWidth / 2) - (width / 2)
    y = (screenHeight / 2) - (height / 2)

    return x, y

def functionForlexicalAnalyzer():
    lexeme.configure(state="normal")
    lexemeToken.configure(state="normal")
    errorTextBox.configure(state="normal")
    lexeme.delete("0.0", "end")
    lexemeToken.delete("0.0", "end")
    errorTextBox.delete("0.0", "end")
    lexicalAnalyzer()
    if not lexer.tokensForUnknown:
        errorTextBox.insert(END, "LEXICAL COMPILE SUCCESSFUL\n")
        buttonForSyntax.configure(state="normal")
def update_line_numbers(event=None):
    line_numbers.configure(state=NORMAL)
    line_numbers.delete(1.0, END)
    lines = programEntry.get("1.0", END).splitlines()
    for i, _ in enumerate(lines, start=1):
        line_numbers.insert(END, f"{i}\n")
    line_numbers.configure(state=DISABLED)

    fraction = programEntry.yview()[0]
    line_numbers.yview_moveto(fraction)

def block_tab(event):
    if event.keysym == 'Tab':
        programEntry.insert(INSERT, '    ')  # Insert four spaces
        return 'break'

def syncScrollLexemeAndTokens(*args):
    lexeme.yview(*args)
    lexemeToken.yview(*args)

def lexemesAndTokens():
    global lexeme
    global lexemeToken
    global errorTextBox

    lexemeAndTokensFrame = CTkFrame(root, width=388, height=790, border_width=2, border_color="black", fg_color="#997B4A")
    lexemeAndTokensFrame.place(x=995, y=120)

    scrollbarLexemeToken = Scrollbar(lexemeAndTokensFrame, width=20, bg="#51642A", troughcolor="#51642A",
                                     activebackground="#51642A",
                                     highlightcolor="#51642A")
    scrollbarLexemeToken.pack(side=RIGHT, fill=Y)

    lexeme = CTkTextbox(lexemeAndTokensFrame, width=198.0, height=740.0, font=("Courier New", 15, "bold"), text_color="Black",
                        fg_color="#D8B57E", border_width=1, border_color="Black", yscrollcommand=scrollbarLexemeToken.set, activate_scrollbars=False)
    lexeme.pack(side=LEFT, fill=Y)

    lexemeToken = CTkTextbox(lexemeAndTokensFrame, width=182.0, height=740.0, font=("Courier New", 15, "bold"), text_color="Black",
                             fg_color="#D8B57E", border_width=1, border_color="Black", yscrollcommand=scrollbarLexemeToken.set, activate_scrollbars=False)
    lexemeToken.pack(side=LEFT, fill=BOTH)



    errorTextBox = CTkTextbox(root, width=923.0, height=190.0, font=("Courier New", 15, "bold"), text_color="Black",
                            fg_color="#D8B57E", border_width=1, border_color="Black")
    errorTextBox.place(x=20, y=670)
    scrollbarLexemeToken.config(command=syncScrollLexemeAndTokens, bg="#51642A")


def enteringLexemeAndTokens():
    counter = lenCounter = 0
    newLineCounter = 0
    for element in lexer.tokens:
        counter += 1
        if element[0] == ":":
            token, lexemeValue = ":", ":"
        else:
            token, lexemeValue = element.split(":", 1)  # flag in case something goes wrong
        token = token.strip()
        lexemeValue = lexemeValue.strip()
        lexeme.insert(END, str(counter) + ". " + lexemeValue + "\n")
        lexemeToken.insert(END, str(counter) + ". " + token + "\n")
        if token == "STARLIT" or lexemeValue == "\n":
            for c in token:
                lenCounter += 1
                if lenCounter >= 18 and newLineCounter == 0:
                    newLineCounter += 1
                    lenCounter = 0
                elif lenCounter >= 21 and newLineCounter >= 1:
                    newLineCounter += 1
                    lenCounter = 0
            while True:
                if newLineCounter == 0:
                    break
                lexeme.insert(END, "\n")
                newLineCounter -= 1
            lenCounter = 0
            newLineCounter = 0
            lexeme.insert(END,'-------------------' + "\n")
            for c in lexemeValue:
                lenCounter += 1
                if lenCounter >= 18 and newLineCounter == 0:
                    newLineCounter += 1
                    lenCounter = 0
                elif lenCounter >= 21 and newLineCounter >= 1:
                    newLineCounter += 1
                    lenCounter = 0
            while newLineCounter > 0:
                lexemeToken.insert(END, "\n")
                newLineCounter -= 1
            lexemeToken.insert(END,'------------------' + "\n")
            newLineCounter = 0
        else:
            lexemeToken.insert(END, '------------------' + "\n")
            lexeme.insert(END, '-------------------' + "\n")
    lexeme.configure(state="disabled")
    lexemeToken.configure(state="disabled")

    return lexer.tokens


def enteringErrors():
    errorTextBox.delete("1.0", END)

    for element in lexer.tokensForUnknown:
        parts = element.split(":",2)
        print(element, parts)
        if len(parts) >= 3: # Nice niceee, nakalimutan ko yan
            lineNumber, token, lexemeValue, = element.split(":",2)
            errorTextBox.insert(END, lineNumber + " " + token + " " + lexemeValue + "\n")

    scrollbarError = Scrollbar(root, command=errorTextBox.yview, width=20, bg="gray", troughcolor="#51642A",
                               activebackground="#51642A", highlightcolor="#51642A")
    scrollbarError.place(x=930, y=670, height=190)

    errorTextBox.configure(yscrollcommand=scrollbarError.set)

    return lexer.tokensForUnknown

    errorTextBox.configure(state="disabled")

def lexicalAnalyzer():
    global lexer
    global LexemeTokens
    global ErrorTokens
    try:
        program = programEntry.get("0.0", "end-1c")
        lexer = lex.Lexer(program)
        print("Token type: Token Value")
        lexer.getNextTokens()
        print(lexer.tokens)
        print(lexer.tokensForUnknown)
        LexemeTokens = enteringLexemeAndTokens()
        ErrorTokens = enteringErrors()
        if not lexer.tokensForUnknown:
            buttonForSyntax.configure(state="normal")
        else:
            buttonForSyntax.configure(state="disabled")
    except:
        print("An error occurred. Refer to our documentation for better understanding")

def enteringErrorsOfSyntax(syntaxErrors):
    errorTextBox.delete("1.0", END)

    if syntaxErrors[0] == "SYNTAX COMPILE SUCCESSFUL":
        errorTextBox.insert(END, syntaxErrors[0])
    else:
        errorTextBox.insert(END, syntaxErrors[0])

def syntaxAnalyzer():
    syntax_analyzer = Syntax.Syn(LexemeTokens)
    syntax_analyzer.ListToDict()
    syntax_analyzer.GetNextTerminal()
    syntaxErrors = syntax_analyzer.SyntaxErrors
    enteringErrorsOfSyntax(syntaxErrors)
    if syntaxErrors[0] == '               SYNTAX COMPILE SUCCESSFUL\n-------------------------------------------------------------\n\n':
        semanticAnalyzer(syntax_analyzer.Terminals, syntax_analyzer.SemanticSequence)
def EnteringOutputSemantic(output, errorfound):
    for d in output:
        errorTextBox.insert(END, str(d))
    if errorfound == 0:
        errorTextBox.insert(END, "\n\n-------------------------------------------------------------\nSemantic Compile Successful...")
    else:
        errorTextBox.insert(END,"\n\n-------------------------------------------------------------\nError\s found during the Semantic Compilation...")

def inputter(desc):
    top = Toplevel()  # Create a new window for input
    top.title("Input")
    Label(top, text=desc, font=("Helvetica", 14), anchor='w', justify='left').pack(pady=10) # Display the description with a larger font
    entry = Entry(top, font=("Helvetica", 12), width=40)  # Entry widget for user input with larger font and width
    entry.pack(padx=20, pady=10)  # Add padding to the Entry widget
    entry.focus_set()  # Set focus to the Entry widget
    value = None

    def submit():
        nonlocal value
        value = str(entry.get()).replace("_", "-")  # Get the value from the Entry widget
        top.destroy()  # Close the input window

    Button(top, text="Submit", command=submit, font=("Helvetica", 12), padx=20, pady=5).pack()  # Button to submit the input with larger font and padding
    top.wait_window()  # Wait for the input window to be closed
    try:
        if value in [True, False]:
            pass
        elif type(eval(value)) == int:
            pass
        elif type(eval(value)) == float:
            pass
    except:
        value = "\"" + value + "\""
    return value

def semanticAnalyzer(Terminals, Sequence):
    sem = Semantic.Sem(Terminals, Sequence)
    sem.keyval_fix()
    sem.token_type()
    output = sem.Output
    errorfound = 0
    for item in output:
        try:
            if '|||Semantic Error' in item:
                output = [item.replace("|||", "")]
                errorfound = 1
                break
        except:
            pass
    print(output)
    EnteringOutputSemantic(output, errorfound)

def multiple_yview(*args):
	line_numbers.yview(*args)
	programEntry.yview(*args)

def mainScreen():
    global root
    global programEntry
    global line_numbers
    global text_widget
    global buttonForSyntax

    root = CTk()
    w = 1400
    h = 900
    root.resizable(False, False)
    x, y = centerLoginReg(w, h)
    root.geometry('%dx%d+%d+%d' % (w, h, x , y ))
    root.title("Pymon")
    root.configure(fg_color="#997B4A")

    icon = PhotoImage(file="imagesUsed/icon.png")
    icon = ImageTk.PhotoImage(file=os.path.join("imagesUsed", "icon.png"))
    root.wm_iconbitmap()
    root.iconphoto(False, icon)

    path = "imagesUsed/background.png"
    bgImage = CTkImage(light_image=PIL.Image.open(path),
                            size=(1400, 1000))
    image_label = CTkLabel(root, image=bgImage, text="")
    image_label.pack()

    path1 = "imagesUsed/title.png"
    titleImage = CTkImage(light_image=PIL.Image.open(path1),
                        size=(380, 70))
    title_label = CTkLabel(root, image=titleImage, text="")
    title_label.place(x=995, y=30)


    errorTitle = CTkTextbox(root,fg_color="#51642A",
                          width=100,
                          height=33,
                          text_color="white",
                          font=("Courier new", 16, "bold"),
                          border_width=1,
                          border_color="Black")
    errorTitle.place(x=32, y=625)
    errorTitle.insert(END, " Output")

    codeTitle = CTkTextbox(root,fg_color="#51642A",
                          width=100,
                          height=33,
                          text_color="white",
                          font=("Courier new", 16, "bold"),
                          border_width=1,
                          border_color="Black")
    codeTitle.place(x=32, y=120)
    codeTitle.insert(END, "  Code:  ")
    codeTitle.configure(state="disabled")



    promptFrame = CTkFrame(root, width=923, height=490, border_width=2, border_color="black", fg_color="#997B4A")
    promptFrame.place(x=20, y=170)

    scrollbar = Scrollbar(promptFrame, command=multiple_yview, width=20, bg="gray", troughcolor="#51642A", activebackground="#51642A", highlightcolor="#51642A")
    scrollbar.pack(side=RIGHT, fill=Y)
    line_numbers = CTkTextbox(promptFrame, width=50, height=430, pady=2, border_width=2, border_color="black", wrap=NONE,   spacing3=5, state="disabled", fg_color="#51642A",
                           text_color="black", font=("Courier New", 20), yscrollcommand=scrollbar.set, activate_scrollbars=False)
    line_numbers.pack(side=LEFT, fill=Y)

    programEntry = CTkTextbox(promptFrame, width=860, height=0, pady=2, font=("Courier New", 20),  spacing3=5,
                             text_color="Black", fg_color="#D8B57E", border_width=2, border_color="black", yscrollcommand=scrollbar.set, wrap="none" )
    programEntry.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=multiple_yview)


    buttonForLexical = CTkButton(root, command=functionForlexicalAnalyzer,
                               text="Lexical",
                               text_color="Black",
                               font=("Courier new", 20, "bold"),
                               border_width=1,
                               border_color="Black",
                               width=100,
                               height=60,
                               corner_radius=10,
                               fg_color="#51642A", hover_color="#CB9D55")
    buttonForLexical.place(x=50, y=30)

    buttonForSyntax = CTkButton(root, command=syntaxAnalyzer,
                                 text="Syntax & Semantic",
                                 text_color="Black",
                                 font=("Courier new", 20, "bold"),
                                 border_width=1,
                                 border_color="Black",
                                 width=120,
                                 height=60,
                                 corner_radius=10,
                                 state="disabled",#
                                 fg_color="#51642A", hover_color="#CB9D55")
    buttonForSyntax.place(x=200, y=30)

    lexemesAndTokens()
    programEntry.bind("<Key>", update_line_numbers)
    programEntry.bind("<MouseWheel>", lambda event: update_line_numbers(event))
    programEntry.bind("<Tab>", block_tab)
    image_label.pack()

    update_line_numbers()  # Call the function to initialize line numbers
    root.mainloop()

if __name__ == "__main__":
    mainScreen()