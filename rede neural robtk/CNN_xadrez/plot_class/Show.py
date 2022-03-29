import matplotlib.pyplot as plt
import cv2
from scipy import misc

img = misc.imread("/Users/renatohidaka/Downloads/03.jpg")
p1 = cv2.resize(img, (250, 350))

img = misc.imread("/Users/renatohidaka/Downloads/02.jpg")
p2 = cv2.resize(img, (250, 350))

img = misc.imread("/Users/renatohidaka/Downloads/01.jpg")
p3 = cv2.resize(img, (250, 350))

img = misc.imread("/Users/renatohidaka/Downloads/06.jpg")
p4 = cv2.resize(img, (250, 350))

img = misc.imread("/Users/renatohidaka/Downloads/05.jpg")
p5 = cv2.resize(img, (250, 350))

img = misc.imread("/Users/renatohidaka/Downloads/04.jpg")
p6 = cv2.resize(img, (250, 350))

fig = plt.figure()

ax1 = fig.add_subplot(331)
ax1.title.set_text('C0: Rei')
plt.imshow(p1)

ax2 = fig.add_subplot(332)
ax2.title.set_text('C1: Rainha')
plt.imshow(p2)

ax3 = fig.add_subplot(333)
ax3.title.set_text('C2: Bispo')
plt.imshow(p3)

ax4 = fig.add_subplot(334)
ax4.title.set_text('C3: Cavalo')
plt.imshow(p4)

ax5 = fig.add_subplot(335)
ax5.title.set_text('C4: Torre')
plt.imshow(p5)

ax6 = fig.add_subplot(336)
ax6.title.set_text('C5: Peão')
plt.imshow(p6)


ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)

ax3.get_xaxis().set_visible(False)
ax3.get_yaxis().set_visible(False)

ax4.get_xaxis().set_visible(False)
ax4.get_yaxis().set_visible(False)

ax5.get_xaxis().set_visible(False)
ax5.get_yaxis().set_visible(False)

ax6.get_xaxis().set_visible(False)
ax6.get_yaxis().set_visible(False)

plt.show()
