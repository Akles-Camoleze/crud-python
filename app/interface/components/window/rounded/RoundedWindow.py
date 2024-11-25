from app.interface.providers.gdk.GdkProvider import GdkProvider
from app.interface.providers.gtk.GtkProvider import GtkProvider


class RoundedWindow(GtkProvider.Window):
    def __init__(self, title="Rounded Window", radius=20, bg_color="#ffffff", shadow=True, modal=False):
        super().__init__(title=title, modal=modal)

        self.set_default_size(400, 300)
        self.set_app_paintable(True)

        self._add_header(title)
        self._apply_css(radius, bg_color, shadow)

        self.main_container = GtkProvider.Box(orientation=GtkProvider.Orientation.VERTICAL, spacing=10)
        self.main_container.set_name("main_container")
        self.main_container.set_hexpand(True)
        self.add(self.main_container)

    def _add_header(self, title):
        header = GtkProvider.HeaderBar()
        header.set_title(title)
        header.set_show_close_button(True)
        self.set_titlebar(header)

    def _apply_css(self, radius, bg_color, shadow):
        css_provider = GtkProvider.CssProvider()

        shadow_css = (
            "box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);" if shadow else ""
        )

        css = f"""
        window {{
            background-color: transparent;  /* Define fundo transparente para a janela */
            border-radius: {radius}px;
            {shadow_css}
        }}
        #main_container {{
            background-color: {bg_color};  /* Aplica o fundo à box interna */
        }}
        """
        css_provider.load_from_data(css.encode())

        screen = GdkProvider.Screen.get_default()
        GtkProvider.StyleContext.add_provider_for_screen(
            screen, css_provider, GtkProvider.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    def on_close(self, widget):
        self.destroy()

    def add_content(self, widget):
        self.main_container.pack_start(widget, True, True, 0)
