# Employees
Pay-R allows you to manage your employees information with ease regardless of the number. You can create new records, update existing records individually or in bulk.

## Adding Employees
You can add a single employee by accessing the add employee page or you can include all your employees in a csv file and import them in bulk.

### Adding Individual Employees
To add a single employee expand the employee menu and click on "Add New", You will then be presented with a set of personal information fields for you to fill.

![Add Employee](/employees/add-employee.png)

Once you compelete filling all the files click the "Add Employee" button and all the information will be stored in the database. You then be presented with an employee
details screen.

#### Issuing employee contract

For an employee to be valid there has to be a valid contract associated with them. Once you complete adding an employee, in the employee data page find and click a green button labeled "Create Contract" at the bottom of the
page. 

![Add Employee](/employees/issue-contract.png)

##### Contract Fields
* **Basic Salary** - Amount before any allowances or deductions
* **Allowances** - Select the allowance you would like to offer to the employee
* **Pay Basis** - Eg. Fixed, Production-Based or Work-time-Based
* **Pay Frequency** - Eg. Monthly, Weekly or Daily
* **Pay Currency** - Uses the currency of a country defined in the company information
* **Leave Quota** - Number of days allowed for leave in a year
* **Start Date** - The date when the contract begins
* **End Date** - The date when the contract Ends
* **Deduct PAYE** - Whether to deduct Pay as you earn from salary or not
* **Deduct Pension** - Whether to deduct Pension Contribution from salary or not
* **Status** - eg active or inactive

Once you complete filling in the above fields click the "Create Contract" Button and the contract will be
issued to that employee and the employee will marked as valid.

### Adding Employees in Bulk
Pay-R supports adding a bulk list of employees. To access this functionality, expand the employees menu
and click Bulk Add.

First download template csv file by clicking the link as highlighted in the screen shoot below

![Add Employee Bulk](/employees/add-employee-bulk-csv-template.png)

Once downloaded the template csv, fill in the details of your employees. You will find a sample row showing the format
for each column of data.

#### Columns in the template csv
* **FirstName** - First Name of the employee (required)
* **MiddleName** - Middle Name of the employee (optional)
* **LastName** - Last Name of the employee (required)
* **Gender** - male or female (required)
* **City** - City where the employee resides (required)
* **Department** - Code of the department the employee will work in (optional)
* **JobTitle** - Professional Title of the employee (required)
* **BasicSalary** - Salary of the employee before any allowances and deductions (required)
* **SSN** - Social Security Number of the employee (optional)
* **JoinDate** - Date of joining the company in format of mm/dd/yyyy (required)   
* **JoinDate** - Date of joining the company in format of mm/dd/yyyy (required)
* **EmploymentType** - Type of employment eg full-time, part-time, internship or probation (required)  
* **Nationality** - (required)  
* **Phone** - (required)  
* **Email** - (optional)  
* **BirthDate** - Date of birth in format mm/dd/yyyy (required)  
* **PayFrequency** - How frequent the salary is paid eg monthly, weekly, hourly, daily (required) 
* **EndDate** - Date of finishing of contract in format mm/dd/yyyy (required)   


Click on the "browse" field and locate the csv file that you filled in your computer then select it and click the "upload"
button.

Pay-R will read the contents of your csv file and populate them on the screen shown in the screenshot below

![Uploaded Employees Bulk](/employees/uploaded-bulk-employees.png)

When you are ready to save the information click on the "Store Records" button and wait for the progress to complete

## Accessing All Employees
To access all your employee, expand the Employees Menu in the side bar and click "All Employees". Your employees will be 
listed as appearing in the screen shot below.

![All Employees](/employees/all-employees.png)

### Viewing Employee Detail
To view employee detail from all employees page, click on the employee you are interested in and their respective data will
load in the Employee Details Section as it appears in the screen shot below

![Employee Details](/employees/employee-details.png)

### Employee Details Sections
When viewing an employee, the details are arranged into clickable sections where you can view specific 
information. Once the employee detail has been loaded you will find tabs representing different sections as shown below

![Employee Details](/employees/employee-sections.png)

* #### Personal info Section
Here you will find personal information of that specific employee including the contract information.

* #### Discipline Section
Disciplinary issues of that specific employees will be located in this section

* #### Leaves Section
This section will display the leave quota of that employee as well as all the leave requests of that employee.

* #### Allowances Section
In this section you will find all the allowances of issued to the employee. You may also activate any allowance in 
this section

* #### Deductions Section
In this section you will find all the deductions to the employee. You may also activate any deduction in 
this section

* #### Documents Section
Any document related to the employee such as cv, ids and others can be viewed in this section

### Deleting Employee
Deleting an employee is easy with Pay-R, the functionality is accessible via all employees page. Click the name
of the employee you would like to delete in the employees list, and once the information is loaded in the employee details 
section, scroll to the bottom of the "Personal Info" tab and locate a red button labelled "Delete Employee".

::: warning
Deleting an employee will also delete any record associated with that particular employee including allowances, payslips, leave data, discipline 
and others. This process is irreversible.
:::
![Delete Employee](/employees/delete-employee.png)