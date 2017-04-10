===
CLI
===

This document describes the Command Line Interface to helm. Helm can be
used to populate and render templates based on data passed in.

Basically, it takes a template as an argument with an optional argument
for the data (which defaults to stdin). The template will be rendered
for each line of data.

The input format is parsed using plugins. The following plugins are included
by default with helm:

  * CsvInput: Reads a CSV, assumes that first row is a header
  * JsonInput: Reads JSON, assumes that each line is a JSON document
  * XmlInput: Reads XML, assumes that each line is an XML document and that
    there is just one level of children for the root node

Examples::

    $ cat input.csv | helm -t template.j2
    $ cat input.json | helm -t template.j2 -p JsonInput
    $ cat input.xml | helm -t template.j2 -p XmlInput

    $ helm -t template.j2 -d input.csv
    $ helm -t template.j2 -d input.json -p JsonInput
    $ helm -t template.j2 -d input.xml -p XmlInput
