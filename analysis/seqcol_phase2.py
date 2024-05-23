
# Here is some code that explores using the new gc_count package
# To run the digests using rust, called from Python.
# from 2024-05-22.
# it worked beatifull, just needs to be cleaned up.

from gc_count import checksum
results = checksum("analysis/data/test_data/base.fa")
results

from_gz = checksum("analysis/data/demo/demo0.fa.gz")


import refget
import json

refget.fasta_file_to_digest("analysis/data/test_data/base.fa")
refget.fasta_file_to_digest("analysis/data/demo/demo0.fa.gz")


refget.fasta_file_to_seqcol("analysis/data/test_data/base.fa")
refget.fasta_file_to_seqcol("analysis/data/demo/demo0.fa.gz")


digest_function = refget.sha512t24u_digest_bytes

def canonical_str(item: dict) -> bytes:
    """Convert a dict into a canonical string representation"""
    return json.dumps(
        item, separators=(",", ":"), ensure_ascii=False, allow_nan=False, sort_keys=True
    ).encode()




s = results[0]
for s in results:
    seq_name = s.id
    seq_length = s.length
    seq_digest = "SQ." + s.sha512
    snlp = {"length": seq_length, "name": seq_name}  # sorted_name_length_pairs
    snlp_digest = digest_function(canonical_str(snlp))
    CSC["lengths"].append(seq_length)
    CSC["names"].append(seq_name)
    CSC["sorted_name_length_pairs"].append(snlp_digest)
    CSC["sequences"].append(seq_digest)
CSC["sorted_name_length_pairs"].sort()

refget.seqcol_digest(CSC)

from typing import Optional, Callable, Union

def fasta_file_to_seqcol(
    fasta_file_path: str,
    digest_function: Callable[[bytes], str] = refget.sha512t24u_digest_bytes,
) -> dict:
    """
    Convert a FASTA file into a Sequence Collection digest.
    """
    results = checksum(fasta_file_path)
    CSC = {"lengths": [], "names": [], "sequences": [], "sorted_name_length_pairs": []}
    for s in results:
        seq_name = s.id
        seq_length = s.length
        seq_digest = "SQ." + s.sha512
        snlp = {"length": seq_length, "name": seq_name}  # sorted_name_length_pairs
        snlp_digest = digest_function(canonical_str(snlp))
        CSC["lengths"].append(seq_length)
        CSC["names"].append(seq_name)
        CSC["sorted_name_length_pairs"].append(snlp_digest)
        CSC["sequences"].append(seq_digest)
    CSC["sorted_name_length_pairs"].sort()    
    return CSC

def fasta_file_to_digest(fasta_file_path: str): 
    return refget.seqcol_digest(fasta_to_seqcol(fasta_file_path))

fasta_file_to_seqcol("analysis/data/test_data/base.fa")
fasta_file_to_digest("analysis/data/test_data/base.fa")





# Next, I've been thinking about how to store the collections in a database.
# I would like to move away from using henge, and do models.
# Here I'm exploring how to use SQLModel to do this.
# I actually think I shouldn't bother with the auto-generation of the pydantic
# objects, I should just make the models what I want them to be at first,
# and then later I can worry about that.

# the one issue is this: Sequence collections are made up of lists/arrays. These
# do not naturally fit in the database. So, maybe the models should actually 
# look different.

import pydantic

from pydantic import BaseModel, create_model

from typing import List 
# First, get a dict of attributes from the JSON Schema:

kwargs = {
	"names":(List, []),
	"sequences":(List, []),
	"lengths":(List, []),
}

# Now, create a pydantic model (really, a SQLModel model)
from sqlmodel import SQLModel


SequenceCollection = create_model(
    'SequenceCollection', **kwargs,
    __base__=SQLModel
) 

# could add: __cls_kwargs__={"table": True},

# Now we can create a SequenceCollection object

seqcol1 = SequenceCollection(**{
	"sequences": [1,2,3],
	"lengths": [4,5,6]
})

# Here's another type of object that has had its identifier computed:

DigestedSequenceCollection = create_model(
	'DigestedSequenceCollection', digest=(str, ""), 
	__base__=SequenceCollection,
	__cls_kwargs__={"table": True})

# Create one

sc1id = DigestedSequenceCollection.model_validate(seqcol1)

# Add digest on
sc1id.digest="123"
sc1id

# Should probably just add the level 1 form right there as well:

sc1id.level1 = {
	"attr": digest,
	"attr2": digest2,
	etc.
}

Then








# Need some better code in the refget package for handling schemas. Here's a start:



def is_url(maybe_url):
    from urllib.parse import urlparse

    return " " not in maybe_url and urlparse(maybe_url).scheme != ""

def read_schema(schema):
    """
    Load a schema from a file, URL, dict, or string
    """

    if isinstance(schema, dict):
        return schema
    elif os.path.exists(schema):
        if schema.endswith(".yaml") or schema.endswith(".yml"):
            return yacman.load_yaml(schema_value)
        elif schema.endswith(".json"):
            with open(schema, "r") as f:
                return json.load(f)
    elif is_url(schema):
        try:
            return requests.get(schema).json()
        except requests.exceptions.JSONDecodeError:
            return yacman.load_yaml(schema)
    else:
        raise ValueError(f"Could not read schema from {schema}")

