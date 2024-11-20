import gi
import sys

from app.controller.DispositivoController import DispositivoController
from app.controller.DispositivoPessoaController import DispositivoPessoaController
from app.controller.PessoaController import PessoaController
from app.repository.DispositivoPessoaRepository import DispositivoPessoaRepository
from app.repository.DispositivoRepository import DispositivoRepository
from app.repository.PessoaRepository import PessoaRepository
from config.config import Config
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

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

    print(len(PessoaController().find_all()))
    print(len(DispositivoController().find_all()))
    print(len(DispositivoPessoaController().find_all()))

    print(PessoaController().find_by_id(1))
    print(DispositivoController().find_by_id(1))
    print(DispositivoPessoaController().find_by_id(1))

    sys.stdout.flush()

    window = Gtk.Window(title="Teste GTK")
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()
