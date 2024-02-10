import requests
from src.vehicle_entity import VehicleEntity
from src.vehicle_provder_base import VehicleProviderBase
from typing import Dict
import bs4

class TabelaFipeProBrProvider(VehicleProviderBase):

    def __init__(self):
        super().__init__()
        self.data_source = "https://tabelafipe.pro.br/"

    def _fetch_plate_page(self, plate: str) -> str:
        res = requests.get(f"{self.data_source}placa/{plate}", headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
        })

        if res.status_code != 200:
            raise Exception("Error fetching plate page")

        return res.text

    def _rows_to_vehicle_map(self, rows: bs4.element.ResultSet) -> Dict[str, str]:
        vehicle_map = {}

        for row in rows:
            columns = row.find_all("td")

            if len(columns) != 2:
                continue

            ## [:-1] because the text has a ":" at the end

            vehicle_map[columns[0].text[:-1].strip()] = columns[1].text.strip()

        return vehicle_map

    def _parse_plate_page(self, plate_page: str) -> VehicleEntity:
        soup = bs4.BeautifulSoup(plate_page, "html.parser")

        data_table = soup.find("table", {"class": "fipeTablePriceDetail"})

        rows = data_table.find_all("tr")

        veh_map = self._rows_to_vehicle_map(rows)

        # print(veh_map)

        return VehicleEntity(
            # placa=veh_map.get("Placa", ""),
            chassi=veh_map.get("Chassi", None),

            marca=veh_map.get("Marca", None),
            modelo=veh_map.get("Modelo", None),
            cor=veh_map.get("Cor", None),

            tipo_veiculo=veh_map.get("Tipo Veiculo", None),
            combustivel=veh_map.get("Combustível", None),
            passageiros=veh_map.get("Passageiros", None),

            cidade=veh_map.get("Município", None),
            estado=veh_map.get("UF", None),

            ano=veh_map.get("Ano", None),
            ano_modelo=veh_map.get("Ano Modelo", None),

            # fipe=[],
        )


    def fetch_vehicle(self, plate: str) -> VehicleEntity:
        plate_page = self._fetch_plate_page(plate)

        veh = self._parse_plate_page(plate_page)
        veh.placa = plate.upper()

        return veh
