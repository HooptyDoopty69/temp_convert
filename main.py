import tkinter as tk
import ttkbootstrap as ttk
import functools as fun


#############
# CONSTANTS #
#############

WIDTH = 600
HEIGHT = 300
NAME = "Temperature Converter"
PARAG = "Calibri 16"
HEADING = "Calibri"
H1 = "24"
H2 = "20"


#############
# FUNCTIONS #
#############


def create_app():
    instance = ttk.Window(themename='simplex')
    instance.title(NAME)
    instance.geometry(f"{WIDTH}x{HEIGHT}")
    instance.minsize(width=WIDTH, height=HEIGHT)
    return instance


def create_title(parent):
    title_label = tk.Label(
        master=parent,
        text=NAME,
        font=f"{HEADING} {H1}"
    )
    return title_label


def switch_conversion_method(method, all_methods, output_value, input_value):
    output_value.set("")
    input_value.set("")

    if method.get() == all_methods[0]:
        method.set(all_methods[1])
    elif method.get() == all_methods[1]:
        method.set(all_methods[0])


def convert_to_fahrenheit(val):
    return (val * 1.8) + 32


def convert_to_celsius(val):
    return ((val - 32) * 5) / 9


def run_conversion(method, all_methods, input_value, output):
    try:
        if method.get() == all_methods[0]:
            value = convert_to_fahrenheit(float(input_value.get()))

            original_value = float(input_value.get())
            original_rounded = "{:.2f}".format(round(original_value, 2))
            fahren_rounded = "{:.2f} °F".format(round(value, 2))

            output.set(f"{original_rounded} °C = {fahren_rounded}")

        elif method.get() == all_methods[1]:
            value = convert_to_celsius(float(input_value.get()))

            original_value = float(input_value.get())
            original_rounded = "{:.2f}".format(round(original_value, 2))
            celsius_rounded = "{:.2f} °C".format(round(value, 2))

            output.set(f"{original_rounded} °F = {celsius_rounded}")

    except:
        output.set("Oh man, I didn't think of that")


def main():
    app = create_app()
    title = create_title(app)

    conversion_methods = ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
    current_method = tk.StringVar()
    current_method.set(conversion_methods[0])

    value_to_convert = tk.StringVar()
    converted_value = tk.StringVar()

    # Method Toggle
    mt_frame = tk.Frame(master=app)
    mt_label = tk.Label(
        master=mt_frame,
        text="[DEFAULT METHOD]",
        font=PARAG,
        textvariable=current_method
    )
    mt_button = tk.Button(
        master=mt_frame,
        text="Switch Conversion Method",
        font=PARAG,
        command=fun.partial(
            switch_conversion_method,
            current_method,
            conversion_methods,
            converted_value,
            value_to_convert
        )
    )

    #####################
    # TAKING USER INPUT #
    #####################

    cv_frame = tk.Frame(master=app)
    cv_entry = tk.Entry(
        master=cv_frame,
        font=PARAG,
        textvariable=value_to_convert
    )
    cv_button = tk.Button(
        master=cv_frame,
        text="Convert",
        font=PARAG,
        command=fun.partial(
            run_conversion,
            current_method,
            conversion_methods,
            value_to_convert,
            converted_value
        )
    )

    ####################
    # OUTPUT RENDERING #
    ####################

    or_frame = tk.Frame(master=app)
    or_label = tk.Label(
        master=or_frame,
        font=f"{HEADING} {H2}",
        textvariable=converted_value
    )

    ###########
    # PACKING #
    ###########

    title.pack()

    mt_frame.pack(fill='x', padx=50, pady=25)
    mt_label.pack(side='left')
    mt_button.pack(side='right')

    cv_frame.pack(fill='x', padx=50, pady=25)
    cv_entry.pack(side='left')
    cv_button.pack(side='right')

    or_frame.pack()
    or_label.pack()

    app.mainloop()


#############
# MAIN LOOP #
#############


if __name__ == "__main__":
    main()
