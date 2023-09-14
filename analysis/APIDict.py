import abc
from collections.abc import Mapping, MutableMapping
import requests

# This is meant to be a dict-like object that wraps an API;
# the refget API specifically.
# The idea is that this could be the start of a back-end
# for a henge. But I think I came up with other approaches.

# a = APIDict()
# a["68a178f7c740c5c240aa67ba41843b119d3bf9f8b0f0ac36"]


class APIDict(MutableMapping):
    def __getattr__(self, item, default=None):
        base = "https://refget.herokuapp.com/sequence/"
        url = "{base}{digest}?accept=text/plain".format(base=base, digest=item)
        r = requests.get(url)
        result = r.content.decode("utf-8")
        print(url)
        return result

    def __delitem__(self, item):
        pass

    def __getitem__(self, item):
        base = "https://refget.herokuapp.com/sequence/"
        url = "{base}{digest}?accept=text/plain".format(base=base, digest=item)
        r = requests.get(url)
        result = r.content.decode("utf-8")
        print(url)
        return result

    def __setitem__(self, key, value):
        pass

    def __iter__(self):
        return iter([k for k in self.__dict__.keys()])

    def __len__(self):
        return sum(1 for _ in iter(self))

    def __repr__(self):
        return self._render(
            self._simplify_keyvalue(self._data_for_repr(), self._new_empty_basic_map)
        )
