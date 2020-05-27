Hello World!Hello World againHi Everyone.


>>> with open('python/marks.csv') as f:
...       reader = csv.DictReader(f)
...       marks=[dict(row) for row in reader]
... 