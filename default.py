import sys
import xbmcaddon

Addon = xbmcaddon.Addon('script.demo')

# Script constants
__scriptname__ = Addon.getAddonInfo('name')
__id__ = Addon.getAddonInfo('id')
__author__ = Addon.getAddonInfo('author')
__version__ = Addon.getAddonInfo('version')
__path__ = Addon.getAddonInfo('path')

getLocalizedString = Addon.getLocalizedString
getSetting = Addon.getSetting

print '[SCRIPT][%s] version %s initialized!' % (__scriptname__, __version__)

if (__name__ == "__main__"):
    import resources.lib.demo as demo
    ui = demo.GUI("script-demo.xml", __path__, "default")
    ui.doModal()
    print '[SCRIPT][%s] version %s exited!' % (__scriptname__, __version__)
    del ui

sys.modules.clear()
