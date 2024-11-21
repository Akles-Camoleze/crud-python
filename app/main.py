from app.controller.dispositivo.DispositivoController import DispositivoController
from app.controller.dispositivopessoa.DispositivoPessoaController import DispositivoPessoaController
from app.controller.pessoa.PessoaController import PessoaController
from app.interface.pages.MainPage import MainPage
from app.interface.providers.gtk.GtkProvider import GtkProvider
from app.interface.services.pessoa.PessoaService import PessoaService
from app.repository.dispositivo.DispositivoRepository import DispositivoRepository
from app.repository.dispositivopessoa.DispositivoPessoaRepository import DispositivoPessoaRepository
from app.repository.pessoa.PessoaRepository import PessoaRepository
from config.config import Config

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

def initialize_services():
    PessoaService()

if __name__ == "__main__":
    initialize_singletons()
    initialize_repositories()
    initialize_controllers()
    initialize_services()

    window = MainPage()
    window.show_all()
    GtkProvider.main()
