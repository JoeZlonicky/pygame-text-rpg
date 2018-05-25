from lib.menu import Menu
from lib.gui.labelButton import LabelButton


class InventoryMenu(Menu):
    def __init__(self, parentState, menuToReturnTo):
        super().__init__("inventoryMenu", parentState)
        self.menuToReturnTo = menuToReturnTo

    def isNowCurrentMenu(self):
        self.buttons[:] = []
        inventory = self.getRoot().player.inventory
        for item in inventory.getItems():
            self.addButtons(LabelButton(item.name, self.itemSelected, item))
        self.addButtons(LabelButton("Back", self.goBack))
        self.listElements(self.buttons, 20, 350, spacing=25,align="center")

    def itemSelected(self, item):
        print("Item selected: " + item.name)

    def goBack(self):
        self.getRoot().fadeMenuChange(self.menuToReturnTo, "fast")
