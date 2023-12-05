from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph

file_path = r'C:\Users\est.angelo\Documents\codepy10-11\rel_final_s1.txt'
output_path = r"C:\Users\est.angelo\Documents\codepy10-11\RelatorioPDF.pdf"

def create_pdf(file_path, output_path):
    pdf = canvas.Canvas(output_path, pagesize=letter)
    pdf.setFont("Helvetica", size=12)

    # Adiciona a capa (primeira página)
    pdf.setFont("Helvetica-Bold", size=18)
    pdf.drawCentredString(letter[0] / 2, letter[1] / 2, "Relatório PDF")

    # Texto acima da capa (centralizado horizontalmente)
    text_acima = "AGEPAR - Agência Reguladora do Paraná"
    text_acima_width = pdf.stringWidth(text_acima, "Helvetica", 12)
    pdf.drawCentredString(letter[0] / 2, letter[1] - 40, text_acima)

    # Texto abaixo da capa (centralizado horizontalmente)
    text_abaixo = "Curitiba/PR - Dia 04/12/2023"
    text_abaixo_width = pdf.stringWidth(text_abaixo, "Helvetica", 12)
    pdf.drawCentredString(letter[0] / 2, 20, text_abaixo)


    pdf.showPage()

    styles = getSampleStyleSheet()
    normal_style = styles['Normal']

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    y_position = pdf._pagesize[1] - 50

    for line in lines:
        if line == '=========================================================================================================\n':
            pdf.showPage()
            y_position = pdf._pagesize[1] - 50
        elif line.startswith('=== '):
            line = line.replace('===', '')
            pdf.setFont("Helvetica-Bold", size=12)
            pdf.drawCentredString(letter[0] / 2, y_position, line)
            pdf.setFont("Helvetica", size=12)
            y_position -= 20
        else:
            # Verifica se o texto vai ultrapassar o limite da página
            if y_position < 50:
                pdf.showPage()
                y_position = pdf._pagesize[1] - 50

            # Usa Paragraph para permitir a quebra de linha automaticamente
            try:
                para = Paragraph(line, style=normal_style)
                para.wrap(pdf._pagesize[0] - 30, pdf._pagesize[1])
                para.drawOn(pdf, 15, y_position - para.height)
                y_position -= para.height
            except ValueError:
                # Ignora erros de parse para linhas problemáticas
                pass

    pdf.save()

create_pdf(file_path, output_path)
