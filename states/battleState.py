import pygame
import copy
from menus.battleMenu import BattleMenu
from menus.inventoryMenu import InventoryMenu
from menus.attackChoiceMenu import AttackChoiceMenu
from lib.jsonLoader import JSONLoader
from lib.state import State
from lib.gui.label import Label
from lib.gui.surface import Surface
from core.enemy import Enemy


class BattleState(State):
    def __init__(self, game):
        super().__init__("battleState", game)
        self.addMenus(BattleMenu(self), InventoryMenu(self, "battleMenu"),
                      AttackChoiceMenu(self))
        self.enemies = JSONLoader.loadJSONFile("enemies", Enemy)
        self.currentEnemies = []
        self.itemsDrops = []
        self.goldDrop = 0

    def newBattle(self, location):
        self.currentEnemies[:] = []
        self.itemsDrops[:] = []
        self.goldDrop = 0
        for enemy in location.enemies:
            for enemyType in self.enemies:
                if enemy == enemyType.name:
                    self.currentEnemies.append(copy.deepcopy(enemyType))
                    self.currentEnemies.append(copy.deepcopy(enemyType))
                    self.currentEnemies.append(copy.deepcopy(enemyType))
        self.getRoot().fadeMenuChange("battleState/battleMenu")

    def attackEnemy(self, enemy, damage):
        enemy.takeDamage(damage)
        if enemy.isDead():
            self.calculateEnemyDrops(enemy)
            self.currentEnemies.remove(enemy)
        if len(self.currentEnemies) == 0:
            self.getRoot().player.inventory.gold += self.goldDrop
            self.getRoot().player.inventory.addItems(*self.itemsDrops)
            self.getRoot().fadeMenuChange("locationState/mainLocationMenu")
        else:
            self.getRoot().fadeMenuChange("battleMenu", "fast")

    def calculateEnemyDrops(self, enemy):
        self.goldDrop += enemy.getGoldDrop()
        for itemName in enemy.getItemDrops():
            drop = self.getRoot().itemManager.getItem(itemName)
            self.itemsDrops.append(drop)

    def getEnemyGUISurfaces(self):
        surfaces = []
        for enemy in self.currentEnemies:
            background = pygame.Surface((400, 75))
            points = [[0, 0], [400, 0], [400, 74], [25, 74]]
            pygame.draw.polygon(background, (255, 255, 255), points, 2)
            nameLabel = Label(enemy.name, x=50, y=10)
            health = enemy.currentHealth
            maxHealth = enemy.maxHealth
            healthString = str(health) + "/" + str(maxHealth)
            healthLabel  = Label(healthString, x=50, y=40)
            background.blit(nameLabel.image, nameLabel.rect)
            background.blit(healthLabel.image, healthLabel.rect)
            surfaces.append(Surface(background))
        return surfaces
