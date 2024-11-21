import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GtkProvider:
    Window = Gtk.Window
    Box = Gtk.Box
    Notebook = Gtk.Notebook
    ListBox = Gtk.ListBox
    ListBoxRow = Gtk.ListBoxRow
    Label = Gtk.Label
    main_quit = Gtk.main_quit
    main = Gtk.main
    ListStore = Gtk.ListStore
    TreeView = Gtk.TreeView
    CellRendererText = Gtk.CellRendererText
    TreeViewColumn = Gtk.TreeViewColumn
    Orientation = Gtk.Orientation
    CssProvider = Gtk.CssProvider
    StyleContext = Gtk.StyleContext
    STYLE_PROVIDER_PRIORITY_APPLICATION = Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    Button = Gtk.Button
    Grid = Gtk.Grid
    Align = Gtk.Align