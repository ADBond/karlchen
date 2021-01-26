from .elements import Element, SVG


class Card(SVG):

    def __init__(self, width=72, height=96, outer_margin=7, outline_thickness=2,
                 outline_colour="#000000", design_base_colour="#ffffff", design_elements=[]):

        outer_rectangle = Element(
            "rect", id="outer_rectangle", self_closing=True,
            style=f"display:inline;fill:{outline_colour};fill-rule:evenodd;stroke-width:0",
            width=width - 2*outer_margin,
            height=height - 2*outer_margin,
            x=outer_margin,
            y=outer_margin
        )
        inner_rectangle = Element(
            "rect", id="inner_rectangle", self_closing=True,
            style=f"display:inline;fill:{design_base_colour};fill-rule:evenodd;stroke-width:0",
            width=width - 2*outer_margin - 2*outline_thickness,
            height=height - 2*outer_margin - 2*outline_thickness,
            x=outer_margin + outline_thickness,
            y=outer_margin + outline_thickness
        )

        outline_grouping = Element(
            "g", id="card_outline", children=[outer_rectangle, inner_rectangle], style="display:inline"
        )

        super().__init__(width=width, height=height, children=[outline_grouping, *design_elements])
