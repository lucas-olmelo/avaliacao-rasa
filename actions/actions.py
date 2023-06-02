# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import datetime

class Action_Mostra_Boleto(Action):

    def name(self) -> Text:
        return "action_mostra_boleto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dia = datetime.date.today().day
        mes = datetime.date.today().month

        dia = 26

        if (dia <= 15):
            conta_em_dia = True
        else:
            conta_em_dia = False

        if (conta_em_dia == False):

            dias_atraso = dia - 16
            valor_conta = 149.90

            juros_dia = valor_conta * 0.02
            juros_totais = juros_dia * dias_atraso
            valor_com_juros = valor_conta + juros_totais

            txt_confirmacao = f'O valor da sua conta, referente ao mês {(mes)} é de R${(valor_com_juros):,.2f}, sendo o valor de sua conta (R$149,90), acrescido de R${(juros_totais):,.2f} de juros por {(dias_atraso)} dias de atraso'

        else:
            txt_confirmacao = f"O valor da sua conta, referente ao mês {(mes)} é R$149.90"

        dispatcher.utter_message(text=txt_confirmacao)
        return []
