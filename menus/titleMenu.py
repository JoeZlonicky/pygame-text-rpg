from lib.menu import Menu
from lib.gui.labelButton import LabelButton
from lib.gui.label import Label
from lib.gui.multilineLabel import MultilineLabel


class TitleMenu(Menu):
    def __init__(self, parentState):
        super().__init__("titleMenu", parentState)
        self.addButtons(LabelButton("Begin A New Adventure", 25, 300,
                                   self.newGame),
                        LabelButton("Exit Game", 25, 350, self.exit))

    def newGame(self):
        newMenu = "characterCreationState/raceSelectionMenu"
        self.getRoot().fadeMenuChange(newMenu, "slow")

    def exit(self):
        self.getRoot().running = False
