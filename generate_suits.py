from karlchen.suits import Heart, Diamond

heart_svg = Heart()
heart_svg.to_file("hearts_default", sub_folder="suits")

heart_svg = Heart(
    # centre_roundiness_from_sides_horiz=160,
    # centre_roundiness_from_sides_vert=150,
    new_centre_roundiness_from_sides_horiz=228-160,
    new_centre_roundiness_from_sides_vert=370-150,
    sides_to_bottom_height=370,
    crevice_depth=90,
    top_roundiness_h2=20,
    # centre_roundiness_from_top_horiz=108,
    # centre_roundiness_from_top_horiz=70,
    # centre_roundiness_from_top_vert=10,
    new_centre_roundiness_from_top_horiz=228-120-70,
    new_centre_roundiness_from_top_vert=90-10,
    # top_roundiness_vert=40,
    new_top_roundiness_vert=120-40,
)
heart_svg.to_file("hearts", sub_folder="suits")

diamonds_svg = Diamond()
diamonds_svg.to_file("diamonds_default", sub_folder="suits")
