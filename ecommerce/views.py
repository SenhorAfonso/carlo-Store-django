from django.shortcuts import render, HttpResponse, redirect
import psycopg2 as pg
import os
from django.contrib.messages import constants
from django.contrib import messages

def ecommerce(request):
    os.system('cls||clear')

    conn = pg.connect(host = 'localhost',
                        database = 'ecommerce',
                        user = 'admin',
                        password = 'admin')

    cursor = conn.cursor()

    SQL = 'select * from products.products'
    cursor.execute(SQL)
    produtos = cursor.fetchall()

    context_produtos = {}

    for produto in produtos:

        ecommerce_produtos = {'imagem' : '',
                            'descricao' : '',
                            'titulo' : '',
                            'preco' : '',
                            'preco_prom' : '',
                            'estoque' : '',
                            'altura' : '',
                            'largura' : '',
                            'comprimento' : '',
                            'peso' : ''}
        
        idP = produto[0]
        ecommerce_produtos['titulo'] = produto[1]
        ecommerce_produtos['descricao'] = produto[2]
        ecommerce_produtos['imagem'] = produto[3]
        ecommerce_produtos['preco'] = produto[4]
        ecommerce_produtos['preco_prom'] = produto[5]

        context_produtos[idP] = ecommerce_produtos


    return render(request, 'ecommerce.html', context={'context_produtos' : context_produtos})


produto = ''

def item(request, id):

    global produto

    conn = pg.connect(host = 'localhost',
                        database = 'ecommerce',
                        user = 'admin',
                        password = 'admin')

    cursor = conn.cursor()

    SQL = f'select * from products.products where id = {id}'
    cursor.execute(SQL)
    produto = cursor.fetchone()



    return render(request, 'item.html', context={'produto' : produto})

def pagamento(request):

    global produto

    if request.method == 'POST':
        
        if bool(request.POST.get('checkbox')):
            return render(request, 'pagamento.html', context={'produto': produto, 'pagamento' : '1'})
        
        messages.add_message(request, constants.ERROR, 'Selecione uma forma de pagamento!')
        return render(request, 'item.html', context={'produto' : produto})
    else:
        return render(request, 'item.html', context={'produto' : produto})
