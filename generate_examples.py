from karlchen.elements import Element, SVG
from karlchen.cards import Card

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
example_svg.to_file("example_generated")

plain_card = Card(design_base_colour="#ff0000")
plain_card.to_file("plain_card")

plain_card_alt_dims = Card(
    width=59, height=92, outer_margin=3,
    outline_thickness=5, design_base_colour="#800080"
)
plain_card_alt_dims.to_file("plain_card_alt_dims")
