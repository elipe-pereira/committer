#!/bin/bash

base_dir=`pwd`
dist_path="."
build_path="/tmp/build"
work_path="${build_path}"
spec_path="${build_path}"
name="committer"

mkdir -p $spec_path

pyinstaller --distpath $dist_path \
        --add-data "$base_dir/conf:conf" \
        --add-data "$base_dir/committer.cron:." \
        --workpath $work_path \
        --specpath $spec_path \
        --name $name main.py

test -d $build_path && rm -rf $build_path
