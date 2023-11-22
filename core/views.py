from django.shortcuts import redirect, render

from core.models import Carro

def home(request):
    carros = Carro.objects.all()
    print("home")
    return render(request, "index.html", {"carros": carros})

def areaAdmin(request):
    carros = Carro.objects.all()
    print("Area de admin")
    return render(request, "areaAdmin.html", {"carros": carros})

def salvar(request):
    cMarca = request.POST.get("marca")
    cModelo = request.POST.get("modelo")
    cAnoFabricacao = request.POST.get("anoFabricacao") 
    cPotenciaCV = request.POST.get("potenciaCV") 
    cPreco = request.POST.get("preco")
    cImgUrl = request.POST.get("imgUrl")
    Carro.objects.create(marca=cMarca, modelo=cModelo, anoFabricacao=cAnoFabricacao, potenciaCV=cPotenciaCV, preco=cPreco, imgUrl=cImgUrl)
    carros = Carro.objects.all()
    return render(request, "areaAdmin.html", {"carros": carros})

def editar(request, id):
    carro = Carro.objects.get(id=id)
    return render(request, "update.html", {"carro": carro})

def update(request, id):
    cMarca = request.POST.get("marca")
    cModelo = request.POST.get("modelo") 
    cAnoFabricacao = request.POST.get("anoFabricacao") 
    cpotenciaCV = request.POST.get("potenciaCV")
    cPreco = request.POST.get("preco")
    cImgUrl = request.POST.get("imgUrl") 
    carro = Carro.objects.get(id=id)
    carro.marca = cMarca
    carro.modelo = cModelo
    carro.anoFabricacao = cAnoFabricacao
    carro.potenciaCV = cpotenciaCV
    carro.preco = cPreco
    carro.imgUrl = cImgUrl
    carro.save()
    return redirect(areaAdmin)

def delete(request, id):
    carro = Carro.objects.get(id=id)
    carro.delete()
    return redirect(areaAdmin)
    