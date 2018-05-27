from lib.menu import Menu
from lib.gui.button import Button
from lib.gui.labelButton import LabelButton


class AttackChoiceMenu(Menu):
    def __init__(self, parentState):
        super().__init__("attackChoiceMenu", parentState)

    def isNowCurrentMenu(self):
        self.buttons[:] = []
        enemySurfaces = self.getParent().getEnemyGUISurfaces()
        self.listElements(enemySurfaces, 400, 350, align="center")
        for surface in enemySurfaces:
            index = enemySurfaces.index(surface)
            enemy = self.getParent().currentEnemies[index]
            self.addButtons(EnemyButton(surface, self.enemySelected, enemy))
        self.addButtons(LabelButton("Back", self.goBack, x=20, y=600))

    def enemySelected(self, enemy):
        damage = self.getRoot().player.heldWeapon.damage
        self.getParent().attackEnemy(enemy, damage)

    def goBack(self):
        self.getRoot().fadeMenuChange("battleMenu", "fast")


class EnemyButton(Button):
    def __init__(self, enemyLabel,func, *funcArgs):
        super().__init__(enemyLabel.image, func, *funcArgs, x=enemyLabel.rect.x,
                         y=enemyLabel.rect.y)
        self.originalRect = enemyLabel.rect
        self.hoverAmount = 75

    def hover(self):
        self.rect.x = self.originalRect.x - self.hoverAmount

    def unhover(self):
        self.rect.x = self.originalRect.x
