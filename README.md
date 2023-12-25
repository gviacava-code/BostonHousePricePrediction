# Boston House Price Prediction

See complete model selection and analysis [here](https://github.com/giomvp/AcademicProjects/blob/d892ed547535eb5c82f62663fe59492280278b65/BostonHousesPricePrediction/BostonHousePricePrediction.ipynb).

## 1. Problem Statement

Predict house prices in a town or suburb based on the provided features of the locality. Identify the most important features in the dataset to determine the price.

## 2. Data Description

Each record in the database describes a Boston suburb or town. The data was drawn from the Boston Standard Metropolitan Statistical Area (SMSA) in 1970. Detailed attribute information can be found below.

* Number of instances  - 506
* Number of Attributes - 13 (12 inputs, 1 output)

## 3. Modelling Algorithms

Algorithms were selected following scikit-learn algorithm cheat-sheet

  * Ridge regression
  * SVR (linear)
  * SVR (rbf)
  * Xgbregressor
  * Random Forests

* Metric - Since the target variable is a continuous variable, regression evaluation metric RMSE (Root Mean Squared Error) and R2 Score (Coefficient of Determination) have been used.

## 4. Results

**Random forest (rf)** Shows good and consistent performance results as this model explains **84% (r2_score)** of the variability in the price through its independent variables and can make predictions within **~14% (mape)** of the price value on average.

Metrics:

  1. Train data set ->  r2_score: 0.91  |    mse: 7.15   |  rmse: 2.67  |   mae: 2.08 |   mape: 0.11
  2. test data set ->  r2_score: 0.84  |    mse: 13.93  |  rmse: 3.73  |   mae: 2.55 |   mape: 0.14
  3. Cross Validation Accurracy (r2_score): 0.84 (+/- 0.04)

![Summary Charts](https://github.com/giomvp/AcademicProjects/blob/5b36cf9a000eec3c52c64a75badea0b29f95c820/BostonHousesPricePrediction/img/summary_plt.jpg)


