
def process(file, pdf_method=0, pdf_res=200):

  if not file.endswith('.pdf') or pdf_method == 0:
    import textract
    text = str(textract.process(file).decode('unicode-escape')).strip()
    return text

  else:
    from wand.image import Image as WandImg
    from PIL import Image as pImg
    import pytesseract
    import os
    with WandImg(filename=file, resolution=pdf_res) as source:
        images = source.sequence
        pages = len(images)
        text = ''
        for i in range(pages):
          fn = '_temp_' + str(i) + '.png'
          WandImg(images[i]).save(filename=fn)
          img = pImg.open(fn).convert('RGBA')

          text += pytesseract.image_to_string(img).strip() + '\n'
          os.remove(fn)
        return text

        