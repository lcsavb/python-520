import datetime
import unittest

import exercicio1 as scooby

class CatracaTeste(unittest.TestCase):

    def test_ticket_vencido(self):
        
        validade = datetime.datetime.now() - datetime.timedelta(days=2)
        saldo = scooby.PRECO_DA_PASSAGEM + 300.00
        concessionaria = 'sptrans'

        ticket = scooby.Ticket(validade, saldo, concessionaria)

        catraca = scooby.Catraca(concessionaria='sptrans')

        with self.assertRaises(scooby.ErroTicketExpirado):
            catraca.liberar(ticket)

    def test_saldo_insuficiente(self):

        validade = datetime.datetime.now() + datetime.timedelta(days=30)
        saldo = scooby.PRECO_DA_PASSAGEM - 1.00
        concessionaria = 'sptrans'

        ticket = scooby.Ticket(validade, saldo, concessionaria)
        catraca = scooby.Catraca(concessionaria='sptrans')

        with self.assertRaises(scooby.ErroSaldoInsuficiente):
            catraca.liberar(ticket)


    def test_erro_concessionaria_diferente(self):

        validade = datetime.datetime.now() + datetime.timedelta(days=30)
        saldo = scooby.PRECO_DA_PASSAGEM + 400.00
        concessionaria = 'emtu'

        ticket = scooby.Ticket(validade, saldo, concessionaria)
        catraca = scooby.Catraca(concessionaria='sptrans')

        with self.assertRaises(scooby.ErroConcessionariaDiferente):
            catraca.liberar(ticket)

    def test_estado_catraca(self):

        validade = datetime.datetime.now() + datetime.timedelta(days=2)
        saldo = scooby.PRECO_DA_PASSAGEM + 1
        concessionaria = 'sptrans'

        ticket = scooby.Ticket(validade, saldo, concessionaria)

        catraca = scooby.Catraca(concessionaria='sptrans')
        catraca.liberar(ticket)

        cond_1 = catraca.esta_liberada()
        cond_2 = ticket.saldo == (saldo - scooby.PRECO_DA_PASSAGEM)

        self.assertTrue(cond_1 and cond_2)



if __name__ == '__main__':
    unittest.main()