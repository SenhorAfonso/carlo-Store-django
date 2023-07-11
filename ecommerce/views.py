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

    ecommerce_produtos = {'id' : [],
                          'titulo' : [],
                          'descricao' : [],
                          'imagens' : [],
                          'preco' : [],
                          'preco_prom' : [],
                          'estoque' : [],
                          'altura' : [],
                          'largura' : [],
                          'comprimento' : [],
                          'peso' : []}
    
    database_produtos = []

    for produto in produtos:
        ecommerce_produtos['id'].append(produto[0])
        ecommerce_produtos['titulo'].append(produto[1].strip())
        ecommerce_produtos['descricao'].append(produto[2].strip())
        ecommerce_produtos['imagens'].append(produto[3].strip())
        ecommerce_produtos['preco'].append(produto[4])
        ecommerce_produtos['preco_prom'].append(produto[5])
        # ecommerce_produtos['estoque'].append(produto[6])
        # ecommerce_produtos['altura'].append(produto[7])
        # ecommerce_produtos['largura'].append(produto[8])
        # ecommerce_produtos['comprimento'].append(produto[9])
        # ecommerce_produtos['peso'].append(produto[10])

    ecommerce_produtos = {1: {'imagem' : 'https://s2-techtudo.glbimg.com/8eyNHGaJd2UyYTWwpNa_qjTfshQ=/0x0:695x460/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2022/C/o/p7vJQNRQGI80AyrcsNZQ/9.png', 'titulo' : 'NOTEBOOKAAAAAAAAAAAAAAAAA', 'descricao' : 'notebook pica', 'preco' : '3232'},
                          2: {'imagem' : 'https://live.staticflickr.com/65535/53036859180_97120cee3c_c.jpg', 'titulo' : 'CARRO', 'descricao' : 'carro top', 'preco' : '12312'}}

    return render(request, 'ecommerce.html', context={'ecommerce_produtos' : ecommerce_produtos})
