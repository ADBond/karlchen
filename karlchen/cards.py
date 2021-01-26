from .elements import Element, SVG


class Card(SVG):

    def __init__(self, width=72, height=96, inner_width=54, outer_height=78, outline_thickness=2, design_elements=[]):

        # TODO: sizes
        outer_rectangle = Element(
            "rect", id="outer_rectangle", self_closing=True,
            style="display:inline;fill:#000000;fill-rule:evenodd;stroke-width:0",
            width=58,
            height=82,
            x=7,
            y=7
        )
        inner_colour = "#ff0000"
        inner_rectangle = Element(
            "rect", id="inner_rectangle", self_closing=True,
            style=f"display:inline;fill:{inner_colour};fill-rule:evenodd;stroke-width:0",
            width=54,
            height=78,
            x=9,
            y=9
        )

        outline_grouping = Element(
            "g", id="card_outline", children=[outer_rectangle, inner_rectangle], style="display:inline"
        )

        super().__init__(width=width, height=height, children=[outline_grouping, *design_elements])
