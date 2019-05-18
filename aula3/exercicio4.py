<<<<<<< HEAD
from pymongo import MongoClient

client = MongoClient('0.0.0.0', 27017)
db = client.projeto


def extrair_usuarios():
    return list(db.users.find())


def cadastrar_usuario(nome, email, idade):
    usuario = db.users.find_one({'email': email})
    if not usuario:
        db.users.insert({
            'nome': nome,
            'email': email,
            'idade': idade
        })


cadastrar_usuario(
    'Lucas Ricciardi de Salles',
    'lucas.salle@4linux.com.br',
    25
)

for usuario in extrair_usuarios():
    print(usuario)
=======
import pymongo

client = pymongo.MongoClient()

db = client.projeto

# db.users.insert({'nome': 'Cobrinha aamrela'})

# for user in db.users.find():
# 	print(user)

def cadastrar_usuario(nome,email,idade):
	usuario = db.users.find_one({ 'email': email })
	if not usuario:
	    db.users.insert({
	    	'nome': nome,
	    	'email': email,
	    	'idade': int(idade)
	    	})


def extrair_usuarios():
    return list(db.users.find())
    

cadastrar_usuario(
    'Lucas Amorim Vieira de Barros',
    'lcsavb@gmaildfsdfsdfsda.com',
    32
)


for usuario in extrair_usuarios():
	print(usuario)
>>>>>>> 8880a55cdeb7ad8de756d66d41b48b13be37630b
