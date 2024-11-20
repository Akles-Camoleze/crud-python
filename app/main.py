import gi

from config import config
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


if __name__ == "__main__":
    database_config, app_config = config.init_config()
    database_config.connect()

    window = Gtk.Window(title="Teste GTK")
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()
