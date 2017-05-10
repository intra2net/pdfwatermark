#!/usr/bin/python3

#
# Embed a pdf as background or watermark and place it on each page of another pdf
#

# Copyright 2017 by Intra2net AG, Germany
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import PyPDF2
import os
import sys

if len(sys.argv) != 4:
    raise RuntimeError('Usage {} watermark.pdf source.pdf output.pdf'.format(sys.argv[0]))

watermark_path = sys.argv[1]
if not os.path.isfile(watermark_path):
    raise RuntimeError('Watermark file {} not found'.format(watermark_path))
watermark = PyPDF2.PdfFileReader(open(watermark_path, "rb"))

source_path = sys.argv[2]
if not os.path.isfile(source_path):
    raise RuntimeError('Source file {} not found'.format(source_path))
source = PyPDF2.PdfFileReader(open(source_path, "rb"))

watermark_page = watermark.getPage(0)

pdf_output = PyPDF2.PdfFileWriter()

for pageNum in range(0, source.numPages):
    pageObj = source.getPage(pageNum)
    pageObj.mergePage(watermark_page)
    pdf_output.addPage(pageObj)

output_file = open(sys.argv[3], 'wb')
pdf_output.write(output_file)
output_file.close()
