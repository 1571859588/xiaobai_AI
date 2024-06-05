import dataset as dataset
from matplotlib import pyplot as plt

## Create a dataset
n=100
xs,ys=dataset.get_beans(n)
plt.title('Size-Toxicity Function',fontsize=12)
plt.xlabel('Bean Size',fontsize=12)
plt.ylabel('Toxicity')
plt.scatter(xs,ys)


## Roseblatt
w=0.5
alpha=0.05
for _ in range(100):
    for i in range(n):
        x=xs[i]
        y=ys[i]
        y_pre=w*x
        e=y-y_pre
        w=w+alpha*e*xs

## Visualization
y_pre=w*xs
plt.scatter(xs,ys)
plt.plot(xs,y_pre,'r')
plt.show()
