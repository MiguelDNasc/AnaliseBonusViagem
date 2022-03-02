import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC29e0b6f9fc0478e2c40422d5d1f64ef7"
# Your Auth Token from twilio.com/console
auth_token  = "cf411333242606e89060594a15cb7cac"
client = Client(account_sid, auth_token)

# Passo a passo da solução

# Abrir os 6 arquivos do excel
lista_meses = ['janeiro','fevereiro','março', 'abril','maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        print(f'No mês {mes} encontrou alguém com mais de 55000. Vendedor: {vendedor}. Vendas: R${vendas}')
        message = client.messages.create(
            to="+552198944534",
            from_="+19035463897",
            body="f'No mês {mes} encontrou alguém com mais de 55000. Vendedor: {vendedor}. Vendas: R${vendas}")
        print(message.sid)
# Para cada arquivo

# Verificar se algum valor na coluna de Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 => Envio um SMS com o Nome, o mês e as vendas do vendedor



