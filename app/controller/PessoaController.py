from app.controller.BaseController import BaseController
from app.repository.PessoaRepository import PessoaRepository

class PessoaController(BaseController):
    def __init__(self):
        super().__init__(PessoaRepository())