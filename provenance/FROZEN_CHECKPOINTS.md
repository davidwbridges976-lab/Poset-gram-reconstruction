# Frozen Checkpoint Provenance

Current packaged checkpoint: **v80 - Track A / Track C Descriptive Matched-Population Comparison**.

## Represented checkpoint chain

* v74 - Track A independent benchmark: 315/315 validated reconstructions.
* v75 - Track B cvc5 partial run: 10/315 executed; all 10 TIMEOUT; frozen incomplete.
* v76 - Track C 2-WL matched-workload protocol defined before execution.
* v77 - exact 2-WL implementation and timing boundary audited and frozen before benchmark execution.
* v78 - optimized 2-WL matched its reference on specified controls and frozen workload; zero Track C timing observations at this stage.
* v79 - Track C benchmark frozen complete.
* v80 - descriptive Track A / Track C comparison frozen complete.

## Selected SHA-256 records

* v74 Track A executed source: `ef5a91e87597da0cfaa2869d10f8aae0978d3880123db5ae40d6d7a085de4040`
* v74 Track A raw results: `429430fb692d2b2e36afd10da03330e93566906ae650b9362f12207f29dfcd91`
* v75 frozen ZIP: `8ced7ffd080c68237b44e5500f7f9b0e8eb25a64d23222cceed1442788a407ff`
* historical 2-WL reference source: `c02dfc41a5217ee106d314f79d7cc12e2433df10bc6677850e9f3980eee78135`
* v78 optimized 2-WL source: `e027b937b9b403f7f7427f22da038b8a7d3ace7f1cd2218e1e0c2b50ec4a581c`
* v79 frozen ZIP: `24f9ccb4f18197e5269c32f84aa67accef7f763d25a6541fe7eac22c916d2494`
* v80 frozen result JSON: `72260846e719199aa733cb1e5a44c0375ab336a0dc7f9a5a7c860b53696b8b17`
* v80 frozen ZIP: `a072083876100a48b0cd447e81b41c94821b77350a5ce487ebae277285305114`

This repository is a packaging layer. These historical hashes are retained so later publication work does not silently rewrite the frozen research record.
