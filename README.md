# Team-Niner-Inc
Capstone Project for Fullstack Academy Cybersecurity Bootcamp (Fettuccine)

## Summary
Broken Access Control has been ranked as the number one OWASP Top 10 security risk and the goal of this project is to reduce unauthorized access to information. We created a python script that uses a GUI to gather information about an employee and generate a summary of accesses granted based off the department and scope of their job. The File Integrity Monitor or FIM uses powershell to monitor the employee access files generated and alerts when changes have been made to the file.

### Python
This project starts with the python script [AccessCtrl.pyw](https://github.com/njnelso/Team-Niner-Inc/blob/main/AccessCtrl.pyw)

Using PySimpleGUI, we built a GUI with User Inputs and dropdown menus to fill out an employee's information. The extension .pyw allows the script to run from the desktop without needing a console. Simply double click to open the GUI.

![alt text](https://github.com/njnelso/Team-Niner-Inc/blob/main/Pic1.png?raw=true)

Example of a form filled out

![alt text](https://github.com/njnelso/Team-Niner-Inc/blob/main/Pic2.png?raw=true)

### The Process
After you submit, several things are happening here. First, the employee ID number is being stored as a variable that will be manipulated in several ways. The output of this script will produce a text file that is saved under the employee ID number. A Username for the new account is also using the first initial followed by the employee ID number. Lastly, the Temporary Password is being set using 10 randomized string of characters made up of both lowercase and uppercase letters, followed by the last three numbers of the employee ID number.

The other inputs are being called in a series of 'If' statements to determine the level of access each employee gets, both physical and electronically. This prevents unauthorized access between different departments, as well as employees with no supervisory/managerial responsibilities from accessing files outside of their job scope. The following Access Summary will show the result of an example employee's accesses:

![alt text](https://github.com/njnelso/Team-Niner-Inc/blob/main/Pic5.png?raw=true)

### Text Output
The title of the text file is determined based off what the last two dropdown menu items are set to. If this is a new employee, 'Grant Access' will be listed at the top. If there is an internal change in position or promotion, the new job might include new access granted based off job scope. Finally, 'Revoke Access' is listed if the employee is terminated. In this case, the employee summary section will be the only thing listed, while the accesses are removed in the process.

You can specify the filepath in the final section of the python script where it outputs the text file. You could set a shared drive for the team that performs Onboarding/Employee Indoc or whatever your process is called.
