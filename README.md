# PDF Generator with Table of Contents

This project is a Python script that generates a PDF document with a table of contents (at the end, "output.txt"). The PDF document is created from a CSV file that contains a list of topics and the number of pages for each topic ("topics.csv").

[DEMO](https://i.imgur.com/u6NEDjx.gif)
## Features

- Generates a PDF document with a table of contents.
- The table of contents lists all the topics and their starting page numbers.
- Each topic is given a title and a footer on its page(s).
- If the table of contents is too long to fit on one page, it is split across multiple pages.

## Requirements

- Python 3
- pandas
- fpdf

## Usage

1. Prepare a CSV file with the following format:
2. Run the script:

```bash
python main.py
```
3. The output PDF will be saved as output.pdf.


