from app.interface.providers.gdk.GdkPixbufProvider import GdkPixbufProvider
from app.interface.providers.gtk.GtkProvider import GtkProvider


class WidgetUtils:
    @staticmethod
    def create_icon_button(callback, icon_name, *args):
        icon_path = f"resources/icons/{icon_name}.svg"

        button = GtkProvider.Button()
        button.set_relief(GtkProvider.ReliefStyle.NONE)
        delete_icon = GtkProvider.Image.new_from_pixbuf(WidgetUtils.load_and_resize_svg(icon_path))
        button.set_image(delete_icon)

        button.connect("clicked", lambda widget: callback(widget, *args))

        return button

    @staticmethod
    def load_and_resize_svg(icon_path, width=26, height=26):
        return GdkPixbufProvider.Pixbuf.new_from_file_at_size(icon_path, width, height)