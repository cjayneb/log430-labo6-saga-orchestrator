"""
Handler: decrease stock
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import requests
from logger import Logger
from handlers.handler import Handler
from order_saga_state import OrderSagaState

class DecreaseStockHandler(Handler):
    """ Handle the stock check-out of a given list of products and quantities. Trigger rollback of previous steps in case of failure. """

    def __init__(self, order_item_data):
        """ Constructor method """
        self.order_item_data = order_item_data
        super().__init__()

    def run(self):
        """Call StoreManager to check out from stock"""
        try:
            # TODO: effectuer une requête à /stocks pour modifier le stock
            """
            POST my-api-gateway-address/stocks ...
            json={
                    "items": self.order_item_data,
                    "operation": "-"
                },
            """
            response_ok = True
            if response_ok:
                self.logger.debug("La sortie des articles du stock a réussi")
                return OrderSagaState.CREATING_PAYMENT
            else:
                self.logger.error(f"Erreur : {response_ok}")
                return OrderSagaState.CANCELLING_ORDER
            
        except Exception as e:
            self.logger.error("La sortie des articles du stock a échoué : " + str(e))
            return OrderSagaState.CANCELLING_ORDER
        
    def rollback(self):
        """ Call StoreManager to revert stock check out (in other words, check-in the previously checked-out product and quantity) """
        # TODO: effectuer une requête à /stocks pour modifier le stock
        self.logger.debug("L'entrée des articles dans le stock a réussi")
        return OrderSagaState.CANCELLING_ORDER