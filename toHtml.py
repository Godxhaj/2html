from ansi2html import Ansi2HTMLConverter

with open("output.txt", "r", encoding="utf-8") as f:
    ansi_text = f.read()

conv = Ansi2HTMLConverter()
html_output = conv.convert(ansi_text)

with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_output)