from app.interface.pages.pessoa.listagem.ListagemPessoaPage import ListagemPessoaPage
from app.interface.providers.gtk.GtkProvider import GtkProvider


class MainPage(GtkProvider.Window):
    def __init__(self):
        super().__init__(title="CRUD em Python")

        self.set_default_size(800, 600)

        self.set_name("main-window")

        notebook = GtkProvider.Notebook()

        page_listagem_pessoa = ListagemPessoaPage()
        list_tab_label = GtkProvider.Label(label="Listagem de Pessoas")
        notebook.append_page(page_listagem_pessoa, list_tab_label)

        self.add(notebook)
        self.connect("destroy", GtkProvider.main_quit)
