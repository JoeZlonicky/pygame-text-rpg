import pygame
from core.inputField import InputField
class MenuNavigationHandler:
    def __init__(self, menu):
        self.menu = menu
        self.buttonSelection = 0
        self.currentTextField = None

    def handleNavigationEvents(self, events):
        self.handleMouseEvents(events)
        self.handleKeyPressEvents(events)

    def handleKeyPressEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.currentTextField is not None:
                    self.handleTextFieldInputEvent(event)
                else:
                    self.handleButtonNavigationEvent(event)

    def handleMouseEvents(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                self.updateButtons(event.pos)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.checkForButtonClick()

    def updateButtons(self, mousePosition):
        for button in self.menu.buttons:
            button.update(mousePosition)
            if button.isHovering(mousePosition):
                self.buttonSelection = self.menu.buttons.index(button)

    def checkForButtonClick(self):
        if self.currentTextField is not None:
            self.currentTextField.unselected()
            self.currentTextField = None
        for button in self.menu.buttons:
            if button.hovered:
                button.click(*button.funcArgs)
                if isinstance(button, InputField):
                    self.currentTextField = button
                    self.currentTextField.selected()

    def handleTextFieldInputEvent(self, event):
        if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
            self.currentTextField.unselected()
            self.currentTextField = None
        elif event.key == pygame.K_BACKSPACE:
            self.currentTextField.backspace()
        else:
            self.currentTextField.addInput(event.unicode)

    def handleButtonNavigationEvent(self, event):
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.buttonSelection = max(self.buttonSelection - 1, 0)
            self.updateButtonFocus()
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.buttonSelection = min(self.buttonSelection + 1,
                                       len(self.menu.buttons) - 1)
            self.updateButtonFocus()
        elif event.key == pygame.K_RETURN:
            selectedButton = self.menu.buttons[self.buttonSelection]
            selectedButton.checkForClick()
            if isinstance(selectedButton, InputField):
                self.currentTextField = selectedButton

    def updateButtonFocus(self):
        for i in range(len(self.menu.buttons)):
            if i == self.buttonSelection:
                self.menu.buttons[i].forceHover()
                if isinstance(self.menu.buttons[i], InputField):
                    self.currentTextField = self.menu.buttons[i]
                    self.menu.buttons[i].selected()
            else:
                self.menu.buttons[i].forceUnhover()