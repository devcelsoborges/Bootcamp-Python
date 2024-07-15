from typing import Annotated

from pydantic import Field
from contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT Square', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do centro de treinamento', example='Bairro:Aeroclube Rua: Francisco...,Nº1', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietário do centro de treinamento', example='Carlos', max_length=30)]

