import psycopg2

import psycopg2.extras

conn = psycopg2.connect(
    user='lcsavb',
    password='rraptnor',
    host='127.0.0.1',
    database='4linux'
)


cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

cursor.execute('SELECT * FROM scripts;')
for resultado in cursor.fetchall():
    print(resultado)


def cadastrar_usuario(nome,email,idade):
    email_nao_existe = True
    if email_nao_existe
    cursor.execute("""
    INSERT INTO users (nome,email,idade)
    VALUES ('{}', '{}', {});
""".format(nome, email, idade))
    conn.commit()


def extrair_usuarios():
    cursor.execute('SELECT * FROM users;')
    return cursor.fetchall()


cadastrar_usuario(
    'Lucas Amorim Vieira de Barros',
    'lcsavb@gmail.com',
    32
)


for usuario in extrair_usuarios():
    print(usuario)