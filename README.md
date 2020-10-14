# genbank_filter.py
Sometimes MultiFASTA files from GenBank may be pretty random in terms of taxonomy. You may find duplicate sequences in files for different genera. The issue was more severe years ago, but still occurs from time to time. This sctipt checks for identical entiries in MultiFASTA files (using sequence names only), deletes them from all original files and writes them into a separate file called "repeats.fas".

Usage:
./genbank_filter.py file_1.fas file_2.fas


# Warning!
If repeating sequences are found, the sctipt changes original file structure. Sequences are joined into one line and their order might be changed.
