#! python3
# telefone_email.py - Encontra números de telefone e endereços de email no clipboard.

import re
import pyperclip

# Cria a regex para o telefone
telefone_regex = re.compile(r'''(
(\d{3}|\(\d{3}\))?              #código de área
(\s|-|\.)?                      # separador
(\d{3})                         # primeiros 3 dígitos
(\s|-|\.)                       # separador
(\d{4})                         # últimos 4 dígitos
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extensão
)''', re.VERBOSE)

# Cria a regex para email
email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+  # nome do usuário
@                  # símbolo arroba
[a-zA-Z0-9.-]+     # nome do domínio
(\.[a-zA-Z]{2,4})  # ponto seguido de outros caracteres
)''', re.VERBOSE)

# Encontrar as correspondências no texto do clipboard
texto = str(pyperclip.paste())

matches = []
for grupos in telefone_regex.findall(texto):
    num_telefone = '-'.join([grupos[1], grupos[3], grupos[5]])
    if grupos[8] != '':
        num_telefone += 'x' + grupos[8]
    matches.append(num_telefone)
for grupos in email_regex.findall(texto):
    matches.append(grupos[0])

# Copiar os resultados para o clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copiado no clipboard:')
    print('\n'.join(matches))
else:
    print('Nenhum telefone ou email foram encontrados.')
