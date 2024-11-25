from app.entities.dispositivo.Dispositivo import Dispositivo
from app.interface.components.window.rounded.RoundedWindow import RoundedWindow
from app.interface.providers.gtk.GtkProvider import GtkProvider
from app.interface.services.dispositivo.DispositivoService import DispositivoService


class ModalDispositivo(RoundedWindow):
    def __init__(self, parent, callback, dispositivo_id=None):
        super().__init__(title=f"{'Editar' if dispositivo_id else 'Adicionar'} Dispositivo", modal=True)

        self.parent = parent
        self.callback = callback

        self._dispositivo = None
        if dispositivo_id:
            self._dispositivo = DispositivoService().find_by_id(dispositivo_id)

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

        save_button = GtkProvider.Button(label="Salvar")
        save_button.connect("clicked", self.on_save_clicked)
        box.pack_start(save_button, False, False, 0)

        if self._dispositivo:
            self.nome_entry.set_text(self._dispositivo.nome)

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
        if not self._dispositivo:
            self._dispositivo = Dispositivo()

        self._dispositivo.nome = self.nome_entry.get_text()

        # Salva o dispositivo utilizando o serviço
        DispositivoService().save(self._dispositivo)

        # Esconde o modal e limpa a variável _dispositivo
        self.hide()
        self._dispositivo = None

        # Chama o callback para atualizar a lista
        if self.callback:
            self.callback()
