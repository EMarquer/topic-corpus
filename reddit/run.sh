#!/bin/bash

{
    scrapy runspider ./spider.py -o output.json
} || {
    echo "failed to directly activate scrapy, falling back to"
    echo "D:/Logiciels/Anaconda3/condabin/conda.bat run scrapy"
    D:/Logiciels/Anaconda3/condabin/conda.bat run scrapy runspider ./spider.py -o output.json
}


sleep 20