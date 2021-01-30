from karlchen.suits import Heart, Diamond

heart_svg = Heart()
heart_svg.to_file("hearts_default", sub_folder="suits")

heart_svg = Heart(
    centre_roundiness_from_sides_horiz=68,
    centre_roundiness_from_sides_vert=220,
    height=490,
    crevice_depth=90,
    top_roundiness_h2=20,
    centre_roundiness_from_top_horiz=38,
    centre_roundiness_from_top_vert=80,
    top_roundiness_vert=80,
)
heart_svg.to_file("hearts", sub_folder="suits")

diamonds_svg = Diamond()
diamonds_svg.to_file("diamonds_default", sub_folder="suits")
