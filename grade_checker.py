from tkinter import *

# Grade algorithm
def calculate_grade_necessary(current_grade, wanted_grade, final_weight):
        final_weight = final_weight / 100
        weight_of_rest = 1 - final_weight

        current_portion = current_grade * weight_of_rest
        necessary_grade = (wanted_grade - current_portion) / final_weight

        ent_results.delete(0, END)
        ent_results.insert(0, str(round(necessary_grade, 2)))

# Wrapper for button
def calculate_wrapper():
    try:
        current_grade = float(ent_current_grade.get())
        wanted_grade = float(ent_wanted_grade.get())
        final_weight = float(ent_final_weight.get())

        calculate_grade_necessary(current_grade, wanted_grade, final_weight)

    except:
        ent_results.delete(0, END)
        ent_results.insert(0, "Error!")
    

# Intialize window
window = Tk()
window.title("What Grade Do I Need?")
window.minsize(width=200, height=100)


# Current grade
frame_current_grade = Frame(master=window)
frame_current_grade.grid(row=0, column=0, padx=5, pady=5)

lbl_current_grade = Label(master=frame_current_grade, text="Current grade: ")
ent_current_grade = Entry(master=frame_current_grade, width=5)

lbl_current_grade.grid(row=0, column=0)
ent_current_grade.grid(row=0, column=1)


# Desired final class grade
frame_wanted_grade = Frame(master=window)
frame_wanted_grade.grid(row=1, column=0, pady=5)

lbl_wanted_grade = Label(master=frame_wanted_grade, text="Grade wanted: ")
ent_wanted_grade = Entry(master=frame_wanted_grade, width=5)

lbl_wanted_grade.grid(row = 0, column=0)
ent_wanted_grade.grid(row = 0, column=1)


# Weight of final exam
frame_final_weight = Frame(master=window)
frame_final_weight.grid(row=2, column=0, pady=5)

lbl_final_weight = Label(master=frame_final_weight, text="Final weight: ")
ent_final_weight = Entry(master=frame_final_weight, width=5)

lbl_final_weight.grid(row = 0, column=0)
ent_final_weight.grid(row = 0, column=1)


# Submit button
btn_submit = Button(master=window, text="Submit", command=calculate_wrapper)
btn_submit.grid(row=3, column=0)

frame_results = Frame(master=window)
frame_results.grid(row=4, column=0, padx=50)

lbl_results = Label(master=frame_results, text="Grade necessary: ")
ent_results = Entry(master=frame_results, width=5)

lbl_results.grid(row=1, column=0)
ent_results.grid(row=1, column=1, sticky="N", pady=10)

# Start app
window.mainloop()
