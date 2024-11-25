from app.entities.dispositivopessoa.DispositivoPessoa import DispositivoPessoa
from app.interface.components.window.rounded.RoundedWindow import RoundedWindow
from app.interface.providers.gdk.GdkPixbufProvider import GdkPixbufProvider
from app.interface.providers.gtk.GtkProvider import GtkProvider
from app.interface.services.dispositivo.DispositivoService import DispositivoService
from app.interface.services.dispositivopessoa.DispositivoPessoaService import DispositivoPessoaService
from app.interface.utils.WidgetUtils import WidgetUtils


class ModalDispositivos(RoundedWindow):
    def __init__(self, parent, callback, pessoa=None):
        super().__init__(title=f"Dispositivos de {pessoa.nome}", modal=True)

        self.parent = parent
        self.callback = callback
        self.pessoa_id = pessoa.id

        self.set_default_size(400, 200)

        box = GtkProvider.Box(orientation=GtkProvider.Orientation.VERTICAL, spacing=10)

        form_grid = GtkProvider.Grid()
        form_grid.set_column_spacing(10)
        form_grid.set_row_spacing(10)

        dispositivos_label = GtkProvider.Label(label="Dispositivos:")
        dispositivos_label.set_halign(GtkProvider.Align.START)
        self.list_box_dispositivos = GtkProvider.ListBox()
        self.list_box_dispositivos.set_selection_mode(GtkProvider.SelectionMode.NONE)

        self.dispositivos_combo = GtkProvider.ComboBox()
        self.load_all_dispositivos()

        add_dispositivo_button = GtkProvider.Button(label="Adicionar Dispositivo")
        add_dispositivo_button.connect("clicked", self.on_add_dispositivo_clicked)

        form_grid.attach(dispositivos_label, 0, 0, 1, 1)
        form_grid.attach(self.list_box_dispositivos, 0, 1, 2, 1)

        form_grid.attach(self.dispositivos_combo, 0, 2, 1, 1)
        form_grid.attach(add_dispositivo_button, 1, 2, 1, 1)

        box.pack_start(form_grid, True, True, 0)

        box.set_margin_top(20)
        box.set_margin_bottom(20)
        box.set_margin_start(20)
        box.set_margin_end(20)

        self.add_content(box)

        if self.pessoa_id:
            self.load_dispositivos()

    def load_all_dispositivos(self):
        dispositivos = DispositivoService().find_all()

        list_store = GtkProvider.ListStore(str, int)
        self.dispositivos_combo.set_model(list_store)

        cell_renderer = GtkProvider.CellRendererText()
        self.dispositivos_combo.pack_start(cell_renderer, True)
        self.dispositivos_combo.add_attribute(cell_renderer, "text", 0)

        for dispositivo in dispositivos:
            iter = list_store.append()
            list_store.set(iter, 0, dispositivo.nome, 1, dispositivo.id)

        if dispositivos:
            self.dispositivos_combo.set_active(0)

    def load_dispositivos(self):
        dispositivos = DispositivoService().find_by_id_pessoa(self.pessoa_id)
        self.list_box_dispositivos.foreach(lambda widget: self.list_box_dispositivos.remove(widget))

        if dispositivos:
            for dispositivo in dispositivos:
                self.create_dispositivo_row(dispositivo)

    def create_dispositivo_row(self, dispositivo):
        row = GtkProvider.ListBoxRow()

        row_box = GtkProvider.Box(orientation=GtkProvider.Orientation.HORIZONTAL, spacing=10)

        label = GtkProvider.Label(label=dispositivo.nome)
        row_box.pack_start(label, True, True, 0)

        delete_button = WidgetUtils.create_icon_button(self.on_delete_clicked, "trash", dispositivo.id)

        row_box.pack_start(delete_button, False, False, 0)

        row.add(row_box)

        self.list_box_dispositivos.add(row)

    def on_add_dispositivo_clicked(self, button):
        self.add_new_dispositivo()

    def add_new_dispositivo(self):
        active_iter = self.dispositivos_combo.get_active_iter()

        if not active_iter:
            return

        dispositivo_id = self.dispositivos_combo.get_model().get(active_iter, 1)[0]

        if not dispositivo_id:
            return

        disp_pessoa = DispositivoPessoa()
        disp_pessoa.pe_id = self.pessoa_id
        disp_pessoa.di_id = dispositivo_id
        DispositivoPessoaService().save(disp_pessoa)

        self.load_dispositivos()
        self.load_all_dispositivos()
        self.callback()
        self.hide()

    def on_delete_clicked(self):
        pass