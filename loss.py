import matplotlib.pyplot as plt
data = [[1,2],[2,4],[3,6]]
lost = []

def forward(x, y, w):
    return (w*x-y)**2
w = 0
def gradient(x, y, w):
    return (2*(x*w-y)*x)

gradients = []
while w <= 4.1:
    sum_loss_w = 0
    sum_gradient = 0
    for item in data:
        sum_loss_w += forward(item[0], item[1], w)
        sum_gradient += gradient(item[0], item[1], w)
    lost.append(sum_loss_w / len(data))
    gradients.append((sum_loss_w / len(data)) / (sum_gradient / len(data)))
    w += 0.1
    # gradients.append(gradient(2, 4, w))

print(gradients)
plt.plot(lost)
plt.plot(gradients)
plt.ylabel("fox x")
plt.ylabel("fox y")
plt.show()
