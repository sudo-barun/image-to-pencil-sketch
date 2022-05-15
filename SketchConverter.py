import cv2
import os


class SketchConverter:
	image = None
	sketch = None

	def __init__(self, file):
		self.file = file

	def convert(self):
		assert os.path.isfile(self.file)
		self.image = image = cv2.imread(self.file)

		gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		inverted_image = 255 - gray_image

		blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
		inverted_blurred = 255 - blurred
		self.sketch = sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

		return sketch
