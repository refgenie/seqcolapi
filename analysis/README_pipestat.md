## How could SeqColAPI use a pipestat-backed henge?

### Problem description

For a henge object, I use a `RDBDict`. This is basically a dict object backed by postgres. It just turns it into a key-value store. I wanted to see if I could use pipestat for this instead, because then I wouldn't need to maintain a separate database-insertion tool (RDBDict), I could just use pipestat.

At first, I thought it wouldn't work because of the restriction caused by the schema. In the typical dict, you can insert whatever key:value pairs you want. The keys are not restricted. In contrast, with pipestat, the keys *are* restricted to the output schema. This is because it uses those keys as table attributes, such that each sample is a row in the table. That has its advantages, but it means I can't just insert arbitrary keys. So, I thought pipestat wouldn't work there. However, this was assuming that the identifier would be a result key -- in fact, this turns out to not be true.

### Solution: it should actually work...

Right now, bracket notation on a pipestat object actually means a `record_identifier`, not a `result_identifier`. This means it *will* work as a back-end for Henge. In fact, its a schema with one attribute: "value". YES! Record identifier = digest, content = value (seqcol content)

| record_id | value   |
| --------- | ------- |
| digest1   | content |
| digest2   | content |

Basically, this just means you can use Pipestat as a key-value store if you think of the keys as record identifiers (in some namespace), and the value as a single result reported for that sample.

Here, we made the changes so that you could use a pipestat manager as a Mapping object, enabling item-based insertion/retrieval: https://github.com/pepkit/pipestat/issues/99

I guess the RBDBict object could live under a db-optional-dependencies in henge. (?)
