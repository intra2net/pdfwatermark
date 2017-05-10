# pdfwatermark

Embed a pdf as background or watermark and place it on each page of another pdf.

## How to use

```
pdfwatermark.py watermark.pdf source.pdf output.pdf
```

This puts the content of the first page of watermark.pdf in the background of each
page of source.pdf. The merged data is written into output.pdf.

## Dependencies

- python 3 https://www.python.org/
- pyPDF2 http://mstamy2.github.io/PyPDF2/

## Reason for development

Previously we used PDFtk https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/ for this task.
But PDFtk relies on gcj which was deprecated for a long time and is not easily available
on current distributions anymore.

So I was looking for a replacement. There are some tools offered as replacement for PDFtk,
but most of them don't offer a equivalent of the pdftk "background" command.

Mcpdf offers it, but requires iText which is not easily available on CentOS 7. Adding a
background in QPDF is possible, but not easily scriptable.

## Alternatives

- Mcpdf https://github.com/m-click/mcpdf
- QPDF http://qpdf.sourceforge.net/

## License

MIT X11 License
