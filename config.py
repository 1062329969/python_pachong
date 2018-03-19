import re

imgurl = 'https://images.pexels.com/photos/267885/pexels-photo-267885.jpeg'

val = re.search(r'\d\/(.*)\.jpeg', imgurl).group()

print(val)