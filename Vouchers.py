import pandas as pd
import jinja2
import pdfkit

# Abrimos el excel con los codigos de Voucher
df = pd.read_excel("50 vouchers 3er Meetup.xlsx")
codigos = df["Codigo"]

# Usamos el template para completar los codigos
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "voucher_template.html"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render(codigos=codigos)

# Guardamos los datos en un html
f = open("vouchers.html", "w")
f.write(outputText)
f.close()

# Generamos el pdf
pdfkit.from_file('vouchers.html', 'vouchers.pdf')
