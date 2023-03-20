class Venda:
    def __init__(self,cod_produto:str,desc_produto:str,valor_unt:float,data_venda:str) -> None:
        self.cod_produto = cod_produto
        self.desc_produto = desc_produto
        self.valor_unt = valor_unt
        self.data_venda = data_venda

base_vendas = [
    Venda('001','Produto 1',50.00,'01/01/2023'),
    Venda('002','Produto 2',20.00,'01/01/2023'),
    Venda('003','Produto 3',30.00,'01/01/2023'),
    Venda('001','Produto 1',20.00,'05/02/2023'),
    Venda('003','Produto 3',30.00,'01/02/2023'),
    Venda('003','Produto 3',30.00,'02/02/2023'),
    Venda('001','Produto 1',50.00,'01/03/2023'),
    Venda('003','Produto 3',30.00,'01/03/2023'),
    Venda('002','Produto 2',20.00,'05/03/2023')
]

with open("base_vendas.csv","w") as file:
    file.write("cod_produto;desc_produto;valor_unt;data_venda\n")

    for i in base_vendas:
        cod_p = i.cod_produto
        des_p = i.desc_produto
        val_p = str(i.valor_unt)
        dat_v = i.data_venda

        file.write(";".join([cod_p,des_p,val_p,dat_v]) + "\n")
