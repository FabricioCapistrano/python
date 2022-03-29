import matplotlib.pyplot as plt

acc = [1-0.5565, 1-0.8582, 1-0.9258, 1-0.9463, 1-0.9572, 1-0.9645, 1-0.9678, 1-0.9704, 1-0.9753, 1-0.9772,
       1-0.9791, 1-0.9803, 1-0.9841]

val_acc=[1-0.9255, 1-0.9812, 1-0.9877, 1-0.9880, 1-0.9886, 1-0.9840, 1-0.9846, 1-0.9920, 1-0.9914, 1-0.9908,
         1-0.9938, 1-0.9908, 1-0.9926]

plt.plot(acc, 'b')
plt.plot(acc, 'b^', label="training")
plt.plot(val_acc, 'g')
plt.plot(val_acc, 'go', label="test")
plt.legend(fontsize=20)
plt.title("Learning curve", fontsize=20)
plt.xlabel("epochs", fontsize=20)
plt.ylabel("error", fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()