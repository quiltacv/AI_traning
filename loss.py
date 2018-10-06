import matplotlib.pyplot as plt
data = [[1,2],[2,4],[3,6]]
lost = []

def forward(x,y,w):
    return (w*x-y)**2
w = 0

while w < 4:
    sum_loss_w = 0
    for item in data:
        sum_loss_w += forward(item[0], item[1], w)
    lost.append(sum_loss_w / len(data))
    w += 0.1
print(lost)
plt.plot(lost)
plt.ylabel("fox x")
plt.ylabel("fox y")
plt.show()
