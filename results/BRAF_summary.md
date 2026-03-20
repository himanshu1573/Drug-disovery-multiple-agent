# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT

## 1. Executive Summary
This report consolidates multi-source evidence on BRAF, integrating target annotation, functional genetic dependency data, disease associations, and peer‑reviewed literature. Across sources, BRAF consistently emerges as a clinically validated kinase target with extensive small‑molecule tractability, a defined pattern of CRISPR-based genetic dependency in a substantial subset of cell lines, strong and high-confidence disease associations spanning multiple oncologic and syndromic indications, and exceptionally deep and highly cited literature coverage.

From DepMap CRISPR gene effect data (DepMap 25Q3), the average BRAF dependency across 1169 cell lines is modest (raw_value −0.1739226449597499; support average_gene_effect −0.1739), yet 96 cell lines (8.21%) show strong dependency (≤ −0.5). The dependency tail includes very strong effects in top-ranked lines (e.g., gene effect −2.673487063135547 in ACH‑000614; −2.517898513217056 in ACH‑000441), highlighting context-selective essentiality.

Target annotation (Pharos) classifies BRAF as Tclin (clinically validated) within the Kinase family, with 2031 ligands cataloged and a low novelty value (0.00253795), signaling extensive prior pharmacology and development. Open Targets association scores are high across diverse diseases—ranked top-scoring associations include cardiofaciocutaneous syndrome (score 0.8773194129589376), Noonan syndrome (0.8452460780163003), melanoma (0.8081262884383028), and several malignancies (e.g., lung and colorectal cancers), with a reported total of 1559 associations. Literature evidence encompasses 15 highly cited publications (total_hit_count 94193; article_count_returned 15) that reflect seminal contributions in cancer genomics, tumor classification, immune checkpoint therapy contexts, and BRAF-focused therapeutic studies; citation counts in this set reach up to 11732.

Collectively, these data support BRAF as a mature, druggable target with strong translational relevance. The genetic dependency profile indicates robust vulnerabilities in defined cellular contexts, while disease association breadth and literature strength reinforce a compelling therapeutic rationale.

## 2. Target Annotation Evidence
Pharos provides a high-confidence annotation situating BRAF as a clinically validated kinase with extensive ligand engagement and low novelty, consistent with a well‑studied therapeutic target profile.

- Source: Community Pharos MCP (Cloudflare Workers)
- Target name: Serine/threonine-protein kinase B-raf
- Family: Kinase
- Target Development Level (TDL): Tclin
- Ligand total: 2031
- Novelty: 0.00253795
- Disease association count (source field): 0
- Top diseases (source field): []
- Description: not provided

Table: Pharos target annotation key metrics
| Field                       | Value                         |
|----------------------------|-------------------------------|
| Target symbol              | BRAF                          |
| Target name                | Serine/threonine-protein kinase B-raf |
| Family                     | Kinase                        |
| TDL                        | Tclin                         |
| Ligand_total               | 2031                          |
| Novelty                    | 0.00253795                    |
| Disease_association_count  | 0                             |
| Source                     | Community Pharos MCP          |
| Confidence                 | 0.85                          |
| Normalized score           | 1.0                           |

Interpretation (annotation): The Tclin classification and 2031 ligands underscore extensive prior clinical and medicinal chemistry work on BRAF. The low novelty value (0.00253795) is concordant with a mature target with substantial existing knowledge and tools. While this specific Pharos record lists disease_association_count=0 and no top diseases, comprehensive disease linkage is established independently in Open Targets (see Section 4), indicating source-specific differences in how disease links are enumerated.

## 3. Genetic Dependency Evidence

### Global Dependency Analysis
DepMap CRISPRGeneEffect data (DepMap 25Q3) quantify BRAF dependency across 1169 cell lines. The overall average dependency (negative values denote reduced viability upon knockout) is modestly negative, with a subset showing pronounced sensitivity.

Table: DepMap global CRISPR gene effect metrics for BRAF
| Metric                         | Value                              |
|--------------------------------|------------------------------------|
| Screen type                    | CRISPRGeneEffect                   |
| Data release                   | DepMap 25Q3                        |
| Column name                    | BRAF (673)                         |
| Cell lines tested (n)          | 1169                               |
| Raw value (global avg effect)  | −0.1739226449597499                |
| Support average_gene_effect    | −0.1739                            |
| Strong dependency count        | 96                                 |
| Strong dependency fraction     | 0.0821                             |
| Normalized score               | 0.5579742149865833                 |
| Confidence                     | 0.8246364414029085                 |
| Summary                        | DepMap CRISPR gene effect for BRAF: −0.174 avg across 1169 cell lines (96 show strong dependency ≤ −0.5). |

Interpretation (global): The aggregate profile indicates BRAF is not universally essential but exhibits significant context-specific essentiality: 96/1169 (8.21%) cell lines show strong dependency (≤ −0.5). The presence of a negative mean effect suggests a mild general tendency toward reduced fitness upon BRAF loss, with a distinct tail of high dependency.

### Top Dependent Cell Lines
The most BRAF-dependent cell lines demonstrate very strong gene effects (up to around −2.67), reflecting substantial viability impact upon gene perturbation in specific contexts.

Table: Top BRAF‑dependent cell lines (CRISPRGeneEffect, DepMap 25Q3)
| Rank within gene | Cell line ID | Gene effect (raw_value) | Normalized score | Confidence            | Screen type       | Data release  |
|------------------|--------------|-------------------------|------------------|-----------------------|-------------------|---------------|
| 1                | ACH-000614   | −2.673487063135547      | 1.0              | 0.95                  | CRISPRGeneEffect  | DepMap 25Q3   |
| 2                | ACH-000441   | −2.517898513217056      | 1.0              | 0.95                  | CRISPRGeneEffect  | DepMap 25Q3   |
| 3                | ACH-000477   | −2.5054048163945386     | 1.0              | 0.95                  | CRISPRGeneEffect  | DepMap 25Q3   |
| 4                | ACH-000425   | −2.421266026298504      | 1.0              | 0.95                  | CRISPRGeneEffect  | DepMap 25Q3   |
| 5                | ACH-000765   | −2.094475284925373      | 1.0              | 0.9397237642462687    | CRISPRGeneEffect  | DepMap 25Q3   |
| 6                | ACH-001838   | −2.0769148822225425     | 1.0              | 0.9388457441111272    | CRISPRGeneEffect  | DepMap 25Q3   |
| 7                | ACH-000014   | −1.9399667946770416     | 1.0              | 0.9319983397338522    | CRISPRGeneEffect  | DepMap 25Q3   |
| 8                | ACH-001982   | −1.9379336216222511     | 1.0              | 0.9318966810811126    | CRISPRGeneEffect  | DepMap 25Q3   |
| 9                | ACH-001239   | −1.903525110913149      | 1.0              | 0.9301762555456575    | CRISPRGeneEffect  | DepMap 25Q3   |
| 10               | ACH-000676   | −1.886802695649923      | 1.0              | 0.9293401347824962    | CRISPRGeneEffect  | DepMap 25Q3   |
| 11               | ACH-001522   | −1.8647236153132356     | 1.0              | 0.9282361807656618    | CRISPRGeneEffect  | DepMap 25Q3   |
| 12               | ACH-001975   | −1.8639472859250303     | 1.0              | 0.9281973642962515    | CRISPRGeneEffect  | DepMap 25Q3   |
| 13               | ACH-000827   | −1.828654655528953      | 1.0              | 0.9264327327764477    | CRISPRGeneEffect  | DepMap 25Q3   |
| 14               | ACH-001970   | −1.819094173801336      | 1.0              | 0.9259547086900668    | CRISPRGeneEffect  | DepMap 25Q3   |

Interpretation (cell-line specificity): The magnitude of the top dependencies (from −1.819 to −2.673) highlights a set of cellular models in which BRAF function is acutely required for fitness. The uniform normalized scores (1.0) and high confidence values further support the robustness of these individual dependency calls. These findings, combined with the global summary, indicate that therapeutic strategies aimed at BRAF are most compelling in biologically defined subsets rather than pan-lineage universal contexts.

## 4. Disease Association Evidence
Open Targets provides 15 high-confidence disease associations for BRAF, each with an association score and tractability annotations. All entries share an association_count of 1559 for the target across the platform and report that BRAF is a “Druggable Family,” has “Human Protein Atlas loc” tractability for antibodies (AB), and is a “Small Molecule Binder” (PR).

Table: Open Targets disease associations for BRAF
| Rank | Disease name                                   | Disease ID       | Score                | Confidence           | Tractability (SM / AB / PR)                 |
|------|------------------------------------------------|------------------|----------------------|----------------------|---------------------------------------------|
| 1    | cardiofaciocutaneous syndrome                  | MONDO_0015280    | 0.8773194129589376   | 0.9131958238876813   | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |
| 2    | Noonan syndrome                                | MONDO_0018997    | 0.8452460780163003   | 0.9035738234048901   | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |
| 3    | melanoma                                       | EFO_0000756      | 0.8081262884383028   | 0.8924378865314909   | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |
| 4    | Noonan syndrome with multiple lentigines       | MONDO_0007893    | 0.802590459554312    | 0.8907771378662935   | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |
| 5    | cancer                                         | MONDO_0004992    | 0.7333219588280876   | 0.8699965876484262   | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |
| 6    | non-small cell lung carcinoma                  | EFO_0003060      | 0.7125104704482613   | 0.8637531411344784   | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |
| 7    | lung adenocarcinoma                            | EFO_0000571      | 0.7058629996164565   | 0.8617588998849369   | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |
| 8    | lung cancer                                    | MONDO_0008903    | 0.7038967449066093   | 0.8611690234719828   | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |
| 9    | colorectal cancer                              | MONDO_0005575    | 0.6915373756372566   | 0.857461212691177    | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |
| 10   | cardiofaciocutaneous syndrome 1                | MONDO_0007265    | 0.6716960338870795   | 0.8515088101661239   | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |
| 11   | LEOPARD syndrome 3                             | MONDO_0013380    | 0.6716960338870795   | 0.8515088101661239   | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |
| 12   | Noonan syndrome 7                              | MONDO_0013379    | 0.6695134896512528   | 0.8508540468953759   | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |
| 13   | neoplasm                                       | EFO_0000616      | 0.6674851233275804   | 0.8502455369982741   | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |
| 14   | lymphoma                                       | EFO_0000574      | 0.648787584929222    | 0.8446362754787666   | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |
| 15   | colorectal adenocarcinoma                      | EFO_0000365      | 0.6251472559382876   | 0.8375441767814863   | Druggable Family / Human Protein Atlas loc / Small Molecule Binder |

Notes:
- Target approved_name: B-Raf proto-oncogene, serine/threonine kinase (shared across entries).
- Biotype: protein_coding (shared across entries).
- Association_count: 1559 (shared across entries).
- Source: Official Open Targets Platform MCP.

Interpretation (disease links): The high and tightly clustered association scores and confidences across specific tumors (e.g., melanoma, lung and colorectal cancers, lymphoma) and named syndromes (e.g., cardiofaciocutaneous syndrome, Noonan spectrum, LEOPARD syndrome) indicate broad and strong disease relevance for BRAF. Tractability flags consistently support small‑molecule binding potential and broader druggability attributes.

## 5. Literature Evidence
The literature corpus returned by Europe PMC for “BRAF” (article_count_returned 15; total_hit_count 94193) comprises landmark studies and guidance spanning cancer genomics, therapeutic targeting, and clinical management, with very high citation counts, indicative of deep and broad scientific and clinical engagement with BRAF.

Table: Top literature items referencing BRAF
| Rank | PMID      | Title                                                                                                                                                                      | Pub year | Cited by count | Normalized score | Confidence |
|------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|----------------|------------------|------------|
| 1    | 23550210  | Integrative analysis of complex cancer genomics and clinical profiles using the cBioPortal.                                                                                | 2013     | 11732          | 1.0              | 0.85       |
| 2    | 22658127  | Safety, activity, and immune correlates of anti-PD-1 antibody in cancer.                                                                                                   | 2012     | 9544           | 1.0              | 0.85       |
| 3    | 23000897  | Comprehensive molecular portraits of human breast tumours.                                                                                                                 | 2012     | 9406           | 1.0              | 0.85       |
| 4    | 26462967  | 2015 American Thyroid Association Management Guidelines for Adult Patients with Thyroid Nodules and Differentiated Thyroid Cancer: The American Thyroid Association Guidelines Task Force on Thyroid Nodules and Differentiated Thyroid Cancer. | 2016     | 9349           | 1.0              | 0.85       |
| 5    | 34185076  | The 2021 WHO Classification of Tumors of the Central Nervous System: a summary.                                                                                           | 2021     | 7621           | 1.0              | 0.85       |
| 6    | 12068308  | Mutations of the BRAF gene in human cancer.                                                                                                                                | 2002     | 7425           | 1.0              | 0.85       |
| 7    | 26028255  | PD-1 Blockade in Tumors with Mismatch-Repair Deficiency.                                                                                                                   | 2015     | 7009           | 1.0              | 0.85       |
| 8    | 22810696  | Comprehensive molecular characterization of human colon and rectal cancer.                                                                                                  | 2012     | 6579           | 1.0              | 0.85       |
| 9    | 22460905  | The Cancer Cell Line Encyclopedia enables predictive modelling of anticancer drug sensitivity.                                                                              | 2012     | 6210           | 1.0              | 0.85       |
| 10   | 22658128  | Safety and activity of anti-PD-L1 antibody in patients with advanced cancer.                                                                                               | 2012     | 6003           | 1.0              | 0.85       |
| 11   | 21720365  | Integrated genomic analyses of ovarian carcinoma.                                                                                                                           | 2011     | 5978           | 1.0              | 0.85       |
| 12   | 18772890  | Comprehensive genomic characterization defines human glioblastoma genes and core pathways.                                                                                  | 2008     | 5888           | 1.0              | 0.85       |
| 13   | 26027431  | Combined Nivolumab and Ipilimumab or Monotherapy in Untreated Melanoma.                                                                                                     | 2015     | 5717           | 0.95             | 0.85       |
| 14   | 23539594  | Cancer genome landscapes.                                                                                                                                                   | 2013     | 5565           | 0.9              | 0.85       |
| 15   | 21639808  | Improved survival with vemurafenib in melanoma with BRAF V600E mutation.                                                                                                   | 2011     | 5543           | 0.85             | 0.8        |

Notes:
- Query used: "BRAF".
- The set includes foundational and practice‑informing studies relevant to BRAF biology and therapeutic contexts.

Interpretation (literature): The magnitude of citation counts (up to 11732) across diverse, high-impact articles supports the centrality of BRAF within oncology and related clinical research. The presence of titles directly referencing BRAF mutations and BRAF‑targeted therapy alongside large-scale cancer genomics resources indicates both mechanistic and translational depth.

## 6. Integrated Evidence Interpretation
The compiled evidence forms a coherent picture of BRAF as a mature, high‑value therapeutic target:

- Druggability and clinical maturity: Pharos designates BRAF as Tclin within the Kinase family with 2031 ligands and a low novelty score (0.00253795), evidencing extensive prior pharmacology and clinical development. Open Targets tractability flags further reinforce small‑molecule binding capacity and general druggability.

- Functional dependency pattern: DepMap CRISPR data reveal a bimodal profile—while the mean gene effect across 1169 cell lines is only modestly negative (raw_value −0.1739226449597499; support average −0.1739), a noteworthy subset (96 cell lines; 0.0821 fraction) exhibits strong dependency (≤ −0.5). The top-ranked dependencies reach severe levels (down to −2.673487063135547), indicating pronounced fitness consequences when BRAF is perturbed in particular cellular contexts. This selective essentiality aligns with therapeutic strategies focused on biomarker-defined subsets rather than broad, undifferentiated populations.

- Disease relevance breadth and depth: Open Targets associations are high across both malignant and named syndromic conditions. Notably, melanoma (score 0.8081262884383028), lung malignancies (e.g., non-small cell lung carcinoma, lung adenocarcinoma, lung cancer; scores 0.7125104704482613, 0.7058629996164565, 0.7038967449066093), and colorectal malignancies (colorectal cancer 0.6915373756372566; colorectal adenocarcinoma 0.6251472559382876) are among the top entries. Syndromic associations include cardiofaciocutaneous syndrome (0.8773194129589376; also cardiofaciocutaneous syndrome 1 at 0.6716960338870795), Noonan syndrome (0.8452460780163003; Noonan syndrome with multiple lentigines 0.802590459554312; Noonan syndrome 7 at 0.6695134896512528), and LEOPARD syndrome 3 (0.6716960338870795). These high scores and confidences (ranging from 0.8375441767814863 to 0.9131958238876813) strongly implicate BRAF across diverse disease categories.

- Literature corroboration: The literature set includes highly cited studies that anchor BRAF within cancer genomics, tumor taxonomy, and therapeutic efficacy contexts (e.g., “Mutations of the BRAF gene in human cancer,” “Improved survival with vemurafenib in melanoma with BRAF V600E mutation”), as well as large-scale resources (e.g., cBioPortal, TCGA analyses, CCLE). The breadth (total_hit_count 94193) and depth (cited_by_count up to 11732) indicate robust scientific consensus and substantial translational momentum around BRAF.

Cross-evidence concordance: The target’s clinical maturity (Tclin), small‑molecule tractability, and extensive ligand landscape are congruent with the disease association profiles and the documented, context-strong genetic dependencies. Collectively, the data support both established therapeutic relevance and ongoing opportunities to optimize context-specific targeting strategies.

## 7. Evidence Strength Assessment
- Target annotation strength: High. The Pharos classification (TDL=Tclin) with 2031 ligands and low novelty (0.00253795) substantiates extensive prior validation. Confidence is 0.85 with a normalized score of 1.0 from the Pharos MCP. Although disease_association_count is 0 in this record, this appears to reflect source-specific reporting; disease links are comprehensively captured by Open Targets.

- Genetic dependency strength: Moderate to strong. The DepMap CRISPR dataset is large (n=1169 cell lines) with contemporary release (DepMap 25Q3) and good overall confidence (0.8246364414029085). The modest average effect (−0.1739226449597499) indicates limited universal essentiality, but the strong-dependency subset (96 cell lines; fraction 0.0821) and extreme gene effects (as low as −2.673487063135547) provide compelling functional support in defined contexts. Top cell-line entries carry high confidence (up to 0.95), reinforcing reliability.

- Disease association strength: High. The top 15 associations carry strong scores (0.6251472559382876 to 0.8773194129589376) with high confidences (0.8375441767814863 to 0.9131958238876813). The consistent tractability annotations (SM: Druggable Family; AB: Human Protein Atlas loc; PR: Small Molecule Binder) further support therapeutic feasibility. The shared association_count of 1559 for BRAF across the platform underscores the breadth of disease linkage.

- Literature strength: Very high. The returned set includes hallmark studies with citation counts ranging from 5543 to 11732 and spans key domains (genomics, classification, immuno-oncology contexts, and BRAF-targeted therapy). Normalized scores are high (0.85–1.0) with confidences up to 0.85 (and 0.8 in one entry), supporting both depth and diversity of evidence.

- Overall coherence and recency: Genetic dependency data are from DepMap 25Q3. Open Targets and Pharos are designated MCP sources. The alignment of clinical maturity, tractability, disease associations, and functional dependency patterns strengthens the overall evidence base.

Limitations and nuances (evidence-derived):
- Dependency heterogeneity: The average CRISPR gene effect is modest, and only 8.21% of lines show strong dependency, indicating that BRAF dependency is context‑specific rather than universal across cell lines.
- Source-specific reporting differences: The Pharos disease_association_count=0 contrasts with Open Targets’ extensive disease association data (association_count 1559), highlighting differences in data capture and presentation across sources.

## 8. Overall Target Assessment
BRAF demonstrates a strong therapeutic target profile characterized by:
- Clinical maturity and tractability: Tclin status, Kinase family membership, and 2031 ligands indicate a well-developed pharmacological landscape and established feasibility for small‑molecule (and potentially other modality) interventions, consistent with Open Targets’ tractability annotations.
- Context-selective functional essentiality: DepMap CRISPR data identify a clear subset of highly dependent models (96/1169; strong dependency ≤ −0.5), with the top dependencies reaching severe levels (e.g., −2.673487063135547). This suggests that precise patient or tumor stratification may be key to maximizing therapeutic impact.
- Broad, high-confidence disease relevance: High association scores across melanoma, lung and colorectal cancers, lymphoma, and multiple named syndromes support a wide range of potential indications. The uniformly strong tractability annotations across these diseases underpin feasibility of therapeutic engagement.
- Extensive and influential literature foundation: Highly cited works encompassing BRAF mutations, clinical outcomes with BRAF-directed approaches (as captured in titles), and integrative cancer genomics provide a robust scientific framework for ongoing and future translational applications.

Risk–benefit considerations (evidence-based):
- Benefit potential is highest in contexts that mirror the strong dependency cell-line subset and top disease associations with high scores and confidences.
- Given the modest average dependency across all lines, broad, unselected applications may yield diluted benefit; evidence favors biomarker- or context-guided strategies.

In sum, the convergence of clinical maturity, tractability, selective but strong functional dependency, extensive disease linkage, and deep literature support positions BRAF as a high-priority therapeutic target with clear translational pathways in defined settings.

## 9. Final Evidence-Based Conclusion
BRAF is a clinically validated kinase target (TDL=Tclin) with an extensive ligand repertoire (2031 ligands) and low novelty (0.00253795), denoting substantial prior development. Functional genomics from DepMap (CRISPRGeneEffect, DepMap 25Q3) show a modest overall dependency (raw_value −0.1739226449597499; support average −0.1739) across 1169 cell lines but identify a meaningful subset of strong dependencies (96 cell lines; fraction 0.0821), with top effects reaching −2.673487063135547. Open Targets reports high-confidence associations across 15 diseases (scores up to 0.8773194129589376; confidences up to 0.9131958238876813) spanning melanoma, lung and colorectal cancers, lymphoma, and multiple named syndromes, supported by consistent tractability annotations (SM: Druggable Family; AB: Human Protein Atlas loc; PR: Small Molecule Binder) and a broad association_count of 1559. The literature corpus is extensive and highly cited (cited_by_count up to 11732; total_hit_count 94193), encompassing seminal studies on BRAF biology and therapeutic contexts.

Together, these data substantiate BRAF as a high-value, druggable therapeutic target with strong disease relevance and context‑dependent functional essentiality, best leveraged through strategies that prioritize biologically defined settings where dependency is pronounced.