
# Performance Management
Pay-HR System comes with a performance management module which allows you to perform periodic performance appraisals for your employees. In order to start making performance appraisals you need to make initial configurations that will allow you to initialize a performance appraisal.

## Performance Configuration
Here is where you can make initial configurations required for your appraisals. To access this section, expand the performance tab and click on 'Configuration' as it appears in the screenshot below;

![Performance-configuration](/performance/performance-configuration.png)


The page consists of different tabs that can be accessed on the left side of your screen as appears in the screenshot above.

### Performance Parameters
These are they key parts of your appraisal process, you need to specify parameters that you will use in your appraisal process a good example would be "Customer Satisfaction" as your performance parameters. To add a parameter simply click the parameter tab in the configuration page and click on the "add parameter" button on teh top right corner of the screen.

![add-performance-parameter](/performance/add-parameter.png)


Once you the parameter is added you can perform actions such as viewing, editing and deleting via the action column of the parameters table

### Key Performance Indicators (KPI)
To add a Key Performance Indicator, simply click on KPI Tab in the configuration tab and select add KPI button at the top right corner. You can create as many KPIs as you wish.

![add-kpi](/performance/add-kpi.png)

### Ratings
Ratings will be used as a measure for the KPIs that you specify, you can add a rating while creating KPIs, on the Add KPI page find the rating field and click on "New Rating". 

![add-kpi](/performance/add-rating.png)

Specify the name and scale then fill in the rating values, text and description.

![new-rating](/performance/new-rating.png)


Once you are through with the configuration you will be ready to initialize your first performance appraisal.

## Creating a new Performance Appraisal
To create a new perfomance appraisal, expand the performance tab in the sidebar menu and click on 'Initialize Appraisal'

![initialize-appraisal](/performance/initialize-appraisal.png)

Once you are done with the first step click 'Proceed'

### Assigning Line Manager
Line managers will be the ones to do the rating for the employees in a specific appraisal. You can set line managers as per your company hierrarchy or you can manually set the line managers

![appraisal-assign-line-managers](/performance/appraisal-line-managers.png)

#### From Organization Hierarrchy
In order for this option to work, you need to specify the reporting relationships through department hierrarchy, visit [Assigning Authority page](/departments/#assigning-authorities-to-departments) for more information

#### Manual Assignment
You also have the option of manually assigning the line managers, simply click on the "Assign line managers to employees" button, select from available line managers then select the employees you would like to assign in the field that appears below the line manager. You can select as many employees as you want. Once you are done with employees selection click 'Add to list' as show below.

![add-to-list-line-managers](/performance/add-to-list-line-managers.png)

A line manager selection will appear in the "Selected Relationships Section". To remove the relationship simply click the red trash can icon besides the relationship

![selected-relationships](/performance/selected-relationships.png)

Once you are done selecting the relationships click "save changes" button to proceed to the next step.

### Assigning KPIs
In this section you can select the KPIs to for each of the employees in the performance appraisal. You have the option of setting the KPIs for all employees or create custom groups and assign KPIs.

![assigning-kpi-to-all-employees](/performance/assigning-kpi-to-all-employees.png)

#### To all employees
To assign KPIs to all employees simply click the "All Employees" button, confirm your selection and check the the KPIs that you would like to assign as shown in the screenshot below. 

![check-kpi-all-employees](/performance/check-kpi-all-employees.png)

#### To customized employee group
With this option you can create groups of employees and assign them the KPIs. Click on "Customized Employee Groups" and confirm your selection. Once the data loads select the employees and click 'Create Group'.

![employee-groups-kpi](/performance/employee-groups-kpi.png)

Repeat the process until all employees are selected. The groups will appear as follows.

![assign-kpi-to-group](/performance/assign-kpi-to-group.png)

Click on Assign KPIs for each group to set the Applicable KPIs.

Once done you can save and initialize the appraisal or save and initialize later

### Initializing Appraisal
When you click on the initialize button the KPIs assignments will be saved and the appraisal will be initialized

#### What happens
Once the appraisal has been initialized notifications will be sent to line managers and employees for them to take actions.


## Allowing Employees to Insert Performance Objectives
Sometimes you may wish to allow all employees to manually insert their performance objectives into the system. To do this, you have to enable to enable the option in your system settings. 

At the sidebar menu collapse the company option and click settings
![screenshot-for-collapsing-setting-option](/performance/screenshot-for-collapsing-setting-option.png)

Click the performance tab
![Screenshot clicking the performance tab](/performance/screenshot-clicking-the-performance-tab.png)
Turn-on the switch labeled “Allow employees to insert their performance objectives”

#### What happens
Once this option in enabled employees will be able to insert their performance objective by logging in to their accounts.

## Employee: How to insert your performance objectives
After logging in to your account, at your dashboard, expand my career option at the sidebar menu and click performance objectives
![screenshot expanding my career option sidebar](/performance/screenshot-expanding-my-career-option-sidebar.png)

Your page will look similar to the screenshot below
![screenshot my career page](/performance/screenshot-my-career-page.png)

Your performance objectives will be categorized based on your job key functional areas. Click on the “New KFA” button to add your first Key functional area
![screenshot of add kfa empty modal](/performance/screenshot-of-add-kfa-empty-modal.png)
Type the name of your KFA e.g. Business Operations, then assign weight to it.

::: tip
The weight of all of your Key Functional Areas (KFAs) must sum up to 100
:::

Add your performance objectives by including their names, weight as well as the target date
![screenshot of adding objectives to kfa](/performance/screenshot-of-adding-objectives-to-kfa.png)

::: tip
The sum of weight of all the objective should equal the weight of the KFA
:::

Click on “Save Changes” button to save your objective

Continue adding KFAs until the reaching the total weight of 100
![screenshot showing the total weight](/performance/screenshot-showing-the-total-weight.png)

Once the insertion of objective is completed your objectives will be sent to your supervisor for approval.

::: tip
You will get a notification once your objectives have been approved
:::

## Supervisor: Approving performance objectives of subordinates
After logging in to your account you will see a notification at the top right corner of your screen regarding the new performance objectives that were inserted. Click review
![screenshot of notification](/performance/screenshot-of-notification.png)

Review and make changes to objectives as you see fit, and once completed click on “Approve Objectives” button. The respective employee will receive a notification regarding the approval.