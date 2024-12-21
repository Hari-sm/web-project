import pyttsx3
from PyPDF2 import PdfReader

# Chapter dictionary with chapter names and corresponding page ranges
chapter_dict = {
    "Introduction": (15, 24),
    "Lesson 1 The Rich Don't Work For Money": (2, 9),
    "Lesson 2 Why Teach Financial Literacy": (56, 86),
    "Lesson 3 Mind Your Own Business": (86, 94),
    "Lesson 4 The History of Taxes and the Power of Corporation": (94, 106),
    "Lesson 5 The Rich Invent Money": (106, 130),
    "Lesson 6 Work to Learn - Don't Work For Money": (130, 144),
    "Lesson 7 Overcoming Obstacles": (144, 160),
    "Lesson 8 Getting Started": (160, 182),
    "Lesson 9 Still Want More? Here Are Some To Dos": (182, 188),
}

def convert_to_audio(text: str, file_name: str):
    """Converts given text to an audio file."""
    engine = pyttsx3.init()
    engine.save_to_file(text, file_name)
    engine.runAndWait()
    print(f"Audio saved as {file_name}")

def generate_audio_text(pdf_object: PdfReader, chapter_name: str, start_page: int, end_page: int):
    """Generates audio from the text of specified pages in the PDF."""
    try:
        print(f"Processing Chapter: {chapter_name}, Pages: {start_page} to {end_page}")
        text = ""
        for page_number in range(start_page - 1, end_page):  # PyPDF2 uses 0-based indexing
            text += pdf_object.pages[page_number].extract_text()
        
        if text.strip():
            convert_to_audio(text, f"{chapter_name}.mp3")
        else:
            print(f"No text extracted for {chapter_name}. Check page range or PDF structure.")
    except IndexError:
        print(f"Invalid page range for {chapter_name}. Ensure the pages exist in the PDF.")

def main():
    try:
        reader = PdfReader("Rich Dad Poor Dad.pdf.pdf")  # Ensure the file path is correct
        for chapter_name, page_numbers in chapter_dict.items():
            generate_audio_text(
                pdf_object=reader,
                chapter_name=chapter_name,
                start_page=page_numbers[0],
                end_page=page_numbers[1]
            )
    except FileNotFoundError:
        print("The PDF file was not found. Please check the file name and path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
