import pikepdf
def analyze(filename):
    try:
        pdf = pikepdf.open(filename)
        meta = pdf.docinfo
        pdf_meta = {}
        for key, value in meta.items():
            pdf_meta[key.replace("/","")] = str(value)
    except:
        pdf_meta = {}
    return pdf_meta