import PySimpleGUI as sg
import random
import string

# GUI Color/Theme
sg.theme('Dark2')	

layout = [
	[sg.Text('Please enter your Info Below:')],
	[sg.Text('Employee ID', size =(15, 1)), sg.InputText()],
	[sg.Text('Full Name', size =(15, 1)), sg.InputText()],
	[sg.Text('Contractor',size=(15, 1), font='Lucida',justification='left')],
    [sg.Combo(['Yes','No'],key='con')],
    [sg.Text('Employee Level',size=(15, 1), font='Lucida',justification='left')],
    [sg.Combo(['Non-Employee','Employee','Supervisor', 'Manager','Executive'],key='lev')],
	[sg.Text('Department',size=(15, 1), font='Lucida',justification='left')],
    [sg.Combo(['Supply','Human Resources','Information Technology', 'Executive'],key='dep')],
	[sg.Text('Remote Job',size=(15, 1), font='Lucida',justification='left')],
    [sg.Combo(['Yes','No'],key='rem')],
    [sg.Text('Transfer, Change of Job, or Promotion',size=(30, 1), font='Lucida',justification='left')],
    [sg.Combo(['Yes','No'],key='tra')],
	[sg.Text('Revoke Access',size=(15, 1), font='Lucida',justification='left')],
    [sg.Combo(['Yes','No'],key='rev')],
	[sg.Submit('Submit'), sg.Cancel('Exit')]
]
# GUI Behavior
window = sg.Window('Employee Access Form', layout, no_titlebar=True, grab_anywhere=True)
event, values = window.read()
window.close()

# Variables to be used later
access_var = ""
id_number = values[0]
con_var = ""
lev_var = ""
dir_var = ""
rem_var = ""
last_three = values[0][-3::] # Last 3 numbers of the employee ID

# Title and type of access request
if values['rev'] == "Yes":
    access_var = "Revoke Access"
elif values['tra'] == "Yes":
    access_var = "Change Access"
else:
    access_var = "Grant Access"

# Contractor
if values['con'] == "Yes":
    con_var = "Access Category: Restricted"

elif values['con'] == "No":
    con_var = "Access Category: Normal"

# Employee Level
if values['lev'] == "Non-Employee":
    lev_var = "Physical Access: Escort Required"

# File Directory Access
if values['dep'] == "Human Resources":
      
    if values['lev'] == "Employee":
        dir_var = "File Directory Access: /HR/SectionA/Employee Data"
        lev_var = "Physical Access: Common Areas, HR Department"

    elif values['lev'] == "Supervisor":
        dir_var = "File Directory Access: /HR/SectionA"
        lev_var = "Physical Access: Common Areas, HR Department, Supervised Section"

    elif values['lev'] == "Manager":
        dir_var = "File Directory Access: /HR/"
        lev_var = "Physical Access: Common Areas, Department-Wide"

elif values['dep'] == "Supply":

    if values['lev'] == "Employee":
        dir_var = "File Directory Access: /Supply/Team1/Invoices"
        lev_var = "Physical Access: Common Areas, Supply Department"

    elif values['lev'] == "Supervisor":
        dir_var = "File Directory Access: /Supply/Team1"
        lev_var = "Physical Access: Common Areas, Supply Department, Supervised Section"

    elif values['lev'] == "Manager":
        dir_var = "File Directory Access: /Supply/"
        lev_var = "Physical Access: Common Areas, Department-Wide"

elif values['dep'] == "Information Technology":
      
    if values['lev'] == "Employee":
        dir_var = "File Directory Access: /IT/ITadmin/Help Tickets"
        lev_var = "Physical Access: Common Areas, IT Department"

    elif values['lev'] == "Supervisor":
        dir_var = "File Directory Access: /IT/ITadmin"
        lev_var = "Physical Access: Common Areas, IT Department, Supervised Section"

    elif values['lev'] == "Manager":
        dir_var = "File Directory Access: /IT/"
        lev_var = "Physical Access: Common Areas, Department-Wide"

elif values['dep'] == "Executive":
    dir_var = "File Directory Access: /"
    lev_var = "Physical Access: All Departments"

# VPN Access required for remote employees
if values['rem'] == "Yes":
    rem_var = "VPN Access Required: Yes"

elif values['rem'] == "No":
    rem_var = "VPN Access Required: No"
    
# Random Password Generator
letters = string.ascii_letters
x = ''.join(random.choice(letters) for i in range(10)) 

# File Output for new/change in access
if access_var == "Grant Access" or access_var == "Change Access":
    with open("C:/Users/nicho/OneDrive/Documents/Access Ctrl/"+id_number+'.txt', 'w') as f:
        f.write(access_var + '\n' + '--------------------------------------------------------' + '\n' +
            "Employee Summary:" + '\n' + '\n' +
            "Employee ID: " + values[0] + '\n' +
            "Full Name: " + values[1] + '\n' +
            "Contractor: " + values['con'] + '\n' +    
            "Employee Level: " + values['lev'] + '\n' +
            "Department: " + values['dep'] + '\n' +
            "Remote: " + values['rem'] + '\n' +
            "Lateral Transfer, Change of Position, or Promotion: " + values['tra'] + '\n' +
            "Revoke Access: " + values['rev'] + '\n' +'\n' +
            '--------------------------------------------------------' + '\n' +
            "Access Summary:" + '\n' + '\n' +
            con_var + '\n' + 
            lev_var + '\n' +
            dir_var + '\n' +
            rem_var + '\n' +
            '--------------------------------------------------------' + '\n' +
            "Login Credentials:" + '\n' + '\n' +
            'Username: ' + values[1][:1:]+values[0] + '\n' +
            'Temporary Password: ' + x+last_three)

# File output for removing accesses        
elif access_var == "Revoke Access":
    with open("C:/Users/nicho/OneDrive/Documents/Access Ctrl/"+id_number+'.txt', 'w') as f:
        f.write(access_var + '\n' + '--------------------------------------------------------' + '\n' +
            "Employee ID: " + values[0] + '\n' +
            "Full Name: " + values[1] + '\n' +
            "Contractor: " + values['con'] + '\n' +    
            "Employee Level: " + values['lev'] + '\n' +
            "Department: " + values['dep'] + '\n' +
            "Remote: " + values['rem'] + '\n' +
            "Lateral Transfer, Change of Position, or Promotion: " + values['tra'] + '\n' +
            "Revoke Access: " + values['rev'])