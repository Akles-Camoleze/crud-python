from app.entities.pessoa.Pessoa import Pessoa
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

        list_box.foreach(lambda widget: list_box.remove(widget))

        pessoas = PessoaService().find_all()

        if pessoas:
            for pessoa in pessoas:
                self.create_row(list_box, pessoa)
        else:
            empty_label = GtkProvider.Label(label="Nenhuma pessoa encontrada.", hexpand=True, halign=GtkProvider.Align.CENTER)
            list_box.add(empty_label)

        self.pack_start(list_box, True, True, 0)

        add_button = GtkProvider.Button(label="Adicionar")
        add_button.connect("clicked", self.on_add_clicked)
        self.pack_start(add_button, False, False, 0)

        self.modal = None

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

    def on_add_clicked(self, button):
        if not self.modal:
            self.create_modal()
        self.modal.show_all()

    def create_modal(self):
        # Criando a janela modal
        self.modal = GtkProvider.Window(title="Adicionar Pessoa", modal=True)

        # Criando o formulário
        form_grid = GtkProvider.Grid()
        form_grid.set_column_spacing(10)
        form_grid.set_row_spacing(10)

        # Campos do formulário
        nome_label = GtkProvider.Label(label="Nome:")
        self.nome_entry = GtkProvider.Entry()
        form_grid.attach(nome_label, 0, 0, 1, 1)
        form_grid.attach(self.nome_entry, 1, 0, 1, 1)

        sobrenome_label = GtkProvider.Label(label="Sobrenome:")
        self.sobrenome_entry = GtkProvider.Entry()
        form_grid.attach(sobrenome_label, 0, 1, 1, 1)
        form_grid.attach(self.sobrenome_entry, 1, 1, 1, 1)

        idade_label = GtkProvider.Label(label="Idade:")
        self.idade_entry = GtkProvider.Entry()
        form_grid.attach(idade_label, 0, 2, 1, 1)
        form_grid.attach(self.idade_entry, 1, 2, 1, 1)

        cpf_label = GtkProvider.Label(label="CPF:")
        self.cpf_entry = GtkProvider.Entry()
        form_grid.attach(cpf_label, 0, 3, 1, 1)
        form_grid.attach(self.cpf_entry, 1, 3, 1, 1)

        # Botão para salvar a pessoa
        save_button = GtkProvider.Button(label="Salvar")
        save_button.connect("clicked", self.on_save_clicked)
        form_grid.attach(save_button, 1, 4, 1, 1)

        self.modal.add(form_grid)

    def on_save_clicked(self, button):
        pessoa = Pessoa()
        pessoa.nome = self.nome_entry.get_text()
        pessoa.sobrenome = self.sobrenome_entry.get_text()
        pessoa.idade = int(self.idade_entry.get_text())
        pessoa.cpf = self.cpf_entry.get_text()

        PessoaService().save(pessoa)

        self.modal.hide()
        self.update_list()

    def update_list(self):
        pass

