# Estimation of people's weight
To learn more about how to solve questions in the field of machine learning, we have examined and evaluated a very simple dataset. In this matter, having the height and gender of people, we have to predict their weight.

## Data
Each row of the problem data is related to a person and its characteristics according to the table below.

## Before seeing the code, it is better to know the following things!
- We have used scikit learn, pandas and seaborn libraries to solve this problem. scikit learn was used for modeling, pandas was used for reading and data manipulation, and seaborn was used for illustration.
- In this issue, the information of each person, which includes his height, weight and gender, is considered as an example.
- T's task in this question is to predict people's weight!
- The experience of E in this problem is the information of each person, by seeing which the model can improve the measure of P in doing the task of T.
- The P measure for this question is MAE. MAE or Mean Absolute Error shows the average absolute value of the difference between the actual value and the value predicted by the model.
- MAE
https://quera.ir/qbox/view/ZC4vi6pWhg/mae.JPG
- As mentioned, we are supposed to predict people's weight, and according to the above table, there is a weight column in the dataset. So the weight column of the same label will be considered and it is a supervised learning problem.
- The folder containing the dataset and the notebook file can be accessed from here. Open the file weight_prediction.ipynb to see the solution of the question (code).
