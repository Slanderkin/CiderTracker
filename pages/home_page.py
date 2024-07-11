from nicegui import ui
import gui_elements.theme as theme

class HomePage:
    def __init__(self, dataHandler) -> None:
        @ui.page('/')
        def home_page() -> None:
            with theme.frame('Homepage'):
                pass
            self.content(dataHandler)
    
    def content(self, dataHandler):
        ui.label("Homebrew Tracker").tailwind("self-center", "text-4xl").font_weight("extrabold")
        ui.separator()
        
        def add_row():
            new_id = max((dx['id'] for dx in dataHandler.rows), default=-1) + 1
            dataHandler.rows.append({'id': new_id, 'name': 'New name', 'age': None})
            ui.notify(f'Added row with ID {new_id}')
            aggrid.update()

        def handle_cell_value_change(e):
            new_row = e.args['data']
            ui.notify(f'Updated row to: {e.args["data"]}')
            dataHandler.rows[:] = [row | new_row if row['id'] == new_row['id'] else row for row in dataHandler.rows]

        async def delete_selected():
            selected_id = [row['id'] for row in await aggrid.get_selected_rows()]
            dataHandler.rows[:] = [row for row in dataHandler.rows if row['id'] not in selected_id]
            ui.notify(f'Deleted row with ID {selected_id}')
            aggrid.update()

        aggrid = ui.aggrid({
            'columnDefs': dataHandler.header,
            'rowData': dataHandler.rows,
            'rowSelection': 'multiple',
            'stopEditingWhenCellsLoseFocus': True,
        },
        theme="balham-dark").on('cellValueChanged', handle_cell_value_change)

        ui.button('Delete selected', on_click=delete_selected)
        ui.button('Add Row', on_click=add_row)
        ui.button('Save Data', on_click=dataHandler.SaveData)