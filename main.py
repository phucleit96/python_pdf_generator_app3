from fpdf import FPDF
import pandas as pd

# Create a new PDF object with A4 page size
pdf = FPDF(orientation="P", unit="mm", format='A4')

# Disable automatic page break
pdf.set_auto_page_break(auto=False, margin=0)

# Initialize page number
page_number = 0

# Read the CSV file containing the topics
df = pd.read_csv('topics.csv', sep=",")

# Create a dictionary to store topics and their starting page numbers
toc = {}

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # For each page in the 'Pages' column of the row
    for _ in range(row['Pages']):
        # Add a new page to the PDF
        pdf.add_page()

        # Increment the page number
        page_number += 1

        # Set the font for the topic title
        pdf.set_font(family="Times", style="B", size=24)

        # Set the text color for the topic title
        pdf.set_text_color(100, 100, 100)

        # Add the topic title to the page
        pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="L", ln=1)

        # Draw a line under the topic title
        pdf.line(10, 21, 200, 21)

        # Move the cursor down to where the footer will be
        pdf.ln(258)

        # Set the font for the footer
        pdf.set_font(family='Times', style="I", size=8)

        # Set the text color for the footer
        pdf.set_text_color(180, 180, 180)

        # Add the footer to the page
        pdf.cell(w=0, h=10, txt=f"Page number: {page_number} - {row['Topic']}", align="R")

    # Store the starting page number for each topic
    toc[row['Topic']] = page_number - row['Pages'] + 1

# Add a new page for the table of contents at the beginning
pdf.add_page()

# Set the font for the table of contents title
pdf.set_font(family="Times", style="B", size=24)

# Add the table of contents title to the page
pdf.cell(w=0, h=12, txt="Table of Contents", align="L", ln=1)

# Set the font for the table of contents entries
pdf.set_font(family="Times", style="B", size=12)

# Initialize the y position for the table of contents entries
y = 30

# Add each topic and its page number to the table of contents
for topic, page in toc.items():
    # If the y position exceeds the page height, add a new page
    if y > 275:
        pdf.add_page()
        y = 10

    # Add the topic and its page number to the table of contents
    pdf.set_xy(10, y)
    pdf.cell(w=0, h=10, txt=f"{topic}: {page}", align="L")

    # Increment the y position
    y += 10

# Save the PDF to a file
pdf.output('output.pdf')