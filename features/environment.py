from behave.runner import Context

from src.gorest_handler import GorestAPIHandler
from src.my_classes import Calculator


def before_all(context: Context):
    context.calculator = Calculator()
    context.gorest_handler = GorestAPIHandler("Bearer 106f3e7a3a32bcf14303de2cbfa28452a0e1dd3880d2a11676bc11971f186ebb")
