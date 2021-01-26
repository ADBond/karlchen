from karlchen.elements import Element

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
example_svg = Element(
    "svg", children=[rect, circle, text], split_lines=True,
    version="1.1", baseProfile="full", width="300", height="200", xmlns="http://www.w3.org/2000/svg"
)

example_svg.to_file("example_generated")
