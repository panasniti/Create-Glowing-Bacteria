# Create-Glowing-Bacteria
Learn about bacterial genome organization and genetic engineering techniques, work on data sequencing, and see how Python can be applied to bioinformatics.

STAGE-1: Write a code that creates a complementary strand of the original DNA sequence.

STAGE-2: Cut a double-stranded plasmid to form the sticky ends.

STAGE-3: Create a complementary strand of the GFP gene sequence.

STAGE-4: Cut a double-stranded GFP gene to produce the sticky ends that are complementary to the sticky ends of the plasmid.

STAGE-5: Insert the gene in the plasmid gap and ligate the sticky ends.

STAGE-6: Apply the knowledge from the previous stage and get the final bacterium!



Write code that takes the file's name as input and automatically processes the data. The file content you can find below.
Your code should create complementary strands for plasmid and GFP sequences, cut them according to restriction sites, and ligate the sticky parts together. The result should be a double-stranded modified plasmid with a GFP insertion. Do not forget to print it!

If there are multiple restriction sites in the GFP sequence, use the sites closest to the edges of the GFP sequence. This action will avoid cutting the functional part of the GFP gene and losing its functionality.

The input file content:
* The original plasmid strand;
* The restriction site for cutting the plasmid;
* The GFP original strand;
* Two left and right restriction sites for GFP cutting.
You have an example files "plasmid_gfp_example.txt" and "example1.txt". Use it to test that your program takes a file name as input and processes it correctly.
