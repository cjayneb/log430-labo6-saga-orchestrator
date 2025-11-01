"""
Saga states
SPDX-License-Identifier: LGPL-3.0-or-later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from enum import Enum

# TODO: Veuillez consulter le diagramme de machine à états pour en savoir plus
class OrderSagaState(Enum):
    CREATING_ORDER = 1
    DECREASING_STOCK = 2
    CREATING_PAYMENT = 3
    INCREASING_STOCK = 4
    CANCELLING_ORDER = 5
    COMPLETED = 6
