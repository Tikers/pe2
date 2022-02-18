from sys import path
# if zipped, python can acces files in a zip package
# path.append('D:\\programming\\Python\\pe2\\pe2\\module1\\packages\\extrapack.zip')

path.append('D:\\programming\\Python\\pe2\\pe2\\module1\\packages\\')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())