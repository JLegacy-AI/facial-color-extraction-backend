#import cv2 
#import numpy as np 
#from PIL import Image
#from HairColorDetector import HairColorDetector
from ..hair_color_detector import HairColorDetector


if __name__ == "__main__":
    hair_color_detector = HairColorDetector()
    similarity = hair_color_detector.get_histogram_similarity('blue_medium.jpg','blue_medium.jpg')
    print('Hair Similarity: ', similarity)