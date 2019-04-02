import unittest
from src import dicionarios

class DictionaryTest(unittest.TestCase):

    def test_must_get_all_keys(self):
        dict_keys = ["nome", "país"]
        d = { "nome": "Vladimir Lênin", "país": "Rússia" }
        actual = dicionarios.get_keys_from_dict(d)
        self.assertEqual(dict_keys, actual)

    def test_must_get_all_values(self):
        dict_values = ["Frida Kahlo", "México"]
        d = { "nome": "Frida Kahlo", "país": "México" }
        actual = dicionarios.get_values_from_dict(d)
        self.assertEqual(dict_values, actual)
    
    def test_must_transform_two_lists_into_dicts(self):
        dict_keys = ["nome", "país"]
        dict_values = ["Thomas Sankara", "Burkina Faso"]
        expected =  { "nome":"Thomas Sankara", "país": "Burkina Faso" }
        actual = dicionarios.transform_two_lists_into_dict(dict_keys, dict_values)
        self.assertEqual(actual, expected)
    
    def test_must_switch_keys_and_values(self):
        wrong_order = { "Che Guevara":"nome", "Argentina":"país" }
        expected = { "nome":"Che Guevara", "país": "Argentina" }
        actual = dicionarios.switch_keys_and_values(wrong_order)
        self.assertEqual(actual, expected)

    def test_must_create_new_dict_from_two_dicts(self):
        grande_homem = { "nome":"Josef Stalin", "país": "Geórgia" }
        curriculum = {
                        "feitos": ["Salvou o mundo derrotando 3/4 dos exécitos nazistas",
                                "impediu que um novo reich surgisse na Ucrânia",
                                "Mandou tropas pra ajudar os parça espanhóis durante a guerra civil"]
                     }
        expected = {
                        "nome":"Josef Stalin", "país": "Geórgia",
                        "feitos": ["Salvou o mundo derrotando 3/4 dos exécitos nazistas",
                                "impediu que um novo reich surgisse na Ucrânia",
                                "Mandou tropas pra ajudar os parça espanhóis durante a guerra civil"]
                     }
        actual = dicionarios.merge_two_dicts(grande_homem, curriculum)
        self.assertEqual(actual, expected)
    
    def test_must_remove_non_string_indexes(self):
        d = {
                "nome": "Leon Trostky", 
                1: "picareta", 
                "funcoes": ["montar o exército vermelho", 
                            "ser expulso do exército vermelho por incompetência",
                            "odiar camponeses",
                            "ser contrarrevolucionário"]
            }
        expected = {
                "nome": "Leon Trostky", 
                "funcoes": ["montar o exército vermelho", 
                            "ser expulso do exército vermelho por incompetência",
                            "odiar camponeses",
                            "ser contrarrevolucionário"]
            }
        actual = dicionarios.remove_non_string_indexes(d)
        self.assertEqual(actual, expected)