#!/usr/bin/env python3
import click
import fitz  # Import PyMuPDF

# Define the conversion function with click decorators for CLI integration
@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def convert_to_lettersize(input_file: str, output_file: str) -> None:
    """
    Converts PDF document to Letter size, preserving the content's size and proportions.
    """
    letter_size = [612, 792]  # Letter size in points (8.5 x 11 inches)
    new_doc = fitz.open()  # Create a new empty document

    with fitz.open(input_file) as doc:
        for page in doc:
            original_rect = page.rect
            scale = 1  # Default scale is 1 (no scaling)

            # Calculate the new width and height based on scaling
            new_width = original_rect.width * scale
            new_height = original_rect.height * scale

            # Calculate translation to center the content
            translate_x = (letter_size[0] - new_width) / 2
            translate_y = (letter_size[1] - new_height) / 2

            # Create a new page with Letter dimensions
            new_page = new_doc.new_page(width=letter_size[0], height=letter_size[1])

            # Define the target rectangle for the scaled and centered content
            target_rect = fitz.Rect(translate_x, translate_y, translate_x + new_width, translate_y + new_height)

            # Insert the scaled and centered content of the current page into the new page
            new_page.show_pdf_page(target_rect, doc, page.number)

    # Save the new document
    new_doc.save(output_file)
    click.echo(f"Converted file saved to {output_file}")

if __name__ == '__main__':
    convert_to_lettersize()

