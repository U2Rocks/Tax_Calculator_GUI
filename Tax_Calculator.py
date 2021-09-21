import tkinter as tk
from Tax_Info import tax_dict
from Initial_Converter import converter
import re


def remove_start_menu():  # function that removes start menu items
    start_large_title.destroy()
    start_label.destroy()
    state_options.destroy()
    start_button.destroy()


def load_tax_calculation_screen():  # main function that starts application
    def tab_counter(number):  # function that manage tab statuses
        global income_tax
        global property_tax
        if number == 0:  # initiate tab statuses
            income_tax = True
            property_tax = False
        if number == 1:  # switch from income to property tax
            income_tax = False
            property_tax = True
        if number == 2:  # switch from property to income tax
            income_tax = True
            property_tax = False

    def check_if_tab_loaded(tax_type):  # check which tab is loaded
        if tax_type == 'income_tax':
            return income_tax
        if tax_type == 'property_tax':
            return property_tax

    def load_tax_tabs():  # create two tabs to switch between windows
        income_tax_tab = tk.Button(
            root, text="Income Tax Calculator", font="Helvetica 14", command=income_tax_tab_onclick)
        property_tax_tab = tk.Button(
            root, text="Property Tax Calculator", font="Helvetica 14", command=property_tax_tab_onlick)
        income_tax_tab.grid(row=0, column=0, padx=10, pady=10)
        property_tax_tab.grid(row=0, column=1, padx=10, pady=10)

    def load_income_tax_screen():  # load income tax screen
        # create income tax screen elements
        global income_tax_title
        global income_tax_input
        global income_tax_calculation_button
        global income_tax_explain_label
        global income_tax_calculation_box
        income_tax_title = tk.Label(
            root, text="2021 Income Tax Calculator", font="Helvetica 18")
        income_tax_input = tk.Entry(
            root, text="Enter your 2021 Annual Income", font="Helvetica 14")
        income_tax_calculation_button = tk.Button(
            root, text="Calculate", font="Helvetica 14", command=lambda: calculate_tax('income'))
        income_tax_explain_label = tk.Label(
            root, text="Your Tax Payment will be:", font="Helvetica 14")
        income_tax_calculation_box = tk.Label(
            root, text="N/A", font="Helvetica 14")
        # place income tax screen elements
        income_tax_title.grid(row=1, column=0, columnspan=3, pady=20)
        income_tax_input.grid(row=2, column=0, pady=10, columnspan=3)
        income_tax_calculation_button.grid(
            row=3, column=0, pady=10, columnspan=3)
        income_tax_explain_label.grid(row=4, column=0, pady=10, columnspan=3)
        income_tax_calculation_box.grid(row=5, column=0, pady=10, columnspan=3)

    def load_property_tax_screen():  # load property tax screen
        # create property tax screen elements
        global property_tax_title
        global property_tax_input
        global property_tax_calculation_button
        global property_tax_explain_label
        global property_tax_calculation_box
        property_tax_title = tk.Label(
            root, text="2021 Property Tax Calculator", font="Helvetica 18")
        property_tax_input = tk.Entry(
            root, text="Enter your Property Value", font="Helvetica 14")
        property_tax_calculation_button = tk.Button(
            root, text="Calculate", font="Helvetica 14", command=lambda: calculate_tax('property'))
        property_tax_explain_label = tk.Label(
            root, text="Your Tax Payment will be:", font="Helvetica 14")
        property_tax_calculation_box = tk.Label(
            root, text="N/A", font="Helvetica 14")
        # place property tax screen elements
        property_tax_title.grid(row=1, column=0, columnspan=3, pady=20)
        property_tax_input.grid(row=2, column=0, columnspan=3, pady=10)
        property_tax_calculation_button.grid(
            row=3, column=0, columnspan=3, pady=10)
        property_tax_explain_label.grid(row=4, column=0, columnspan=3, pady=10)
        property_tax_calculation_box.grid(
            row=5, column=0, columnspan=3, pady=10)

    def calculate_tax(type):  # function to calculate income tax
        try:  # try statement prevents error when not select a state
            calculation_state = selected_state  # get selected state for bracket searching
        except NameError:
            calculation_state = select_state[0]
        converted_calc_state = converter(calculation_state)  # convert inital
        if type == "income":  # check what type of tax we have to calculate
            # get tax rate from dictionary and make a float
            tax_rate = float(tax_dict[converted_calc_state]['income'])
            # get text input from box and make a float
            input_num = get_text_input('income')
            if check_for_improper_input(input_num) == 'no matches':  # sanitize input
                return
            float_input_num = float(input_num)
            # calculate tax total and make into string for later
            calculated_tax = str(tax_rate * float_input_num)
            # change appropriate calculation box with new tax number
            update_calculation_box('income', calculated_tax)
        if type == "property":
            tax_rate = float(tax_dict[converted_calc_state]['property'])
            input_num = get_text_input('property')
            if check_for_improper_input(input_num) == 'no matches':  # sanitize input
                return
            float_input_num = float(input_num)
            calculated_tax = str(tax_rate * float_input_num)
            update_calculation_box('property', calculated_tax)

    def remove_income_tax_screen():  # remove income tax screen
        income_tax_title.grid_remove()
        income_tax_input.grid_remove()
        income_tax_calculation_button.grid_remove()
        income_tax_explain_label.grid_remove()
        income_tax_calculation_box.grid_remove()

    def remove_property_tax_screen():  # remove property tax screen
        property_tax_title.grid_remove()
        property_tax_input.grid_remove()
        property_tax_calculation_button.grid_remove()
        property_tax_explain_label.grid_remove()
        property_tax_calculation_box.grid_remove()

    def switch_to_property_tax():  # change interface to property tax from income tax
        remove_income_tax_screen()
        load_property_tax_screen()

    def swtich_to_income_tax():  # change interface to income tax from property tax
        remove_property_tax_screen()
        load_income_tax_screen()

    def income_tax_tab_onclick():
        income_tax_status = check_if_tab_loaded('income_tax')
        if income_tax_status == True:
            return
        tab_counter(2)
        swtich_to_income_tax()
        income_tax_input.delete(0, 'end')
        income_tax_input.insert(0, 'Enter your Annual Income')

    def property_tax_tab_onlick():
        property_tax_status = check_if_tab_loaded('property_tax')
        if property_tax_status == True:
            return
        tab_counter(1)
        switch_to_property_tax()
        property_tax_input.delete(0, 'end')
        property_tax_input.insert(0, 'Enter your Property Value')

    def get_text_input(type):  # function that gets value from correct entry box
        if type == "income":
            num_value = income_tax_input.get()
            return num_value
        if type == "property":
            num_value = property_tax_input.get()
            return num_value

    # function that changes label text
    def update_calculation_box(type, newtext):
        if type == "income":
            income_tax_calculation_box.config(text=newtext)
        if type == "property":
            property_tax_calculation_box.config(text=newtext)

    def check_for_improper_input(input_text):
        number_match = re.compile(r'[0-9]+')
        match_finds = re.findall(number_match, input_text)
        if not match_finds:
            return 'no matches'

    remove_start_menu()  # remove old GUI
    tab_counter(0)  # start tab counter with income tax on
    load_tax_tabs()  # load tax tabs onto window
    load_income_tax_screen()  # load initial income tax screen
    # put initial text into input box
    income_tax_input.insert(0, 'Enter your Annual Income')


# create root
root = tk.Tk()
root.title("Tax Calculator")
root.geometry("460x360")
root.minsize(460, 360)
root.maxsize(460, 360)
root.config(bg="#35bda2")

# create list of states and var for select box
global select_state
state_value = tk.StringVar(root)
select_state = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN',
                'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
state_value.set(select_state[0])


# function that updates selection choice for state(ADD CASE HANDLING FOR NO SELECT CLICK)
# def create_selected_state():
#    global selected_state
#    selected_state = select_state[0]


def change_state(choice):
    global selected_state
    choice = state_value.get()
    selected_state = choice


# initialize components for start screen
start_label = tk.Label(root, text="Choose a US State", font="Helvetica 14")
state_options = tk.OptionMenu(
    root, state_value, *select_state, command=change_state)
state_options.config(width=15)
start_large_title = tk.Label(
    root, text="Income and Property Tax Calculation App", font="Helvetica 18")
start_button = tk.Button(root, text="Select State",
                         font="Helvetica 11", command=load_tax_calculation_screen)


# place components onto start screen
start_large_title.grid(row=0, column=0, columnspan=3, pady=20)
start_label.grid(row=1, column=1, pady=10)
state_options.grid(row=2, column=1, pady=10)
start_button.grid(row=3, column=1, pady=10)


# start root mainloop and start necessary variables
# create_selected_state()  # create variable incase no state is selected
root.mainloop()
