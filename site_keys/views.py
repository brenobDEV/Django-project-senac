from django.contrib.auth.decorators import login_required
from django.db.models import F, Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import KeysForm
from .models import Key

def home_view(request):
    jogos = Key.objects.filter(ativo=True).order_by("titulo")
    ofertas = Key.objects.filter(ativo=True, preco_anterior__isnull=False, preco__lt=F("preco_anterior")).order_by("titulo")
    return render(request, "home.html", {"jogos": jogos, "ofertas": ofertas})

def keys_shop(request):
    jogos = Key.objects.filter(ativo=True).order_by("titulo")
    termo = request.GET.get("q", "").strip()
    plataforma = request.GET.get("plataforma", "").strip()
    apenas_ofertas = request.GET.get("ofertas") == "1"

    if termo:
        jogos = jogos.filter(Q(titulo__icontains=termo) | Q(plataforma__icontains=termo) | Q(regiao__icontains=termo))
    if plataforma:
        jogos = jogos.filter(plataforma=plataforma)
    if apenas_ofertas:
        jogos = jogos.filter(preco_anterior__isnull=False, preco__lt=F("preco_anterior"))

    plataformas = Key.objects.filter(ativo=True).values_list("plataforma", flat=True).distinct().order_by("plataforma")
    context = {"jogos": jogos, "termo": termo, "plataforma_selecionada": plataforma, "plataformas": plataformas, "apenas_ofertas": apenas_ofertas}
    return render(request, "keys_shop.html", context)

def detalhe_jogo(request, pk):
    jogo = get_object_or_404(Key, pk=pk)
    return render(request, "detalhe_jogo.html", {"jogo": jogo})

@login_required
def criar_jogo(request):
    form = KeysForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        jogo = form.save()
        return redirect("detalhe_jogo", pk=jogo.pk)
    return render(request, "formulario_jogo.html", {"form": form, "modo": "criar"})

@login_required
def editar_jogo(request, pk):
    jogo = get_object_or_404(Key, pk=pk)
    form = KeysForm(request.POST or None, instance=jogo)
    if request.method == "POST" and form.is_valid():
        jogo = form.save()
        return redirect("detalhe_jogo", pk=jogo.pk)
    return render(request, "formulario_jogo.html", {"form": form, "modo": "editar", "jogo": jogo})

@login_required
def excluir_jogo(request, pk):
    jogo = get_object_or_404(Key, pk=pk)
    if request.method == "POST":
        jogo.delete()
        return redirect("keys_shop")
    return render(request, "confirmar_exclusao.html", {"jogo": jogo})

@login_required
def perfil(request):
    return render(request, "perfil.html")

@login_required
def minhas_compras(request):
    return render(request, "minhas_compras.html")

@login_required
def configuracoes(request):
    return render(request, "configuracoes.html")

def detalhes_produto_view(request, id):  
    produto_banco = get_object_or_404(Key, id=id)  
    return render(request, 'detalhes.html', {'produto': produto_banco})