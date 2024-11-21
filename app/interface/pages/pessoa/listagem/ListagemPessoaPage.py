from app.interface.providers.gtk.GtkProvider import GtkProvider
from app.interface.services.pessoa.PessoaService import PessoaService


class ListagemPessoaPage(GtkProvider.Box):
    def __init__(self):
        super().__init__(orientation=GtkProvider.Orientation.VERTICAL, spacing=10)

        header_grid = GtkProvider.Grid()
        header_grid.set_column_spacing(10)
        header_grid.set_column_homogeneous(True)

        header_grid.attach(GtkProvider.Label(label="Nome", hexpand=True, halign=GtkProvider.Align.START), 0, 0, 1, 1)
        header_grid.attach(GtkProvider.Label(label="Idade", hexpand=True, halign=GtkProvider.Align.START), 1, 0, 1, 1)
        header_grid.attach(GtkProvider.Label(label="CPF", hexpand=True, halign=GtkProvider.Align.START), 2, 0, 1, 1)
        header_grid.attach(GtkProvider.Label(label="Ações", hexpand=True, halign=GtkProvider.Align.END), 3, 0, 1, 1)

        self.pack_start(header_grid, False, False, 0)

        list_box = GtkProvider.ListBox()
        for pessoa in PessoaService().find_all():
            self.create_row(list_box, pessoa)

        self.pack_start(list_box, True, True, 0)

    def create_row(self, list_box, pessoa):
        row = GtkProvider.ListBoxRow()
        grid = GtkProvider.Grid()
        grid.set_column_spacing(10)
        grid.set_column_homogeneous(True)

        nome_label = GtkProvider.Label(label=f"{pessoa.nome} {pessoa.sobrenome}")
        nome_label.set_hexpand(True)
        nome_label.set_halign(GtkProvider.Align.START)
        grid.attach(nome_label, 0, 0, 1, 1)

        idade_label = GtkProvider.Label(label=str(pessoa.idade))
        idade_label.set_hexpand(True)
        idade_label.set_halign(GtkProvider.Align.START)
        grid.attach(idade_label, 1, 0, 1, 1)

        cpf_label = GtkProvider.Label(label=pessoa.cpf)
        cpf_label.set_hexpand(True)
        cpf_label.set_halign(GtkProvider.Align.START)
        grid.attach(cpf_label, 2, 0, 1, 1)

        delete_button = GtkProvider.Button(label="Excluir")
        delete_button.connect("clicked", self.on_delete_clicked, pessoa.id)
        delete_button.set_hexpand(False)
        delete_button.set_halign(GtkProvider.Align.END)
        grid.attach(delete_button, 3, 0, 1, 1)

        row.add(grid)
        list_box.add(row)

    def on_delete_clicked(self, button, pessoa_id):
        print(f"Excluindo pessoa com ID: {pessoa_id}")
        PessoaService().delete_by_id(pessoa_id)
        button.get_parent().get_parent().destroy()

