from app.interface.pages.dispositivo.modaldispositivo.ModalDispositivo import ModalDispositivo
from app.interface.providers.gtk.GtkProvider import GtkProvider
from app.interface.services.dispositivo.DispositivoService import DispositivoService
from app.interface.utils.WidgetUtils import WidgetUtils

class ListagemDispositivoPage(GtkProvider.Box):
    def __init__(self):
        super().__init__(orientation=GtkProvider.Orientation.VERTICAL, spacing=10)

        # Header com as colunas "Nome" e "Ações"
        header_grid = GtkProvider.Grid()
        header_grid.set_column_spacing(10)
        header_grid.set_column_homogeneous(True)

        header_grid.attach(GtkProvider.Label(label="Nome", hexpand=True, halign=GtkProvider.Align.START), 0, 0, 1, 1)
        header_grid.attach(GtkProvider.Label(label="Ações", hexpand=True, halign=GtkProvider.Align.START), 1, 0, 1, 1)

        self.pack_start(header_grid, False, False, 0)

        # Listbox onde os dispositivos serão listados
        self.list_box = GtkProvider.ListBox()
        self.pack_start(self.list_box, True, True, 0)

        # Botão para adicionar novo dispositivo
        add_button = GtkProvider.Button(label="Adicionar Dispositivo")
        add_button.connect("clicked", self.on_add_clicked)
        self.pack_start(add_button, False, False, 0)

        self.update_list()

    def create_row(self, list_box, dispositivo):
        row = GtkProvider.ListBoxRow()
        grid = GtkProvider.Grid()
        grid.set_column_spacing(10)
        grid.set_column_homogeneous(True)

        # Coluna de Nome
        self.column_name(grid, dispositivo)

        # Coluna de Ações
        self.column_actions(grid, dispositivo)

        row.add(grid)
        list_box.add(row)

    def column_actions(self, grid, dispositivo):
        actions_box = GtkProvider.HBox(spacing=10)
        edit_button = WidgetUtils.create_icon_button(self.on_edit_clicked, "edit", dispositivo.id)
        actions_box.pack_start(edit_button, False, False, 0)

        delete_button = WidgetUtils.create_icon_button(self.on_delete_clicked, "trash", dispositivo.id)
        actions_box.pack_start(delete_button, False, False, 0)

        grid.attach(actions_box, 1, 0, 1, 1)

    def column_name(self, grid, dispositivo):
        nome_label = GtkProvider.Label(label=dispositivo.nome)
        nome_label.set_hexpand(True)
        nome_label.set_halign(GtkProvider.Align.START)
        grid.attach(nome_label, 0, 0, 1, 1)

    def on_delete_clicked(self, button, dispositivo_id):
        print(f"Excluindo dispositivo com ID: {dispositivo_id}")
        DispositivoService().delete_by_id(dispositivo_id)
        self.update_list()

    def on_add_clicked(self, button):
        modal = ModalDispositivo(self, self.update_list)
        modal.show_all()

    def on_edit_clicked(self, button, dispositivo_id):
        modal = ModalDispositivo(self, self.update_list, dispositivo_id)
        modal.show_all()

    def update_list(self):
        self.list_box.foreach(lambda widget: self.list_box.remove(widget))

        dispositivos = DispositivoService().find_all()

        if dispositivos:
            for dispositivo in dispositivos:
                self.create_row(self.list_box, dispositivo)
        else:
            empty_label = GtkProvider.Label(label="Nenhum dispositivo encontrado.", hexpand=True, halign=GtkProvider.Align.CENTER)
            self.list_box.add(empty_label)

        self.list_box.queue_resize()
        self.show_all()
