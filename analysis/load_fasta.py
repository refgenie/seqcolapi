import henge
import os
import sys
import logging
import refgenconf
import seqcol

# TODO put this somewhere permanent
sys.path.append("seqcolapi")
from scconf import RDBDict

# set logging
_LOGGER = logging.getLogger()  # root logger
stream = logging.StreamHandler(sys.stdout)
fmt = logging.Formatter("%(levelname)s %(asctime)s | %(name)s:%(module)s:%(lineno)d > %(message)s ")
stream.setFormatter(fmt)
_LOGGER.setLevel(os.environ.get("LOGLEVEL", "DEBUG"))
_LOGGER.addHandler(stream)

scc = seqcol.SeqColConf()

# rgc = refgenconf.RefGenConf("/home/nsheff/Dropbox/env/refgenie_config/zither.yaml")

pgdb = RDBDict()  # parameterized through env vars

schenge = seqcol.SeqColHenge(
    database=pgdb,
    schemas=["/home/nsheff/code/seqcol/seqcol/schemas/SeqColArraySetInherent.yaml"],
    checksum_function=henge.sha512t24u_digest)

schenge.retrieve('xysio2')


from jinja2 import Environment, FileSystemLoader

def build_compare_table_html(results, outfile, host="http://seqcolapi.databio.org"):
    """ Build a "compare" link table. """
    env = Environment(loader=FileSystemLoader('/home/nsheff/code/seqcolapi/seqcolapi/templates'))
    template = env.get_template('comparison_matrix.html')
    output_from_parsed_template = template.render(results=results, host=host)
    print(output_from_parsed_template)
    # to save the results
    with open(outfile, "w") as fh:
        fh.write(output_from_parsed_template)

# Load demo fasta files
folder = "/home/nsheff/code/seqcol/demo_fasta"
demo_fasta_files = {
    "demo0": { "fasta": f"{folder}/demo0.fa" },
    "demo1": { "fasta": f"{folder}/demo1.fa.gz" },
    "demo2": { "fasta": f"{folder}/demo2.fa" },
    "demo3": { "fasta": f"{folder}/demo3.fa" },
    "demo4": { "fasta": f"{folder}/demo4.fa" },
    "demo5": { "fasta": f"{folder}/demo5.fa.gz" },
    "demo6": { "fasta": f"{folder}/demo6.fa" },
}

results = schenge.load_multiple_fastas(demo_fasta_files)
outfile = "/home/nsheff/work/resources/reference_fasta/links_demo.html"
outfile_local = "/home/nsheff/work/resources/reference_fasta/links_demo_local.html"
build_compare_table_html(results, outfile, host="")
build_compare_table_html(results, outfile_local, host="http://localhost:8101")


# Load reference human genomes
folder = "/home/nsheff/work/resources/reference_fasta"
ref_fasta_files = {
  "Ensembl GRCh38 primary assembly": f"{folder}/Homo_sapiens.GRCh38.dna.primary_assembly.fa",
  "Ensembl GRCh38 toplevel assembly": f"{folder}/Homo_sapiens.GRCh38.dna.toplevel.fa",
  "UCSC hg38": f"{folder}/hg38.fa",
  "NCBI GCA 000001405.28": f"{folder}/GCA_000001405.28_GRCh38.p13_genomic.fa",
  "chm13v2": f"{folder}/GCA_009914755.4_CHM13_T2T_v2.0_genomic.fna",
  "chm13v1.1": f"{folder}/chm13.draft_v1.1.fasta",
  "Refgenie hg38": rgc.seek("hg38", "fasta"),
  "Refgenie hg38 primary": rgc.seek("hg38_primary", "fasta"),
}

results_ref = schenge.load_multiple_fastas(ref_fasta_files)
outfile = "/home/nsheff/work/resources/reference_fasta/links_ref.html"
outfile_local = "/home/nsheff/work/resources/reference_fasta/links_new_local.html"
build_compare_table_html(results_ref, outfile, host="")
build_compare_table_html(results_ref, outfile_local, host="http://localhost:8101")

# If you want to get an output JSON of the loading results:
import json
print(json.dumps(results, default=lambda o: '<not serializable>', indent=2))

# How to view a database:
# schenge.show()  # only works for databases that implement .items()
# for k in pgdb:
#     print(k)

# How to empty a database
# for k in pgdb:
#     print(k)
#     del pgdb[k]


# Turn on debug logging like so:
import logging
import sys
log = logging.getLogger()
log.setLevel(logging.DEBUG)
stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.DEBUG)
log.addHandler(stream)
logging.getLogger("henge").setLevel(logging.DEBUG)
logging.getLogger("seqcol").setLevel(logging.DEBUG)



# Now this is just unpolished exploratory code for an interactive session:
# Can probably be removed soon (2023-03-02)

schenge.compare_digests("2786eb8a921aa97018c214f64b9960a0", "a6748aa0f6a1e165f871dbed5e54ba62")
schenge.compare_digests("c345e091cce0b1df78bfc124b03fba1c", "bd21d38bad9c8970bf7b1c725daa1939")
schenge.compare_digests("0183ee16bc66279006da59036441e0a9", "6e8e6adc1b11c0ef4b6550ce6a84e144")
schenge.compare_digests("6e8e6adc1b11c0ef4b6550ce6a84e144", "0183ee16bc66279006da59036441e0a9")
schenge.compare_digests("514c871928a74885ce981faa61ccbb1a", "c345e091cce0b1df78bfc124b03fba1c")
schenge.compare_digests("514c871928a74885ce981faa61ccbb1a", "6e8e6adc1b11c0ef4b6550ce6a84e144")
schenge.compare_digests("c345e091cce0b1df78bfc124b03fba1c", "6e8e6adc1b11c0ef4b6550ce6a84e144")
schenge.compare_digests("bd21d38bad9c8970bf7b1c725daa1939", "0183ee16bc66279006da59036441e0a9")

import pyfaidx
fa_object.keys()
fa_object = pyfaidx.Fasta("/home/nsheff/work/resources/reference_fasta/CM000663.2.fasta")
henge.md5(str(fa_object[0]))

fa_object2 = pyfaidx.Fasta("/home/nsheff/work/resources/reference_fasta/GCA_000001405.28_GRCh38.p13_genomic.fa")
henge.md5(str(fa_object2[0]).upper())

str(fa_object[0])[100:1000]

output_array = {}
step = 5000
for i in range(0, 10):
    start = i*step+1
    end = start + step -1
    print(i, start, end)
    output_array[i] = fa_object[0][start:end].seq fa_object2[0][start:end].seq

import difflib
x = [li for li in difflib.ndiff(str(fa_object[0]), str(fa_object2[0])) if li[0] != ' ']


# hg38 = load_refgenie_fasta("hg38")
# hg38_primary = load_refgenie_fasta("hg38_primary")
# t7 = load_refgenie_fasta("t7")
# sc.insert(seqcol.parse_fasta(fa_filepath))

import os
os.chdir("/home/nsheff/code/seqcolapi/seqcolapi")
import henge
import refgenconf
import scconf
import seqcol
rgc = refgenconf.RefGenConf("/home/nsheff/Dropbox/env/refgenie_config/zither.yaml")
import pyfaidx
filepath = rgc.seek("hg38_chr22", "fasta")

fa_object = pyfaidx.Fasta(filepath)
x2 = seqcol.fasta_to_scas(fa_object)

scc = scconf.SeqColConf(filepath="/home/nsheff/code/seqcolapi.databio.org/config/seqcolapi.yaml")

pgdb = scconf.RDBDict(scc.exp["database"]["name"],
                scc.exp["database"]["user"],
                scc.exp["database"]["password"],
                scc.exp["database"]["host"],
                scc.exp["database"]["port"])

schenge = seqcol.SeqColClient(database=pgdb,
    api_url_base="https://www.ebi.ac.uk/ena/cram/sequence/",
    schemas=["/home/nsheff/code/seqcol/seqcol/schemas/SeqColArraySetInherent.yaml"],
    checksum_function=henge.md5)

d = schenge.insert(x2, "SeqColArraySet", reclimit=1)
d
s
schenge.retrieve("8934293c230d540b3746d6d9b44171dd", reclimit=1)
schenge.retrieve(d, reclimit=0)


SCAS = schenge.load_fasta_from_filepath(filepath)
SCAS["SCAS"].keys()

SCAS["SCAS"]["names_lengths"] = seqcol.build_names_lengths(SCAS["SCAS"], schenge.checksum_function)
SCAS["SCAS"].keys()
valid_schema = schenge.schemas["SeqColArraySet"]

      item_inherent_split = henge.select_inherent_properties(SCAS["SCAS"], valid_schema)
      attr_string = henge.canonical_str(item_inherent_split["inherent"])
      external_string = henge.canonical_str(item_inherent_split["external"])

digest = schenge.insert(SCAS["SCAS"], "SeqColArraySet", reclimit=1)

SCAS.keys()


fa_file = rgc.seek("hg38", "fasta")
_LOGGER.info("Loading fasta file...")
import seqcol
fa_object = seqcol.parse_fasta(rgc.seek("hg38_chr22", "fasta"))
x = fasta_to_scas(fa_object)

fa_file = rgc.seek("hg38_primary", "fasta")
seqcol.fasta_to_scas(seqcol.parse_fasta(fa_file))

digest = sc.insert(seqcol.parse_fasta(rgc.seek("hg38_primary", "fasta")), "SeqColArraySet", reclimit=1)


t1: 12477e59b376cfb65257f320c95dc0c4







# OLDER NOTES below on how to load fastas
# and some exploratory code for how to load up different
# types of objects.

# This script will load all refgenie fasta assets into a seqcol database.

import os
os.chdir("/home/nsheff/code/seqcolapi/seqcolapi")

import refgenconf
from scconf import RDBDict, SeqColConf
import seqcol


rgc = refgenconf.RefGenConf("/home/nsheff/Dropbox/env/refgenie_config/zither.yaml")
scc = SeqColConf(filepath="/home/nsheff/code/seqcolapi.databio.org/config/seqcolapi.yaml")

pgdb = RDBDict(scc.database.name,
                scc.database.user,
                scc.database.password,
                scc.database.host,
                scc.database.port)

sc = seqcol.SeqColClient(database=pgdb,
    api_url_base="https://www.ebi.ac.uk/ena/cram/sequence/",
    schemas=["http://schema.databio.org/refget/TASeqCol.yaml"])

import henge

sc = seqcol.SeqColClient(database=pgdb,
    api_url_base="https://www.ebi.ac.uk/ena/cram/sequence/",
    schemas=["/home/nsheff/code/seqcol/seqcol/schemas/SeqColArraySet.yaml"],
    checksum_function=henge.md5)


rgc.seek("t7", "fasta")
rgc.seek("hg38", "fasta")
for g in rgc.list_genomes_by_asset("fasta"):
    print("Genome: {}".format(g))
    print(rgc.seek(g, "fasta"))
    res = sc.load_fasta2(rgc.seek(g, "fasta"))


    print(res)

fa_file= rgc.seek("t7", "fasta")
_LOGGER.info("Loading fasta file...")
fa_object = seqcol.parse_fasta(fa_file)


# Load fasta files, just the first layers.

# demo
import henge
k = 'V01146.1'
seq = str(fa_object[k])
digest = henge.md5(seq)
seqlen = len(seq)
name = k
asd = {'name': name, 'length': seqlen, 'sequence':digest}
sc.insert([asd], "RawSeqCol", reclimit=1)
cde034d7ba003ee98ff5e0ac7a8a5b49435b36d7a0151d2d
sc.retrieve("cde034d7ba003ee98ff5e0ac7a8a5b49435b36d7a0151d2d")
sc.retrieve("cde034d7ba003ee98ff5e0ac7a8a5b49435b36d7a0151d2d", reclimit=1)
sc.show()

# loop
for k in fa_object.keys():
    seq = str(fa_object[k])
    digest = henge.md5(seq)
    seqlen = len(seq)
    asd = {'name': name, 'length': seqlen, 'sequence':digest}
    digest = sc.insert([asd], "RawSeqCol", reclimit=1)
    _LOGGER.info("Digest: {}".format(digest))
    return digest


import henge
fa_file= rgc.seek("hg38", "fasta")
logging.info("Loading fasta file...")
logging.getLogger().setLevel("DEBUG")

logging.getLogger("henge").setLevel("DEBUG")

fa_object = seqcol.parse_fasta(fa_file)
import logging
ary = []
for k in fa_object.keys():
    seq = str(fa_object[k])
    digest = henge.md5(seq.upper())
    seqlen = len(seq)
    asd = {'name': k, 'length': seqlen, 'sequence':digest}
    ary.append(asd)
    logging.info("Name: {}. Length: {}. Digest: {}".format(k, seqlen, digest))
    
ary
digest = sc.insert(ary, "RawSeqCol", reclimit=1)

digest2 = sc.insert(ary[24:30], "RawSeqCol", reclimit=1)
sc.retrieve(digest2)
sc.database


digest
sc.retrieve(digest, reclimit=1)
hg19 demo:

sc.retrieve("6115e19530a7738af5be03469fe82b82c7485960b98741cd", reclimit=1)
6115e19530a7738af5be03469fe82b82c7485960b98741cd

# A few small examples from hg19
#INFO:root:Name: chrUn_KI270742v1. Length: 186739. Digest: 2f31c013a4a8301deb8ab7ed1ca1cd99                                                                        
#INFO:root:Name: chrUn_GL000216v2. Length: 176608. Digest: 725009a7e3f5b78752b68afa922c090c                                                                        
#INFO:root:Name: chrUn_GL000218v1. Length: 161147. Digest: 1d708b54644c26c7e01c2dad5426d38c 


x = [{"name": "chrUn_KI270742v1", "length": 186739, "sequence": "2f31c013a4a8301deb8ab7ed1ca1cd99"},
{"name": "chrUn_GL000216v2", "length": 176608, "sequence": "725009a7e3f5b78752b68afa922c090c"},                                                                        
{"name": "chrUn_GL000218v1", "length": 161147, "sequence": "1d708b54644c26c7e01c2dad5426d38c"}] 

y = ['linear', 'linear', 'linear']

topotest = sc.insert(x, "RawSeqCol", reclimit=1)
5655f27ed3dd7b8bb7c108c4ddc562979f82bc294877988c
z = {"topology": y,
"rawseqcol": ["ca1486e4dda7ca98fbeb3b2acdabfb2030485ca38ccab2ee","bdbec4e93a1b3ab28227d5ab8eec8a4411380c07809f35fd","b8457c89c79afff009c8c1737bf3edd9387ac8280a23364c"]}

complete = sc.insert(z, "TASeqCol", reclimit=1)
8c2396be37de71f77685fa36e5206da3dd5b702fa1511600

sc.retrieve("2f31c013a4a8301deb8ab7ed1ca1cd99")

sc.retrieve("8c2396be37de71f77685fa36e5206da3dd5b702fa1511600", reclimit=0)
sc.retrieve("8c2396be37de71f77685fa36e5206da3dd5b702fa1511600", reclimit=1)
sc.retrieve("8c2396be37de71f77685fa36e5206da3dd5b702fa1511600", reclimit=2)
res3 = sc.retrieve("8c2396be37de71f77685fa36e5206da3dd5b702fa1511600", reclimit=3)
resX = sc.retrieve("8c2396be37de71f77685fa36e5206da3dd5b702fa1511600")
resX[0]
resX.keys()
sc.retrieve("951c378c80dd043fe97bbb44c22bd7afb6931573905e3a13")

sc.retrieve("cda7ee53e5c2181a2f75ab4dffa608ee18874938ea13ae3d", reclimit=0)

# Load fasta files, all the way.
aslist = []
for k in fa_object.keys():
    seq = str(fa_object[k])
    _LOGGER.info("Loading key: {k} / Length: {l}...".format(k=k, l=len(seq)))
    aslist.append(
        {NAME_KEY: k, LEN_KEY: len(seq), TOPO_KEY: topology_default,
         SEQ_KEY: "" if skip_seq else seq}
    )
_LOGGER.info("Inserting into database...")
collection_checksum = self.insert(aslist, "RawSeqCol")
_LOGGER.debug(f"Loaded {ASL_NAME}: {aslist}")
return collection_checksum, aslist




# Topology-aware
http://seqcolapi.databio.org/seqcol/8c2396be37de71f77685fa36e5206da3dd5b702fa1511600/0
# {"topology":"951c378c80dd043fe97bbb44c22bd7afb6931573905e3a13",
# "rawseqcol":"5655f27ed3dd7b8bb7c108c4ddc562979f82bc294877988c"}

http://seqcolapi.databio.org/seqcol/8c2396be37de71f77685fa36e5206da3dd5b702fa1511600/1
#{"topology":["linear","linear","linear"],
# "rawseqcol":["ca1486e4dda7ca98fbeb3b2acdabfb2030485ca38ccab2ee",
# "bdbec4e93a1b3ab28227d5ab8eec8a4411380c07809f35fd",
# "b8457c89c79afff009c8c1737bf3edd9387ac8280a23364c"]}


# Just the contained RawSeqCol: 5655f27ed3dd7b8bb7c108c4ddc562979f82bc294877988c
http://seqcolapi.databio.org/seqcol/5655f27ed3dd7b8bb7c108c4ddc562979f82bc294877988c/0
#["ca1486e4dda7ca98fbeb3b2acdabfb2030485ca38ccab2ee",
# "bdbec4e93a1b3ab28227d5ab8eec8a4411380c07809f35fd",
# "b8457c89c79afff009c8c1737bf3edd9387ac8280a23364c"]
#

# And, of course, you can recurse.
http://seqcolapi.databio.org/seqcol/5655f27ed3dd7b8bb7c108c4ddc562979f82bc294877988c/1



# ArrayedSequenceCollections
# 2021-02-03
import logging
logging.basicConfig()
logging.getLogger('henge').setLevel(logging.DEBUG)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger().debug('bah')
logging.getLogger().info('bah')
logging.getLogger().warning('bah')
logging.getLogger('henge').debug('bah')

sc = seqcol.SeqColClient(database=pgdb,
    api_url_base="https://www.ebi.ac.uk/ena/cram/sequence/",
    schemas=["/home/nsheff/code/schema.databio.org/refget/ArrayedSequenceCollection.yaml"])



x = [{"name": "chrUn_KI270742v1", "length": 186739, "sequence": "2f31c013a4a8301deb8ab7ed1ca1cd99"},
{"name": "chrUn_GL000216v2", "length": 176608, "sequence": "725009a7e3f5b78752b68afa922c090c"},                                                                        
{"name": "chrUn_GL000218v1", "length": 161147, "sequence": "1d708b54644c26c7e01c2dad5426d38c"}] 


scarray = {"names": ["chrUn_KI270742v1", "chrUn_GL000216v2", "chrUn_GL000218v1"],
"lengths": ["186739", "176608", "161147"],
"sequences": ["2f31c013a4a8301deb8ab7ed1ca1cd99", "725009a7e3f5b78752b68afa922c090c",
"1d708b54644c26c7e01c2dad5426d38c"]
}

y = ['linear', 'linear', 'linear']
scarray2 = {"names": ["chrUn_KI270742v1", "chrUn_GL000216v2", "chrUn_GL000218v1"],
"lengths": ["186739", "176608", "161147"],
"sequences": ["2f31c013a4a8301deb8ab7ed1ca1cd99", "725009a7e3f5b78752b68afa922c090c",
"1d708b54644c26c7e01c2dad5426d38c"],
"topologies": y
}


arraytest = sc.insert(scarray, "ArrayedSequenceCollection", reclimit=1)
arraytest2 = sc.insert(scarray2, "ArrayedSequenceCollection", reclimit=1)

arraytest

sc.retrieve(arraytest, reclimit=0)
sc.retrieve(arraytest2, reclimit=0)
sc.retrieve(arraytest, reclimit=1)
res = sc.retrieve(arraytest, reclimit=2)
sc.retrieve(arraytest, reclimit=3)
sc.retrieve(arraytest)
topologies



sc.retrieve(arraytest, reclimit=0)
res2 = sc.retrieve(arraytest2, reclimit=1)

ks = list(res2.keys())
print(ks)
for i in range(len(res2)//2):
    print([v[i] if v else None for k,v in res2.items()])




annoarray = {
    "seqcol": {
        "names": ["chrUn_KI270742v1", "chrUn_GL000216v2", "chrUn_GL000218v1"],
        "lengths": ["186739", "176608", "161147"],
        "sequences": ["2f31c013a4a8301deb8ab7ed1ca1cd99", "725009a7e3f5b78752b68afa922c090c", "1d708b54644c26c7e01c2dad5426d38c"]
    },
    "annotation": [{
        "property_name": "topology"
        "property_value": y
    }]
}

annoarray = {
    "seqcol": {
        "names": ["chrUn_KI270742v1", "chrUn_GL000216v2", "chrUn_GL000218v1"],
        "lengths": ["186739", "176608", "161147"],
        "sequences": ["2f31c013a4a8301deb8ab7ed1ca1cd99", "725009a7e3f5b78752b68afa922c090c", "1d708b54644c26c7e01c2dad5426d38c"]
    },
    "annotation": [{"name": "topology",
                    "value": y },
                    {"name": "importance",
                    "value": ['primary', 'primary', 'primary']}]
}



{'seqcol': {'names': ['chrUn_KI270742v1',
   'chrUn_GL000216v2',
   'chrUn_GL000218v1'],
  'lengths': ['186739', '176608', '161147'],
  'sequences': ['2f31c013a4a8301deb8ab7ed1ca1cd99',
   '725009a7e3f5b78752b68afa922c090c',
   '1d708b54644c26c7e01c2dad5426d38c']},
 'annotation': [{'name': 'topology', 'value': ['linear', 'linear', 'linear']},
  {'name': 'priority', 'value': ['primary', 'primary', 'primary']}]}




{'seqcol': {'names': ['chrUn_KI270742v1',
   'chrUn_GL000216v2',
   'chrUn_GL000218v1'],
  'lengths': ['186739', '176608', '161147'],
  'sequences': ['2f31c013a4a8301deb8ab7ed1ca1cd99',
   '725009a7e3f5b78752b68afa922c090c',
   '1d708b54644c26c7e01c2dad5426d38c']},
 'annotation': [{'name': 'topology', 'value': ['linear', 'linear', 'linear']},
  {'name': 'priority', 'value': ['primary', 'primary', 'primary']}]}


{'lengths': ['186739', '176608', '161147'],
 'sequences': ['2f31c013a4a8301deb8ab7ed1ca1cd99',
   '725009a7e3f5b78752b68afa922c090c',
   '1d708b54644c26c7e01c2dad5426d38c'],
 'annotation': {
    'names': ['chrUn_KI270742v1', 'chrUn_GL000216v2', 'chrUn_GL000218v1'],
    'topologies': ['linear', 'linear', 'linear'],
    'masks': '',
    'priorities': ''
 }
}

'topologies': '951c378c80dd043fe97bbb44c22bd7afb6931573905e3a13',

{'annotation': [{'name': 'topology', 'value': ['linear', 'linear', 'linear']},
  {'name': 'priority', 'value': ['primary', 'primary', 'primary']}]


digest:


name-chrUn_KI270742v1,chrUn_GL000216v2,chrUn_GL000218v1;sequence-2f31c013a4a8301deb8ab7ed1ca1cd99,725009a7e3f5b78752b68afa922c090c,1d708b54644c26c7e01c2dad5426d38c;




description: "A collection of sequences"
type: object
properties:
  seqcol:
    type: object
    properties:
      names:
        type: array
        items:
          type: string
      lengths:
        type: array
        items:
          type: integer
      sequences:
        type: array
        items:
          type: string
          description: "Actual sequence content"
  annotation:
    type: array
    items:
      type: object
      properties:
        name:
          type: string
        value:
          type: array
required:
  - lengths




# If we nest them so it's seqcol/annotation, then the seqcols can get their
# own aggregate identifier. but, it adds some hierarchy.

# if we make the annotation with fixed slots, we can't add something else in
# the future, like new flags, because digests under the new schema would not
# be backwards compatible for the same content, as the digest includes a slot
# for elements that did not exist in the outdated schema.

# if we make the annotation with flexible slots, we
# require some other specification for slot names and what they allow, like a
# subschema.

# The solution was to not use the schema



# Testing array approach with flexible digests; 2021-04-07

y = {"names": ["A", "B", "C"],
  "lengths": ["1216", "970", "1788"],
  "sequences": ["76f9f3315fa4b831e93c36cd88196480", "d5171e863a3d8f832f0559235987b1e5",
    "b9b1baaa7abf206f6b70cf31654172db"]}

d = sc.insert(y, "SeqColArraySet", reclimit=1)
d = "a6748aa0f6a1e165f871dbed5e54ba62"
sc.retrieve(d)

sc.retrieve(d, reclimit=1)




y2 = {"topologies": ["linear", "linear", "linear"],
  "names": ["A", "B", "C"],
  "lengths": ["1216", "970", "1788"],
  "sequences": ["76f9f3315fa4b831e93c36cd88196480", "d5171e863a3d8f832f0559235987b1e5",
    "b9b1baaa7abf206f6b70cf31654172db"]}

d2 = sc.insert(y2, "SeqColArraySet", reclimit=1)
d2 = "2786eb8a921aa97018c214f64b9960a0"




# http://localhost:8100/seqcol/2786eb8a921aa97018c214f64b9960a0/0
# http://localhost:8100/seqcol/a6748aa0f6a1e165f871dbed5e54ba62/0





