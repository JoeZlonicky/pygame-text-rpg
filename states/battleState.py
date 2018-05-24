import copy
from menus.battleMenu import BattleMenu
from menus.inventoryMenu import InventoryMenu
from lib.jsonLoader import JSONLoader
from lib.state import State
from core.enemy import Enemy


class BattleState(State):
    def __init__(self, game):
        super().__init__("battleState", game)
        self.addMenus(BattleMenu(self), InventoryMenu(self, "battleMenu"))
        self.enemies = JSONLoader.loadJSONFile("enemies", Enemy)
        self.currentEnemes = []

    def newBattle(self, location):
        self.currentEnemes[:] = []
        for enemy in location.enemies:
            for enemyType in self.enemies:
                if enemy == enemyType.name:
                    self.currentEnemes.append(copy.deepcopy(enemyType))
        self.getRoot().fadeMenuChange("battleState/battleMenu")

    def getEnemyGUI(self):
        # Return the images with enemy names and health bars
        pass
