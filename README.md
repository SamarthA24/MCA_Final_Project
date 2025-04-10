## Introduction
<p>
Healthcare industries generate vast volumes of data that contain hidden insights useful for diagnostics and decision-making. This study focuses on developing a Heart Disease Prediction System (HDPS) utilizing Naive Bayes and Decision Tree algorithms to assess the risk of heart disease based on 13 clinical parameters (e.g., age, sex, cholesterol, obesity, etc.). The system also incorporates a multilayer perceptron neural network trained with backpropagation to improve predictive capabilities. The results demonstrate that HDPS can effectively identify patterns and relationships among medical variables, supporting doctors and patients with informed decisions regarding heart health.
</p>


### Objective
<p>
  The primary goal is to implement a Heart Disease Prediction System capable of extracting meaningful insights from historical health data. The system will leverage data mining and machine learning to assist in diagnosing heart conditions, thereby aiding healthcare professionals and enhancing diagnostic accuracy.
</p>

## System Analysis
### Modules:
- **Patient Login:-** *Patient Login to the system using his ID and Password.*
- **Patient Registration:_** *If Patient is a new user he will enter his personal details and he
will user Id and password through which he can login to the system.*
- **My Details:-** *Patient can view his personal details.*
- **Disease Prediction:-** *- Patient will specify the input parameter values. System will take
input values and predict the disease based on the input data values specified by the
patient and system will also suggest doctors based on the locality*
- **Search Doctor:-** *Patient can search for doctor by specifying name, address or type.*
- **Feedback:-** *Patient will give feedback this will be reported to the admin*
- **Doctor Login:-** *Doctor will access the system using his User ID and Password.*
- **Patient Details:-** *Doctor can view patient’s personal details.*
- **Notification:-** *Admin and doctor will get notification how many people had accessed
the system and what all are the diseases predicted by the system.*
- **Admin Login:-** *Admin can login to the system using his ID and Password.*
- **Add Doctor:-** *Admin can add new doctor details into the database.*
- **Add Dataset:-** *Admin can add dataset file in database.*
- **View Doctor:-** *Admin can view various Doctors along with their personal details.*
- **View Disease:-** *Admin can view various diseases details stored in database.*
- **View Patient:-** *Admin can view various patient details that had accessed the system.*
- **View Feedback:-** *Admin can view feedback provided by various users.*
  
## Technology Used

### Languages:
- HTML5
- CSS3
- JavaScript
- Python

### Frameworks:
- Bootstrap
- Django

### Machine Learning Algorithms:
- Gradient Boosting Algorithm
- Logistic Regression

### ML/DL Libraries:
- NumPy
- Pandas
- Scikit-learn

### Database:
- SQLite

### Data Set for Training:
- heart Data 

### IDEs:
- Visual Studio Code

## Run Locally

Clone the project

```bash
  git clone repo link
```

Go to the project directory

```bash
  cd project directory
```

Start the server

```bash
  python manage.py runserver
```