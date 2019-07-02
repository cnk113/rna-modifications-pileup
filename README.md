# rna-modifications-pileup

## Scripts

`downloadReads.py` Downloads raw direct RNA-seq reads from the output of mapper.py which contains downloads to each individual raw FAST5 reads. Exact position matching the splice site reads.

```python downloadReads.py -reads [READS] -direct [DIRECTORY] -position [chr#:##]```

`generateIntrons.py` Use spliceSitePileup instead to generate intron retention events.

`getSpliceSeq.py` Outputs the sequence 5 bases upstream and downstream of that specific position. Uses output from spliceSitePileup.

```python getSpliceSeq.py -splice [SPLICE SITES] -fasta [REFERENCE FASTA] > [FILE]```

`kmerCoverage.py` Appends the IVT frequency and raw counts of the respective kmers from the output of `pileupParser.py`. Uses output from pileupParser for the direct reads.

```python kmerCoverage.py -i [IVT] -d [DIRECT] > [FILE]```

`mapper.py` Maps the read ID of the FAST5 reads to the respective download link and outputs the reads and the links. Uses output of spliceSitePileup for splice sites.

```python mapper.py -splice [SPLICE SITES] -runs [NANOPORE RUNS] -links [FAST5] > [FILE]```

`pileupParser.py` Parses mpileup output of reads and outputs the mismatch frequency and raw counts of inputted positions. Needs intron coordinates, direct reads, and reference FASTA.

```python pileupParser.py -p [MPILEUP] -c [INTRON] -f [FASTA] > [FILE]```

`removeReads.py` Removes given inputted reads from a FASTQ file and outputs the filtered reads. Uses output of spliceSitePileup or other barcode outputters.

```python removeReads.py -f [FASTQ] -r [SPLICE] > [FILE]```

`spliceSitePileup.py` Takes in intron coordinates as a BED file and psl of exons and outputs to stdout intron retention sites.

```python spliceSitePileup.py -introns [INTRONS] -psl [PSL] > [FILE]```

`subset.py` Outputs the FASTA sequence of the FAST5 reads. Needs reference FASTA, and exact position of the reads.

```python subset.py -fasta [FASTA] -reads [SPLICE] -pos [chr#:##] > [FILE]```

## Data
The current data in top directory is outputs of intermediary files of the scripts. The /splice directory contains all the ouputs from the spliceSitePileup.py with the file names as descriptors for the ends. The /pileup directory contains all the mpileup outputs. The /chr is the bed and psl files split by chromosome since spliceSitePileup.py is not parallelized yet. The /raw directory contains raw signal level data. The IVT data is in a single file, however the direct RNA is in multiple directories with variable depth directories which are split up by seperate runs, and this would require a custom directory parser to pull into a single directory. The rna-modifications-pileup directory contains all the scripts which is part of a github repo. A lot of the code needs to be refactored and some will be combined in the future. 

