#!/usr/bin/perl
use warnings;
use strict;

# Copy "only the files needed to run on replit" to a separate folder.
# Don't need git files, original-db, project-task pdf, pycache, etc.
# Easier to upload to replit this way.
# On replit: select open file, select all files in the folder at once,
#            upload all the files to the top directory of replit.
# Note: Instructor Tim said replit works best when all the files are
#       in the top level directory and there are no sub-folders. Often
#       get issues if you use sub-folders.

# Copy command will copy and overwrite existing file of same name.
qx(copy *.py replit-upload-folder\\);
qx(copy filmflix.db replit-upload-folder\\);
