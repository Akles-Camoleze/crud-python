from app.interface.components.window.rounded.RoundedWindow import RoundedWindow
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
        padded_container = GtkProvider.Box(orientation=GtkProvider.Orientation.VERTICAL, spacing=10)
        padded_container.set_margin_top(20)
        padded_container.set_margin_bottom(20)
        padded_container.set_margin_start(20)
        padded_container.set_margin_end(20)
        padded_container.pack_start(page_listagem_pessoa, True, True, 0)

        list_tab_label = GtkProvider.Label(label="Listagem de Pessoas")
        notebook.append_page(padded_container, list_tab_label)

        # Adiciona o notebook ao container principal da janela
        self.add_content(notebook)

        # Configurações de finalização
        self.connect("destroy", GtkProvider.main_quit)
        self.show_all()
