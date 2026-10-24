
import json
import sys

MINIMUM_ACCURACY = 0.85

print("Reading model evaluation metrics...")

with open("metrics.json", "r") as file:
    metrics = json.load(file)

accuracy = metrics["accuracy"]

print(f"Model Accuracy : {accuracy:.4f}")
print(f"Required Accuracy: {MINIMUM_ACCURACY:.2f}")

if accuracy >= MINIMUM_ACCURACY:
    print("QUALITY GATE PASSED")
    print("Model performance satisfies the required threshold.")
else:
    print("QUALITY GATE FAILED")
    print("Model performance is below the required threshold.")
    sys.exit(1)
