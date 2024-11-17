# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

The model is a Random Forest Classifier from scikit learn. It was trained to predict if a person makes above $50,000 per year. [Census data from 1994](https://archive.ics.uci.edu/dataset/20/census+income) was used to train the model.

## Intended Use

The model is intended to predit if a person will earn more above $50,000 per year based on several factors within the census data. This model is intended for academic purposes only.

## Training Data

The model was trained from [1994 Census data](https://archive.ics.uci.edu/dataset/20/census+income). This data contains several variables like: age, workclass, education, marital-status, occupation, and race. This data was split to create training data and test data (80% training, 20% test). These datasets were used to train and evaluate the models performance.

## Evaluation Data

Evalution data is the test data. It is made up of 20 percent of the original dataset. All of the original variables were maintained.

## Metrics

Precision, Recall, and F1 were utilized to measure model performance.

 - Precision: 0.7419
 - Recall: 0.6384
 - F1: 0.6863

 View the full metrics in: slice_output.txt

## Ethical Considerations

As this was extracted from a larger dataset by an individual, there may be bias toward a certain population set.

## Caveats and Recommendations

The data is not current and should not be used to make decisions for today. If updated datasets are provided, the model should be retrained as it is likely there would be more complete data. Using this data for education and practice would be it's best use.