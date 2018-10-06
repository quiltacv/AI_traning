import matplotlib.pyplot as plt
import numpy
a = [0,1,2,3,4]
data = [[1,2],[2,4],[3,6]]
lost = []
def forward(x,y,w):
    return (w*x-y)**2
for i in a:
    sum = 0
    for item in data:
        sum += forward(item[0], item[1], i)
    lost.append(round(sum / len(data),1))
print(lost)
plt.plot(lost)
plt.ylabel("fox x")
plt.ylabel("fox y")
plt.show()
