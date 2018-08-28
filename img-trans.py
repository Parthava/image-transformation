import cv2
import matplotlib.pyplot as plt
from random import randint
ex='.jpg'
imgname=input("Enter the name and format of the image: ")
im=cv2.imread(imgname)
print("Original image\n")
plt.imshow(im)
plt.show()
im2=im[::-1,:] #invert
im3=im[:,::-1] #flip
rez=[[im[j][i] for j in range (len(im))] for i in range(len(im[0]))] #rotate
print("Enter your option: ")
print("\n1. Invert \n2. Flip \n3. Rotate")
d=int(input("Enter your option: "))
if(d==1):
    plt.imshow(im2)
    plt.show()
    r1=(randint(1, 10000000))
    r2=str(r1)
    path=r2+ex
    cv2.imwrite(path,im2)
    print("The image is successfully saved in your drive")
elif(d==2):
    plt.imshow(im3)
    plt.show()
    r1=(randint(1, 10000000))
    r2=str(r1)
    path=r2+ex
    cv2.imwrite(path,im3)
    print("The image is successfully saved in your drive")
elif(d==3):
    plt.imshow(rez)
    plt.show()
    r1=(randint(1, 10000000))
    r2=str(r1)
    path=r2+ex
    cv2.imwrite(path,rez)
    print("The image is successfully saved in your drive")
else:
    print("Wrong input")