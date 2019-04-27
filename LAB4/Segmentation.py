from sklearn.cluster import KMeans

import glob
import matplotlib.pyplot as plt
from PIL import Image

cv_img = []

for img in glob.glob("images/*.jpg"):
    try:
        print(img)
        x =img[:img.find('.')]
        # print(x)
        pic = plt.imread(img)/255  # dividing by 255 to bring the pixel values between 0 and 1
        print(pic.shape)
        plt.imshow(pic)
        pic_n = pic.reshape(pic.shape[0]*pic.shape[1], pic.shape[2])
        pic_n.shape
        print(pic_n.shape)
        kmeans = KMeans(n_clusters=8, random_state=0).fit(pic_n)
        pic2show = kmeans.cluster_centers_[kmeans.labels_]
        cluster_pic = pic2show.reshape(pic.shape[0], pic.shape[1], pic.shape[2])
        plt.imshow(cluster_pic)
        plt.savefig("convimages/"+x[7:img.find('.')]+".jpg")
    except Exception as e:
        print(e)
        print("exceptional image ------------------"+img[7:])
