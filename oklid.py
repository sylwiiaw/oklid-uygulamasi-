import math



# Öklid Mesafesi Fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Noktaların Tanımlanması
points = [(1,3), (3, 4), (5, 6), (7, 8), (9, 10)]

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
min_distance = min(distances)

print("Noktalar arasındaki minimum mesafe:", min_distance)

