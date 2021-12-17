import os
import cv2
import numpy as np

class Image:
    def __init__(self, path):
        self.path = path
        self.filename = self.path.split('/')[-1]
        self.dir_path = '/'.join(self.path.split('/')[:-1])+'/'+(self.filename).split('.')[0]+'/'
        self.img = cv2.imread(self.path)
        self.create_dir()
        
    def create_dir(self):
        try:
            os.mkdir(self.dir_path)
        except:
            pass
        cv2.imwrite(self.dir_path+'/'+self.filename, self.img)

    
    def median(self):
        median = cv2.medianBlur(np.float32(self.img),5)
        cv2.imwrite(self.dir_path+self.filename.split('.')[0]+"_median."+self.filename.split('.')[-1], median)
    
    def canny_edge(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        canny = cv2.Canny(gray, 30, 100)
        cv2.imwrite(self.dir_path+self.filename.split('.')[0]+"_canny."+self.filename.split('.')[-1], canny)
    
    def blur(self):
        fblur = cv2.blur(self.img, (30,30))
        cv2.imwrite(self.dir_path+self.filename.split('.')[0]+"_blur."+self.filename.split('.')[-1], fblur)
    
    def gaussian(self):
        gaussian = cv2.GaussianBlur(self.img,(5,5),0,0) # kernel size = 5
        cv2.imwrite(self.dir_path+self.filename.split('.')[0]+"_gaussian."+self.filename.split('.')[-1], gaussian)
    
    def grayscale(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(self.dir_path+self.filename.split('.')[0]+"_gray."+self.filename.split('.')[-1], gray)
    