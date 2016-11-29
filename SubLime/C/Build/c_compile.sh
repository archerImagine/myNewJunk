#!/bin/bash
#c_compile.sh
#Strip the path component.
file_name=$(basename $1)
dir_name=$(dirname $1)

#Path to a directory for storing class files.
PATH_TO_BIN_DIR=$dir_name"/bin"

#Create the directory above if not exists.
mkdir -p $PATH_TO_BIN_DIR

#Remove all binary files created at the previous compile time.
find $PATH_TO_BIN_DIR -type f -name "*.out" -exec rm -f {} \;

#Strip the file extension.
class_name="${file_name%.*}"

echo $file_name
echo $dir_name
echo $PATH_TO_BIN_DIR
echo $class_name

gcc $dir_name/$file_name -o $PATH_TO_BIN_DIR/$class_name.out