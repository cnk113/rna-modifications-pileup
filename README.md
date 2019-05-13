# rna-modifications-pileup

## Scripts

`downloadReads.py` Downloads raw direct RNA-seq reads from the output of mapper.py which contains downloads to each individual raw FAST5 reads.

`generateIntrons.py` Outputs the introns that are retained from a PSL file that has the coordinates of intron coordinates.

`getSpliceSeq.py` Outputs the sequence 5 bases upstream and downstream of that specific position.

`kmerCoverage.py` Appends the IVT frequency and raw counts of the respective kmers from the output of `pileupParser.py`.

`mapper.py` Maps the read ID of the FAST5 reads to the respective download link and outputs the reads and the links.

`pileupParser.py` Parses mpileup output of reads and outputs the mismatch frequency and raw counts of inputted positions.

`removeReads.py` Removes given inputted reads from a FASTQ file and outputs the filtered reads.

`spliceSitePileup.py` Takes in intron coordinates as a BED file and psl of exons and outputs to stdout intron retention sites.

`subset.py` Outputs the FASTA sequence of the FAST5 reads.
