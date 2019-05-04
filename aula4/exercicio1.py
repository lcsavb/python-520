import datetime

'''
    Quando o usuário passar um ticket válido na catraca,
    a catraca deve liberar e o preço da passagem deve ser 
    descontado do saldo do ticket. Um ticket válido é um 
    ticket que está dentro do prazo de validade, tem saldo 
    suficiente para pagar a passagem e pertence a mesma
    concessionária da catraca.
'''
#################################################################################################################
# Constantes
#################################################################################################################

PRECO_DA_PASSAGEM = 4.00


#################################################################################################################
# Testes
#################################################################################################################

class ErroTicketExpirado(Exception):
    pass

class ErroConcessionariaDiferente(Exception):
    pass

class ErroSaldoInsuficiente(Exception):
    pass


#################################################################################################################
# Classes
#################################################################################################################

class Ticket():

    def __init__(self, validade, saldo, concessionaria):
        self.validade = validade
        self.saldo = saldo
        self.concessionaria = concessionaria


class Catraca():

    def __init__(self,concessionaria):
        self.concessionaria = concessionaria
        self.estado = 'travada'


    def liberar(self, ticket):
        if ticket.validade < datetime.datetime.now():
            raise ErroTicketExpirado

        if ticket.saldo < PRECO_DA_PASSAGEM:
            raise ErroSaldoInsuficiente

        if ticket.concessionaria != self.concessionaria:
            raise ErroConcessionariaDiferente

        ticket.saldo = ticket.saldo - PRECO_DA_PASSAGEM
        self.estado = 'liberada'

    def esta_liberada(self):
        if self.estado == 'liberada':
            return True
        return False

if __name__ == '__main__':
#################################################################################################################
# Testes
#################################################################################################################

    try:

        validade = datetime.datetime.now() - datetime.timedelta(days=2)
        saldo = PRECO_DA_PASSAGEM + 300.00
        concessionaria = 'sptrans'

        ticket = Ticket(validade, saldo, concessionaria)

        catraca = Catraca(concessionaria='sptrans')
        catraca.liberar(ticket)

        print('BUG ENCONTRADO: TICKET EXPIRADO FUNCIONOU')

    except ErroTicketExpirado:
        print('Teste de ticket expirado ok')


    #teste de ticket sem saldo

    try:

        validade = datetime.datetime.now() + datetime.timedelta(days=30)
        saldo = PRECO_DA_PASSAGEM - 1.00
        concessionaria = 'sptrans'

        ticket = Ticket(validade, saldo, concessionaria)
        catraca = Catraca(concessionaria='sptrans')
        catraca.liberar(ticket)

        print('BUG ENCONTRADO: TICKET COM SALDO INSUFICIENTE FUNCIONOU')


    except ErroSaldoInsuficiente:
        print('Teste de saldo insuficiente ok')


    #teste de concessionária diferente:

    try:

        validade = datetime.datetime.now() + datetime.timedelta(days=30)
        saldo = 400
        concessionaria = 'emtu'

        ticket = Ticket(validade, saldo, concessionaria)
        catraca = Catraca(concessionaria='sptrans')
        catraca.liberar(ticket)

        print('BUG ENCONTRADO: TICKET DE OUTRA CONCESSIONÁRIA FUNCIONOU')

    except ErroConcessionariaDiferente:
        print('Teste de concessionária ok')


    # teste de catraca liberada

    validade = datetime.datetime.now() + datetime.timedelta(days=2)
    saldo = PRECO_DA_PASSAGEM + saldo
    concessionaria = 'sptrans'

    ticket = Ticket(validade, saldo, concessionaria)

    catraca = Catraca(concessionaria='sptrans')
    catraca.liberar(ticket)

    try:

        assert catraca.esta_liberada()
        assert ticket.saldo == (saldo - PRECO_DA_PASSAGEM)

        print('teste ok')
    except:
        print('BUG encontrado. Catraca não liberou com ticket váido e/ou não descontou o saldo.')
