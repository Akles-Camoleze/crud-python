from app.interface.providers.gtk.GtkProvider import GtkProvider
from app.interface.services.pessoa.PessoaService import PessoaService


class ListagemPessoaPage(GtkProvider.Box):
    def __init__(self):
        super().__init__(orientation=GtkProvider.Orientation.VERTICAL)
        self.list_store = GtkProvider.ListStore(str, int, str)

        pessoas = PessoaService().find_all()

        for pessoa in pessoas:
            self.list_store.append([f"{pessoa.nome} {pessoa.sobrenome}", pessoa.idade, pessoa.cpf])

        tree_view = GtkProvider.TreeView(model=self.list_store)

        renderer_text_nome = GtkProvider.CellRendererText()
        column_nome = GtkProvider.TreeViewColumn("Nome", renderer_text_nome, text=0)
        tree_view.append_column(column_nome)

        renderer_text_idade = GtkProvider.CellRendererText()
        column_idade = GtkProvider.TreeViewColumn("Idade", renderer_text_idade, text=1)
        tree_view.append_column(column_idade)

        renderer_text_cpf = GtkProvider.CellRendererText()
        column_cpf = GtkProvider.TreeViewColumn("CPF", renderer_text_cpf, text=2)
        tree_view.append_column(column_cpf)

        self.pack_start(tree_view, True, True, 0)
