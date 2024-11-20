from app.controller.BaseController import BaseController
from app.repository.DispositivoPessoaRepository import DispositivoRepository


class DispositivoController(BaseController):
    def __init__(self):
        super().__init__(DispositivoRepository())