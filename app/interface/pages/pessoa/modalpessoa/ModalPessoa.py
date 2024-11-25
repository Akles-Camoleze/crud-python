from app.entities.pessoa.Pessoa import Pessoa
from app.interface.components.window.rounded.RoundedWindow import RoundedWindow
from app.interface.providers.gtk.GtkProvider import GtkProvider
from app.interface.services.pessoa.PessoaService import PessoaService


class ModalPessoa(RoundedWindow):
    def __init__(self, parent, callback, pessoa_id=None):
        super().__init__(title=f"{'Editar' if pessoa_id else 'Adicionar'} Pessoa", modal=True)

        self.parent = parent
        self.callback = callback

        self._pessoa = None
        if pessoa_id:
            self._pessoa = PessoaService().find_by_id(pessoa_id)

        box = GtkProvider.Box(orientation=GtkProvider.Orientation.VERTICAL, spacing=20)
        box.set_halign(GtkProvider.Align.CENTER)
        box.set_valign(GtkProvider.Align.CENTER)
        box.set_hexpand(True)

        box.set_margin_top(20)
        box.set_margin_bottom(20)
        box.set_margin_start(20)
        box.set_margin_end(20)

        box.set_name("modal_box")

        nome_box = self.create_field("Nome:")
        self.nome_entry = nome_box[1]
        box.pack_start(nome_box[0], False, False, 0)

        sobrenome_box = self.create_field("Sobrenome:")
        self.sobrenome_entry = sobrenome_box[1]
        box.pack_start(sobrenome_box[0], False, False, 0)

        idade_box = self.create_field("Idade:")
        self.idade_entry = idade_box[1]
        box.pack_start(idade_box[0], False, False, 0)

        cpf_box = self.create_field("CPF:")
        self.cpf_entry = cpf_box[1]
        box.pack_start(cpf_box[0], False, False, 0)

        save_button = GtkProvider.Button(label="Salvar")
        save_button.connect("clicked", self.on_save_clicked)
        box.pack_start(save_button, False, False, 0)

        if self._pessoa:
            self.nome_entry.set_text(self._pessoa.nome)
            self.sobrenome_entry.set_text(self._pessoa.sobrenome)
            self.idade_entry.set_text(str(self._pessoa.idade))
            self.cpf_entry.set_text(self._pessoa.cpf)

        self.add_content(box)

    def create_field(self, label_text):
        field_box = GtkProvider.Box(orientation=GtkProvider.Orientation.VERTICAL, spacing=5)

        label = GtkProvider.Label(label=label_text)
        label.set_xalign(0)

        entry = GtkProvider.Entry()
        entry.set_hexpand(True)
        entry.set_halign(GtkProvider.Align.CENTER)

        field_box.pack_start(label, False, False, 0)
        field_box.pack_start(entry, True, True, 0)

        return field_box, entry

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