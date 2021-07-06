from tkinter import *


def mile_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=50, pady=50)

miles_input = Entry(width=7, font=("Arial", 20))
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 20))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 20))
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0",font=("Arial", 20))
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km", font=("Arial", 20))
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", font=("Arial", 20), command=mile_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
