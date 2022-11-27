from financialMovement.serializers import FinancialSerializer
from financialMovement.models import FinancialMovement
from rest_framework.views import APIView, Response
from django.shortcuts import render
from . import models


def upload_file(request):
    if request.method == 'POST':
            
            file_name = list(request.FILES.keys())[0]
            data = request.FILES[file_name].read().decode().split("\n")
            for x in data:
                result = { "tipo": int(x[0:1]), "data": x[1:9], "valor": float(x[9:19])/100, "CPF": x[19:30], "cartao": x[30:42], "hora": x[42:48], "dono": x[48:62], "loja": x[62:81] } 
                serializer = FinancialSerializer(data=result)
                serializer.is_valid(raise_exception=True)
                serializer.save()

    documents = models.FinancialMovement.objects.all()
    total_joao = 0
    total_maria = 0
    total_marcos = 0
    total_jose = 0
    total_maria2 = 0
    for x in documents:
        if x.loja == "BAR DO JOÃO":

            if x.tipo == 2 or x.tipo == 3 or x.tipo == 9:
                total_joao -= float(x.valor)
            else:
                total_joao += float(x.valor)

        if x.loja == "LOJA DO Ó - MATRIZ":

            if x.tipo == 2 or x.tipo == 3 or x.tipo == 9:
                total_maria -= float(x.valor)
            else:
                total_maria += float(x.valor)

        if x.loja == "MERCADO DA AVENIDA":

            if x.tipo == 2 or x.tipo == 3 or x.tipo == 9:
                total_marcos -= float(x.valor)
            else:
                total_marcos += float(x.valor)

        if x.loja == "MERCEARIA 3 IRMÃOS":

            if x.tipo == 2 or x.tipo == 3 or x.tipo == 9:
                total_jose -= float(x.valor)
            else:
                total_jose += float(x.valor)

        if x.loja == "LOJA DO Ó - FILIAL":

            if x.tipo == 2 or x.tipo == 3 or x.tipo == 9:
                total_maria2 -= float(x.valor)
            else:
                 total_maria2 += float(x.valor)


    obj = [{"loja": "BAR DO JOÃO", "valor": total_joao, "dono": "JOÃO MACEDO" },
    {"loja": "LOJA DO Ó - MATRIZ", "valor": total_maria, "dono": "MARIA JOSEFINA"},
    {"loja": "MERCADO DA AVENIDA", "valor": total_marcos, "dono": "MARCOS PEREIRA"},
    {"loja": "MERCEARIA 3 IRMÃOS", "valor": total_jose, "dono": "JOSÉ COSTA"},
    {"loja": "LOJA DO Ó - FILIAL", "valor": total_maria2, "dono": "MARIA JOSEFINA"},
    ]

    return render(request, "financialMovement/upload_file.html", context = {
        "files": obj
    })



class FinancialViews(APIView):
    serializer_class = FinancialSerializer
    queryset = FinancialMovement.objects.all()

    def post(self,request):
        if request.method == 'POST':
            
            file_name = list(request.FILES.keys())[0]
            data = request.FILES[file_name].read().decode().split("\n")
            for x in data:
                result = { "tipo": int(x[0:1]), "data": x[1:9], "valor": float(x[9:19])/100, "CPF": x[19:30], "cartao": x[30:42], "hora": x[42:48], "dono": x[48:62], "loja": x[62:81] } 
                serializer = FinancialSerializer(data=result)
                serializer.is_valid(raise_exception=True)
                serializer.save()
            
        return Response(request.FILES[file_name])



    def get(self, request):
        user = FinancialMovement.objects.all()
        serializer = FinancialSerializer (user, many=True)
        return Response(serializer.data)





