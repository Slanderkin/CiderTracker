from nicegui import ui
import gui_elements.theme as theme

#https://github.com/zauberzeug/nicegui/discussions/2724
class IngredientsPage:
    def __init__(self) -> None:
        self.cards = {}
        @ui.page('/ingredients')
        def home_page() -> None:
            with theme.frame('Ingredients Page'):
                pass
            self.content()
    
    def content(self):
        card_id = ui.input('Recipe Name', value='Default Recipe')
        ui.button('New Recipe', on_click=lambda: self.AddCard(card_id.value))
        ui.button('edit card', on_click=lambda: self.EditCard(card_id.value))
        ui.button('remove card', on_click=lambda: self.RemoveCard(card_id.value))
        self.grid()

        ui.label("The ingredients page goes here")
        
    @ui.refreshable
    def grid(self) -> None:
        with ui.dialog() as self.rule_dialog,ui.card():
            ui.label('dialog')
        ui.button('Open diag', on_click=self.rule_dialog.open)
        with ui.grid(columns=5, rows=5):
            for card_id, card_items in self.cards.items():
                with ui.card().tight():
                    #The top row of the card
                    #https://github.com/zauberzeug/nicegui/discussions/3269
                    with ui.row().classes('w-full'):
                        ui.label(card_id).classes('text-bold')
                        ui.space()
                        ui.icon(name='edit').tailwind('self-center')
                    with ui.column().classes('justify-content: flex-start; w-full'):
                        for item in card_items:
                            with ui.row().classes('w-full'):
                                ui.label(item).tailwind('self-center')
                                ui.input().tailwind('self-center')
                    
                    #ui.button("Add Item", on_click=self.AddItem(card_id, 'test'))

    def AddCard(self, card_id: str) -> None:
        self.cards.update({card_id: ['a', 'b', 'c']})
        self.grid.refresh()

    def EditCard(self, card_id: str) -> None:
        self.cards[card_id].append('d')
        self.grid.refresh()

    def RemoveCard(self, card_id: str) -> None:
        del self.cards[card_id]
        self.grid.refresh()
        
    def AddItem(self, card_id: str, value: str) -> None:
        self.cards[card_id].append(value)
        self.grid.refresh()
        
        
'''
TODO
Let the user create a new recipe, adding each ingredient and its amount as they go, possibly a when column?
Let the user create a template for recipies
'''