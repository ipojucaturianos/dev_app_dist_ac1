import brasileirao
import unittest

class TestClientes(unittest.TestCase):
    def test_01_datas_de_jogo(self):
        dados = pega_dados()
        datas = brasileirao.datas_de_jogo(dados)
        self.assertEqual(len(datas), 107)
        self.assertTrue('2018-04-14' in datas)
        self.assertTrue('2018-07-26' in datas)
        self.assertTrue('2018-10-26' in datas)

    def test_02_datas_de_jogo(self):
        dados = pega_dados()
        del dados['fases']['2700']['jogos']['data']['2018-04-14']
        datas = brasileirao.datas_de_jogo(dados)
        self.assertEqual(len(datas), 106)
        self.assertFalse('2018-04-14' in datas)
        self.assertTrue('2018-07-26' in datas)
        self.assertTrue('2018-10-26' in datas)

    def test_03_data_de_um_jogo(self):
        dados = pega_dados()
        self.assertEqual(brasileirao.data_de_um_jogo(
            dados, '102132'), '2018-05-06')
        self.assertEqual(brasileirao.data_de_um_jogo(
            dados, '102187'), '2018-06-06')
        self.assertEqual(brasileirao.data_de_um_jogo(
            dados, '102540'), 'não encontrado')

    def test_04_ids_dos_times_de_um_jogo(self):
        dados = pega_dados()
        t1, t2 = brasileirao.ids_dos_times_de_um_jogo(dados, '102099')
        self.assertTrue(t1 in ['5', '17'])
        self.assertTrue(t2 in ['5', '17'])
        t1, t2 = brasileirao.ids_dos_times_de_um_jogo(dados, '102109')
        self.assertTrue(t1 in ['1', '26'])
        self.assertTrue(t2 in ['1', '26'])

    def test_05_nome_do_time(self):
        dados = pega_dados()
        self.assertEqual(brasileirao.nome_do_time(dados, '1'), 'Flamengo')
        self.assertEqual(brasileirao.nome_do_time(dados, '695'), 'Chapecoense')

    def test_06_nomes_dos_times_de_um_jogo(self):
        dados = pega_dados()
        t1, t2 = brasileirao.nomes_dos_times_de_um_jogo(dados, '102099')
        self.assertTrue(t1 in ['Botafogo', 'Palmeiras'])
        self.assertTrue(t2 in ['Botafogo', 'Palmeiras'])
        t1, t2 = brasileirao.nomes_dos_times_de_um_jogo(dados, '102109')
        self.assertTrue(t1 in ['Flamengo', 'América-MG'])
        self.assertTrue(t2 in ['Flamengo', 'América-MG'])

    def test_07_id_do_time(self):
        dados = pega_dados()
        self.assertEqual(brasileirao.id_do_time(dados, 'Cruzeiro'), '9')
        self.assertEqual(brasileirao.id_do_time(dados, 'Athletico'), '3')

    def test_08_busca_imprecisa_por_nome_de_time(self):
        dados = pega_dados()
        ids_times = brasileirao.busca_imprecisa_por_nome_de_time(
            dados, 'Paulo')
        self.assertTrue('24' in ids_times)
        ids_times = brasileirao.busca_imprecisa_por_nome_de_time(dados, 'SPA')
        self.assertTrue('24' in ids_times)
        ids_times = brasileirao.busca_imprecisa_por_nome_de_time(dados, 'anto')
        self.assertTrue('22' in ids_times)

    def test_09_ids_de_jogos_de_um_time(self):
        dados = pega_dados()
        jogos_chapeco = brasileirao.ids_de_jogos_de_um_time(dados, '695')
        self.assertEqual(len(jogos_chapeco), 38)
        self.assertTrue('102330' in jogos_chapeco)
        self.assertTrue('102422' in jogos_chapeco)
        jogos_santos = brasileirao.ids_de_jogos_de_um_time(dados, '22')
        self.assertEqual(len(jogos_santos), 38)
        self.assertTrue('102208' in jogos_santos)
        self.assertTrue('102259' in jogos_santos)

    def test_10_datas_de_jogos_de_um_time(self):
        dados = pega_dados()
        datas_santos = brasileirao.datas_de_jogos_de_um_time(dados, 'Santos')
        self.assertEqual(len(datas_santos), 38)
        self.assertTrue('2018-04-21' in datas_santos)
        self.assertTrue('2018-10-13' in datas_santos)
        datas_chapeco = brasileirao.datas_de_jogos_de_um_time(dados,
                                                              'Chapecoense')
        self.assertEqual(len(datas_chapeco), 38)
        self.assertTrue('2018-11-25' in datas_chapeco)
        self.assertTrue('2018-12-02' in datas_chapeco)

    def test_11_dicionario_de_gols(self):
        dados = pega_dados()
        dic_gols = brasileirao.dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'], 34)
        # Vou falsificar os dados para testar se você está lendo direito da estrutura ou não.
        dados['fases']['2700']['jogos']['id']['102330']['placar2'] = 1
        dic_gols = brasileirao.dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'], 35)
        dados['fases']['2700']['jogos']['id']['102422']['placar2'] = 2
        dic_gols = brasileirao.dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'], 36)
        dados['fases']['2700']['jogos']['id']['102422']['placar2'] = 12
        dic_gols = brasileirao.dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'], 46)

    def test_12_time_que_fez_mais_gols(self):
        dados = pega_dados()
        time = brasileirao.time_que_fez_mais_gols(dados)
        self.assertEqual(time, '17')
        # Vou falsificar os dados para testar se você está lendo direito da estrutura ou não.
        dados['fases']['2700']['jogos']['id']['102422']['placar2'] = 120
        time = brasileirao.time_que_fez_mais_gols(dados)
        self.assertEqual(time, '695')

    def test_13_dicionario_id_estadio_e_nro_jogos(self):
        dados = pega_dados()
        estadios = brasileirao.dicionario_id_estadio_e_nro_jogos(dados)
        self.assertEqual(estadios['72'], 16)
        # Vou falsificar os dados para testar se você está lendo direito da estrutura ou não.
        dados['fases']['2700']['jogos']['id']['102097']['estadio_id'] = '72'
        estadios = brasileirao.dicionario_id_estadio_e_nro_jogos(dados)
        self.assertEqual(estadios['72'], 17)

    def test_14_qtos_libertadores(self):
        dados = pega_dados()
        self.assertEqual(brasileirao.qtos_libertadores(dados), 6)
        # Vou falsificar os dados para testar se você está lendo direito da estrutura ou não.
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa'] = '1-8'
        self.assertEqual(brasileirao.qtos_libertadores(dados), 8)

    def test_15_ids_dos_melhor_classificados(self):
        dados = pega_dados()
        self.assertEqual(brasileirao.ids_dos_melhor_classificados(dados, 10),
                         ["17", "1", "15", "13", "24", "4", "3", "9", "5", "22"])
        self.assertEqual(brasileirao.ids_dos_melhor_classificados(dados, 5),
                         ["17", "1", "15", "13", "24"])
        self.assertEqual(brasileirao.ids_dos_melhor_classificados(dados, 3),
                         ["17", "1", "15"])

    def test_16_classificados_libertadores(self):
        dados = pega_dados()
        self.assertEqual(brasileirao.classificados_libertadores(
            dados), ["17", "1", "15", "13", "24", "4"])
        # Vou falsificar os dados para testar se você está lendo direito da estrutura ou não.
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa'] = '1-8'
        self.assertEqual(brasileirao.classificados_libertadores(
            dados), ["17", "1", "15", "13", "24", "4", "3", "9"])

    def test_17_rebaixados(self):
        dados = pega_dados()
        self.assertEqual(brasileirao.rebaixados(
            dados), ['76', '26', '21', '18'])
        # Vou falsificar os dados para testar se você está lendo direito da estrutura ou não.
        dados['fases']['2700']['faixas-classificacao']['classifica3']['faixa'] = '15-20'
        self.assertEqual(brasileirao.rebaixados(dados), [
                         '33', '25', '76', '26', '21', '18'])

    def test_18_classificacao_do_time_por_id(self):
        dados = pega_dados()
        self.assertEqual(
            brasileirao.classificacao_do_time_por_id(dados, '17'), 1)
        self.assertEqual(
            brasileirao.classificacao_do_time_por_id(dados, '30'), 11)
        self.assertEqual(
            brasileirao.classificacao_do_time_por_id(dados, '695'), 14)
        self.assertEqual(brasileirao.classificacao_do_time_por_id(
            dados, '1313'), 'não encontrado')


def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestClientes)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


'''
Essa função é utilizada para ler o arquivo JSON.
'''


def pega_dados():
    import json
    with open('/home/filipeverrone/Documentos/Faculdade/EC3/DEVAPP/codes/brasileirao/ano2018.json') as f:
        return json.load(f)


if __name__ == '__main__':
    runTests() 



# def dicionario_de_gols(dados):
#     dicio = {}

#     def teste():
#         print("Teste")

#     for chave in dados["equipes"]:
#         # print(ids_de_jogos_de_um_time(dados, dados["equipes"][chave]["id"]))
#         teste()
#         # print(dados["equipes"][chave]["id"])