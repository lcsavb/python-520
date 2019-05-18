import os
import time

import pymongo


MONGODB_URL = 'mongodb://admin:aPSFpvXDLWfHtEX7@cluster0-shard-00-00-nstlp.mongodb.net:27017,cluster0-shard-00-01-nstlp.mongodb.net:27017,cluster0-shard-00-02-nstlp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'



try:
    client = pymongo.MongoClient(MONGODB_URL)
    db = client.chat
except Exception as err:
    print('ERRO: {}'.format(err))
    exit()


def cadastrar_mensagem(nome, mensagem):
    db.mensagens.insert({
        'nome': nome,
        'mensagem': mensagem,
        'hora': time.strftime('%d-%m-%Y %H:%M:%S')
    })


def ler_mensagens():
    ultima = [x for x in db.mensagens.find().sort('_id', pymongo.DESCENDING)]
    while True:
        atual = [x for x in db.mensagens.find().sort('_id', pymongo.DESCENDING)]
        if atual != ultima:
            ultima = atual
            print('[{}] {} : {}'. format(
            atual[0]['hora'], atual[0]['nome'], atual[0]['mensagem']
            ))
        time.sleep(1.0 / 30.0)