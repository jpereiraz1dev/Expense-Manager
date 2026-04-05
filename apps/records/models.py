from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from decimal import Decimal

CHOICES_TYPE = [
        ("LAZER","Lazer"),
        ("ESTUDO","Estudo"),
        ("INVESTIMENTO","Investimento"),
        ("SAUDE","Saude"),
        ("OUTROS","Outros"),
    ]

# Valor desejado para comprar um item
class MetaInvestimento(models.Model):
    PRAZO_CHOICES = [
        ('CURTO', 'Curto Prazo'),
        ('MEDIO', 'Medio Prazo'),
        ('LONGO', 'Longo Prazo'),
    ]

    item_nome = models.CharField(max_length=100) # Ex: "Playstation 5" ou "Aposentadoria"
    valor_alvo = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(Decimal('0.00'))]) # Ex: 4500.00
    prazo = models.CharField(max_length=10, choices=PRAZO_CHOICES)
    
    def __str__(self):
        return f"{self.item_nome} ({self.get_prazo_display()})"
    
    @property
    def total_acumulado(self):
        # Soma todos os "Gastos" (aportes) relacionados a esta meta
        total = self.aportes.aggregate(models.Sum('valor'))['valor__sum']
        return total or 0

    @property
    def progresso_percentual(self):
        if self.valor_alvo > 0:
            percentual = (self.total_acumulado / self.valor_alvo) * 100
            return round(percentual, 2)
        return 0

# Qualquer gasto mensal nao fixo
class Gasto(models.Model):
    

    tipo = models.CharField(max_length=20, choices=CHOICES_TYPE,blank=False,null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2,blank=False,null=False,validators=[MinValueValidator(Decimal('0.00'))])
    descricao = models.CharField(max_length=200,blank=False,null=False)
    data = models.DateField(default=timezone.now)

    # O "pulo do gato": Só preenchemos isso se for Investimento
    meta_relacionada = models.ForeignKey(
        MetaInvestimento, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='aportes' # Isso permite fazer meta.aportes.all()
    )

    def __str__(self):
        return f"{self.tipo} - {self.descricao}"


# Qualquer gasto mensal fixo
class Fixo(models.Model):
    # Usamos as mesmas escolhas do seu Gasto para bater os dados
    CHOICES_FLUXO =[
        ("ENTRADA","Entrada"),
        ("SAIDA","Saida"),
    ]

    nome = models.CharField(max_length=30,null=False,blank=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(Decimal('0.00'))]) # Essencial!
    fluxo = models.CharField(max_length=20,choices = CHOICES_FLUXO)

    def __str__(self):
        return f"{self.nome} - {self.fluxo}"
    
class Parcela(models.Model):
    nome = models.CharField(max_length=30,null=False,blank=False,default="")
    valor = models.DecimalField(max_digits=10, decimal_places=2,blank=False,null=False,validators=[MinValueValidator(Decimal('0.00'))])
    tipo = models.CharField(max_length=20, choices=CHOICES_TYPE,blank=False,null=False)
    parcelas_pagas = models.IntegerField(blank=False,null=False,default=1)
    parcelas_totais = models.IntegerField(blank=False,null=False,default=10)

    def __str__(self):
        return self.nome

class Planejamento(models.Model):
    tipo = models.CharField(blank=False,null=False,choices=CHOICES_TYPE,unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2,blank=False,null=False,validators=[MinValueValidator(Decimal('0.00'))])

    def __str__(self):
        return self.tipo