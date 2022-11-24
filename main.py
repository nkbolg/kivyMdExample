from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp


def speed(wind):
    if wind < 1:
        return "0 баллов, Штиль"
    elif wind <= 2:
        return "1 балл, Тихий ветер"
    elif wind <= 6:
        return "2 балла, Лёгкий ветер"
    elif wind <= 10:
        return "3 балла, Слабый ветер"
    elif wind <= 15:
        return "4 балла, Умеренный ветер"
    elif wind <= 20:
        return "5 баллов, Свежий ветер"
    elif wind <= 26:
        return "6 баллов, Сильный ветер"
    elif wind <= 33:
        return "7 баллов, Крепкий ветер"
    elif wind <= 40:
        return "8 баллов, Очень крепкий ветер"
    elif wind <= 47:
        return "9 баллов, Шторм"
    elif wind <= 55:
        return "10 баллов, Сильный шторм"
    elif wind <= 63:
        return "11 баллов, Жесткий шторм"
    else:
        return "12 баллов, Ураган"


Builder.load_string(
    """
#:import Window kivy.core.window.Window

<ExampleTextFields@MDBoxLayout>:
    orientation: "vertical"
    spacing: "10dp"

    ScrollView:

        MDBoxLayout:
            orientation: "vertical"
            adaptive_height: True
            padding: dp(48)
            spacing: dp(15)


            MDTextField:
                id: text_field
                input_filter: "int"
                hint_text: "Сила ветра"

            MDLabel:
                id: text_label
                text: ""

"""
)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Калькулятор силы ветра"
        self.theme_cls.primary_palette = "Blue"

    def set_label(self, value):
        self.root.ids.text_label.text = speed(int(value.text))

    def build(self):
        self.root = Factory.ExampleTextFields()
        self.root.ids.text_field.bind(
            on_text_validate=self.set_label
        )


if __name__ == "__main__":
    MainApp().run()
