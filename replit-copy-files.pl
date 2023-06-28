#!/usr/bin/perl
use warnings;
use strict;

# Copy of "only the files needed to run on replit" to a separate folder.
# Easier to upload to replit this way.
# Don't need git files, original-db, project-task pdf, pycache, etc.

# Copy command will copy and overwrite existing file of same name.
qx(copy *.py replit-upload-folder\\);
qx(copy filmflix.db replit-upload-folder\\);
