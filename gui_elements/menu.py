from nicegui import ui

class Menu:
    def __init__(self) -> None:
        ui.link('Home', '/').classes(replace='text-white')
        ui.link('Ingredients', '/ingredients').classes(replace='text-white')