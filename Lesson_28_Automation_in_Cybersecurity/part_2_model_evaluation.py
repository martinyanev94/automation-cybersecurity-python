from sklearn.metrics import classification_report, confusion_matrix

# Evaluating the model
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
