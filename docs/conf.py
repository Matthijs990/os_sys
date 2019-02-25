from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
    '.html': CommonMarkParser,
}

source_suffix = ['.rst', '.md', '.html']
