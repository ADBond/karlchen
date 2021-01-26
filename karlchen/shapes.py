from .elements import Element

class Polygon(Element):

    def __init__(self, id_num, colour, points):
        d_value = "M "
        for x, y in points:
            d_value += f"{x},{y} "
        d_value += "Z"
        num_points = len(points)
        poly_name = {
            3: "triangle",
            4: "quad",
            5: "pent",
            6: "hex",
        }.get(num_points, f"poly{num_points}")
        super().__init__(
            "path", fill=colour, stroke="none", d=d_value, id=f"{poly_name}-{id_num}",
            self_closing=True
        )
