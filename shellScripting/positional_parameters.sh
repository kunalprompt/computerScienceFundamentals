#!/bin/sh

echo '\nScript Name $0: '$0
echo 'Command Line Arguments Count $# (except 0th arg): '$#
echo 'All Command line args except 0th arg $*:  '$*
echo 'All command line args except 0th arg $@: ' $@
echo 'Get a command line arg between $0 and $9 as $X: ' $0, $1
echo 'Get command line arg higher than $9 like ${10}: ' ${10}, ${11}
echo '\n'
