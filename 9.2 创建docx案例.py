# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:18:04 2023

@author: Mora

9.2 创建docx案例
"""

from docx import Document
from docx.shared import Cm

document = Document()

document.add_heading('Document Title', 0)

p = document.add_paragraph('A plain paragraph having some ')
p.add_run('bold').bold = True
p.add_run(' and some ')
p.add_run('italic.').italic = True

document.add_heading('Heading, level 1', level=1)
document.add_paragraph('Intense quote', style='Intense Quote')

document.add_paragraph(
    'first item in unordered list', style='List Bullet'
)
document.add_paragraph(
    'first item in ordered list', style='List Number'
)

document.add_picture('D:/富途证券/女生篮球赛/篮球.png', width=Cm(4.5))

document.add_section()

records = (
    ('1', '8', '小涵'),
    ('2', '12', '小敏'),
    ('3', '3', '小文')
)

table = document.add_table(rows=1, cols=3)
table.style = 'Colorful Grid Accent 1'
hdr_cells = table.rows[0].cells
hdr_cells[0].text = '编号'
hdr_cells[1].text = '进球数'
hdr_cells[2].text = '姓名'
for qty, id, name in records:
    row_cells = table.add_row().cells
    row_cells[0].text = str(qty)
    row_cells[1].text = id
    row_cells[2].text = name

document.add_page_break()

document.save('D:/富途证券/表格/demo.docx')


