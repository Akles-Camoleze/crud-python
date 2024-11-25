from app.interface.pages.pessoa.modaldispositivo.ModalDispositivoPessoa import ModalDispositivos
from app.interface.pages.pessoa.modalpessoa.ModalPessoa import ModalPessoa
from app.interface.providers.gdk.GdkPixbufProvider import GdkPixbufProvider
from app.interface.providers.gtk.GtkProvider import GtkProvider
from app.interface.services.pessoa.PessoaService import PessoaService
from app.interface.utils.WidgetUtils import WidgetUtils


class ListagemPessoaPage(GtkProvider.Box):
    def __init__(self):
        super().__init__(orientation=GtkProvider.Orientation.VERTICAL, spacing=10)

        header_grid = GtkProvider.Grid()
        header_grid.set_column_spacing(10)
        header_grid.set_column_homogeneous(True)

        header_grid.attach(GtkProvider.Label(label="Nome", hexpand=True, halign=GtkProvider.Align.START), 0, 0, 1, 1)
        header_grid.attach(GtkProvider.Label(label="Idade", hexpand=True, halign=GtkProvider.Align.START), 1, 0, 1, 1)
        header_grid.attach(GtkProvider.Label(label="CPF", hexpand=True, halign=GtkProvider.Align.START), 2, 0, 1, 1)
        header_grid.attach(GtkProvider.Label(label="Ações", hexpand=True, halign=GtkProvider.Align.START), 3, 0, 1, 1)

        self.pack_start(header_grid, False, False, 0)

        self.list_box = GtkProvider.ListBox()
        self.pack_start(self.list_box, True, True, 0)

        add_button = GtkProvider.Button(label="Adicionar")
        add_button.connect("clicked", self.on_add_clicked)
        self.pack_start(add_button, False, False, 0)

        self.update_list()

    def create_row(self, list_box, pessoa):
        row = GtkProvider.ListBoxRow()
        grid = GtkProvider.Grid()
        grid.set_column_spacing(10)
        grid.set_column_homogeneous(True)

        self.column_name(grid, pessoa)

        self.column_idade(grid, pessoa)

        self.column_cpf(grid, pessoa)

        self.column_actions(grid, pessoa)

        row.add(grid)
        list_box.add(row)

    def column_actions(self, grid, pessoa):
        actions_box = GtkProvider.HBox(spacing=10)
        edit_button = WidgetUtils.create_icon_button(self.on_edit_clicked, "edit", pessoa.id)
        actions_box.pack_start(edit_button, False, False, 0)

        delete_button = WidgetUtils.create_icon_button(self.on_menu_clicked, "trash", pessoa.id)
        actions_box.pack_start(delete_button, False, False, 0)

        menu_button = WidgetUtils.create_icon_button(self.on_menu_clicked, "menu", pessoa)
        actions_box.pack_start(menu_button, False, False, 0)

        grid.attach(actions_box, 3, 0, 1, 1)

    def column_cpf(self, grid, pessoa):
        cpf_label = GtkProvider.Label(label=pessoa.cpf)
        cpf_label.set_hexpand(True)
        cpf_label.set_halign(GtkProvider.Align.START)
        grid.attach(cpf_label, 2, 0, 1, 1)

    def column_idade(self, grid, pessoa):
        idade_label = GtkProvider.Label(label=str(pessoa.idade))
        idade_label.set_hexpand(True)
        idade_label.set_halign(GtkProvider.Align.START)
        grid.attach(idade_label, 1, 0, 1, 1)

    def column_name(self, grid, pessoa):
        nome_label = GtkProvider.Label(label=f"{pessoa.nome} {pessoa.sobrenome}")
        nome_label.set_hexpand(True)
        nome_label.set_halign(GtkProvider.Align.START)
        grid.attach(nome_label, 0, 0, 1, 1)

    def on_delete_clicked(self, button, pessoa_id):
        print(f"Excluindo pessoa com ID: {pessoa_id}")
        PessoaService().delete_by_id(pessoa_id)
        self.update_list()

    def on_add_clicked(self, button):
        modal = ModalPessoa(self, self.update_list)
        modal.show_all()

    def on_menu_clicked(self, button, pessoa):
        modal = ModalDispositivos(self, self.update_list, pessoa)
        modal.show_all()

    def on_edit_clicked(self, button, pessoa_id):
        modal = ModalPessoa(self, self.update_list, pessoa_id)
        modal.show_all()

    def update_list(self):
        self.list_box.foreach(lambda widget: self.list_box.remove(widget))

        pessoas = PessoaService().find_all()

        if pessoas:
            for pessoa in pessoas:
                self.create_row(self.list_box, pessoa)
        else:
            empty_label = GtkProvider.Label(label="Nenhuma pessoa encontrada.", hexpand=True, halign=GtkProvider.Align.CENTER)
            self.list_box.add(empty_label)

        self.list_box.queue_resize()
        self.show_all()
