from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import constants
from django.core.files.base import File
from django.contrib import messages
from .models import EcommerceImages
import psycopg2 as pg
import os

def painel_admin(request):
    return render(request, 'painel_admin.html')

def cadastrar_produto(request):
    if request.method == 'POST':
        os.system('cls||clear')

        titulo = request.POST.get('produto-titulo')
        descricao = request.POST.get('produto-descricao')
        preco = request.POST.get('produto-preco')
        preco_prom = request.POST.get('produto-preco-prom') if request.POST.get('produto-preco-prom') != '' else 'null'
        estoque = request.POST.get('produto-estoque')
        imagem = request.POST.get('produto-imagem')

        altura = request.POST.get('produto-altura') if request.POST.get('produto-altura') != '' else 'null'
        largura = request.POST.get('produto-largura') if request.POST.get('produto-largura') != '' else 'null'
        comprimento = request.POST.get('produto-comprimento') if request.POST.get('produto-comprimento') != '' else 'null'
        peso = request.POST.get('produto-peso') if request.POST.get('produto-peso') != '' else 'null'

        if not titulo or not descricao or not preco or not estoque or not imagem:
            messages.add_message(request, constants.ERROR, 'Os campos marcados com (*) são obrigatórios!')
            return redirect('/admin/painel_admin/')
        else:

            conn = pg.connect(host = 'localhost',
                              database = 'ecommerce',
                              user = 'admin',
                              password = 'admin')
            
            cursor = conn.cursor()

            sql = f"""
insert into products.products (titulo,
								descricao,
								imagens,
								preco,
								preco_prom,
								estoque,
								altura,
								largura,
								comprimento,
								peso) values ('{titulo}',
                                              '{descricao}',
                                              '{imagem}',
                                              {preco},
                                              {preco_prom},
                                              {estoque},
                                              {altura},
                                              {largura},
                                              {comprimento},
                                              {peso})
"""
            
            cursor.execute(sql)
            conn.commit()

            return redirect('/admin/painel_admin')

    else:
        return redirect('admin/painel_admin')