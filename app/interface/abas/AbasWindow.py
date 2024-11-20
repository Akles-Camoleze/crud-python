from app.interface.providers.gtk.GtkProvider import GtkProvider


class AbasWindow(GtkProvider.Window):
    def __init__(self, items):
        super().__init__(title="Janela com Abas")

        # Criar o notebook (controle de abas)
        notebook = GtkProvider.Notebook()

        # Criar a primeira aba com uma lista
        list_box = GtkProvider.ListBox()

        for item in items:
            row = GtkProvider.ListBoxRow()
            label = GtkProvider.Label(label=item)
            row.add(label)
            list_box.add(row)

        list_tab_label = GtkProvider.Label(label="Lista")
        notebook.append_page(list_box, list_tab_label)

        label = GtkProvider.Label(label="Conteúdo da Aba 2")
        notebook.append_page(label, GtkProvider.Label(label="Aba 2"))

        self.add(notebook)
        self.connect("destroy", GtkProvider.main_quit)
