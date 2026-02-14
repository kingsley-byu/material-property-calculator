import tkinter as tk
from tkinter import Frame, Label, Button, Entry

def main():
    window = tk.Tk()
    frm_main = Frame(window)
    frm_main.master.title("Material property calculator")
    frm_main.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    window.configure(bg="#e6ffe6")
    
    get_gui(frm_main)
    frm_main.mainloop()

def calculate_stress(force, area):
    stress = force/area
    return stress

def cal_strain(original_length, final_length):
    length_change = final_length - original_length
    strain = length_change/original_length
    return strain

def calculate_thermal_expansion(initial_length, coefficient, temperature_change):
    change_in_length = coefficient*initial_length*temperature_change
    return change_in_length

def get_input_and_compute(ent_force, ent_area, ent_original, ent_final,ent_length, ent_alpha, ent_temp, lbl_result):
    # Create an empty text that will hold the results that is successfully calculated
    text = ""
    # Get stress
    try:
        force = float(ent_force.get())
        area = float(ent_area.get())
        if area != 0:
            stress = calculate_stress(force, area)
            text += f"Stress: {stress:.3f} N\n"
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
    lbl_inst_on_stress_calculation = Label(frm_main, text=" the linear thermal expansion of material", fg="blue", font=("Arial", 10))
    lbl_inst_on_stress_calculation.grid(row=4, column=2, columnspan=2)

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
