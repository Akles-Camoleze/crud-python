from app.entities.pessoa.Pessoa import Pessoa
from app.interface.providers.gtk.GtkProvider import GtkProvider
from app.interface.services.pessoa.PessoaService import PessoaService


class ModalPessoa(GtkProvider.Window):
    def __init__(self, parent, callback, pessoa_id=None):
        super().__init__(title="Adicionar Pessoa", modal=True)

        self.parent = parent
        self.callback = callback

        self._pessoa = None
        if pessoa_id:
            self._pessoa = PessoaService().find_by_id(pessoa_id)

        form_grid = GtkProvider.Grid()
        form_grid.set_column_spacing(10)
        form_grid.set_row_spacing(10)

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

        save_button = GtkProvider.Button(label="Salvar")
        save_button.connect("clicked", self.on_save_clicked)
        form_grid.attach(save_button, 1, 4, 1, 1)

        if self._pessoa:
            self.nome_entry.set_text(self._pessoa.nome)
            self.sobrenome_entry.set_text(self._pessoa.sobrenome)
            self.idade_entry.set_text(str(self._pessoa.idade))
            self.cpf_entry.set_text(self._pessoa.cpf)

        self.add(form_grid)

    def on_save_clicked(self, button):
        if not self._pessoa:
            self._pessoa = Pessoa()

        self._pessoa.nome = self.nome_entry.get_text()
        self._pessoa.sobrenome = self.sobrenome_entry.get_text()
        self._pessoa.idade = int(self.idade_entry.get_text())
        self._pessoa.cpf = self.cpf_entry.get_text()

        PessoaService().save(self._pessoa)

        self.hide()
        self._pessoa = None

        if self.callback:
            self.callback()
