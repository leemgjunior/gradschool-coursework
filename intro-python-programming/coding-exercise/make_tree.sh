#!/bin/bash
rm -r s1
mkdir s1
mkdir s1/s3
touch s1/s3/conf.txt
mkdir s1/s2
touch s1/s2/text_chunk1.txt
mkdir s1/s2/Advanced
echo "Virtual (conda) environments are my favorite new technology" > s1/s3/conf.txt
echo "Virtual environments are good for isolating environments for scripting and software development" > s1/s2/text_chunk1.txt
cp s1/s2/text_chunk1.txt s1/s2/Advanced/text_chunk2.txt
echo "I like them because they help to keep dependencies required by different projects separate by creating isolated spaces for them that can be used for separate per-project dependencies" >> s1/s2/Advanced/text_chunk2.txt