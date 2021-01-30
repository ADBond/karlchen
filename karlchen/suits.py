from .elements import Element, SVG

# any point in having an abstract suit base class?

# adjust this as necessary
SUIT_RED = "#D40000"

class Heart(SVG):

    def __init__(self, **kwargs):
        # print([total := total + i for i in [140,303,-303,-120,69,-69]])
        # hearts based on the excellent https://github.com/mathieudutour/svg-path-visualizer
        # TL crest -> leftmost -> point -> rightmost -> TR crest -> crevice -> TL crest

        scale = 1.0
        def make_heart_string(
            margin_x=20*scale,
            margin_y=20*scale,
            
            height=423,
            width=456,

            top_wideness=120*scale,
            top_height=120*scale,

            middle_wideness=228*scale,

            top_roundiness_horiz=67*scale,
            top_roundiness_vert=66,

            bottom_roundiness_vert=135*scale,
            centre_roundiness_from_sides_horiz=92,
            centre_roundiness_from_sides_vert=133,

            crevice_depth=69*scale,
            top_roundiness_h2=48*scale,
            centre_roundiness_from_top_horiz=18,
            centre_roundiness_from_top_vert=41,
        ):
            # parameters easier to use in construction
            sides_to_bottom_height = height - top_height
            sides_to_centre = width/2

            # TODO: set default values so we don't need scaling
            x_scale, y_scale = 0.8, 1.0
            # surely a cleaner way??
            x_args = (
                margin_x, top_wideness, middle_wideness, top_roundiness_horiz, sides_to_centre,
                centre_roundiness_from_sides_horiz, top_roundiness_h2, centre_roundiness_from_top_horiz,
            )
            x_args = (i*x_scale for i in x_args)
            (
                margin_x, top_wideness, middle_wideness, top_roundiness_horiz, sides_to_centre,
                centre_roundiness_from_sides_horiz, top_roundiness_h2, centre_roundiness_from_top_horiz,
            ) = x_args

            starting_point = f"M {margin_x + top_wideness},{margin_y} "
            top_to_left = f"c -{top_roundiness_horiz},0 -{top_wideness},{top_height-top_roundiness_vert} " + \
                f"-{top_wideness},{top_height} "

            left_to_bottom = f"c 0,{bottom_roundiness_vert} " + \
                f"{sides_to_centre - centre_roundiness_from_sides_horiz}," + \
                f"{sides_to_bottom_height - centre_roundiness_from_sides_vert} " + \
                f"{sides_to_centre},{sides_to_bottom_height} "

            bottom_to_right = f"c {centre_roundiness_from_sides_horiz}," + \
                            f"-{centre_roundiness_from_sides_vert} " + \
                f"{sides_to_centre},-{sides_to_bottom_height - bottom_roundiness_vert} " + \
                f"{sides_to_centre},-{sides_to_bottom_height} "

            right_to_top = f"c 0,-{top_roundiness_vert} " + \
                f"-{top_wideness - top_roundiness_horiz},-{top_height} " + \
                f"-{top_wideness},-{top_height} "

            top_to_crevice = f"c -{top_roundiness_h2},0 " + \
                f"-{sides_to_centre - top_wideness - centre_roundiness_from_top_horiz}," + \
                f"{crevice_depth - centre_roundiness_from_top_vert} " + \
                f"-{sides_to_centre - top_wideness},{crevice_depth} "
            crevice_to_start = f"c -{centre_roundiness_from_top_horiz}," + \
                                f"-{centre_roundiness_from_top_vert} " + \
                f"-{sides_to_centre - top_wideness - top_roundiness_h2},-{crevice_depth} " + \
                f"-{sides_to_centre - top_wideness},-{crevice_depth} "

            heart_string = starting_point + top_to_left + left_to_bottom + bottom_to_right + \
                right_to_top + top_to_crevice + crevice_to_start + " Z"
            return heart_string

        heart = Element(
            "path", fill=f"{SUIT_RED}", stroke="none", d=make_heart_string(**kwargs), id=f"heart",
            self_closing=True
        )
        super().__init__(
            width=500, height=600, children=[heart]
        )
        

# TODO: this module could get bloated, maybe split each into a single file?
class Diamond(SVG):

    def __init__(self, **kwargs):
        # reckon I can make this one up from scratch easy enough
        def make_diamond_string(
            margin_x=20,
            margin_y=20,

            height=500,
            width=400,
        ):
            half_width = width/2
            half_height = height/2
            starting_point = f"M {margin_x + half_width },{margin_y} "
            top_to_left = f"l -{half_width},{half_height} "
            left_to_bottom = f"l {half_width},{half_height} "
            bottom_to_right = f"l {half_width},-{half_height} "
            right_to_top = f"l -{half_width},-{half_height} "
            return starting_point + top_to_left + left_to_bottom + bottom_to_right + right_to_top + "Z"

        diamond = Element(
            "path", fill=f"{SUIT_RED}", stroke="none", d=make_diamond_string(**kwargs), id=f"diamond",
            self_closing=True
        )
        super().__init__(
            width=500, height=600, children=[diamond]
        )
