# Approach 1:
# import pack1.module1
# import pack1.module2
#
# pack1.module1.display()
# pack1.module2.show()

# Approach 2: Prefferable

from pack1.module1 import *
from pack1.module2 import *

display()
show()

# Approach 2:

# from pack1 import module1
# from pack1 import module2
# module1.display()
# module2.show()