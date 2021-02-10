import re
import csv
# custom imports
from section import Section


class Facturas():
    def __init__(self, name, it):
        self.name = name
        self.number = it
        self.full_name = self.get_name()
        self.get_text = self.open_file_txt()
        self.nota_de_venta = self.get_nota_de_venta()
        self.numero_cliente = self.get_numero_cliente()
        self.nombre_cliente = self.get_nombre_cliente()
        self.nombre_producto = self.get_nombre_producto()
        self.nombre_lote = self.get_nombre_lote()
        self.cantidad = self.get_cantidad()
        self.lote_2 = self.get_lote2()

    def get_name(self):
        ext = ".txt"
        full_name = self.name + str(self.number) + ext
        return full_name

    def open_file_txt(self):
        text = ''
        with open(self.full_name, 'r') as f:
            text = f.readlines()
            return '\n'.join(text)

    def get_nota_de_venta(self):

        pattern = '(?:Factura - Directa'
        pattern += '|'
        pattern += 'Factura - Nota de'
        pattern += '|'
        pattern += 'Factura - Pedido'
        pattern += ')\s+\w{1,4}\d{5,7}'
        match = re.findall(pattern, self.get_text)

        if match:
            nota = match[0].split()
            return nota[-1]
        return None

    def get_numero_cliente(self):

        pattern = 'Cliente:\s*'
        pattern += '[A-Z]{1,2}'
        pattern += '\d{1,3}'
        pattern += '\s'
        match = re.findall(pattern, self.get_text)
        if match:
            nota = match[0].split()
            return nota[-1]
        return None

    def get_nombre_cliente(self):

        pattern = 'Nombre:\s+'
        pattern += '([A-Z]{4,})+\s+([A-Z]{2,})*'
        match = re.findall(pattern, self.get_text)
        if match:
            return ' '.join(match[0])
        return None

    def get_nombre_producto(self):

        # pattern += '\s+(\d{1,3}[A-Z]{2,5}([\d{1,3}])+?)'
        pattern = '(?<=MYN1).*'
        match = re.findall(pattern, self.get_text)
        if match:
            return match[0].split()[0]
        return None

    def get_nombre_lote(self):

        pattern = '(?<=Observaciones:).*'
        match = re.findall(pattern, self.get_text)
        if match:
            return ' '.join(match)
        return None

    def get_cantidad(self):
        try:
            text = Section(self.get_text,
                           ('Precio', 1),
                           ('Total:', -1))
            return float(text.reduced_text.split()[0].replace(',', ''))/40
        except Exception as e:
            print(e)
        return None

    def get_lote2(self):
        try:
            text = Section(self.get_text,
                           ('Precio', 3),
                           ('Total:', -1))
            return text.reduced_text.split()[-1]
        except Exception as e:
            print(e)
        return None


# name_ = "Ene_2021_"
# ext = ".txt"
# total = 77
# Notas_array = []
# for i in range(0, total):

#     Uno = Facturas(name_, i)
#     print(Uno.nota_de_venta, " ",
#           Uno.nombre_cliente, " ",
#           Uno.numero_cliente, " ",
#           Uno.nombre_producto, " ",
#           Uno.nombre_lote, " ",
#           Uno.lote_2, " ",
#           Uno.cantidad)
#     Notas_array.append(Uno)

# with open('final_notas.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Factura', 'Cliente', '#Cliente', 'Producto', 'Observaciones', 'Lote', 'SACOS']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for notas in Notas_array:
#         writer.writerow(
#             {'Factura': notas.nota_de_venta,
#              'Cliente': notas.nombre_cliente,
#              '#Cliente': notas.numero_cliente,
#              'Producto': notas.nombre_producto,
#              'Observaciones': notas.nombre_lote,
#              'Lote': notas.lote_2,
#              'SACOS': notas.cantidad})
