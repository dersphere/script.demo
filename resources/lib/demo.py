import sys
import xbmcgui

getLocalizedString = sys.modules['__main__'].getLocalizedString

# Buttons               3000-3009
# Textboxes             3010-3019
# Transl. for Controls  3100-3119
# Transl. for Usage     3200-3219


class GUI(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)

    def onInit(self):
        # store xbmc keycodes for exit and backspace
        self.action_exitkeys_id = [10, 13]
        # get control ids
        self.control_id_button_hello = 3000
        self.control_id_button_exit = 3001
        self.control_id_label_hello = 3011
        # set actions
        self.button_hello = self.getControl(self.control_id_button_hello)
        self.button_exit = self.getControl(self.control_id_button_exit)
        self.label_hello = self.getControl(self.control_id_label_hello)
        # translate buttons
        self.button_hello.setLabel(getLocalizedString(3101))
        self.button_exit.setLabel(getLocalizedString(3102))

    def onAction(self, action):
        # onAction will be called on keyboard or mouse action
        # action is the action which was triggered
        if action in self.action_exitkeys_id:
            self.closeDialog()

    def onFocus(self, controlId):
        # onFocus will be called on any focus
        pass

    def onClick(self, controlId):
        # onClick will be called on any click
        # controlID is the ID of the item which is clicked
        if controlId == self.control_id_button_hello:
            self.sayHello()
        elif controlId == self.control_id_button_exit:
            self.closeDialog()

    def sayHello(self):
        self.label_hello.setLabel(getLocalizedString(3120))

    def closeDialog(self):
        self.close()
