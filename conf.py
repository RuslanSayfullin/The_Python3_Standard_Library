#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PyMOTW-3 documentation build configuration file, created by
# sphinx-quickstart on Sun Aug 11 11:16:58 2013.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# flake8: noqa

import datetime
import os
import subprocess
import sys
import sysconfig

from docutils import nodes

from sphinx.environment.adapters import toctree

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('./_exts'))

# -- General configuration ---------------------------------------------------

building_book = bool(os.environ.get('_BUILDING_BOOK') or False)

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    #'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.extlinks',
    'sphinx.ext.graphviz',
    'tableref',
    'figureref',
    'pydoc',
]

python_version = '{}.{}'.format(*(sys.version_info[:2]))

extlinks = {
    'pyissue': ('http://bugs.python.org/issue%s', 'Python issue '),
    # 'pydoc': ('http://docs.python.org/' + python_version + '/library/%s.html',
    #           'Standard library documentation for '),
}

linkcheck_timeout = 5
linkcheck_anchors = False
linkcheck_ignore = [
    r'https://blogs.gnome.org/markmc.*',
    r'.*sourceforge.net.*',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
if building_book:
    master_doc = 'book'
else:
    master_doc = 'index'

# General information about the project.
year = datetime.date.today().year
project = 'PyMOTW-3'
copyright = '{}, Doug Hellmann'.format(year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
if building_book:
    exclude_patterns = [
        'index.rst',
    ]
else:
    exclude_patterns = [
        'book.rst',
    ]

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'
if os.environ.get('_PYGMENTS_STYLE'):
    pygments_style = os.environ['_PYGMENTS_STYLE']

# The default syntax highlighter is 'python', which assumes python 2
# syntax. Set it to 'python3' since all of the examples are python 3.
highlight_language = 'python3'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pymotw'

html_context = {
    'python_version': sysconfig.get_config_vars()['py_version'],
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'PyMOTW 3'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
no_toc_sidebars = [
    'sidebar_book.html',
]
html_sidebars = {
    'index': ['sidebar_subscribe.html'] + no_toc_sidebars,
    'genindex': no_toc_sidebars,
    'py-modindex': no_toc_sidebars,
    '**': [
        'sidebar_toc.html',
        'sidebar_lastupdated.html',
        'sidebar_nav.html',
        'sidebar_book.html',
        'sidebar_examples.html',
    ],
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'PyMOTW-3doc'


# -- Options for LaTeX output ------------------------------------------------
preamble_parts = [

'''
% Start preamble from conf.py
''',

r'''
% Enable unicode and use Courier New to ensure the card suit
% characters that are part of the 'random' module examples
% appear properly in the PDF output.
% from http://tex.stackexchange.com/questions/20182/how-to-use-unicode-characters-with-sphinx-rst-documents-and-properly-generate-pd
\usepackage{fontspec}
\setmonofont{Courier New}
''',
# Other font setting instructions:
# \setsansfont{Helvetica}
# \setromanfont{Helvetica}
# \setmonofont{Menlo Regular}

# '''
# % Double-spaces the entire document (used for manual edit review)
# \usepackage{setspace}
# \doublespacing
# ''',

# Using these geometry settings with the sphinx styles causes
# rendering issues with the footnotes overrunning the page footer.
# Maybe a setting missing somewhere?

# r'''
# % Geometry settings from Pearson template
# \usepackage[twoside,dvips]{geometry}
# \geometry{%
# paperwidth=7in,
# paperheight=9.25in,
# lmargin=.75in,
# rmargin=.75in,
# bmargin=.625in,
# tmargin=.625in,
# width=5.5in,
# height=7.525in, %7.3
# marginparwidth=0.35in,
# headheight=0.2in,
# headsep=.25in,
# footskip=.025in}
# ''',

r'''
%% Load the crop package
% This form, with the "letter" option, uses a full letter page size
% and draws the box around the real page.
\usepackage[letter,center,dvips]{crop}

% This form sets the width and height of the page in a way
% that means there is no margin around the outside, and the PDF
% shows the real page size.
%\usepackage[width=7truein,height=9.25truein,center,dvips]{crop}

% This form sets the paper size to larger than the page size
% so the crop box shows up.
%\special{papersize=11in,8.5in}

% Draws the crop-box around the pages for margin checking
%\crop[frame]
%%
''',

'% End preamble from conf.py',

]

latex_elements = {
    'preamble': '\n'.join(preamble_parts),

    'atendofbody': r'''
% footer set by conf.py

% Set up the list of figures so it appears in the TOC
\cleardoublepage
\phantomsection \label{listoffig}
\addcontentsline{toc}{chapter}{List of Figures}
\listoffigures

% Set up the list of tables so it appears in the TOC
\cleardoublepage
\phantomsection \label{listoftab}
\addcontentsline{toc}{chapter}{List of Tables}
\listoftables
''',

    # disable the release line in the output since I don't tag
    # releases
    'releasename': '',

    # disable font inclusion
    # from https://github.com/jterrace/sphinxtr/blob/master/conf.py
    'fontpkg': '',
    'fontenc': '',

    # Fix Unicode handling by disabling the defaults for a few items
    # set by sphinx
    'inputenc': '',
    'utf8extra': '',

    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'twoside',
    'papersize': 'letterpaper',

    # Options for documentclass directive, values from Pearson template
    'classoptions': ',letterpaper,english',
    # 'docclass': 'newphstyle',
    # 'wrapperclass': 'newphstyle',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',
    # 'pointsize': '10pt',

    # Use a chapter heading that does not spell out the chapter
    # number.
    'fncychap': r'\usepackage[Sonny]{fncychap}',
    # Pearson template does not use fncychap at all?
    # 'fncychap': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author,
#  documentclass [howto/manual]).
latex_documents = [
    ('book',  # startdocname
     'py3_stdlib.tex',  # targetname
     'The Python 3 Standard Library By Example',  # title
     'Doug Hellmann',  # author
     'manual',  # documentclass
     True,  # toctree_only
    ),
]

latex_additional_files = [
    'images/replacement-character.png',
    '../pearson/newphstyle.cls',
    '../pearson/newphstyle.sty',
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
latex_show_pagerefs = True

latex_show_urls = 'footnote'

# Documents to append as an appendix to all manuals.
latex_appendices = [
    'porting_notes',
    'third_party',
    'about',
]

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'pymotw-3', 'PyMOTW-3 Documentation',
     ['Doug Hellmann'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'PyMOTW-3', 'PyMOTW-3 Documentation',
     'Doug Hellmann', 'PyMOTW-3', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}


def _get_last_updated(app, pagename):
    # Use the last modified date from git instead of applying a single
    # value to the entire site.
    last_updated = None
    src_file = app.builder.env.doc2path(pagename)
    if os.path.exists(src_file):
        try:
            last_updated_t = subprocess.check_output(
                [
                    'git', 'log', '-n1', '--format=%ad', '--date=short',
                    '--', src_file,
                ]
            ).decode('utf-8').strip()
            last_updated = datetime.datetime.strptime(last_updated_t,
                                                      '%Y-%m-%d')
        except (ValueError, subprocess.CalledProcessError):
            pass
    return last_updated


def html_page_context(app, pagename, templatename, context, doctree):
    # Build a list of the local table of contents entries to appear in
    # the sidebar
    try:
        adapter = toctree.TocTree(app.builder.env)
        toc = adapter.get_toc_for(pagename, app.builder)
    except KeyError:
        # Pages like genindex may not show up in the list of pages
        # with table of contents, and that breaks
        # environment.get_toc_for, which throws an KeyError.
        pass
    else:
        toc_menu = []
        for node in toc.traverse(nodes.reference):
            # Skip the node at the top that points back to this page
            if node['refuri'] == '#':
                continue
            toc_menu.append({
                'title': str(node.children[0]),
                'href': node['anchorname'],
            })
        context['toc_menu'] = toc_menu

    # Only show comments when we are rendering a page inside a module
    # directory, to prevent people from commenting on the main page,
    # about page, index, etc.
    # context['show_comments'] = '/' in pagename

    # Use the last modified date from git instead of applying a single
    # value to the entire site.
    context['last_updated'] = _get_last_updated(app, pagename)


def setup(app):
    app.connect('html-page-context', html_page_context)
    app.add_config_value('building_book', False, 'env')