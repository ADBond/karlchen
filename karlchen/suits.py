from .elements import Element, SVG

class Heart(SVG):

    def __init__(self):
        # print([total := total + i for i in [140,303,-303,-120,69,-69]])
        # hearts based on the excellent https://github.com/mathieudutour/svg-path-visualizer
        # 140,20 -> 20,140 -> 248,443 -> 477,140 -> 357,20 -> 248,89 -> 140, 20
        # TL crest -> leftmost -> point -> rightmost -> TR crest -> crevice -> TL crest
        heart_string = "M 140,20 " + \
            "C 73,20 20,74 20,140 " + \
            "c 0,135 136,170 228,303 " + \
            "c 88,-132 229,-173 229,-303 " \
            "c 0,-66 -54,-120 -120,-120 " + \
            "c -48,0 -90,28 -109,69 " + \
            "c -19,-41 -60,-69 -108,-69 " + \
            "Z"
        heart = Element(
            "path", fill="#FF0000", stroke="none", d=heart_string, id=f"heart",
            self_closing=True
        )
        super().__init__(
            width=500, height=450, children=[heart]
        )
        
