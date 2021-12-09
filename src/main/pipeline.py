from helpers import helpers
from Initialization import Initialization

class Pipeline:
    def __init__(self, img_dir, K_file):
        self.h = helpers()
        self.images = self.h.loadImages(img_dir)
        self.K = self.h.load_poses(K_file)
    
    def run(self):
        initialise_vo = Initialization(self.images[0], self.images[2], self.K)
        keypoints, landmarks, R, T = initialise_vo.run()
        print(keypoints, landmarks, R, T)
