Use case:
```
python3 main.py -p <path-to-datachunk>
```



or with multiple paths to datachunks:
```
python3 main.py -p <path1-to-datachunk> <path2-to-datachunk> <path3-to-datachunk>
```

<br/>

For example:
```
python3 main.py -p "crawl-data/CC-MAIN-2022-49/segments/1669446706285.92/wat/CC-MAIN-20221126080725-20221126110725-00000.warc.wat.gz"
```

<br/>

Uses HTTPS to get datachunk via https://data.commoncrawl.org/.

<br/>

Links found in the datachunks that have links to images is saved in the file called ```records-img-links.csv``` with the origin link as the first column and a string of the list with image links as the second column in the csv file.
