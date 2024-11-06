#AnkiDroid Deck Creation

import re
import android.anki.python.Python
from docx import Document
from io import BytesIO
from PIL import Image

# Load the Word document and extract text and images
docx_path = 'D:\documents\CCNA\CCNA Miscellaneous Questios.docx'
doc = Document(docx_path)
all_elements = []
for element in doc.element.body:
    if isinstance(element, (docx.text.paragraph.Paragraph, docx.text.table.Table)):
        all_elements.append(element)
    elif isinstance(element, docx.oxml.ns.qn('w:pict')):
        image_bytes = element.find('.//a:blip', namespaces=element.nsmap).get(docx.oxml.ns.qn('r:embed'))
        all_elements.append(image_bytes)

# Rest of the script remains mostly the same...

# Modify the loop to process elements
for pair in qa_pairs:
    question, answer = pair.split('Answer:', 1)
    question = question.strip()
    answer = answer.strip()

    # Search for images in the question and answer
    question_images = re.findall(r'(?<=<img src="data:image/png;base64,)[^"]+', question)
    answer_images = re.findall(r'(?<=<img src="data:image/png;base64,)[^"]+', answer)

    # Load and add images to the Anki note
    note = genanki.Note(
        model=my_model,
        fields=[question, answer],
    )

    for img_base64 in question_images + answer_images:
        img_data = BytesIO(img_base64.encode())
        img = Image.open(img_data)
        img.show()  # You can save, display, or manipulate the image here

    my_deck.add_note(note)

# Rest of the script remains the same...
