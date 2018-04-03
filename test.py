import re


imgre = re.findall(r'(.*)/(.*)', 'https://images.pexels.com/photos/416405/pexels-photo-416405.jpeg')
print(imgre[0][1])
