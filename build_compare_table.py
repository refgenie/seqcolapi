
from jinja2 import Environment, FileSystemLoader

# This code just builds a "compare" link table
def build_compare_table_html(digests, outfile):
    env = Environment(loader=FileSystemLoader('/home/nsheff/code/seqcolapi/seqcolapi/templates'))
    template = env.get_template('comparison_matrix.html')
    output_from_parsed_template = template.render(digests=digests)
    print(output_from_parsed_template)
    # to save the results
    with open(outfile, "w") as fh:
        fh.write(output_from_parsed_template)

# Example:
digests = {
    "Ensembl GRCh38 primary assembly": "6e8e6adc1b11c0ef4b6550ce6a84e144",
    "Ensembl GRCh38 toplevel assembly": "0183ee16bc66279006da59036441e0a9",
    "UCSC hg38": "2edb0726016c13426eaa607f64450f52",
    "NCBI GCA 000001405.28": "bd21d38bad9c8970bf7b1c725daa1939",
    "Refgenie hg38": "514c871928a74885ce981faa61ccbb1a",
    "Refgenie hg38 primary": "c345e091cce0b1df78bfc124b03fba1c"
}

outfile = "/home/nsheff/work/resources/reference_fasta/links.html"
build_compare_table_html(digests, outfile)

