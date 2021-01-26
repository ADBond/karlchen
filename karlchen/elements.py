from os import path

def space_string(length):
    return "".join([" " for i in range(length)])

class BadElement(Exception):
    pass

class Element():

    def __init__(self, element_name, id=None, self_closing=False, children=[], split_lines=True, **kwargs):
        if self_closing and children:
            raise BadElement("Self-closing tags cannot have children")
        self.element_name = element_name
        self.id = id if id is not None else "TODO"
        self.children = children
        self.attributes = kwargs
        self.self_closing = self_closing
        self.split_lines = split_lines

    def string_lines(self, overall_indent=0):
        element_lines = [f"<{self.element_name}"]
        attribute_indent = 3
        child_indent = 2
        indent_string = space_string(attribute_indent)
        for attribute, value in self.attributes.items():
            attr_string = f'{attribute}="{value}"'
            if self.split_lines:
                element_lines.append(f"{indent_string}{attr_string}")
            else:
                element_lines[0] += f" {attr_string}"
        element_lines[-1] += " />" if self.self_closing else ">"
        for child in self.children:
            element_lines += child.string_lines(child_indent) if isinstance(child, Element) \
                                    else [f"{space_string(child_indent)}{child}"]
        if not self.self_closing:
            element_lines.append(f"</{self.element_name}>")
        overall_indent_string = space_string(overall_indent)
        return map(lambda x: f"{overall_indent_string}{x}", element_lines)
    
    def to_string(self):
        return "\n".join(self.string_lines(0))

    def to_file(self, name, location="./examples"):
        file_path = path.join(location, f"{name}.svg")
        with open(file_path, "w+") as svg_file:
            svg_file.write(self.to_string())

class SVG(Element):

    def __init__(self, id=None, children=[], width=300, height=200, **kwargs):
        super().__init__(
            "svg", id=id, children=children,
            version="1.1", baseProfile="full", width=width, height=height, xmlns="http://www.w3.org/2000/svg",
            **kwargs
        )
