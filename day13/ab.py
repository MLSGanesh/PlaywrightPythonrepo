# # Approach 1:
#
# import a
# import b
#
# aobj=a.Animal()
# aobj.display()
#
# bobj=b.Bird()
# bobj.display()


# Approach 2:
# from a import Animal
# from b import Bird

from a import *
from b import *

aobj=Animal()
aobj.display()

bobj=Bird()
bobj.display()