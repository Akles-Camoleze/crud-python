import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GtkProvider:
    Window = Gtk.Window
    Notebook = Gtk.Notebook
    ListBox = Gtk.ListBox
    ListBoxRow = Gtk.ListBoxRow
    Label = Gtk.Label
    main_quit = Gtk.main_quit
    main = Gtk.main