"""
decorator
выводить текст, оборачивая его
    жирный
    курсив
    зачеркнут
TextComponent render() - просто возвращает строку
PlainText - просто текст
    BoldDecorator **текст**
    курсивdecorator *текст*
    зачеркнутdecorator ~~текст~~
"""

class TextComponent:
    def render(self) -> str:
        raise NotImplementedError

class PlainText(TextComponent):
    def __init__(self, text: str):
        self.text= text

    def render(self) -> str:
        return self.text

class TextDecorator(TextComponent):
    def __init__(self, component: TextComponent):
        self._component = component

    def render(self) -> str:
        return self._component.render()

class BoldDecorator(TextDecorator):
    def render(self) -> str:
        return f"**{super().render()}**"

class ItalicDecorator(TextDecorator):
    def render(self) -> str:
        return f"*{super().render()}*"

class StrikethroughDecorator(TextDecorator):
    def render(self) -> str:
        return f"~~{super().render()}~~"

base = PlainText("hi")
decorated = ItalicDecorator(BoldDecorator(StrikethroughDecorator(base)))
print(decorated.render())