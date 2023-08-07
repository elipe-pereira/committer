#!/bin/bash

base_dir=`pwd`
dist_path="."
work_path="/tmp"
build_path="/tmp/build"
spec_path="${build_path}/committer"
name="committer"

mkdir -p $spec_path

pyinstaller --distpath $dist_path\
        --add-data "$base_dir/etc:etc"\
        --workpath $work_path\
        --specpath $spec_path\
        --name $name main.py

test -d $build_path && rm -rf $build_path
