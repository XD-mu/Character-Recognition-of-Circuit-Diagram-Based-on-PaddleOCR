import cv2 as cv
import os
import numpy as np
from PIL import Image
# # 读入原图片
# path = 'C:/Users/m/Desktop/numpy_testdata/'
# for filename in os.listdir(r'F:/OCR_Project/Final_dense text_dataset/Dense text dataset/crop_img/'):
#     if filename.endswith('jpg') or filename.endswith('png'):
#         img = cv.imread('F:/OCR_Project/Final_dense text_dataset/Dense text dataset/crop_img/'+filename,0)
#         mat = np.array(img)
#         hangshu = mat.shape[0]
#         lieshu = mat.shape[1]
#         mid = np.zeros((int(hangshu / 2)+1, int(lieshu / 2) + 1))
#         a = 0
#         b = 0
#         for i in range(hangshu):
#             if int(i / 2) == i / 2:
#                 b = 0
#                 for j in range(lieshu):
#                     if int(j / 2) == j / 2:
#                         mid[a][b] = mat[i][j]
#                         b = b + 1
#                 a = a + 1
#         mg2 = Image.fromarray(mid)
#         # cv.imwrite(os.path.join(path, filename), mg2)
#         mg2.convert('RGB').save(path+filename,'JPEG')
#         # img.save('/absolute/path/to/myphoto.jpg', 'JPEG')


img = cv.imread('test.jpg',0)
mat = np.array(img)
hangshu = mat.shape[0]
lieshu = mat.shape[1]
mid = np.zeros((int(hangshu / 2)+1, int(lieshu / 2) + 1))
a = 0
b = 0
for i in range(hangshu):
    if int(i / 2) == i / 2:
        b = 0
        for j in range(lieshu):
            if int(j / 2) == j / 2:
                mid[a][b] = mat[i][j]
                b = b + 1
        a = a + 1
mg2 = Image.fromarray(mid)
# cv.imwrite(os.path.join(path, filename), mg2)
mg2.convert('RGB').save('C:/Users/m/Desktop/resize.jpg','JPEG')
# img.save('/absolute/path/to/myphoto.jpg', 'JPEG')



# import cv2
# import numpy as np
# import math
#
# # 加高斯噪声
# def clamp(pv):
#     if pv > 255:
#         return 255
#     if pv < 0:
#         return 0
#     else:
#         return pv
#
# def gaussian_noise(image):
#     h, w, c = image.shape
#     for row in range(h):
#         for col in range(w):
#             s = np.random.normal(0, 25, 3)# 产生随机数，每次产生三个
#             b = image[row, col, 0]   # blue
#             g = image[row, col, 1]   # green
#             r = image[row, col, 2]   # red
#             image[row, col, 0] = clamp(b + s[0])
#             image[row, col, 1] = clamp(g + s[1])
#             image[row, col, 2] = clamp(r + s[2])
#     cv2.imshow("noise_image", image)
#     cv2.imwrite('noise.jpg', image)
#
# src = cv2.imread('test.jpg')
# cv2.imshow('input_image', src)
#
# #高斯模糊
# gaussian_noise(src)
# dst = cv2.GaussianBlur(src, (5,5), 0)
# cv2.imshow("Gaussian_Blur", dst)
# cv2.imwrite('Gaussian_Blur.png', dst)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 最近邻插值法缩放
# 缩放到原来的四分之一
# img_test2 = cv.resize(img, (0, 0), fx=0.25, fy=0.25, interpolation=cv.INTER_NEAREST)
# cv.imshow('resize', img_test2)
# cv.imwrite("resize.jpg",img_test2)
# cv.waitKey()
# cv.destroyAllWindows()

# import cv2
# import numpy as np
#
# img = cv2.imread('test.jpg')
# img = cv2.resize(img,(400,500))
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,gray = cv2.threshold(gray,127,255,0)
# gray2 = gray.copy()
#
# contours, hier = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# for cnt in contours:
#     if 200<cv2.contourArea(cnt)<5000:
#         (x,y,w,h) = cv2.boundingRect(cnt)
#         cv2.rectangle(gray2,(x,y),(x+w,y+h),0,-1)
#
# cv2.imshow('IMG',gray2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

