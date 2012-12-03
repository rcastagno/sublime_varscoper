Sublime Varscoper
=============

[Sublime Text 2](http://www.sublimetext.com/) plugin to verify scoped variables in the active CFC/CFML file.

It relies on Mike Schierberl's [VarScoper](http://varscoper.riaforge.org/) tool.

Two function are provided:
* Run this file on VarScoper : open a browser pointing VarScoper passing the active file as parameter
* Highlight VarScoper violations : highlights lines containing unscoped variables

Due to VarScoper issues, highlighted lines may not always be correct.

Installation
------------

### Manual installation

Go to your Packages subdirectory under Sublime Text 2 data directory:

* Windows: %APPDATA%\Sublime Text 2
* OS X: ~/Library/Application Support/Sublime Text 2
* Linux: ~/.config/sublime-text-2

and extract there the sublime_varscoper folder.

Configuration
-------------

By default, VarScoper is searched at this URL:

	http://localhost/tools/varscoper/varScoper.cfm

you can define a custom location for varScoper.cfm by creating a key in the user preferences file:

	"varscoper_cfm_url":"http://host:port/varscoper/varScoper.cfm"
