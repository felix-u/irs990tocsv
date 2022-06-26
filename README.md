Extracts certain data from IRS 990 forms in XML format into a CSV spreadsheet.

Requires `beautifulsoup4`:
```sh
pip install beautifulsoup4
```

The path to the input file and output file must be edited at the top of the
file. New fields can be added to the `fields` dictionary by specifying the
column name as the dictionary key. The value corresponding to the key must be
an array referencing the path to the relevant data in the XML tree.