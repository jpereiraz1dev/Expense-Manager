from django.shortcuts import render,redirect
import datetime
from .forms import GastoForm
from .models import Gasto,Fixo,MetaInvestimento,Parcela,Planejamento
from django.db.models import Sum
from django.http import JsonResponse
from django.db.models import F
from .models import CHOICES_TYPE

def index(request):

    # Gastos Reais (Variáveis)
    def buscar_gasto(tipo_cat):
        total = Gasto.objects.filter(tipo=tipo_cat).aggregate(Sum('valor'))['valor__sum']
        return float(total) if total else 0.0

    # Metas Planejadas
    def buscar_planejado(tipo_cat):
        obj = Planejamento.objects.filter(tipo=tipo_cat).first()
        return float(obj.valor) if obj else 0.0

    total_parcelas_aberto = Parcela.objects.filter(
        parcelas_pagas__lt=F('parcelas_totais')
    ).aggregate(Sum('valor'))['valor__sum'] or 0

    # 2. Pegar Gasto Fixo
    gasto_fixo_real = Fixo.objects.filter(fluxo="SAIDA").aggregate(Sum('valor'))['valor__sum'] or 0

    # 3. Montar a lista de LABELS (6 itens)
    labels = [x[1] for x in CHOICES_TYPE]
    labels.append("Parcelas")
    labels.append("Gasto Fixo")

    # 4. Montar a lista de DADOS REAIS (6 itens)
    # Note que as parcelas entram como o último item para bater com o label
    dados_gastos = [buscar_gasto(x[0]) for x in CHOICES_TYPE]
    dados_gastos.append(float(gasto_fixo_real)) 
    dados_gastos.append(float(total_parcelas_aberto)) 

    # 5. Montar a lista de METAS (6 itens)
    # Se você não planeja "parcelas", coloque 0.0 no final
    dados_planejados = [buscar_planejado(x[0]) for x in CHOICES_TYPE]
    dados_planejados.append(float(gasto_fixo_real)) # A meta de gasto fixo eh igual ao gasto atual
    dados_planejados.append(float(total_parcelas_aberto)) # A meta de gasto das parcelas eh igual ao gasto atual


    total_gasto_real = sum(dados_gastos)
    total_planejado = float(Fixo.objects.filter(fluxo="ENTRADA").aggregate(Sum('valor'))['valor__sum'] or 0)
    context = {
        "labels": labels,
        "dados_gastos": dados_gastos,
        "dados_planejados": dados_planejados,
        "total_gasto_real": total_gasto_real,
        "total_planejado": total_planejado,
        "total_parcelas_aberto": total_parcelas_aberto,
        "valor_excedido": total_gasto_real - total_planejado,
    }

    return render(request, "records/index.html", context)


def records(request):
    # Captura o filtro da URL (ex: ?tipo=LAZER)
    filtro_tipo = request.GET.get('tipo')

    # Busca as QuerySets originais
    gastos_qs = Gasto.objects.all().order_by('-data')
    fixos_qs = Fixo.objects.all()

    # Aplica o filtro se ele existir
    if filtro_tipo:
        if filtro_tipo == 'FIXO':
            # Se filtrar por Fixo, esvaziamos a lista de gastos pontuais
            gastos_qs = gastos_qs.none()
        else:
            # Se filtrar por uma categoria específica (LAZER, etc), esvaziamos os Fixos
            gastos_qs = gastos_qs.filter(tipo=filtro_tipo)
            fixos_qs = fixos_qs.none()

    # Cálculos dos Cards (sempre baseados no total, ou no filtrado - você escolhe)
    # Aqui vou manter o total geral nos cards para referência
    total_entradas = float(Fixo.objects.filter(fluxo="ENTRADA").aggregate(Sum('valor'))['valor__sum'] or 0)
    total_saidas = float(Fixo.objects.filter(fluxo="SAIDA").aggregate(Sum('valor'))['valor__sum'] or 0) + \
                   float(Gasto.objects.aggregate(Sum('valor'))['valor__sum'] or 0)

    # Montagem da lista unificada (mesma lógica anterior)
    lista_extrato = []
    for f in fixos_qs:
        lista_extrato.append({'data': 'Todo mês', 'descricao': f.nome, 'categoria': 'Fixo', 'valor': float(f.valor), 'fluxo': f.fluxo, 'status': 'Recorrente'})
    
    for g in gastos_qs:
        lista_extrato.append({'data': g.data, 'descricao': g.descricao, 'categoria': g.tipo, 'valor': float(g.valor), 'fluxo': 'SAIDA', 'status': 'Confirmado'})

    context = {
        'total_entradas': total_entradas,
        'total_saidas': total_saidas,
        'saldo_atual': total_entradas - total_saidas,
        'extrato': lista_extrato,
        'filtro_atual': filtro_tipo # Passamos para o HTML saber qual botão destacar
    }
    return render(request, 'records/records.html', context)

def add_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save() # O Django salva no banco sozinho!
            return redirect('index')
    else:
        form = GastoForm()
    
    return render(request, 'add_gasto.html', {'form': form})

def investimentos(request):
    metas = MetaInvestimento.objects.all().order_by('prazo', 'item_nome')
    total_geral = sum(m.total_acumulado for m in metas)
    
    return render(request, 'records/investimentos.html', {
        'metas': metas,
        'total_geral': total_geral
    })


def fixos(request):
    if request.method == "POST":
        # Lógica para salvar via AJAX
        nome = request.POST.get('nome')
        valor = request.POST.get('valor')
        fluxo = request.POST.get('fluxo')
        
        novo = Fixo.objects.create(nome=nome, valor=valor, fluxo=fluxo)
        
        # Em vez de renderizar a página, devolve só os dados do novo item
        return JsonResponse({
            "success": True,
            "nome": novo.nome,
            "valor": float(novo.valor),
            "fluxo": novo.fluxo
        })


    entradas = Fixo.objects.filter(fluxo="ENTRADA")
    saidas = Fixo.objects.filter(fluxo="SAIDA")
    
    context = {
        "entradas": entradas,
        "saidas": saidas
    }

    return render(request,"records/fixos.html",context)

def parcelas(request):
    parcelas = Parcela.objects.all()

    total_comprometido = parcelas.aggregate(Sum('valor'))['valor__sum'] or 0

    context = {
        'parcelas': parcelas,
        'total_parcelas_mes': total_comprometido,
    }
    
    return render(request, 'records/parcelas.html', context)


# Pagina de Planejamento
def planejamento(request):
    from .models import CHOICES_TYPE

    # 1. Cálculos de Base
    receita_total = Fixo.objects.filter(fluxo="ENTRADA").aggregate(Sum('valor'))['valor__sum'] or 0
    gastos_fixos = Fixo.objects.filter(fluxo="SAIDA").aggregate(Sum('valor'))['valor__sum'] or 0
    total_parcelas = Parcela.objects.all().aggregate(Sum('valor'))['valor__sum'] or 0
    saldo_disponivel = float(receita_total) - float(gastos_fixos) - float(total_parcelas)

    if request.method == "POST":
        soma_planejamento = 0
        dados_para_salvar = {}

        # Primeiro, calculamos quanto o usuário quer planejar no total
        for key, value in request.POST.items():
            if key.startswith('valor_'):
                valor = float(value) if value else 0
                soma_planejamento += valor
                dados_para_salvar[key.replace('valor_', '')] = valor

        # VALIDAÇÃO CRÍTICA
        if soma_planejamento > saldo_disponivel:
            return JsonResponse({
                'success': False, 
                'message': f'Orçamento insuficiente! Você só tem R$ {saldo_disponivel:.2f} livres, mas tentou planejar R$ {soma_planejamento:.2f}.'
            }, status=400)

        # Se passou na validação, salva
        for tipo, valor in dados_para_salvar.items():
            Planejamento.objects.update_or_create(tipo=tipo, defaults={'valor': valor})
        
        return JsonResponse({'success': True})

    # 2. Buscar o que já está planejado no banco
    planejados_db = {p.tipo: p.valor for p in Planejamento.objects.all()}
    
    # 3. Calcular a soma total do que já foi planejado
    total_ja_planejado = sum(float(v) for v in planejados_db.values())
    
    # 4. Calcular quanto sobra de fato (Saldo - Planejado)
    saldo_restante = saldo_disponivel - total_ja_planejado

    # 5. Montar lista de categorias
    categorias = []
    cores = [
        'pink', 'indigo', 'rose', 'purple', 'emerald', 'amber', 
        'teal', 'cyan', 'orange', 'lime', 'fuchsia', 'violet'
    ]
    for i, choice in enumerate(CHOICES_TYPE):
        tipo_id = choice[0]
        categorias.append({
            'id': tipo_id,
            'nome': choice[1],
            'sub': f'Meta para {choice[1]}',
            'cor': cores[i % len(cores)],
            'valor_atual': planejados_db.get(tipo_id, 0)
        })

    return render(request, 'records/planejamento.html', {
        'categorias': categorias,
        'saldo_disponivel': saldo_disponivel,
        'saldo_restante': saldo_restante, # Envia o que sobrou
    })