Sure, here's the Markdown text in English:

```markdown
# Project btcSearch

This project is designed to search for specific keywords in various types of files within the specified directory.

## Installing Required Libraries

Before running the project, you need to install the following libraries using `pip install`:

- `python-docx`
- `openpyxl`
- `olefile`
- `alive_progress`
- `PyPDF2`

```bash
pip install python-docx openpyxl olefile alive_progress PyPDF2
```

## Running the Project

1. **Enter the directory**: The program will prompt you to enter the directory in which you want to perform the search.

2. **Run the script**: After entering the directory, execute the script.

```python
python btcSearch.py
```

Example usage:

```bash
Enter Directory: C:\\
```

## Supported File Formats

The project searches for keywords in the following types of files:

- PDF (.pdf)
- Word (.doc, .docx)
- Excel (.xls, .xlsx)
- Text files (.txt)

## File Processing

The `search_words_in_files` script iterates through each file in the specified directory and looks for keywords. If words are found, it saves information about the file, the found words, and the context of their usage.

```python
def search_words_in_files(directory, word_list):
    ...
```

## Errors and Handling

If errors occur during file processing, they will be printed to the console. The program will continue working with other files.

```python
except Exception as e:
    print(f"Error processing file: {e}")
```

## Note

Make sure you have necessary permissions to read files in the chosen directory.

```

This text provides users with instructions on installing necessary libraries, running the project, supported file formats, and error handling.
