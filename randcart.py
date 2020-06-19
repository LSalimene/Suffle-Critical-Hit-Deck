import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random as rdm
#generate a random number
n = rdm.randrange(1,55)
#chose with deck is be used
critic = input("If you roll a critical hit type S, for a critical fumble type F: ")
#suffle the deck using the ramdom number
if (critic=='S'):
  img=mpimg.imread('/s'+str(n)+'.JPG')
  imgplot=plt.imshow(img)
  plt.axis('off')
  plt.show()
elif (critic=="F"):
  img=mpimg.imread('f'+str(n)+'.JPG')
  imgplot=plt.imshow(img)
  plt.axis('off')
  plt.show()
