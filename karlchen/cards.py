from .elements import Element, SVG, BadElementError

class BadCardError(BadElementError):
    pass

class Card(SVG):

    def __init__(self, width=72, height=96, outer_margin=7, outline_thickness=2,
                 outline_colour="#000000", design_base_colour="#ffffff", design_elements=[]):

        self.outer_box_width = width - 2*outer_margin
        self.outer_box_height = height - 2*outer_margin

        self.design_width = self.outer_box_width - 2*outline_thickness
        self.design_height = self.outer_box_height - 2*outline_thickness

        self.design_offset = outer_margin + outline_thickness

        base = Element(
            "rect", id="base", self_closing=True,
            style=f"display:inline;fill:#ffffff;stroke-width:0",
            width=width,
            height=height,
            x=0,
            y=0
        )
        outer_rectangle = Element(
            "rect", id="outer_rectangle", self_closing=True,
            style=f"display:inline;fill:{outline_colour};stroke-width:0",
            width=self.outer_box_width,
            height=self.outer_box_height,
            x=outer_margin,
            y=outer_margin
        )
        inner_rectangle = Element(
            "rect", id="inner_rectangle", self_closing=True,
            style=f"display:inline;fill:{design_base_colour};stroke-width:0",
            width=self.design_width,
            height=self.design_height,
            x=self.design_offset,
            y=self.design_offset
        )

        outline_grouping = Element(
            "g", id="card_outline", children=[base, outer_rectangle, inner_rectangle], style="display:inline"
        )

        super().__init__(width=width, height=height, children=[outline_grouping, *design_elements])
