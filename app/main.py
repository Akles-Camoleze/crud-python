import gi

from config.config import Config
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def initialize_singletons():
    Config()


if __name__ == "__main__":
    initialize_singletons()

    window = Gtk.Window(title="Teste GTK")
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()
