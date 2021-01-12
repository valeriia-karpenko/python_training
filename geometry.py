from geom2d.point import Point

l1 = [Point(0, 0), Point(3, 1), Point(1, 2)]

l2 = sorted(l1, key=lambda p: p.x)

l3 = sorted(l1, key=lambda p: p.distance(Point(0, 0)))

print(l1)
print(l2)
print(l3)

# l = [Point(i, i * i) for i in range(-5, 6)]
l = list(map(lambda i: Point(i, i * i), range(-5, 6)))

# for i in range(-5, 6):
#     l.append(Point(i, i * i))
# print(l)
#
# for el in l:
#     print(el)
#
# for el in l:
#     el.y = -el.y

print(l)

l2 =[Point(el.x, -el.y) for el in l]
l2 = list(filter(lambda p: p.x % 2 == 0, l))
#
# for el in l:
#     l2.append(Point(el.x, -el.y))
print(l2)
