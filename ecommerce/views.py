from django.shortcuts import render, HttpResponse
import psycopg2 as pg
import os

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
    
    context_produtos = {}

    for produto in produtos:
        
        ecommerce_produtos['titulo'] = produto[1]
        ecommerce_produtos['descricao'] = produto[2]
        ecommerce_produtos['imagem'] = produto[3]
        ecommerce_produtos['preco'] = produto[4]
        ecommerce_produtos['preco_prom'] = produto[5]

        context_produtos.update({produto[0] : ecommerce_produtos})
    print(f'{context_produtos}\n\n\n')


    return render(request, 'ecommerce.html', context={'context_produtos' : context_produtos})
