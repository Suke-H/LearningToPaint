from glob import glob
import numpy as np
import shutil
import os

SOURCE_PATH = "data/LLD-logo-files/"
MV_PATH = "image/"

imgs = np.array(glob(SOURCE_PATH + "**"))
N = len(imgs)
print(N)

choice = np.random.choice(N, 10)
print(choice)

for img in imgs[choice]:
    # img_name = os.path.basename(img)
    # os.remove(MV_PATH + img_name)
    shutil.copy(img, MV_PATH)