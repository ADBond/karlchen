from karlchen.elements import Element, SVG
from karlchen.cards import Card
from karlchen.suits import Heart

heart_svg = Heart()
heart_svg.to_file("hearts", sub_folder="suits")
