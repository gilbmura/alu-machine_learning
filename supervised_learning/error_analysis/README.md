# Error Analysis

The `error_analysis` directory contains various modules and functions for analyzing the performance of classification models using confusion matrices. This analysis includes calculating metrics such as sensitivity, precision, specificity, and the F1 score.

## Modules

### 1. Create Confusion Matrix

- **File:** `0-create_confusion.py`
- **Function:** `create_confusion_matrix(labels, logits)`
- **Description:** Creates a confusion matrix from the true labels and predicted logits. The confusion matrix is a 2D array where the rows represent the actual classes and the columns represent the predicted classes.

### 2. Sensitivity

- **File:** `1-sensitivity.py`
- **Function:** `sensitivity(confusion)`
- **Description:** Calculates the sensitivity (true positive rate) for each class in a confusion matrix. Sensitivity measures the proportion of actual positives that are correctly identified.

### 3. Precision

- **File:** `2-precision.py`
- **Function:** `precision(confusion)`
- **Description:** Calculates the precision for each class in a confusion matrix. Precision measures the proportion of positive identifications that were actually correct.

### 4. Specificity

- **File:** `3-specificity.py`
- **Function:** `specificity(confusion)`
- **Description:** Calculates the specificity (true negative rate) for each class in a confusion matrix. Specificity measures the proportion of actual negatives that are correctly identified.

### 5. F1 Score

- **File:** `4-f1_score.py`
- **Function:** `f1_score(confusion)`
- **Description:** Computes the F1 score for each class in a confusion matrix. The F1 score is the harmonic mean of precision and sensitivity, providing a balance between the two metrics.

### 6. Error Handling

- **File:** `5-error_handling`
- **Description:** Contains error handling mechanisms for the analysis functions.

### 7. Compare and Contrast

- **File:** `6-compare_and_contrast`
- **Description:** Provides functionality to compare and contrast different error metrics.

## Usage

To use the functions in this directory, you can import them as follows:
