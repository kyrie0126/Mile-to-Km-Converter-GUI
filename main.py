import tkinter as tk

FONT_LABEL = ("arial", 15, "normal")


# setup window
window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


# labels
is_equal_label = tk.Label(text="is equal to", font=FONT_LABEL)
is_equal_label.grid(column=0, row=1)
miles_label = tk.Label(text="Miles", font=FONT_LABEL)
miles_label.grid(column=2, row=0)
km_label = tk.Label(text="Km", font=FONT_LABEL)
km_label.grid(column=2, row=1)
conversion_label = tk.Label(text="0", font=FONT_LABEL)
conversion_label.grid(column=1, row=1)


# mile input
mile_entry = tk.Entry(width=20)
mile_entry.grid(column=1, row=0)


# calculate button
def calc():
    conversion_label.config(text=f"{int(mile_entry.get()) * 1.609}")


calculate_button = tk.Button(text="Calculate", command=calc)
calculate_button.grid(column=1, row=2)


window.mainloop()
