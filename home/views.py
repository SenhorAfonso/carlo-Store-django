from django.shortcuts import render, redirect
import psycopg2 as pg
import os
from django.contrib import messages
from django.contrib.messages import constants

def home(request):
    return render(request, 'home.html')

def realizar_login(request):
    os.system('cls||clear')
    login_user = request.POST.get('email-input')
    login_password = request.POST.get('senha-input')

    conn = pg.connect(host = 'localhost',
                      database = 'users',
                      user = 'admin',
                      password = 'admin')
    
    cursor = conn.cursor()
    sql = f"select user_name, user_password, is_admin from users.users u where u.user_name = '{login_user}' and u.user_password = '{login_password}'"
    cursor.execute(sql)

    users = cursor.fetchall()

    if users:
        if users[0][2] == 'true':
            pass
            #TODO: logar e redirecionar para a página administrativa
        else:
            pass
            #TODO: logar e redirecionar para a home do e-commerce
    else:
        #TODO: redirecionar para a página de cadastro
        return redirect('/home/realizar_cadastro/')

    return redirect('/home/')

def realizar_cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        login_user = request.POST.get('email-input')
        login_password = request.POST.get('senha-input')
        login_confirm_password = request.POST.get('confirma-senha-input')

        if login_confirm_password != login_password:
            messages.add_message(request, constants.WARNING, 'As senhas não são iguais!')
            return redirect('/home/realizar_cadastro/')

        conn = pg.connect(host = 'localhost',
                        database = 'users',
                        user = 'admin',
                        password = 'admin')
        
        cursor = conn.cursor()
        sql = f"insert into users.users (user_name, user_password, is_admin) values ('{login_user}', '{login_password}', false)"

        try:
            cursor.execute(sql)
            conn.commit()
        except: #TODO: fazer mensagens de erro mais explicativas
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar novo usuário. Por favor, tente novamente')
        else:
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')

        return redirect('/home/')
