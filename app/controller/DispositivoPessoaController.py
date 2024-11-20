from app.controller.BaseController import BaseController
from app.repository.DispositivoPessoaRepository import DispositivoPessoaRepository


class DispositivoController(BaseController):
    def __init__(self):
        super().__init__(DispositivoPessoaRepository())