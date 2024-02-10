from providers.tabelafipe_pro_br import TabelaFipeProBrProvider

provider = TabelaFipeProBrProvider()

print(provider.fetch_vehicle("MJX2659").__dict__)
