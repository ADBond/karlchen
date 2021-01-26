from ..elements import Element
from ..cards import Card, BadCardError


def make_polygon(id_num, colour, points):
    d_value = "M "
    for x, y in points:
        d_value += f"{x},{y} "
    d_value += "Z"
    num_points = len(points)
    poly_name = {
        3: "triangle",
        4: "quad",
    }.get(num_points, f"poly{num_points}")
    return Element(
        "path", fill=colour, stroke="none", d=d_value, id=f"{poly_name}-{id_num}",
        self_closing=True
    )

class HalfDiagonalCard(Card):
    # stripes SW-NE in top/left half
    # colours from TL down to centre
    def __init__(self, colours=["#ff0000"], **kwargs):
        super().__init__(**kwargs)
        num_colours = len(colours)
        if num_colours == 0:
            raise BadCardError("Half-diagonal cards need at least one colour")

        width_break_size = self.design_width/num_colours
        height_break_size = self.design_height/num_colours
    
        def get_coords(indices):
            x_ind, y_ind = indices
            x_val = self.design_offset + x_ind*width_break_size
            y_val = self.design_offset + y_ind*height_break_size
            return x_val, y_val

        # always have the triangle
        triangle_indices = [(0, 0), (1, 0), (0, 1)]
        diagonal_elements = [
            make_polygon(0, colours[0],
            points=list(map(get_coords, triangle_indices)))
        ]

        for idx in range(1, num_colours):
            quad_indices = [(0, idx), (idx, 0), (idx+1, 0), (0, idx+1)]
            diagonal_elements += [
                make_polygon(0, colours[idx],
                points=list(map(get_coords, quad_indices)))
            ]
        
        upper_left_design = Element("g", children=diagonal_elements)
        self.children += [upper_left_design]
