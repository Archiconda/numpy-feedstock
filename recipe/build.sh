#!/bin/bash

cat > site.cfg <<EOF
[DEFAULT]
library_dirs = $PREFIX/lib
include_dirs = $PREFIX/include

[atlas]
atlas_libs = openblas
libraries = openblas

[openblas]
libraries = openblas
library_dirs = $PREFIX/lib
include_dirs = $PREFIX/include

EOF

# Regenerate this specific file
rm numpy/random/mtrand/mtrand.c
$PYTHON -m pip install --no-deps --ignore-installed .
