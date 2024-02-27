# a4tolettersize
Convert smaller format pdf document to letter size while maintaining size and proportion of content.

This will resize the pages in the document to letter size and center the existing content.
Content will maintain its absolute size and proportions when printed.

This tool was created to convert old sewing pattern PDFs to US letter size, allowing me to print them at a US print shop.

## how to use
To use for yourself, first clone this repository and `cd` to it:
```cmd
git clone https://github.com/cpparnell/converttolettersize.git
cd converttolettersize
```
Then, install the command line tool:
```cmd
pip install . 
```
Finally, you can convert from smaller formats to letter size using:
```cmd
converttolettersize /path/to/input/file.pdf /path/to/output/file.pdf
```
