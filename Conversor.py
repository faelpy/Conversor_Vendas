import xlsxwriter

workbook = xlsxwriter.Workbook('Pedidos_Atrasados.xlsx')
tabela = workbook.add_worksheet()
tabela.set_column('A:A', 13)
tabela.set_column('B:B', 13)
tabela.set_column('C:C', 23)
tabela.set_column('D:D', 10)
tabela.set_column('E:E', 9)
tabela.set_column('F:H', 8)
tabela.set_column('I:I', 3)
tabela.set_column('J:J', 11)

estilo = workbook.add_format({'font_color':'white', 'bg_color':'black', 'align':'center'})
centro = workbook.add_format({'align':'center', 'border':1, 'num_format': '0'})

dic = {'dicionario de itens'}

f = open("pedidos.txt", "r")
pedidos = f.readlines()
lin, col = 0, 0;gravar=[]

cabecalho = ['Data','Pedido','Cliente','Item','Cor','Qtd.','Exp.','Alm.','S', 'It.']
for dado in cabecalho:
    tabela.write(lin, col, dado, estilo)
    col+=1

for line in pedidos:
    col=0
    if line[0].isdigit() or line[0] == " " and line.find(',') != -1:
        if line[0].isdigit():
            data ='/'.join((line.rstrip().split("-")[0].split()[0]).split('/')[:2])+'/20'+(line.rstrip().split("-")[0].split()[0]).split('/')[-1]
            pedido = line.rstrip().split("-")[0].split()[2]
            cliente = line.rstrip().split("-")[0].split()[3]+'-'+' '.join(line.rstrip().split("-")[1].split()[:-6])
            item, cor, qtd, exp, alm, s = line.rstrip().split("-")[1].split()[-6:]

            if cor[0].isdigit():
                cor = int(cor)
            try:
                item2 = dic[item]
            except:
                if item[0:4]=='9010':
                  item2=item
                else:
                  item2 = '0'
            try:    
                gravar = [data, pedido, cliente, item, cor, int(qtd.split(',')[0]), int(exp.split(',')[0]), int(alm.split(',')[0]), int(s), int(item2)]
            except:
                gravar = [0]
#            print gravar
        else:
            item, cor, qtd, exp, alm, s = line.rstrip().split()
            if cor[0].isdigit():
                cor = int(cor)
            try:
                item2 = dic[item]
            except:
                if item[0:4]=='9010':
                  item2=item
                else:
                  item2 = '0'
            try:
                gravar = [data, pedido, cliente, item, cor, int(qtd.split(',')[0]), int(exp.split(',')[0]), int(alm.split(',')[0]), int(s), int(item2)]
            except:
                gravar = [0]
        lin+=1

    for dado in gravar:
        tabela.write(lin, col, dado, centro)
        col+=1

workbook.close()
