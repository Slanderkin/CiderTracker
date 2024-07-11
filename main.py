#3rd Party Packages
from nicegui import ui

#Local Files
from data.data_handler import DataHandler
from pages.ingredients_page import IngredientsPage
from pages.home_page import HomePage

dataHandler = DataHandler()
dataHandler.LoadData()
homePage = HomePage(dataHandler)
ingredientsPage = IngredientsPage()

    
ui.run(dark=True)