###BtcSearch
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
- `docx2txt`
- `xlrd`
- `chardet`

```


```bash
pip install python-docx openpyxl olefile alive_progress PyPDF2 docx2txt xlrd chardet
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

## Errors and Handling

If errors occur during file processing, they will be printe
