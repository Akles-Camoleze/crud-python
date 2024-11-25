from app.interface.components.window.rounded.RoundedWindow import RoundedWindow
from app.interface.pages.dispositivo.listagem.ListagemDispositivoPage import ListagemDispositivoPage
from app.interface.pages.pessoa.listagem.ListagemPessoaPage import ListagemPessoaPage
from app.interface.providers.gtk.GtkProvider import GtkProvider


class MainPage(RoundedWindow):
    def __init__(self):
        # Inicializa a janela base com título e estilos específicos
        super().__init__(title="CRUDzin em Python", radius=10, bg_color="#ffffff", shadow=True)

        # Configurações da janela principal
        self.set_default_size(800, 600)
        self.set_name("main-window")

        # Criação de um notebook (abas)
        notebook = GtkProvider.Notebook()

        # Adiciona a página de Listagem de Pessoas com padding
        page_listagem_pessoa = ListagemPessoaPage()
        padded_container_pessoa = GtkProvider.Box(orientation=GtkProvider.Orientation.VERTICAL, spacing=10)
        padded_container_pessoa.set_margin_top(20)
        padded_container_pessoa.set_margin_bottom(20)
        padded_container_pessoa.set_margin_start(20)
        padded_container_pessoa.set_margin_end(20)
        padded_container_pessoa.pack_start(page_listagem_pessoa, True, True, 0)

        list_tab_label_pessoa = GtkProvider.Label(label="Listagem de Pessoas")
        notebook.append_page(padded_container_pessoa, list_tab_label_pessoa)

        # Adiciona a página de Listagem de Dispositivos com padding
        page_dispositivo = ListagemDispositivoPage()
        padded_container_dispositivo = GtkProvider.Box(orientation=GtkProvider.Orientation.VERTICAL, spacing=10)
        padded_container_dispositivo.set_margin_top(20)
        padded_container_dispositivo.set_margin_bottom(20)
        padded_container_dispositivo.set_margin_start(20)
        padded_container_dispositivo.set_margin_end(20)
        padded_container_dispositivo.pack_start(page_dispositivo, True, True, 0)

        list_tab_label_dispositivo = GtkProvider.Label(label="Listagem de Dispositivos")
        notebook.append_page(padded_container_dispositivo, list_tab_label_dispositivo)

        # Adiciona o notebook ao container principal da janela
        self.add_content(notebook)

        # Configurações de finalização
        self.connect("destroy", GtkProvider.main_quit)
        self.show_all()
