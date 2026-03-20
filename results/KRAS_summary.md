# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT

## 1. Executive Summary

This report consolidates multi-source evidence on KRAS across target annotation, genetic dependency profiling, disease associations, and literature coverage.

- Target annotation (Pharos): KRAS is annotated as “GTPase KRas” within the Enzyme family, Target Development Level (TDL) = Tclin, with 223 ligands and novelty = 0.00013856. The source reports disease_association_count = 0 (top_diseases list empty).
- Genetic dependency (DepMap 25Q3 CRISPRGeneEffect): A global average gene effect of −0.701960413292113 (supporting average_gene_effect = −0.702) across 1169 cell lines, with 571 cell lines meeting a strong dependency threshold (≤ −0.5), corresponding to a strong_dependency_fraction of 0.4885. Fourteen top cell-line–specific records show very strong negative gene effects ranging from −4.282333642061707 to −3.116811038474391, each ranked among the most depleted for KRAS in its profile.
- Disease association (Open Targets official MCP): Fifteen high-ranking disease associations are reported, with evidence scores between 0.8263230926056322 and 0.6928072321318326. The associated diseases span developmental syndromes (e.g., Noonan syndrome 3, cardiofaciocutaneous syndrome 2) and malignancies (e.g., non-small cell lung carcinoma, gastric cancer, acute myeloid leukemia, lung adenocarcinoma, urinary bladder cancer, Juvenile Myelomonocytic Leukemia). Tractability annotations include “SM: High-Quality Ligand,” “PR: Small Molecule Binder,” and “AB: GO CC high conf.”
- Literature (Europe PMC): The query “KRAS” returned 121,780 total hits, with the top 15 articles (by citations) showing cited-by counts from 4,703 to 12,773 and publication years 2011–2020. Titles span hallmark resources and disease-specific characterizations, underscoring extensive research coverage involving KRAS.

Integrated, these data depict KRAS as a clinically developed enzyme target with substantial small-molecule tractability indicators, strong and frequent in vitro genetic dependencies across nearly half of profiled cancer cell lines, extensive disease linkages across both syndromic and neoplastic conditions, and a large, highly cited literature corpus. While some cross-source divergences exist (e.g., Pharos disease_association_count = 0 versus extensive Open Targets disease associations), the overall evidence converges on KRAS as a highly validated therapeutic target supported by robust quantitative and bibliographic signals.

## 2. Target Annotation Evidence

Pharos provides a concise target-level annotation indicating clinical development status, biochemical categorization, and ligand landscape.

Table: Pharos target annotation (KRAS)
- Source: PHAROS (community MCP)
- Provider (provenance): PHAROS (community MCP)
- Endpoint: http://127.0.0.1:8787/sse
- Retrieved at: 2026-02-23T13:16:16.754321Z / 2026-02-23T13:16:16.754625Z

| Target Symbol | Target Name    | Family | TDL   | Ligand Total | Novelty   | Disease Association Count | Top Diseases |
|---------------|----------------|--------|-------|--------------|-----------|---------------------------|--------------|
| KRAS          | GTPase KRas    | Enzyme | Tclin | 223          | 0.00013856| 0                         | []           |

Interpretation grounded in the evidence:
- KRAS is classified within the Enzyme family and annotated at the Tclin stage, accompanied by a high ligand count (223) and a very low novelty metric (0.00013856), which together indicate a mature target landscape in this source. Pharos lists no associated diseases in this record (disease_association_count = 0; top_diseases empty), which should be contextualized alongside disease association data from Open Targets presented below.

## 3. Genetic Dependency Evidence

DepMap CRISPR gene effect profiling (data release: DepMap 25Q3) offers both a global dependency perspective and high-confidence cell line–specific dependencies for KRAS.

### - Global Dependency Analysis

- Summary (DepMap CRISPRGeneEffect, column "KRAS (3845)"): Average gene effect = −0.701960413292113 (supporting average_gene_effect = −0.702) across 1169 cell lines. Strong dependency defined at ≤ −0.5 was observed in 571 lines, yielding a strong_dependency_fraction of 0.4885.
- Normalized_score = 0.7339868044307044; confidence = 0.9465355004277161.
- Provenance: DepMap (Broad Institute), endpoint: /Users/apple/Projects/Agent4agent/mcps/connectors/.depmap_cache/CRISPRGeneEffect.csv, retrieved at 2026-02-23T13:16:25.149734Z / 2026-02-23T13:16:25.150480Z.

Table: DepMap global KRAS dependency metrics

| Screen Type       | Data Release | Cell Line Count | Raw Avg Gene Effect | Average Gene Effect (support) | Strong Dependency Count (≤ −0.5) | Strong Dependency Fraction | Column Name    | Normalized Score       | Confidence            |
|-------------------|--------------|-----------------|---------------------|-------------------------------|-----------------------------------|----------------------------|----------------|------------------------|-----------------------|
| CRISPRGeneEffect  | DepMap 25Q3  | 1169            | −0.701960413292113  | −0.702                        | 571                               | 0.4885                     | KRAS (3845)    | 0.7339868044307044     | 0.9465355004277161    |

Interpretation grounded in the evidence:
- The magnitude of the global average gene effect (negative values indicate reduced viability upon gene knockout in this screen) and the strong dependency fraction of 0.4885 indicate that KRAS shows a pervasive dependency phenotype across a large fraction of the profiled cell line panel. The high confidence value (0.9465355004277161) further supports the robustness of this observation within the dataset.

### - Top Dependent Cell Lines

DepMap provides 14 top-ranking cell line–specific dependencies for KRAS, each with strongly negative gene effects and consistent screen metadata (CRISPRGeneEffect; DepMap 25Q3). All show normalized_score = 1.0 and confidence = 0.95 in these cell-specific records.

Table: KRAS cell line–specific dependencies (DepMap 25Q3)

| Cell Line ID | Gene Effect (raw_value)      | Rank Within Gene | Screen Type       | Data Release | Normalized Score | Confidence | Column Name  | Retrieved At                          |
|--------------|------------------------------|------------------|-------------------|--------------|------------------|------------|--------------|----------------------------------------|
| ACH-000222   | −4.282333642061707           | 1                | CRISPRGeneEffect  | DepMap 25Q3  | 1.0              | 0.95       | KRAS (3845)  | 2026-02-23T13:16:25.154337Z / .154359Z |
| ACH-000417   | −3.859175181932871           | 2                | CRISPRGeneEffect  | DepMap 25Q3  | 1.0              | 0.95       | KRAS (3845)  | 2026-02-23T13:16:25.154373Z / .154378Z |
| ACH-000505   | −3.813618178730868           | 3                | CRISPRGeneEffect  | DepMap 25Q3  | 1.0              | 0.95       | KRAS (3845)  | 2026-02-23T13:16:25.154385Z / .154389Z |
| ACH-000235   | −3.493769063134753           | 4                | CRISPRGeneEffect  | DepMap 25Q3  | 1.0              | 0.95       | KRAS (3845)  | 2026-02-23T13:16:25.154394Z / .154398Z |
| ACH-000042   | −3.3382458558302908          | 5                | CRISPRGeneEffect  | DepMap 25Q3  | 1.0              | 0.95       | KRAS (3845)  | 2026-02-23T13:16:25.154403Z / .154407Z |
| ACH-000264   | −3.2957726549898902          | 6                | CRISPRGeneEffect  | DepMap 25Q3  | 1.0              | 0.95       | KRAS (3845)  | 2026-02-23T13:16:25.154411Z / .154415Z |
| ACH-000114   | −3.2737514961631673          | 7                | CRISPRGeneEffect  | DepMap 25Q3  | 1.0              | 0.95       | KRAS (3845)  | 2026-02-23T13:16:25.154419Z / .154422Z |
| ACH-001494   | −3.2533369724960775          | 8                | CRISPRGeneEffect  | DepMap 25Q3  | 1.0              | 0.95       | KRAS (3845)  | 2026-02-23T13:16:25.154426Z / .154429Z |
| ACH-000532   | −3.2246661738099593          | 9                | CRISPRGeneEffect  | DepMap 25Q3  | 1.0              | 0.95       | KRAS (3845)  | 2026-02-23T13:16:25.154434Z / .154437Z |
| ACH-000468   | −3.212991606674046           | 10               | CRISPRGeneEffect  | DepMap 25Q3  | 1.0              | 0.95       | KRAS (3845)  | 2026-02-23T13:16:25.154442Z / .154446Z |
| ACH-000489   | −3.148050131195453           | 11               | CRISPRGeneEffect  | DepMap 25Q3  | 1.0              | 0.95       | KRAS (3845)  | 2026-02-23T13:16:25.154450Z / .154458Z |
| ACH-000652   | −3.142153492949226           | 12               | CRISPRGeneEffect  | DepMap 25Q3  | 1.0              | 0.95       | KRAS (3845)  | 2026-02-23T13:16:25.154463Z / .154467Z |
| ACH-000517   | −3.1288553251818207          | 13               | CRISPRGeneEffect  | DepMap 25Q3  | 1.0              | 0.95       | KRAS (3845)  | 2026-02-23T13:16:25.154480Z / .154483Z |
| ACH-000932   | −3.116811038474391           | 14               | CRISPRGeneEffect  | DepMap 25Q3  | 1.0              | 0.95       | KRAS (3845)  | 2026-02-23T13:16:25.154487Z / .154490Z |

Interpretation grounded in the evidence:
- The extreme negative gene effect values across the listed cell lines and their top ranks within the KRAS profile emphasize recurrent, strong functional dependencies in vitro. Combined with the global summary (nearly half of lines strongly dependent), this positions KRAS as a high-impact dependency within the DepMap CRISPR landscape.

## 4. Disease Association Evidence

Open Targets (official MCP) reports 15 high-scoring associations for KRAS spanning both rare syndromic and common oncologic diseases. Each record includes tractability predictions that consistently indicate favorable modalities.

Table: Open Targets KRAS–disease associations (official MCP)

| Rank | Disease ID           | Disease Name                                           | Association Score        | Confidence            | Association Count | Approved Name                         | Biotype         | Tractability SM         | Tractability AB         | Tractability PR            |
|------|----------------------|--------------------------------------------------------|--------------------------|-----------------------|-------------------|----------------------------------------|-----------------|-------------------------|-------------------------|----------------------------|
| 1    | MONDO_0012371        | Noonan syndrome 3                                      | 0.8263230926056322       | 0.8978969277816896    | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |
| 2    | MONDO_0014112        | cardiofaciocutaneous syndrome 2                        | 0.8144683031509619       | 0.8943404909452886    | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |
| 3    | MONDO_0018997        | Noonan syndrome                                        | 0.8131264857870096       | 0.8939379457361029    | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |
| 4    | MONDO_0015280        | cardiofaciocutaneous syndrome                          | 0.7954347832222556       | 0.8886304349666767    | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |
| 5    | EFO_0003060          | non-small cell lung carcinoma                           | 0.7788624604700172       | 0.8836587381410052    | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |
| 6    | MONDO_0001056        | gastric cancer                                         | 0.7682404082964024       | 0.8804721224889207    | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |
| 7    | EFO_0000222          | acute myeloid leukemia                                 | 0.7549011490977062       | 0.8764703447293118    | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |
| 8    | MONDO_0010854        | Toriello-Lacassie-Droste syndrome                       | 0.7432990603989575       | 0.8729897181196873    | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |
| 9    | MONDO_0008097        | linear nevus sebaceous syndrome                         | 0.7377607885509033       | 0.871328236565271     | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |
| 10   | Orphanet_2612        | Linear nevus sebaceus syndrome                          | 0.7302675354218321       | 0.8690802606265496    | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |
| 11   | EFO_0000571          | lung adenocarcinoma                                    | 0.7217319743428353       | 0.8665195923028506    | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |
| 12   | MONDO_0013767        | autoimmune lymphoproliferative syndrome type 4         | 0.714506622270334        | 0.8643519866811002    | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |
| 13   | Orphanet_268114      | RAS-associated autoimmune leukoproliferative disease   | 0.7144474894935844       | 0.8643342468480754    | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |
| 14   | MONDO_0001187        | urinary bladder cancer                                 | 0.6993353670095003       | 0.8598006101028501    | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |
| 15   | EFO_1000309          | Juvenile Myelomonocytic Leukemia                       | 0.6928072321318326       | 0.8578421696395498    | 1801              | KRAS proto-oncogene, GTPase            | protein_coding  | High-Quality Ligand     | GO CC high conf         | Small Molecule Binder      |

Interpretation grounded in the evidence:
- The consistently high association scores (0.8263 to 0.6928) and confidence values (0.8979 to 0.8578) across 15 diverse diseases, together with uniform tractability annotations (“SM: High-Quality Ligand,” “PR: Small Molecule Binder,” “AB: GO CC high conf”), delineate a broad, high-confidence disease spectrum for KRAS with multiple feasible therapeutic modalities indicated by platform tractability labels.

## 5. Literature Evidence

Europe PMC search for “KRAS” returned a total_hit_count of 121,780, from which 15 top-cited articles were extracted. These span foundational resources (e.g., databases, cancer genomic atlases), clinical guideline documents, immuno-oncology studies, and disease-specific molecular characterizations.

Key search/meta details
- Provider: Europe PMC
- Endpoint: https://www.ebi.ac.uk/europepmc/webservices/rest/search
- Query: "KRAS"
- Article_count_returned: 15
- Total_hit_count: 121780

Table: Top 15 KRAS-related articles (by citations)

| Rank | PMID     | Title                                                                                                                                    | Pub Year | Cited By Count | Normalized Score |
|------|----------|-------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------|------------------|
| 1    | 22632970 | Ferroptosis: an iron-dependent form of nonapoptotic cell death.                                                                           | 2012     | 12773          | 1.0              |
| 2    | 26771021 | The Molecular Signatures Database (MSigDB) hallmark gene set collection.                                                                  | 2015     | 10475          | 1.0              |
| 3    | 23000897 | Comprehensive molecular portraits of human breast tumours.                                                                                | 2012     | 9406           | 1.0              |
| 4    | 26462967 | 2015 American Thyroid Association Management Guidelines for Adult Patients with Thyroid Nodules and Differentiated Thyroid Cancer: The American Thyroid Association Guidelines Task Force on Thyroid Nodules and Differentiated Thyroid Cancer. | 2016     | 9349           | 1.0              |
| 5    | 26412456 | Nivolumab versus Docetaxel in Advanced Nonsquamous Non-Small-Cell Lung Cancer.                                                           | 2015     | 7174           | 1.0              |
| 6    | 32029601 | The biology<b>,</b> function<b>,</b> and biomedical applications of exosomes.                                                             | 2020     | 7051           | 1.0              |
| 7    | 26028255 | PD-1 Blockade in Tumors with Mismatch-Repair Deficiency.                                                                                  | 2015     | 7009           | 1.0              |
| 8    | 22810696 | Comprehensive molecular characterization of human colon and rectal cancer.                                                                 | 2012     | 6579           | 1.0              |
| 9    | 25765070 | Cancer immunology. Mutational landscape determines sensitivity to PD-1 blockade in non-small cell lung cancer.                            | 2015     | 6211           | 1.0              |
| 10   | 22460905 | The Cancer Cell Line Encyclopedia enables predictive modelling of anticancer drug sensitivity.                                            | 2012     | 6210           | 1.0              |
| 11   | 21720365 | Integrated genomic analyses of ovarian carcinoma.                                                                                          | 2011     | 5978           | 1.0              |
| 12   | 23539594 | Cancer genome landscapes.                                                                                                                  | 2013     | 5565           | 1.0              |
| 13   | 21802130 | A ceRNA hypothesis: the Rosetta Stone of a hidden RNA language?                                                                            | 2011     | 5440           | 0.9500000000000001 |
| 14   | 29362479 | Molecular mechanisms of cell death: recommendations of the Nomenclature Committee on Cell Death 2018.                                      | 2018     | 4723           | 0.9              |
| 15   | 25079317 | Comprehensive molecular characterization of gastric adenocarcinoma.                                                                        | 2014     | 4703           | 0.8500000000000001 |

Interpretation grounded in the evidence:
- The high citation counts and breadth of topics in which KRAS appears reinforce its centrality in multiple domains relevant to oncology and cell biology. While these titles are not exclusively KRAS-focused, their prominence in the KRAS query context signals the extensive research footprint surrounding KRAS and its pathways.

## 6. Integrated Evidence Interpretation

The aggregation of target annotation, functional genomics dependency, disease association, and literature evidence converges on a coherent picture:

- Functional indispensability in vitro: DepMap 25Q3 CRISPR data demonstrate a robust and widespread dependency on KRAS function. The global raw average gene effect of −0.701960413292113 across 1169 lines, paired with 571 strong dependencies (≤ −0.5) and a strong_dependency_fraction of 0.4885, indicates that KRAS knockout reduces viability broadly across many cellular contexts. The highest-confidence cell line entries show extreme depletion magnitudes (as low as −4.282333642061707), underscoring the strength of this dependency phenotype.

- Disease linkage breadth and confidence: Open Targets provides 15 high-ranking associations spanning developmental syndromes (e.g., Noonan syndrome 3; cardiofaciocutaneous syndromes) and cancers (e.g., non-small cell lung carcinoma; gastric cancer; acute myeloid leukemia; lung adenocarcinoma; urinary bladder cancer; Juvenile Myelomonocytic Leukemia), with association scores from 0.8263230926056322 to 0.6928072321318326 and confidence values from 0.8978969277816896 to 0.8578421696395498. This supports a cross-disease role for KRAS involving both inherited syndromic conditions and acquired malignancies.

- Tractability signals: Open Targets tractability annotations consistently indicate “SM: High-Quality Ligand” and “PR: Small Molecule Binder,” with “AB: GO CC high conf” across all listed diseases. Pharos annotates KRAS as TDL = Tclin and reports 223 ligands along with a very low novelty metric (0.00013856). Together, these annotations point to the availability of ligands and to modalities that are considered tractable by platform heuristics.

- Literature landscape: A total_hit_count of 121780 for the “KRAS” query and the presence of highly cited works within the top 15 (e.g., cited-by counts up to 12773) align with a deeply explored target space, supporting translational relevance and broad scientific engagement.

- Cross-source considerations: The Pharos record reports disease_association_count = 0 for KRAS, whereas Open Targets shows extensive disease associations (association_count field of 1801 across records). This discrepancy likely reflects differences in data coverage and curation scope between sources rather than a contradiction in the underlying biology; however, it should be recognized in evidence integration.

Collectively, the data support KRAS as a high-impact, tractable therapeutic target with strong in vitro genetic dependency signals and wide-ranging, high-confidence disease associations.

## 7. Evidence Strength Assessment

Strengths
- Scale and robustness of functional data: The DepMap dataset covers 1169 cell lines with a clear dependency signal (−0.701960413292113 average gene effect; 571 strong dependencies; strong_dependency_fraction 0.4885), supported by a high confidence score (0.9465355004277161). The top cell-line–specific records show consistent metadata and extreme depletion values, all with normalized_score = 1.0 and confidence = 0.95.
- Consistent and high-confidence disease associations: Open Targets reports 15 associations with scores between 0.8263230926056322 and 0.6928072321318326 and confidence values between 0.8978969277816896 and 0.8578421696395498, spanning multiple disease classes, suggesting a robust cross-indication signal.
- Convergent tractability annotations: Open Targets tractability classifications (“SM: High-Quality Ligand,” “PR: Small Molecule Binder,” “AB: GO CC high conf”) are consistent across all 15 diseases. Pharos adds further weight via TDL = Tclin, ligand_total = 223, and novelty = 0.00013856.
- Extensive literature support: The query yielded 121780 total hits, and the top cited articles show very high citation counts (4703–12773), indicating a mature and active research environment around KRAS.

Limitations and caveats
- Cross-source disparities: Pharos reports disease_association_count = 0, whereas Open Targets identifies broad disease associations. These differences should be interpreted as source-specific data coverage and curation differences; cross-validation within the same platform is not provided here.
- Context specificity: DepMap dependencies are reported without explicit linkage to disease-specific contexts in this dataset excerpt (e.g., tissue of origin, mutation status, or co-dependencies are not provided), limiting immediate stratification by indication based solely on these entries.
- Literature specificity: The literature items are top-cited works returned by a “KRAS” query; not all are KRAS-centric mechanistic studies. They nonetheless contribute to the signal of relevance but need contextual reading to parse KRAS-specific conclusions.

Overall strength judgment (evidence-based):
- The convergence of high-throughput functional genomics (with strong quantitative metrics), multi-disease association evidence with high scores and confidence, favorable tractability annotations across modalities, and a large, highly cited literature base yields a strong overall evidence package for KRAS as a therapeutic target.

## 8. Overall Target Assessment

Synthesis across evidence modalities indicates that KRAS represents a compelling therapeutic target characterization:

- Functional indispensability: Near-half of tested cell lines exhibit strong dependency on KRAS (≤ −0.5), with a global average knockout effect of −0.701960413292113. Extreme cell-line dependencies (−4.282333642061707 to −3.116811038474391) reinforce the magnitude of KRAS’s in vitro essentiality in multiple contexts.
- Disease relevance breadth: High-scoring Open Targets associations encompass both developmental syndromes and multiple cancers, with consistent confidence levels and cross-modality tractability labels, reflecting the multi-indication relevance of KRAS.
- Tractability and development signals: Open Targets tractability annotations (“SM: High-Quality Ligand,” “PR: Small Molecule Binder,” “AB: GO CC high conf”) and Pharos’s TDL = Tclin with 223 ligands and low novelty collectively support feasibility for therapeutic modulation, including small-molecule approaches and additional modalities anticipated by the tractability descriptors.
- Knowledge ecosystem maturity: The literature corpus is extensive (121780 total hits for “KRAS”), with numerous highly cited works within the top 15, indicating broad and sustained scientific engagement.

Given these points, the collated evidence supports a high level of confidence in KRAS as a therapeutically actionable and disease-relevant target with diverse modality tractability signals.

## 9. Final Evidence-Based Conclusion

KRAS emerges from this multi-source synthesis as a high-priority therapeutic target characterized by:
- Strong and prevalent in vitro genetic dependencies (DepMap 25Q3 CRISPRGeneEffect: average gene effect −0.701960413292113 over 1169 lines; 571 strong dependencies; strong_dependency_fraction 0.4885; multiple cell lines with extreme negative gene effects and top dependency ranks).
- Broad, high-confidence disease associations (Open Targets official MCP: 15 diseases with association scores 0.8263230926056322 to 0.6928072321318326 and confidence 0.8978969277816896 to 0.8578421696395498) spanning developmental syndromes and cancers, accompanied by consistent tractability indicators (“SM: High-Quality Ligand,” “PR: Small Molecule Binder,” “AB: GO CC high conf”).
- Mature target annotation and ligand landscape (Pharos: TDL = Tclin; ligand_total = 223; novelty = 0.00013856), albeit with a disease_association_count = 0 in this source, highlighting cross-platform coverage differences rather than negating the Open Targets associations.
- A large and highly cited literature context (Europe PMC “KRAS” total_hit_count = 121780; top 15 cited articles range 4703–12773 citations), reinforcing the depth of foundational and translational research involving KRAS.

Taken together, these data strongly support KRAS as a validated and tractable therapeutic target with substantial relevance across multiple diseases. The alignment of robust functional dependency signals, multi-disease associations with high confidence, convergent tractability annotations, and an extensive literature base underpins a favorable overall assessment grounded strictly in the provided evidence.