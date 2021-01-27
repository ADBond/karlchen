from ..elements import Element
from ..cards import Card, BadCardError
from ..shapes import Polygon


# TODO: combine commonalities, then implement directionalities when patterns a little clearer
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
            Polygon(0, colours[0],
            points=list(map(get_coords, triangle_indices)))
        ]

        for idx in range(1, num_colours):
            quad_indices = [(0, idx), (idx, 0), (idx+1, 0), (0, idx+1)]
            diagonal_elements += [
                Polygon(idx, colours[idx],
                points=list(map(get_coords, quad_indices)))
            ]
        
        upper_left_design = Element("g", children=diagonal_elements)
        self.children += [upper_left_design]


class DiagonalCard(Card):
    # stripes SW-NE along whole card
    # colours from TL down to centre
    def __init__(self, colours=["#ff0000", "#0000ff"], **kwargs):
        super().__init__(**kwargs)
        num_colours = len(colours)
        if num_colours == 0:
            raise BadCardError("Diagonal cards need at least one colour")
        if num_colours % 2 != 0:
            # split into two sub-classes and dispatch - odd number needs special handling
            raise BadCardError("Diagonal cards (currently) need even number of colours")

        half_num_colours = num_colours//2

        width_break_size = self.design_width/half_num_colours
        height_break_size = self.design_height/half_num_colours
    
        def get_coords(indices):
            x_ind, y_ind = indices
            x_val = self.design_offset + x_ind*width_break_size
            y_val = self.design_offset + y_ind*height_break_size
            return x_val, y_val

        # upper triangle
        triangle_indices = [(0, 0), (1, 0), (0, 1)]
        diagonal_elements = [
            Polygon(0, colours[0],
            points=list(map(get_coords, triangle_indices)))
        ]

        # rest of top half as above
        for idx in range(1, half_num_colours):
            quad_indices = [(0, idx), (idx, 0), (idx+1, 0), (0, idx+1)]
            diagonal_elements += [
                Polygon(idx, colours[idx],
                points=list(map(get_coords, quad_indices)))
            ]
        # bottom half is slight variant
        for idx in range(0, half_num_colours-1):
            quad_indices = [
                (idx, half_num_colours), (half_num_colours, idx), (half_num_colours, idx+1), (idx+1, half_num_colours)
            ]
            diagonal_elements += [
                Polygon(idx + half_num_colours, colours[idx + half_num_colours],
                points=list(map(get_coords, quad_indices)))
            ]
        
        triangle_indices = [
            (half_num_colours - 1, half_num_colours),
            (half_num_colours, half_num_colours - 1),
            (half_num_colours, half_num_colours)
        ]
        diagonal_elements += [
            Polygon(0, colours[-1],
            points=list(map(get_coords, triangle_indices)))
        ]

        total_left_design = Element("g", children=diagonal_elements)
        self.children += [total_left_design]
