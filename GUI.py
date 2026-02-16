import tkinter as tk
from tkinter import Frame, Label, Button, Entry

def main():
    """
    Create the main application window for the Material Property Calculator.

    This function initializes the Tkinter window, sets the window title and
    background color, creates the main frame container, and calls the GUI
    setup function to place all widgets (labels, entries, and buttons).

    Finally, it starts the Tkinter event loop so the window remains open
    and responds to user interaction.
    """
    window = tk.Tk()
    frm_main = Frame(window)
    frm_main.master.title("Material property calculator")
    frm_main.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    window.configure(bg="#e6ffe6")
    
    get_gui(frm_main)
    frm_main.mainloop()

def calculate_stress(force, area):
    """
    This function calculate stress  in  N/m²
    parameters:
      - force
      - area
    Return: stress
    """
    stress = force/area
    return stress

def cal_strain(original_length, final_length):
    """
    This function calculate strain based on material length increment
    
    parameters:
      original_length: Description
      final_length: Description
      Return: strain
    """
    length_change = final_length - original_length
    strain = length_change/original_length
    return strain

def calculate_thermal_expansion(initial_length, coefficient, temperature_change):
    """This function calculate linear thermal expansion of metal 
    parameters:
    initial_length
    coefficient
    temperature change
    Return: change in length"""
    change_in_length = coefficient*initial_length*temperature_change
    return change_in_length

def get_input_and_compute(ent_force, ent_area, ent_original, ent_final,ent_length, ent_alpha, ent_temp, lbl_result):
    """
    Retrieve user input from GUI entry fields, perform material property
    calculations, and display the results.

    This function attempts to calculate:
    - Stress using force and area
    - Strain using original and final length
    - Thermal expansion using length, expansion coefficient, and temperature change

    Each calculation runs only if valid numeric values are entered.
    Results are combined into a formatted output string and displayed
    in the result label. If no valid inputs are provided, an error
    message is shown instead.

    Parameters:
        ent_force (Entry): Input field for force value
        ent_area (Entry): Input field for cross-sectional area
        ent_original (Entry): Input field for original length
        ent_final (Entry): Input field for final length
        ent_length (Entry): Input field for length used in thermal expansion
        ent_alpha (Entry): Input field for thermal expansion coefficient
        ent_temp (Entry): Input field for temperature change
        lbl_result (Label): Label used to display calculation results
    """


    # Create an empty text that will hold the results that is successfully calculated
    text = ""
    # Get stress
    try:
        force = float(ent_force.get())
        area = float(ent_area.get())
        if area != 0:
            stress = calculate_stress(force, area)
            text += f"Stress: {stress:.3f} N/m²\n"

    except ValueError:
        pass

    # Get strain
    try:
        original_length = float(ent_original.get())
        final_length = float(ent_final.get())

        if original_length != 0:
            strain = cal_strain(original_length, final_length)
            text += f"Strain: {strain:.3f}\n"

    except ValueError:
        pass

      # # Get thermal expansion      
    try:
        coefficient = float(ent_alpha.get())
        temperature_change = float(ent_temp.get())
        length = float(ent_length.get())
 
        expansion = calculate_thermal_expansion(length, coefficient, temperature_change)
        
        text += f"Thermal Expansion: {expansion} m"

    except ValueError:
        pass
    
    # Final output
    if text == "":
        lbl_result.config(text="Please enter values to calculate")
    else:
        lbl_result.config(text=text)

    

def get_gui(frm_main):
    """
    Build and arrange all graphical user interface components for the
    Material Property Calculator.

    This function creates:
    - Labels and entry fields for force, area, lengths, expansion coefficient,
      and temperature change
    - Instructional text explaining how to use the calculator
    - A result display label for showing computed values
    - Buttons to calculate results and clear all inputs

    The layout is organized using the grid system and connects user input
    fields to the calculation and clearing functions.

    Parameters:
        frm_main (Frame): The main frame where all GUI widgets are placed
    """


    lbl_force = Label(frm_main, text="(1). Force",fg="blue", font=("Arial", 10))
    lbl_force.grid(row=0, column=0, padx=3, pady=3)
    ent_force = Entry(frm_main,font=("Arial", 10) )
    ent_force.grid(row=0, column=1, padx=3, pady=3)

    lbl_area = Label(frm_main,text="(2). Area (m²)" ,fg="blue", font=("Arial", 10))
    lbl_area.grid(row=1, column=0, padx=3, pady=3)
    ent_area = Entry(frm_main,font=("Arial", 10))
    ent_area.grid(row=1, column=1, padx=3, pady=3)

    # Input and entry of original length
    lbl_original = Label(frm_main, text="(3). Original length (m)",fg="green", font=("Arial", 10))
    lbl_original.grid(row=2, column=0, padx=3, pady=3)
    ent_original = Entry(frm_main,font=("Arial", 10))
    ent_original.grid(row=2, column=1, padx=3, pady=3)

    # input and entry of the final length
    lbl_final = Label(frm_main, text="(4). Final length (m)",fg="green", font=("Arial", 10))
    lbl_final.grid(row=3, column=0, padx=3, pady=3)
    ent_final = Entry(frm_main,font=("Arial", 10))
    ent_final.grid(row=3,column=1, padx=3, pady=3)

    # calculate length
    lbl_length = Label(frm_main, text="(5). Length (m)", fg="red", font=("Arial", 10))
    lbl_length.grid(row=4, column=0)
    ent_length = Entry(frm_main,font=("Arial", 10))
    ent_length.grid(row=4, column=1)

    #Thermal expansion coefficient input and entry
    lbl_alpha = Label(frm_main, text="(6). Expansion coefficient(α):",fg="Red", font=("Arial", 10))
    lbl_alpha.grid(row=5, column=0, padx=3, pady=3)
    ent_alpha = Entry(frm_main,font=("Arial", 10))
    ent_alpha.grid(row=5, column=1, padx=3, pady=3)

    # Temperature change input and entry
    lbl_temp = Label(frm_main, text="(7) Temperature change (°C): ",fg="Red", font=("Arial", 10))
    lbl_temp.grid(row=6, column=0, padx=3, pady=3)
    ent_temp = Entry(frm_main,font=("Arial", 10))
    ent_temp.grid(row=6, column=1, padx=3, pady=3)

    # Instruction on how to use the Calculator
    instruction = Label(frm_main, text="INSTRUCTION TO USE", font=("Arial", 12))
    instruction.grid(row=0, column=2)
    lbl_inst_on_stress_calculation = Label(frm_main, text="1. Enter the value of 1 and 2 to calculate the stress", fg="blue", font=("Arial", 10))
    lbl_inst_on_stress_calculation.grid(row=1, column=2, columnspan=2)

    lbl_inst_on_stress_calculation = Label(frm_main, text="2. Enter the value of 3 and 4 to calculate the strain", fg="blue", font=("Arial", 10))
    lbl_inst_on_stress_calculation.grid(row=2, column=2, columnspan=2)
    
    lbl_inst_on_stress_calculation = Label(frm_main, text="3. Enter the value of 5,6 and 7 to calculate the", fg="blue", font=("Arial", 10))
    lbl_inst_on_stress_calculation.grid(row=3, column=2, columnspan=2)
    lbl_inst_on_stress_calculation = Label(frm_main, text="linear thermal expansion of material", fg="blue", font=("Arial", 10))
    lbl_inst_on_stress_calculation.grid(row=4, column=2, columnspan=2)

    cal_description_heading = Label(frm_main, text="DESCRIPTION", font=("Arial", 10) )
    cal_description_heading.grid(row=6, column=2)
    description = Label(frm_main, text="This material property calculator, calculate three properties of material:")
    description.grid(row=7, column=2)
    description = Label(frm_main, text="(Stress, strain and linear thermal expansion) by using the values of both the ")
    description.grid(row=8, column=2)
    description = Label(frm_main, text="area in meters and force in newton to calculate the stress in Newton per meter  (N/m²)")
    description.grid(row=9, column=2, padx=3, pady=3)
    description = Label(frm_main, text="material strain due to elongation or reduction in length")
    description.grid(row=10, column=2, padx=3, pady=3)
    description = Label(frm_main, text="and finally the linear thermal expansion of metal using the length of the")
    description.grid(row=11, column=2, padx=3, pady=3)
    description = Label(frm_main, text="material, coefficient of linear expansion and change in temperature")
    description.grid(row=12, column=2, padx=3, pady=3)



    # result label calculation
    lbl_result = Label(frm_main,text="", fg="blue", justify="left")
    lbl_result.grid(row=8, column=0, columnspan=2, pady=10)
    
    def calculate_input():
        get_input_and_compute(ent_force, ent_area, ent_original, ent_final,ent_length, ent_alpha, ent_temp,lbl_result)

    # calculate button


    button_cal = Button(frm_main,text="Calculate",command=calculate_input)
    button_cal.grid(row=7, column=0, columnspan=2, pady=5)

    def clear_button():
        clear_field(ent_force, ent_area, ent_original, ent_final, ent_length,ent_alpha, ent_temp, lbl_result)
    button_clear = Button(frm_main, text="Clear", command=clear_button)
    button_clear.grid(row=9, column=0, columnspan=2, pady=5)

def clear_field(ent_force, ent_area, ent_original, ent_final,ent_length, ent_alpha, ent_temp, ent_result):
    """
    Clear all input fields and reset the result display in the
    Material Property Calculator.

    This function removes any user-entered values from:
    - Force entry
    - Area entry
    - Original and final length entries
    - Thermal expansion coefficient entry
    - Temperature change entry

    It also clears the result label so the interface is ready
    for a new calculation.

    Parameters:
        ent_force (Entry): Input field for applied force  
        ent_area (Entry): Input field for cross-sectional area  
        ent_original (Entry): Input field for original length  
        ent_final (Entry): Input field for final length  
        ent_length (Entry): Input field for length used in expansion  
        ent_alpha (Entry): Input field for expansion coefficient  
        ent_temp (Entry): Input field for temperature change  
        ent_result (Label): Label used to display calculation results
    """

    ent_force.delete(0, tk.END)
    ent_area.delete(0,tk.END)
    ent_original.delete(0,tk.END)
    ent_final.delete(0,tk.END)
    ent_alpha.delete(0, tk.END)
    ent_temp.delete(0, tk.END)
    ent_length.delete(0, tk.END)

    ent_result.config(text="")


if __name__ == "__main__":
    main()
