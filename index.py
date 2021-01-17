import os
import pickle
import cv2
from pyimagesearch.colordescriptor import ColorDescriptor
class Index:
    def __init__(self):
        self.reindex()

    def reindex(self):
        folder = 'africa_fabric'
        data = {}
        descriptor = ColorDescriptor((8, 12, 3))
        print(len(os.listdir(folder)))
        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder, filename))
            data[filename] = [descriptor.describe(img)]
        print(len(data))
        with open('index.pickle', 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)