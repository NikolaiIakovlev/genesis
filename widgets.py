class Widget:
    def __init__(self):
        self.children = []

    def add_child(self, widget):
        self.children.append(widget)

    def render(self, platform):
        # Рендеринг виджета на платформе
        pass

class Button(Widget):
    def __init__(self, text, on_press=None):
        super().__init__()
        self.text = text
        self.on_press = on_press

    def render(self, platform):
        platform.create_button(self.text, self.on_press)