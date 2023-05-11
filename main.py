import customtkinter
import lettersRound
import lettersDict

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

letters = []

player_answer = ""
button_order = []

def consonant_button():
    global letters
    letters = lettersRound.generateLetter(letters=letters, choice='C')
    vowel_count = lettersRound.getVowelCount(letters=letters)
    if(len(letters) - vowel_count == 6):
        button_consonant.configure(state="disabled")
    label_letters.configure(text=displayLetters())
    if(len(letters) == 9):
        button_consonant.configure(state="disabled")
        button_vowel.configure(state="disabled")
        app.after(4000, continueRound)


def vowel_button():
    global letters
    letters = lettersRound.generateLetter(letters=letters, choice='V')
    vowel_count = lettersRound.getVowelCount(letters=letters)
    if(vowel_count == 5):
        button_vowel.configure(state="disabled")
    label_letters.configure(text=displayLetters())
    if(len(letters) == 9):
        button_consonant.configure(state="disabled")
        button_vowel.configure(state="disabled")
        app.after(4000, continueRound)
    
def displayLetters():
    text = ""
    global letters
    for letter in letters:
        text += letter + " "
    text.strip()
    return text

def displayAnswer():
    global letters
    print(letters)
    answer = lettersDict.findLongestWord(letters)
    if(answer == None):
        return "No answer sorry"
    else:
        return answer

app = customtkinter.CTk()
app.geometry("1280x720")
app.title("Countdown")

frame_1 = customtkinter.CTkFrame(master=app)

frame_2 = customtkinter.CTkFrame(master=app)

frame_3 = customtkinter.CTkFrame(master=app)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Letters Round")


label_letters = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text=displayLetters())


button_consonant = customtkinter.CTkButton(master=frame_1, text="Consonant", command=consonant_button)

label_player_solution = customtkinter.CTkLabel(master=frame_2, justify=customtkinter.LEFT, text="")

button_vowel = customtkinter.CTkButton(master=frame_1, text="Vowel", command=vowel_button)

label_letters_final = customtkinter.CTkLabel(master=frame_2, justify=customtkinter.LEFT, text=displayLetters())

def button_letter1_pressed():
    global player_answer
    player_answer += letters[0]
    button_order.append(0)
    button_letter1.configure(state="disabled")
    label_player_solution.configure(text=player_answer)

def button_letter2_pressed():
    global player_answer
    player_answer += letters[1]
    button_order.append(1)
    button_letter2.configure(state="disabled")
    label_player_solution.configure(text=player_answer)

def button_letter3_pressed():
    global player_answer
    player_answer += letters[2]
    button_order.append(2)
    button_letter3.configure(state="disabled")
    label_player_solution.configure(text=player_answer)

def button_letter4_pressed():
    global player_answer
    player_answer += letters[3]
    button_order.append(3)
    button_letter4.configure(state="disabled")
    label_player_solution.configure(text=player_answer)

def button_letter5_pressed():
    global player_answer
    player_answer += letters[4]
    button_order.append(4)
    button_letter5.configure(state="disabled")
    label_player_solution.configure(text=player_answer)

def button_letter6_pressed():
    global player_answer
    player_answer += letters[5]
    button_order.append(5)
    button_letter6.configure(state="disabled")
    label_player_solution.configure(text=player_answer)

def button_letter7_pressed():
    global player_answer
    player_answer += letters[6]
    button_order.append(6)
    button_letter7.configure(state="disabled")
    label_player_solution.configure(text=player_answer)

def button_letter8_pressed():
    global player_answer
    player_answer += letters[7]
    button_order.append(7)
    button_letter8.configure(state="disabled")
    label_player_solution.configure(text=player_answer)

def button_letter9_pressed():
    global player_answer
    player_answer += letters[8]
    button_order.append(8)
    button_letter9.configure(state="disabled")
    label_player_solution.configure(text=player_answer)

button_letter1 = customtkinter.CTkButton(master=frame_2, command=button_letter1_pressed)
button_letter2 = customtkinter.CTkButton(master=frame_2, command=button_letter2_pressed)
button_letter3 = customtkinter.CTkButton(master=frame_2, command=button_letter3_pressed)
button_letter4 = customtkinter.CTkButton(master=frame_2, command=button_letter4_pressed)
button_letter5 = customtkinter.CTkButton(master=frame_2, command=button_letter5_pressed)
button_letter6 = customtkinter.CTkButton(master=frame_2, command=button_letter6_pressed)
button_letter7 = customtkinter.CTkButton(master=frame_2, command=button_letter7_pressed)
button_letter8 = customtkinter.CTkButton(master=frame_2, command=button_letter8_pressed)
button_letter9 = customtkinter.CTkButton(master=frame_2, command=button_letter9_pressed)

def endRound():
    frame_2.pack_forget()
    frame_3.pack(pady=20, padx=60, fill="both", expand=True)
    best_answer = lettersDict.findLongestWord(letters)
    if(player_answer != "" and lettersDict.checkWordExists(player_answer)):
        if(len(player_answer) == len(best_answer)):
            print("You get double points! You get " + str(len(player_answer) * 2) + " points!")
        else:
            print("You get " + str(len(player_answer)) + " points!")
            print("A better answer would be " + best_answer)
    else:
        print("No Points")
        print("A better answer would be " + best_answer)
    

button_submit = customtkinter.CTkButton(master=frame_2, command=endRound, text="Submit")

def beginRound():
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)
    label_1.pack(pady=10, padx=10)
    label_letters.pack(pady=10, padx=10)
    button_consonant.pack(pady=10, padx=10)
    button_vowel.pack(pady=10, padx=10)

def continueRound():
    global letters
    frame_1.pack_forget()
    frame_2.pack(pady=20, padx=60, fill="both", expand=True)
    # label_letters_final.configure(text=displayLetters())
    # label_letters_final.pack(pady=10, padx=10)
    label_player_solution.pack(pady=10, padx=10)
    button_letter1.configure(text=letters[0])
    button_letter2.configure(text=letters[1])
    button_letter3.configure(text=letters[2])
    button_letter4.configure(text=letters[3])
    button_letter5.configure(text=letters[4])
    button_letter6.configure(text=letters[5])
    button_letter7.configure(text=letters[6])
    button_letter8.configure(text=letters[7])
    button_letter9.configure(text=letters[8])
    button_letter1.pack()
    button_letter2.pack()
    button_letter3.pack()
    button_letter4.pack()
    button_letter5.pack()
    button_letter6.pack()
    button_letter7.pack()
    button_letter8.pack()
    button_letter9.pack()
    button_submit.pack()
    button_arr = [button_letter1, button_letter2, button_letter3, button_letter4, button_letter5, button_letter6, button_letter7, button_letter8, button_letter9]
    app.after(30000, endRound)



beginRound()

app.mainloop()