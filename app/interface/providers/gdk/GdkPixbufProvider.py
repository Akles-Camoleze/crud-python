import gi

gi.require_version('GdkPixbuf', '2.0')
from gi.repository import GdkPixbuf

class GdkPixbufProvider:
    Pixbuf = GdkPixbuf.Pixbuf