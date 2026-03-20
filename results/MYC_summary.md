# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT

## 1. Executive Summary
MYC (MYC proto-oncogene, bHLH transcription factor) is a transcription factor (TF) annotated by Pharos with a Target Development Level (TDL) of Tchem and 95 known ligands, indicating the existence of multiple small-molecule binders and substantial prior chemical biology engagement. The novelty score (5.734e-05) suggests MYC is a highly studied and well-characterized target rather than an emerging entity. Together with Open Targets tractability annotations listing “High-Quality Ligand” for small molecules and “Small Molecule Binder” for protein reagents, these findings place MYC within a tractable chemical space, albeit with the historical challenges common to TF targeting.

Genetic dependency evidence from DepMap (CRISPR Gene Effect, DepMap 25Q3) indicates that MYC exhibits pan-essential characteristics across a large panel of 1,169 cell lines. The average gene effect is -1.976695770106464, and 1,113 of 1,169 lines (strong_dependency_fraction 0.9521) fall at or below the strong-dependency threshold (≤ -0.5). The deepest dependencies observed among the top-ranked cell lines range from -3.947616619618568 to -3.4148100481707404, with all top 14 cell lines ranked for MYC showing markedly negative gene effect values consistent with essential function and strong viability impact upon CRISPR knockout.

Disease association evidence from the Open Targets Platform spans 1,783 associations for MYC, with the highest-scoring relationship to Burkitt’s lymphoma (score=0.6301018613496295). Additional high-scoring associations include urinary bladder carcinoma (0.5555871628006721), neurodegenerative disease (0.5435734368489599), asthma (0.5029912429532041), urinary bladder cancer (0.4957585625804786), and type 2 diabetes mellitus (0.48639843303873204), among others. Across the 15 top-scoring diseases consolidated here, scores range from 0.6301018613496295 to 0.3945725647285015, reflecting broad and diverse disease linkages with an oncologic emphasis and notable representation of immune, metabolic, and neurologic contexts.

The literature corpus retrieved via Europe PMC underscores MYC’s centrality in molecular and cancer biology, reflected by extremely high citation counts in the top-ranked items. The leading article, “Induction of pluripotent stem cells from mouse embryonic and adult fibroblast cultures by defined factors” (PMID: 16904174), has 17,755 citations. Other top articles span foundational resources (ENCODE), key biological paradigms (Warburg effect, apoptosis), and large-scale cancer genomics resources (cBioPortal, TCGA analyses). The total hit count for the query (“MYC”) is 314,948, reinforcing the extensive research footprint around this target and its biological roles.

Integrated across sources, the profile for MYC is characterized by (1) pervasive functional dependency in human cell lines by CRISPR screens, (2) extensive disease associations with highest strength in particular hematologic malignancies and solid tumors but also representation across other disease domains, (3) abundant literature indicative of deep mechanistic and translational exploration, and (4) target annotation supportive of chemical tractability (Tchem; 95 ligands). Collectively, these data converge on MYC as a high-value, high-evidence therapeutic target with broad disease relevance, albeit with the known complexities of modulating a transcription factor in clinical settings.

## 2. Target Annotation Evidence
MYC is annotated in Pharos as “Myc proto-oncogene protein,” classified within the TF (transcription factor) family. The Target Development Level (TDL) is Tchem, and 95 ligands are cataloged, indicating that chemical matter interacting with MYC or relevant binding contexts has been reported. A very low novelty score (5.734e-05) further affirms that MYC is not a novel target but one with extensive historical study and existing ligand knowledge. While the Pharos entry listed no disease association counts, Open Targets tractability metadata complements this by denoting small-molecule tractability (“High-Quality Ligand”) and protein reagent tractability (“Small Molecule Binder”), providing alignment with the Tchem designation and suggesting multiple avenues for pharmacological engagement.

These target annotations, taken together, frame MYC as a well-characterized transcription factor with available chemical tools, supporting feasibility for further development while recognizing that direct TF targeting typically demands nuanced strategies (e.g., disrupting protein–protein interactions or modulating transcriptional complexes). The presence of 95 ligands does not, by itself, establish clinically validated inhibitors but indicates a substantial chemical knowledge base available for optimization or modality diversification.

Target annotation summary table:
| Field                       | Value                                               |
|----------------------------|-----------------------------------------------------|
| Target symbol              | MYC                                                 |
| Target name                | Myc proto-oncogene protein                          |
| Family                     | TF                                                  |
| Target Development Level   | Tchem                                               |
| Ligand total               | 95                                                  |
| Novelty                    | 5.734e-05                                           |
| Disease association count  | 0                                                   |
| Source                     | PHAROS (community MCP)                              |
| Confidence                 | 0.85                                                |
| Normalized score           | 0.95                                                |
| Provenance                 | Community Pharos MCP (Cloudflare Workers)           |

## 3. Genetic Dependency Evidence
### Global Dependency Analysis
DepMap CRISPR Gene Effect data (DepMap 25Q3) for MYC shows strong, pervasive dependency across 1,169 profiled cell lines. The average gene effect is -1.976695770106464, consistent with a pan-essential phenotype. Among these lines, 1,113 meet strong-dependency criteria (≤ -0.5), representing 0.9521 of all lines screened. The global metrics carry high confidence (0.95) and are normalized to 1.0 within the reporting framework. These observations are aligned with the biology of MYC as a central regulator of cell proliferation and metabolism and substantiate MYC’s essentiality across diverse cellular contexts in vitro.

Global MYC dependency metrics (DepMap 25Q3):
| Metric                         | Value                          |
|--------------------------------|--------------------------------|
| Screen type                    | CRISPRGeneEffect               |
| Column name                    | MYC (4609)                     |
| Data release                   | DepMap 25Q3                    |
| Cell line count                | 1169                           |
| Average gene effect            | -1.976695770106464             |
| Strong dependency count        | 1113                           |
| Strong dependency fraction     | 0.9521                         |
| Normalized score               | 1.0                            |
| Confidence                     | 0.95                           |
| Summary                        | “-1.977 avg; 1113/1169 strong” |

### Top Dependent Cell Lines
The strongest MYC dependencies, ranked within gene, show gene effect values ranging from -3.947616619618568 (rank 1) to -3.4148100481707404 (rank 14). All top entries derive from the CRISPRGeneEffect screen (DepMap 25Q3), reflecting pronounced sensitivity to MYC disruption. Although disease lineage annotations are not provided here, the magnitude of gene effect across these top lines supports a broad, deep dependency signature rather than a narrow lineage-specific dependency restricted to a few contexts.

Top MYC-dependent cell lines (CRISPRGeneEffect, DepMap 25Q3):
| Rank | Cell line ID | Gene effect (raw_value)          | Screen type        | Data release  |
|------|---------------|----------------------------------|--------------------|---------------|
| 1    | ACH-002141    | -3.947616619618568               | CRISPRGeneEffect   | DepMap 25Q3   |
| 2    | ACH-000847    | -3.906979188153687               | CRISPRGeneEffect   | DepMap 25Q3   |
| 3    | ACH-002263    | -3.757513423710707               | CRISPRGeneEffect   | DepMap 25Q3   |
| 4    | ACH-000841    | -3.7209032833832576              | CRISPRGeneEffect   | DepMap 25Q3   |
| 5    | ACH-000601    | -3.7028467864655186              | CRISPRGeneEffect   | DepMap 25Q3   |
| 6    | ACH-001494    | -3.7003273669968735              | CRISPRGeneEffect   | DepMap 25Q3   |
| 7    | ACH-000552    | -3.6957412553004874              | CRISPRGeneEffect   | DepMap 25Q3   |
| 8    | ACH-000614    | -3.5678002580202257              | CRISPRGeneEffect   | DepMap 25Q3   |
| 9    | ACH-000651    | -3.5626492924049846              | CRISPRGeneEffect   | DepMap 25Q3   |
| 10   | ACH-000532    | -3.544712496571756               | CRISPRGeneEffect   | DepMap 25Q3   |
| 11   | ACH-000424    | -3.5006484690017277              | CRISPRGeneEffect   | DepMap 25Q3   |
| 12   | ACH-000124    | -3.473646088261795               | CRISPRGeneEffect   | DepMap 25Q3   |
| 13   | ACH-000865    | -3.468130501667723               | CRISPRGeneEffect   | DepMap 25Q3   |
| 14   | ACH-001407    | -3.4148100481707404              | CRISPRGeneEffect   | DepMap 25Q3   |

## 4. Disease Association Evidence
Open Targets evidence links MYC to a wide spectrum of diseases with varying association scores. Among the 1,783 total associations, the top-scoring disease is Burkitt’s lymphoma (score=0.6301018613496295; rank 1/15 in this subset). Other high-scoring oncologic indications include urinary bladder carcinoma (0.5555871628006721), urinary bladder cancer (0.4957585625804786), diffuse large B-cell lymphoma (0.44731503278847806), lymphoma (0.43341526988640233), prostate carcinoma (0.44811515881780484), and pancreatic carcinoma (0.3960294694781224). Notably, substantial associations are also seen with neurodegenerative disease (0.5435734368489599), asthma (0.5029912429532041), type 2 diabetes mellitus (0.48639843303873204), allergic rhinitis (0.45223257553502805), childhood onset asthma (0.44561217501098027), diabetes mellitus (0.4749562461436876), eczematoid dermatitis (0.4255363918150948), and the broader respiratory system disease category (0.3945725647285015). Tractability annotations consistently list “High-Quality Ligand” for small molecules and “Small Molecule Binder” for protein reagents across these entries, aligning with MYC’s Tchem status.

Open Targets disease associations for MYC (top 15 in provided set):
| Rank | Disease ID      | Disease name                         | Association score        | Confidence            | Association count | Tractability (SM)     | Tractability (PR)         |
|------|------------------|--------------------------------------|--------------------------|-----------------------|-------------------|------------------------|---------------------------|
| 1    | EFO_0000309      | Burkitts lymphoma                    | 0.6301018613496295       | 0.8390305584048888    | 1783              | High-Quality Ligand    | Small Molecule Binder     |
| 2    | MONDO_0004986    | urinary bladder carcinoma            | 0.5555871628006721       | 0.8166761488402017    | 1783              | High-Quality Ligand    | Small Molecule Binder     |
| 3    | EFO_0005772      | neurodegenerative disease            | 0.5435734368489599       | 0.813072031054688     | 1783              | High-Quality Ligand    | Small Molecule Binder     |
| 4    | MONDO_0004979    | asthma                               | 0.5029912429532041       | 0.8008973728859613    | 1783              | High-Quality Ligand    | Small Molecule Binder     |
| 5    | MONDO_0001187    | urinary bladder cancer               | 0.4957585625804786       | 0.7987275687741436    | 1783              | High-Quality Ligand    | Small Molecule Binder     |
| 6    | MONDO_0005148    | type 2 diabetes mellitus             | 0.48639843303873204      | 0.7959195299116196    | 1783              | High-Quality Ligand    | Small Molecule Binder     |
| 7    | EFO_0000400      | diabetes mellitus                    | 0.4749562461436876       | 0.7924868738431062    | 1783              | High-Quality Ligand    | Small Molecule Binder     |
| 8    | EFO_0005854      | allergic rhinitis                    | 0.45223257553502805      | 0.7856697726605084    | 1783              | High-Quality Ligand    | Small Molecule Binder     |
| 9    | EFO_0001663      | prostate carcinoma                   | 0.44811515881780484      | 0.7844345476453415    | 1783              | High-Quality Ligand    | Small Molecule Binder     |
| 10   | EFO_0000403      | diffuse large B-cell lymphoma        | 0.44731503278847806      | 0.7841945098365434    | 1783              | High-Quality Ligand    | Small Molecule Binder     |
| 11   | MONDO_0005405    | childhood onset asthma               | 0.44561217501098027      | 0.7836836525032941    | 1783              | High-Quality Ligand    | Small Molecule Binder     |
| 12   | EFO_0000574      | lymphoma                             | 0.43341526988640233      | 0.7800245809659208    | 1783              | High-Quality Ligand    | Small Molecule Binder     |
| 13   | HP_0000964       | Eczematoid dermatitis                | 0.4255363918150948       | 0.7776609175445285    | 1783              | High-Quality Ligand    | Small Molecule Binder     |
| 14   | EFO_0002618      | pancreatic carcinoma                 | 0.3960294694781224       | 0.7688088408434367    | 1783              | High-Quality Ligand    | Small Molecule Binder     |
| 15   | EFO_0000684      | respiratory system disease           | 0.3945725647285015       | 0.7683717694185505    | 1783              | High-Quality Ligand    | Small Molecule Binder     |

## 5. Literature Evidence
The literature evidence returned by Europe PMC for the search term “MYC” illustrates extraordinary breadth and depth. The top 15 ranked items by citation count include seminal studies in cell reprogramming, genome regulation, metabolism, apoptosis, inflammation–cancer linkage, and cancer genomics resources. The highest-cited paper (PMID: 16904174) on induced pluripotency lists MYC among the defined factors, indicating MYC’s centrality in reprogramming biology. Other top-ranked works encompass ENCODE (PMID: 22955616), adult human iPSCs (PMID: 18035408), cBioPortal (PMID: 23550210), RNA-Seq transcript assembly (PMID: 20436464), the Warburg effect (PMID: 19460998), MSigDB Hallmarks (PMID: 26771021), and hallmark cancer genomic maps (e.g., TCGA colon/rectal, ovarian). The total hit count for “MYC” is 314,948, further attesting to the extensive scholarly focus on this gene.

This concentrated body of high-impact literature signals robust mechanistic and translational relevance for MYC across diverse biological systems and diseases. While these articles vary in focus, their prominence and recurrent intersection with MYC underscore the gene’s pervasive influence in cellular control programs and oncogenesis. The citation counts, publication years, and themes collectively support the target’s importance and widespread scientific validation.

Top MYC-related literature (Europe PMC; citations and metadata):
| Rank | PMID      | Title                                                                                              | Pub year | Cited by count | Normalized score | Confidence |
|------|-----------|----------------------------------------------------------------------------------------------------|----------|----------------|------------------|------------|
| 1    | 16904174  | Induction of pluripotent stem cells from mouse embryonic and adult fibroblast cultures by defined factors. | 2006     | 17755          | 1.0              | 0.85       |
| 2    | 22955616  | An integrated encyclopedia of DNA elements in the human genome.                                    | 2012     | 14062          | 1.0              | 0.85       |
| 3    | 18035408  | Induction of pluripotent stem cells from adult human fibroblasts by defined factors.               | 2007     | 13879          | 1.0              | 0.85       |
| 4    | 23550210  | Integrative analysis of complex cancer genomics and clinical profiles using the cBioPortal.        | 2013     | 11732          | 1.0              | 0.85       |
| 5    | 20436464  | Transcript assembly and quantification by RNA-Seq reveals unannotated transcripts and isoform switching during cell differentiation. | 2010     | 11598          | 1.0              | 0.85       |
| 6    | 19460998  | Understanding the Warburg effect: the metabolic requirements of cell proliferation.                | 2009     | 11589          | 1.0              | 0.85       |
| 7    | 26771021  | The Molecular Signatures Database (MSigDB) hallmark gene set collection.                           | 2015     | 10475          | 1.0              | 0.85       |
| 8    | 17562483  | Apoptosis: a review of programmed cell death.                                                      | 2007     | 8723           | 1.0              | 0.85       |
| 9    | 11309499  | Significance analysis of microarrays applied to the ionizing radiation response.                   | 2001     | 8700           | 1.0              | 0.85       |
| 10   | 20303878  | Immunity, inflammation, and cancer.                                                                | 2010     | 7915           | 1.0              | 0.85       |
| 11   | 34185076  | The 2021 WHO Classification of Tumors of the Central Nervous System: a summary.                    | 2021     | 7621           | 1.0              | 0.85       |
| 12   | 25497547  | A 3D map of the human genome at kilobase resolution reveals principles of chromatin looping.       | 2014     | 7453           | 1.0              | 0.85       |
| 13   | 22810696  | Comprehensive molecular characterization of human colon and rectal cancer.                         | 2012     | 6579           | 0.9500000000000001 | 0.85     |
| 14   | 22500797  | mTOR signaling in growth control and disease.                                                      | 2012     | 6545           | 0.9              | 0.85       |
| 15   | 21720365  | Integrated genomic analyses of ovarian carcinoma.                                                  | 2011     | 5978           | 0.8500000000000001 | 0.8      |
Note: Total hit count for the query “MYC” reported by Europe PMC is 314,948; article_count_returned=15.

## 6. Integrated Evidence Interpretation
The collective data supports MYC as a high-priority, extensively validated target with broad biological impact and disease relevance. Pharos annotations (Tchem; 95 ligands; TF family) and Open Targets tractability (small-molecule high-quality ligand and binder designations) converge on the feasibility of pharmacological engagement, though transcription factors often necessitate specialized strategies (e.g., disrupting MYC–MAX interactions or modulating cofactor engagement). The extremely low novelty score highlights MYC as a mature target in terms of literature and prior efforts, which can lower discovery risk in some respects but may also imply competitive and scientific complexity.

DepMap genetic dependency results provide strong functional causality across diverse in vitro contexts. With an average gene effect of -1.976695770106464 across 1,169 lines and 0.9521 of lines exhibiting strong dependency, MYC’s role appears pan-essential, consistent with broad anti-proliferative consequences upon loss of function. The top cell-line dependencies, all below -3.41, demonstrate profound viability defects upon MYC perturbation, indicating a steep dependency gradient and providing a compelling rationale for therapeutic strategies aiming to reduce MYC activity in disease states characterized by MYC-driven biology.

Disease association evidence from Open Targets indicates the highest relative support for hematologic malignancies (e.g., Burkitt’s lymphoma: 0.6301018613496295; diffuse large B-cell lymphoma: 0.44731503278847806; lymphoma: 0.43341526988640233) and significant associations with various solid tumors (e.g., urinary bladder carcinoma/cancer, prostate carcinoma, pancreatic carcinoma). The appearance of non-oncologic associations (e.g., neurodegenerative disease, asthma, type 2 diabetes mellitus) depicts MYC’s wide-ranging biological footprint. While these scores are integrative and not by themselves mechanistic proof, they complement the genetic dependency data by situating MYC within relevant disease frameworks where modulation could produce clinically meaningful effects.

The literature corpus corroborates MYC’s central role across cell fate regulation, genome organization, metabolism, apoptosis, and cancer, as evidenced by extremely high citation counts for seminal publications intersecting with MYC. This scholarly intensity suggests a well-established mechanistic base and abundant resources, datasets, and analytical frameworks to support translational programs. The large total hit count (314,948) indicates that any therapeutic campaign targeting MYC can leverage an unparalleled foundation of prior knowledge and community tools.

Cross-evidence quantitative synopsis:
| Evidence category       | Key metrics / highlights                                                                                 |
|-------------------------|-----------------------------------------------------------------------------------------------------------|
| Target annotation       | TDL=Tchem; ligands=95; family=TF; novelty=5.734e-05; tractability (SM=High-Quality Ligand; PR=Small Molecule Binder) |
| Genetic dependency      | 1,169 lines; avg gene effect=-1.976695770106464; 1,113 strong dependencies; fraction=0.9521; top effects ≤ -3.9476 to -3.4148 |
| Disease associations    | Top score=0.6301018613496295 (Burkitt’s lymphoma); range across top 15: 0.6301–0.3946; association_count=1783 |
| Literature              | Top citations=17,755; total hit count=314,948; top 15 articles include iPSC, ENCODE, Warburg, cBioPortal, TCGA |

## 7. Evidence Strength Assessment
Target annotation strength: Strong. Pharos assigns MYC to Tchem with 95 ligands and an extremely low novelty score (5.734e-05), indicating a deeply characterized target with available chemical matter. Open Targets tractability entries (“High-Quality Ligand” for small molecules; “Small Molecule Binder” for protein reagents) strengthen feasibility signals. Limitation: While ligand presence is confirmed, the annotations do not directly attest to clinical efficacy or safety of MYC-directed agents; transcription factors remain historically difficult to drug directly, necessitating careful modality selection.

Genetic dependency strength: Very strong. The DepMap CRISPRGeneEffect dataset (DepMap 25Q3) shows an average MYC gene effect of -1.976695770106464 over 1,169 cell lines, with 1,113/1,169 (0.9521) meeting strong-dependency criteria (≤ -0.5). The top-ranked dependencies are profoundly negative (down to -3.947616619618568), consistent with essentiality. Confidence (0.95) and normalized score (1.0) are high. Limitation: CRISPR knockout contexts may not fully recapitulate therapeutic modulation (partial inhibition or indirect targeting), and in vitro dependencies may not uniformly translate to in vivo therapeutic windows.

Disease association strength: Moderate to strong (oncology-dominant). Open Targets provides a high top score for Burkitt’s lymphoma (0.6301018613496295) and robust scores for multiple cancers (e.g., urinary bladder carcinoma 0.5555871628006721) and additional diseases (e.g., neurodegenerative disease 0.5435734368489599; asthma 0.5029912429532041). Confidence values span ~0.768–0.839. Limitation: Association scores are integrative and not proof of causality or direct druggability in those indications; indication-specific mechanistic or clinical evidence would be required to prioritize among diverse associated diseases.

Literature strength: Very strong. The top-ranked MYC-related articles show citation counts up to 17,755, and the total hit count is 314,948, reflecting extraordinary research attention. The corpus includes foundational biological and translational works, indicating mature understanding and extensive toolkits. Limitation: Literature prominence does not equate to clinical success; it highlights interest and mechanistic relevance rather than validated therapeutic outcomes.

Evidence strength summary:
| Category            | Strength rating     | Key quantitative support                                            | Primary limitations                                                         |
|---------------------|---------------------|----------------------------------------------------------------------|------------------------------------------------------------------------------|
| Target annotation   | Strong              | TDL=Tchem; ligands=95; novelty=5.734e-05; tractability=High-Quality Ligand | TF druggability challenges; ligand presence ≠ clinical validation            |
| Genetic dependency  | Very strong         | 1,169 lines; avg=-1.9767; 1,113/1,169 strong (0.9521); top ≤ -3.9476 | CRISPR knockout ≠ pharmacologic modulation; in vitro to in vivo translation |
| Disease association | Moderate–Strong     | Top score=0.6301; 15-disease range=0.6301–0.3946; conf. up to 0.8390 | Association ≠ causation; indication triage requires added mechanistic data   |
| Literature          | Very strong         | Top citations=17,755; total hits=314,948                             | Scholarly intensity ≠ therapeutic success                                   |

## 8. Overall Target Assessment
The integrated evidence definitively positions MYC as a high-value therapeutic target with broad disease relevance, particularly in oncology. Target annotation and tractability metadata indicate that MYC has substantial existing chemical engagement (Tchem, 95 ligands) and is recognized as having high-quality small-molecule ligand potential, supporting the feasibility of continued medicinal chemistry or alternative modality development. The genetic dependency dataset demonstrates pan-essential characteristics, with striking average and extreme gene effect values across a large cell line compendium, reinforcing MYC’s central role in cellular viability and proliferation.

Disease association mappings cohere with the dependency landscape by highlighting strong connections to lymphoid malignancies and multiple solid tumors, while also pointing to broader biological implications in immune, metabolic, and neurologic domains. The extensive literature signal confirms that MYC sits at the nexus of key molecular processes—reprogramming, transcriptional control, chromatin architecture, metabolism, and apoptosis—providing a deep knowledge reservoir for hypothesis generation and translational design.

Collectively, the evidence argues for MYC as an attractive strategic hub for therapeutic innovation, with multiple potential routes to intervention. The principal strategic consideration lies in the modality of targeting, given MYC’s transcription factor nature. Feasible strategies may emphasize indirect modulation (e.g., cofactor interaction, stability, transcriptional complex interference) or advanced modalities consistent with the tractability signals (e.g., small molecules with high-quality ligand properties or protein-directed binders), while carefully evaluating therapeutic index and on-target liabilities implied by pan-essentiality.

## 9. Final Evidence-Based Conclusion
Across target annotation, genetic dependency, disease association, and literature domains, MYC exhibits a convergent, high-strength evidence profile consistent with a compelling therapeutic target. Chemical tractability indicators (Tchem; 95 ligands; high-quality ligand tags) and profound CRISPR-based essentiality across 1,169 cell lines (average gene effect -1.976695770106464; strong dependency fraction 0.9521) jointly support the feasibility and potential impact of MYC-directed therapeutic strategies. Disease associations are strongest in hematologic malignancies (e.g., Burkitt’s lymphoma) and extend across multiple solid tumors and non-oncologic conditions, aligning with MYC’s broad biological scope.

The literature corpus, with top citations up to 17,755 and a total hit count of 314,948, underscores the deep mechanistic foundation and translational relevance of MYC. While targeting a transcription factor entails modality-specific challenges and careful attention to therapeutic index, the assembled evidence substantiates MYC as a prioritized, high-evidence target where targeted modulation could yield substantial therapeutic benefit, especially in oncology indications reflected by the highest Open Targets association scores.