from django.shortcuts import render, redirect
import psycopg2 as pg
import os
from django.contrib import messages
from django.contrib.messages import constants

def home(request):
    return render(request, 'home.html')

def realizar_login(request):
    from core.utils import ValidaLogin
    os.system('cls||clear')
    login_email = request.POST.get('email-input')
    login_password = request.POST.get('senha-input')

    if not ValidaLogin(request=request, login_email=login_email, login_pass=login_password).validaLogin():
        return redirect('/login/')

    conn = pg.connect(host = 'localhost',
                      database = 'users',
                      user = 'admin',
                      password = 'admin')
    
    cursor = conn.cursor()
    sql = f"select user_name, user_password, is_admin from users.users u where u.user_name = '{login_email}' and u.user_password = '{login_password}'"
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
        return redirect('/login/realizar_cadastro/')

    return redirect('/login/')

def realizar_cadastro(request):
    from core.utils import ValidaLogin

    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        login_email = request.POST.get('email-input')
        login_password = request.POST.get('senha-input')
        login_confirm_password = request.POST.get('confirma-senha-input')

        if not ValidaLogin(request=request, login_email=login_email, login_pass=login_password, login_confirm_pass=login_confirm_password).validaLogin():
            return redirect('/login/realizar_cadastro/')

        conn = pg.connect(host = 'localhost',
                        database = 'users',
                        user = 'admin',
                        password = 'admin')
        
        cursor = conn.cursor()
        sql = f"insert into users.users (user_name, user_password, is_admin) values ('{login_email}', '{login_password}', false)"

        try:
            cursor.execute(sql)
            conn.commit()
        except: #TODO: fazer mensagens de erro mais explicativas
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar novo usuário. Por favor, tente novamente')
        else:
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')

        return redirect('/login/')
