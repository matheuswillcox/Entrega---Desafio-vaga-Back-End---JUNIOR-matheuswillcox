from rest_framework import serializers
from financialMovement.models import FinancialMovement


class FinancialSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinancialMovement
        fields = [
            "tipo",
            "data",
            "valor",
            "CPF",
            "cartao",
            "hora",
            "dono",
            "loja"
        ]
