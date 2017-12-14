#!/usr/bin/python
# -*- coding: utf-8 -*-

class Document:
    """
    A very simple and straightforward implementation of a document.
    Here, a document is a simple collection of typed fields.

    Note that what we index are normalized versions of the raw fields. We keep
    the raw fields here in order to preserve the original presentation.
    """

    def __init__(self, document_id, fields):
        self.document_id = document_id
        self.fields = fields

    def __repr__(self):
        return str({"document_id": self.document_id, "fields" : self.fields})

class InMemoryCorpus:
    """
    An in-memory implementation of a document store, suitable only for small
    document collections.

    Document identifiers are assigned on a first-come first-serve basis.
    """

    def __init__(self, filename = None):
        self._documents = []
        if filename:
            if filename.endswith(".txt"):
                self._load_text(filename)
            elif filename.endswith(".xml"):
                self._load_xml(filename)
            elif filename.endswith(".json"):
                self._load_json(filename)
            else:
                raise IOError("Unsupported extension")

    def __iter__(self):
        return iter(self._documents)

    def size(self):
        """
        Returns the size of the corpus, i.e., the number of documents in the
        document collection.
        """
        return len(self._documents)

    def get_document(self, document_id):
        """
        Returns the document associated with the given document identifier.
        """
        assert document_id >= 0 and document_id < len(self._documents)
        return self._documents[document_id]

    def add_document(self, document):
        """
        Adds the given document to the corpus. Facilitates testing.
        """
        assert document.document_id == len(self._documents)
        self._documents.append(document)

    def _load_text(self, filename):
        """
        Loads documents from the given text file. One document per line,
        tab-separated fields. Empty lines are ignored. The first field is
        gets named "body", the second field (optional) gets named "meta".
        All other fields are currently ignored.
        """
        document_id = 0
        with open(filename, "r") as f:
            for line in f:
                anonymous_fields = line.strip().split("\t") # One document per line, tab-separated fields.
                if len(anonymous_fields) == 1 and not anonymous_fields[0]:
                    continue
                named_fields = {"body": anonymous_fields[0]}
                if len(anonymous_fields) >= 2:
                    named_fields["meta"] = anonymous_fields[1]
                self.add_document(Document(document_id, named_fields))
                document_id += 1

    def _load_xml(self, filename):
        """
        Loads documents from the given XML file. The schema is assumed to be
        simple <doc> nodes. Each <doc> node gets mapped to a single document field
        named "body".
        """
        from xml.dom.minidom import parse
        def __get_text(nodes):
            data = []
            for node in nodes:
                if node.nodeType == node.TEXT_NODE:
                    data.append(node.data)
            return " ".join(data)
        dom = parse(filename)
        document_id = 0
        for body in [__get_text(n.childNodes) for n in dom.getElementsByTagName("doc")]:
            self.add_document(Document(document_id, {"body": body}))
            document_id += 1

    def _load_json(self, filename):
        """
        Loads documents from the given JSON file. One document per
        line. Lines that do not start with "{" are ignored.
        """
        from json import loads
        document_id = 0
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("{"):
                    named_fields = loads(line)
                    self.add_document(Document(document_id, named_fields))
                    document_id += 1

if __name__ == "__main__":
    corpus = InMemoryCorpus("data/mesh.txt")
    print(*corpus, sep = "\n")
    print(corpus.size())
    corpus = InMemoryCorpus("data/cran.xml")
    print(*corpus, sep = "\n")
    print(corpus.size())
    corpus = InMemoryCorpus("data/docs.json")
    print(*corpus, sep = "\n")
    print(corpus.size())
