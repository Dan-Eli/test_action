![SLYR Logo](logo.png)

# SLYR

A Python library and set of command line tools for extraction, parsing, and conversion of ESRI `.lyr` and `.style` files.

[![Build Status](https://travis-ci.org/nyalldawson/slyr.svg?branch=master)](https://travis-ci.org/nyalldawson/slyr)

Status
=====

- RGB colors can be parsed, within a maximum of 1 unit difference in either the R/G/B components.
- Fill symbols
    - complete support for Simple Fill layers
- Line symbols
    - complete support for Simple Line layers
    - near complete support for Cartographic Line layers, including custom dash patterns. Arrows cannot be decoded yet.
- Marker symbols
    - complete support for Simple Marker layers
    - complete support for Character Marker layers

Tools
=====

 - `bin_dump.py` Converts a binary `.style` database row blob into a symbol and dumps the symbol properties to the console
 - `style_dump.py` Dumps the complete contents of an ESRI `.style` database, printing symbol properties to the console
 - `style_to_bin.py` Exports the contents of an ESRI `.style` database to individual `.bin` binary files, each containing an encoded version of a single symbol
 - `style_to_qgis_xml.py` Converts the contents of an ESRI `.style` database to a QGIS 3.x Style `.xml` file, ready for importing direct into your QGIS style library (requires QGIS 3.x)
 
 All tools require the command line `mdbtools` for handling the `.style` database files. Binaries of these can be downloaded from [https://github.com/lsgunth/mdbtools-win](https://github.com/lsgunth/mdbtools-win), and they should be extracted and available in the Windows path.
 
QGIS Plugin
===========

SLYR also functions as a QGIS plugin (for QGIS >= 3.2). Just copy the whole slyr folder to your QGIS profile Python -> plugins path, launch QGIS and enable the plugin.

The plugin adds a new group to the Processing Toolbox for "SLYR", containing tools for conversion of style databases to QGIS symbol styles. Note that Windows users will first need to setup the path to the mdbtools binaries via Options - Processing - Providers - SLYR.

* And no, this won't be distributed by the normal QGIS plugin channel. It's provided "as-is", with no support offered whatsoever.
 
Specifications
==============

Some description of the `.style` binary format can be found in [specs.md](specs.md), although the most up-to-date reference is the Python parsing code itself.
