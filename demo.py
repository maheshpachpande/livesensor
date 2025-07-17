from src.sensorClassifier.exception import CustomException
import sys

try:    # Your code logic here
    # s = 10/0
    print(d)
except Exception as e:
    raise CustomException(e, sys)