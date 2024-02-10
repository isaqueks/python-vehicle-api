from typing import List
from src.fipe_entity import FipeEntity

class VehicleEntity:
    placa: str
    renavam: str
    chassi: str

    marca: str
    modelo: str
    cor: str

    tipo_veiculo: str
    combustivel: str
    passageiros: int

    cidade: str
    estado: str

    ano: int
    ano_modelo: int

    fipe: List[FipeEntity]

    def __init__(self, **kwargs):
        self.placa = kwargs.get("placa", "")
        self.renavam = kwargs.get("renavam", "")
        self.chassi = kwargs.get("chassi", "")

        self.marca = kwargs.get("marca", "")
        self.modelo = kwargs.get("modelo", "")
        self.cor = kwargs.get("cor", "")

        self.tipo_veiculo = kwargs.get("tipo_veiculo", "")
        self.combustivel = kwargs.get("combustivel", "")
        self.passageiros = kwargs.get("passageiros", 0)

        self.cidade = kwargs.get("cidade", "")
        self.estado = kwargs.get("estado", "")

        self.ano = kwargs.get("ano", 0)
        self.ano_modelo = kwargs.get("ano_modelo", 0)

        self.fipe = kwargs.get("fipe", [])

