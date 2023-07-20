# Age and Gender Detection

from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

# add image for analysis

img1 = cv2.imread("Enter Image Address")

# Get results

result = DeepFace.analyze(img1, actions=['age', 'gender'])
print(result)
