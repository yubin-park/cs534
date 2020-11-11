
roster = ["Howard, Sagar, Sean (3)",
    "Uriel, Xinman (2)",
    "Yiheng, Lindsey, Jialu (3)",
    "Yuxuan, Ye (2)",
    "Wesley, Dylanger (2)",
    "Courtney, Randy (2)",
    "Richa, Fiona, Arabind (3)",
    "Pranav (1)",
    "Soonyoung (1)",
    "Ragip (1)",
    "Shuaicheng (1)",
    "Sonny, Guangji, Ran (3)"]

import random

random.shuffle(roster)
for i, team in enumerate(roster):
    print("{}. {}".format(i, team))
