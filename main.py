import matplotlib.pyplot as plt

plt.axvline(color='g')
xs = list(range(9))
ys = [8-n for n in xs]
decor = set()
for x, y in zip(xs, ys):
    plt.plot([0, -x], [y+1, 0], 'g')
    plt.plot([0, x], [y+1, 0], 'g')
    decor.add((x, 0))
    decor.add((-x, 0))
for x, y in zip(xs[:-2], ys[:-2]):
    plt.plot([0, -x], [y+6, 7], 'g')
    plt.plot([0, x], [y+6, 7], 'g')
    decor.add((x, 7))
    decor.add((-x, 7))
for x, y in zip(xs[:-4], ys[:-4]):
    plt.plot([0, -x], [y+9, 12], 'g')
    plt.plot([0, x], [y+9, 12], 'g')
    decor.add((x, 12))
    decor.add((-x, 12))
for x, y in decor:
    plt.plot(x, y, 'o')
plt.plot(0, 16, 'd', markersize=16)
plt.ylim([-2, 16.8])
plt.axis('off')

plt.savefig('tree.png')
