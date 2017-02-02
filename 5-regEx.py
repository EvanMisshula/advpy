## re

import re

print not re.match("a", "cat"),
print re.search("a", "cat"),
print not re.search("c", "dog"),
print len(re.split("[ab]", "carbs")),
print re.sub("[0-9]", "-", "R2D2")
