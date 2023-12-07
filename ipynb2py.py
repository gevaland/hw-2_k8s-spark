import nbformat
from nbconvert import PythonExporter

with open('spark/pyspark-deltalake.ipynb') as notebook_file:
    notebook = nbformat.reads(notebook_file.read(), nbformat.NO_CONVERT)

exporter = PythonExporter()
source, meta = exporter.from_notebook_node(notebook)

with open('src/pyspark_deltalake.py', 'w+') as source_file:
    source_file.writelines(source.encode('utf-8'))
