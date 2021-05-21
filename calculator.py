from api import req


class Convert:
    def __init__(self,first_valute,money,second_valute=None):
        self.first_valute=first_valute
        self.second_value=second_valute
        self.money=money
    @staticmethod
    def money_find(name):
        for i in reversed(req()['data']):
            if i['name'] == name:
                return i['dgtlBuyRate']

    def convert_to_lari(self):
        one_name = self.first_valute
        money = self.money
        result = money * self.money_find(one_name)

        return result

    def convert_to_other(self,valuta):
        first_valut=self.money_find(valuta)
        second_result=self.money_find(self.first_valute)
        current=second_result/first_valut
        result=self.money*current

        return result


