
import re 
from django.contrib.messages import constants
from django.contrib import messages


class ValidaLogin:

    def __init__(self, request, login_email, login_pass, login_confirm_pass=None):
        self.login_email = login_email
        self.login_pass = login_pass
        self.request = request
        self.login_confirm_pass = login_confirm_pass

    def validaLogin(self):

        if not re.match(pattern='[A-Za-z.0-9]+@[gmail|outlook|hotmail]+.com', string=self.login_email):
            messages.add_message(self.request, constants.ERROR, 'E-mail inválido!')
            return False
    
        if not re.match(pattern='([A-Za-z0-9!@#$&*()]+){8,}', string=self.login_pass):
            messages.add_message(self.request, constants.ERROR, 'A senha deve ter no mínimo 8 caracteres!')
            return False
        
        if self.login_confirm_pass is not None:
            if self.login_confirm_pass != self.login_pass:
                messages.add_message(self.request, constants.ERROR, 'As senhas não são iguais!')
                return False

        return True
    
    #TODO: verificar se o novo email já não consta no banco

