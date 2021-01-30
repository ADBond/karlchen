from .elements import Element, SVG

class Heart(SVG):

    def __init__(self, **kwargs):
        # print([total := total + i for i in [140,303,-303,-120,69,-69]])
        # hearts based on the excellent https://github.com/mathieudutour/svg-path-visualizer
        # TL crest -> leftmost -> point -> rightmost -> TR crest -> crevice -> TL crest

        # scale should not live in arguments
        scale = 1.0
        def make_heart_string(
            margin_x=20*scale,
            margin_y=20*scale,
            top_wideness=120*scale,
            top_height=120*scale,

            middle_wideness=228*scale,

            top_roundiness_horiz=67*scale,
            top_roundiness_vert=54*scale,

            sides_to_bottom_height=303*scale,
            sides_to_centre=228*scale,

            bottom_roundiness_vert=135*scale,
            centre_roundiness_from_sides_horiz=136*scale,
            centre_roundiness_from_sides_vert=170*scale,

            crevice_depth=69*scale,
            top_roundiness_h2=48*scale,
            centre_roundiness_from_top_horiz=90*scale,
            centre_roundiness_from_top_vert=28*scale,
        ):
            starting_point = f"M {margin_x + top_wideness},{margin_y} "
            top_to_left = f"c -{top_roundiness_horiz},0 -{top_wideness},{top_roundiness_vert} -{top_wideness},{top_height} "

            left_to_bottom = f"c 0,{bottom_roundiness_vert} " + \
                f"{centre_roundiness_from_sides_horiz},{centre_roundiness_from_sides_vert} " + \
                f"{sides_to_centre},{sides_to_bottom_height} "

            bottom_to_right = f"c {sides_to_centre - centre_roundiness_from_sides_horiz}," + \
                            f"-{sides_to_bottom_height - centre_roundiness_from_sides_vert} " + \
                f"{sides_to_centre},-{sides_to_bottom_height - bottom_roundiness_vert} " + \
                f"{sides_to_centre},-{sides_to_bottom_height} "

            right_to_top = f"c 0,-{top_height - top_roundiness_vert} " + \
                f"-{top_wideness - top_roundiness_horiz},-{top_height} " + \
                f"-{top_wideness},-{top_height} "

            top_to_crevice = f"c -{top_roundiness_h2},0 " + \
                f"-{centre_roundiness_from_top_horiz},{centre_roundiness_from_top_vert} " + \
                f"-{sides_to_centre - top_wideness},{crevice_depth} "
            crevice_to_start = f"c -{sides_to_centre - top_wideness - centre_roundiness_from_top_horiz}," + \
                                f"-{crevice_depth - centre_roundiness_from_top_vert} " + \
                f"-{sides_to_centre - top_wideness - top_roundiness_h2},-{crevice_depth} " + \
                f"-{sides_to_centre - top_wideness},-{crevice_depth} "

            heart_string = starting_point + top_to_left + left_to_bottom + bottom_to_right + \
                right_to_top + top_to_crevice + crevice_to_start + " Z"
            return heart_string

        heart = Element(
            "path", fill="#FF0000", stroke="none", d=make_heart_string(**kwargs), id=f"heart",
            self_closing=True
        )
        super().__init__(
            width=500, height=600, children=[heart]
        )
        
