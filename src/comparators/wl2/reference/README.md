# Historical directed 2-WL reference

The byte-authoritative historical implementation is identified by SHA-256:

`c02dfc41a5217ee106d314f79d7cc12e2433df10bc6677850e9f3980eee78135`

It was independently recovered in the supplied frozen v77/v78/v80 archive chain and is the reference implementation against which the optimized v78 Track C implementation was checked.

The reference semantics use directed ordered 2-tuples, equality and directed relation data in the initial atomic color, coordinate-replacement refinement with shared palettes across a compared batch, and a stability criterion based on absence of splitting of an old color class.

This note does not substitute reconstructed code for the original source. The original source should be copied here only byte-for-byte from a verified archive.
