from karlchen.elements import Element, SVG
from karlchen.cards import Card
from karlchen.templates.half_diagonal import HalfDiagonalCard

rect = Element(
    "rect", id="rectangle-1", self_closing=True, split_lines=False,
    width="100%", height="100%", fill="red"
)
circle = Element(
    "circle", id="circle-1", self_closing=True, split_lines=False,
    cx="150", cy="100", r="80", fill="green"
)
text = Element(
    "text", id="svg-text", children=["SVG"], split_lines=False,
    # TODO: is this better than using some js-type camel-case solution??
    x="150", y="125", fill="white", **{"font-size": "60", "text-anchor": "middle"}
)
example_svg = SVG(children=[rect, circle, text])
example_svg.to_file("example_generated", sub_folder="generic_svg")

plain_card = Card(design_base_colour="#ff0000")
plain_card.to_file("plain_card", sub_folder="plain_cards")

plain_card_alt_dims = Card(
    width=59, height=92, outer_margin=3,
    outline_thickness=5, design_base_colour="#800080"
)
plain_card_alt_dims.to_file("plain_card_alt_dims", sub_folder="plain_cards")

blue_white_card = HalfDiagonalCard(colours=["#0000ff"])
blue_white_card.to_file("blue_white_diag", sub_folder="diagonals")

calypso_default_design_card = HalfDiagonalCard(
    colours=["#ff00ff", "#ffff00", "#00ff00", "#0000ff", "#ff0000"],
    design_base_colour="#000000"
)
calypso_default_design_card.to_file("calypso_back", sub_folder="diagonals")

very_stripy_card = HalfDiagonalCard(
    colours=[["#ff0000", "#ffffff"][i % 2] for i in range(10)],
    design_base_colour="#ff6666"
)
very_stripy_card.to_file("semi_barbershop", sub_folder="diagonals")
