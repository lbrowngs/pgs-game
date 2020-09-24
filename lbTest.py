import sys
from confidence import confidence
from baking import baking
from produce import produce

name = "Laura"
conf = confidence(name)

#baking
bakedGoods = baking(name, conf)
bakedGoods.bakingAisle()

#produce aisle
produceSection = produce(name, conf)
produceSection.produceAisle()


