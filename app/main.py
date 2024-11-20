import gi

from app.controller.dispositivo.DispositivoController import DispositivoController
from app.controller.dispositivopessoa.DispositivoPessoaController import DispositivoPessoaController
from app.controller.pessoa.PessoaController import PessoaController
from app.interface.abas.AbasWindow import AbasWindow
from app.interface.providers.gtk.GtkProvider import GtkProvider
from app.repository.dispositivo.DispositivoRepository import DispositivoRepository
from app.repository.dispositivopessoa.DispositivoPessoaRepository import DispositivoPessoaRepository
from app.repository.pessoa.PessoaRepository import PessoaRepository
from config.config import Config

gi.require_version('Gtk', '3.0')


def initialize_singletons():
    Config()

def initialize_repositories():
    PessoaRepository()
    DispositivoRepository()
    DispositivoPessoaRepository()

def initialize_controllers():
    PessoaController()
    DispositivoController()
    DispositivoPessoaController()

if __name__ == "__main__":
    initialize_singletons()
    initialize_repositories()
    initialize_controllers()

    nomes = [pessoa.nome for pessoa in PessoaController().find_all()]

    window = AbasWindow(nomes)
    window.show_all()
    GtkProvider.main()
