import gi

gi.require_version('Gdk', '3.0')
from gi.repository import Gdk

class GdkProvider:
    Screen = Gdk.Screen