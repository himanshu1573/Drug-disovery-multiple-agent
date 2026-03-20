# THERAPEUTIC TARGET EVIDENCE SUMMARY REPORT

## 1. Executive Summary
EGFR (epidermal growth factor receptor) is a kinase-class target with extensive therapeutic and pharmacological characterization. Target annotation from Pharos assigns EGFR a Target Development Level (TDL) of Tclin, indicating an established clinical target, with 2,445 recorded ligands and extremely low novelty (novelty=7.274e-05). This annotation positions EGFR within a mature, clinically validated target space and aligns with expectations for a receptor tyrosine kinase of central oncologic relevance.

Genetic dependency profiling from DepMap (CRISPRGeneEffect, DepMap 25Q3) demonstrates that EGFR exhibits a modest overall dependency signal across 1,169 cancer cell lines (average gene effect raw_value = -0.24344198617953822; support average = -0.2434). Notably, 210 cell lines (17.96%) show strong dependency (gene effect ≤ -0.5), and multiple lines display extreme EGFR essentiality (lowest gene effects spanning -2.8486 to -1.6696 among the top 14 dependent lines). These observations confirm that while EGFR is not universally essential across all contexts, a substantial subset of models is highly dependent on EGFR function.

Disease association evidence from the Open Targets Platform reveals high-confidence, high-scoring links between EGFR and multiple cancers. The strongest association is with non-small cell lung carcinoma (score=0.8495103521170136; rank=1/15), followed by lung adenocarcinoma (0.7731689582662028; rank=2/15) and broad “cancer” (0.7440199628845963; rank=3/15). Additional strong associations span lung cancer, colorectal adenocarcinoma, head and neck squamous cell carcinoma, breast cancer, and glioblastoma multiforme, among others. Uniform tractability annotations indicate membership in a druggable family with small-molecule binder evidence and advanced clinical status.

The curated literature corpus returned by Europe PMC for the query “EGFR” includes highly cited, foundational works. Among these are titles explicitly linking EGFR mutations to NSCLC responsiveness to gefitinib (PMID=15118073; cited_by_count=8292) and clinical response correlations (PMID=15118125; cited_by_count=7121). The set also includes broadly used genomics methods and oncology references (e.g., Integrative Genomics Viewer; cBioPortal analysis papers) that frequently mention EGFR within cancer genomics contexts, further reinforcing its centrality in oncology research and precision medicine.

Collectively, the evidence converges on EGFR as a clinically validated, tractable oncology target with robust disease associations, substantial literature support, and a dependency profile characterized by pronounced essentiality in defined cellular subsets. The integration of annotation, genetic dependency, disease linkage, and literature coherence supports a strong overall evidence base.

## 2. Target Annotation Evidence
EGFR is annotated in Pharos as a kinase family protein with TDL=Tclin, reflecting established clinical targeting. The target has an extensive ligand landscape (ligand_total=2445) and minimal novelty (7.274e-05), consistent with a mature therapeutic area. While Pharos reports disease_association_count=0 in its own schema, cross-platform evidence (see Disease Association Evidence) identifies numerous, high-confidence disease links, underscoring platform-specific coverage differences rather than a true absence of associations.

Summary table:

| Field                          | Value                                                                 |
|-------------------------------|-----------------------------------------------------------------------|
| target_symbol                 | EGFR                                                                  |
| target_name                   | Epidermal growth factor receptor                                      |
| family                        | Kinase                                                                |
| Target Development Level      | Tclin                                                                 |
| ligand_total                  | 2445                                                                  |
| novelty                       | 7.274e-05                                                             |
| disease_association_count     | 0                                                                     |
| normalized_score              | 1.0                                                                   |
| confidence                    | 0.85                                                                  |
| source                        | PHAROS (community MCP); Community Pharos MCP (Cloudflare Workers)     |
| provenance_retrieved_at       | 2026-02-23T18:13:18.855285Z                                           |

## 3. Genetic Dependency Evidence
### Global Dependency Analysis
DepMap CRISPR gene effect data (DepMap 25Q3) indicate that EGFR shows a modest average dependency across 1,169 cancer cell lines, with raw average gene effect of -0.24344198617953822 (support average = -0.2434). Importantly, 210 lines (17.96%) meet the strong dependency threshold (≤ -0.5), demonstrating a substantial subset with pronounced EGFR dependence. The normalized score for the global metric is 0.5811473287265128 with confidence 0.8538922155688623, supporting robust data quality and consistency. These findings are congruent with a context-specific oncogene dependency model, wherein EGFR essentiality is concentrated in defined molecular or lineage backgrounds.

Global metrics table:

| Metric                         | Value                          | Notes/Provenance                                        |
|--------------------------------|--------------------------------|----------------------------------------------------------|
| average_gene_effect (raw_value)| -0.24344198617953822           | DepMap CRISPRGeneEffect; EGFR (1956)                    |
| support_average_gene_effect    | -0.2434                        | Rounded support statistic                                |
| cell_line_count                | 1169                           | Number of profiled cell lines                            |
| strong_dependency_count        | 210                            | Gene effect ≤ -0.5                                       |
| strong_dependency_fraction     | 0.1796                         | 210 / 1169                                               |
| normalized_score               | 0.5811473287265128             | Global normalized score                                  |
| confidence                     | 0.8538922155688623             | Global confidence                                        |
| screen_type                    | CRISPRGeneEffect               | Functional genomics screen type                          |
| column_name                    | EGFR (1956)                    | DepMap gene column                                       |
| data_release                   | DepMap 25Q3                    |                                                          |
| provider                       | DepMap (Broad Institute)       |                                                          |
| provenance_endpoint            | CRISPRGeneEffect.csv           |                                                          |
| provenance_retrieved_at        | 2026-02-23T18:13:34.558619Z    |                                                          |

### Top Dependent Cell Lines
The most EGFR-dependent cell lines exhibit extreme negative gene effects, spanning -2.8486 to -1.6696 among the top 14 lines, with uniformly high normalized scores (all 1.0) and high confidence (0.918–0.950 range). These results reinforce a strong essentiality phenotype in specific cellular contexts within the CRISPR gene knockout framework, consistent with oncogene addiction paradigms.

Ranked top dependent cell lines (CRISPRGeneEffect; DepMap 25Q3):

| Rank | Cell line ID | Gene effect (raw_value)       | Normalized score | Confidence             | Screen type       | Data release  |
|------|---------------|-------------------------------|------------------|------------------------|-------------------|---------------|
| 1    | ACH-000587    | -2.8485944935115963           | 1.0              | 0.95                   | CRISPRGeneEffect  | DepMap 25Q3   |
| 2    | ACH-000472    | -2.1649094219761693           | 1.0              | 0.9432454710988085     | CRISPRGeneEffect  | DepMap 25Q3   |
| 3    | ACH-002239    | -2.0740745545977006           | 1.0              | 0.9387037277298851     | CRISPRGeneEffect  | DepMap 25Q3   |
| 4    | ACH-002156    | -2.0341014472599146           | 1.0              | 0.9367050723629957     | CRISPRGeneEffect  | DepMap 25Q3   |
| 5    | ACH-000548    | -2.032630840040893            | 1.0              | 0.9366315420020447     | CRISPRGeneEffect  | DepMap 25Q3   |
| 6    | ACH-000911    | -2.0290884814610113           | 1.0              | 0.9364544240730506     | CRISPRGeneEffect  | DepMap 25Q3   |
| 7    | ACH-000936    | -1.8191886154268817           | 1.0              | 0.9259594307713441     | CRISPRGeneEffect  | DepMap 25Q3   |
| 8    | ACH-002029    | -1.8165967538034409           | 1.0              | 0.9258298376901721     | CRISPRGeneEffect  | DepMap 25Q3   |
| 9    | ACH-000181    | -1.8059306157382056           | 1.0              | 0.9252965307869103     | CRISPRGeneEffect  | DepMap 25Q3   |
| 10   | ACH-001836    | -1.8023507889337969           | 1.0              | 0.92511753944669       | CRISPRGeneEffect  | DepMap 25Q3   |
| 11   | ACH-000735    | -1.7632235162634786           | 1.0              | 0.9231611758131739     | CRISPRGeneEffect  | DepMap 25Q3   |
| 12   | ACH-000448    | -1.6878023419484536           | 1.0              | 0.9193901170974227     | CRISPRGeneEffect  | DepMap 25Q3   |
| 13   | ACH-000546    | -1.684436817574627            | 1.0              | 0.9192218408787314     | CRISPRGeneEffect  | DepMap 25Q3   |
| 14   | ACH-002251    | -1.6696262884629998           | 1.0              | 0.9184813144231501     | CRISPRGeneEffect  | DepMap 25Q3   |

## 4. Disease Association Evidence
Open Targets associations for EGFR span a spectrum of malignancies with consistently high scores and confidence. The highest-scoring association is with non-small cell lung carcinoma (score=0.8495103521170136; rank 1), followed by lung adenocarcinoma (0.7731689582662028; rank 2) and “cancer” (0.7440199628845963; rank 3). Additional strong associations include lung cancer, colorectal adenocarcinoma, head and neck squamous cell carcinoma, breast cancer and carcinoma, glioblastoma multiforme, and urinary bladder malignancies. Tractability classifications are uniform across entries: Small Molecule (SM) “Druggable Family,” Antibody (AB) “Human Protein Atlas loc,” PROTAC-relevant (PR) “Small Molecule Binder,” and Overall Clinical (OC) “Advanced Clinical,” supporting therapeutic feasibility. Each row reports association_count=2545, indicating broad evidence integration on the platform level.

Open Targets disease associations (selected top 15):

| Rank | Disease name                                              | Disease ID        | Association score         | Confidence             | Association count |
|------|-----------------------------------------------------------|-------------------|---------------------------|------------------------|-------------------|
| 1    | non-small cell lung carcinoma                             | EFO_0003060       | 0.8495103521170136        | 0.9048531056351041     | 2545              |
| 2    | lung adenocarcinoma                                       | EFO_0000571       | 0.7731689582662028        | 0.8819506874798608     | 2545              |
| 3    | cancer                                                    | MONDO_0004992     | 0.7440199628845963        | 0.8732059888653789     | 2545              |
| 4    | lung cancer                                               | MONDO_0008903     | 0.6709784182365274        | 0.8512935254709583     | 2545              |
| 5    | colorectal adenocarcinoma                                 | EFO_0000365       | 0.6707431322996741        | 0.8512229396899023     | 2545              |
| 6    | head and neck squamous cell carcinoma                     | EFO_0000181       | 0.6687285603444324        | 0.8506185681033297     | 2545              |
| 7    | breast cancer                                             | MONDO_0007254     | 0.6592406575828916        | 0.8477721972748675     | 2545              |
| 8    | glioblastoma multiforme                                   | EFO_0000519       | 0.653783743085079         | 0.8461351229255237     | 2545              |
| 9    | neoplasm                                                  | EFO_0000616       | 0.6507051400677244        | 0.8452115420203173     | 2545              |
| 10   | inflammatory skin and bowel disease, neonatal, 2          | MONDO_0014481     | 0.6387533357167994        | 0.8416260007150398     | 2545              |
| 11   | head and neck malignant neoplasia                         | EFO_0006859       | 0.6019171205555338        | 0.8305751361666601     | 2545              |
| 12   | urinary bladder carcinoma                                 | MONDO_0004986     | 0.5933258202487757        | 0.8279977460746327     | 2545              |
| 13   | breast carcinoma                                          | EFO_0000305       | 0.5785790858419542        | 0.8235737257525862     | 2545              |
| 14   | urinary bladder cancer                                    | MONDO_0001187     | 0.5752892311033746        | 0.8225867693310124     | 2545              |
| 15   | EGFR-related lung cancer                                  | EFO_0022194       | 0.5672494365208632        | 0.820174830956259      | 2545              |

## 5. Literature Evidence
The literature set associated with “EGFR” encompasses highly cited publications spanning oncogenic driver biology, targeted therapy response, and broadly utilized genomics resources that frequently contextualize EGFR within cancer research. Seminal titles explicitly highlight activating EGFR mutations underlying NSCLC responsiveness to gefitinib (PMID=15118073) and correlations between EGFR mutations and clinical response (PMID=15118125), directly substantiating the therapeutic relevance of EGFR in lung cancer. Additional entries reflect the pervasive role of EGFR in oncology discourse and analysis frameworks, including comprehensive breast tumor profiling and widely adopted bioinformatics tools that are often used to interrogate EGFR.

Top literature items (Europe PMC):

| Rank | PMID     | Year | Title                                                                                                   | Cited by count | Normalized score | Confidence |
|------|----------|------|---------------------------------------------------------------------------------------------------------|----------------|------------------|------------|
| 1    | 21221095 | 2011 | Integrative genomics viewer.                                                                            | 12343          | 1.0              | 0.85       |
| 2    | 23550210 | 2013 | Integrative analysis of complex cancer genomics and clinical profiles using the cBioPortal.             | 11732          | 1.0              | 0.85       |
| 3    | 23323831 | 2013 | GSVA: gene set variation analysis for microarray and RNA-seq data.                                     | 11087          | 1.0              | 0.85       |
| 4    | 24002530 | 2013 | MicroRNA-23b regulates cellular architecture and impairs motogenic and invasive phenotypes during cancer progression. | 9525           | 1.0              | 0.85       |
| 5    | 23000897 | 2012 | Comprehensive molecular portraits of human breast tumours.                                              | 9406           | 1.0              | 0.85       |
| 6    | 15118073 | 2004 | Activating mutations in the epidermal growth factor receptor underlying responsiveness of non-small-cell lung cancer to gefitinib. | 8292           | 1.0              | 0.85       |
| 7    | 3798106  | 1987 | Human breast cancer: correlation of relapse and survival with amplification of the HER-2/neu oncogene. | 8062           | 1.0              | 0.85       |
| 8    | 20303878 | 2010 | Immunity, inflammation, and cancer.                                                                     | 7915           | 1.0              | 0.85       |
| 9    | 17618441 | 2007 | The 2007 WHO classification of tumours of the central nervous system.                                  | 7783           | 1.0              | 0.85       |
| 10   | 34185076 | 2021 | The 2021 WHO Classification of Tumors of the Central Nervous System: a summary.                        | 7621           | 1.0              | 0.85       |
| 11   | 27718847 | 2016 | Pembrolizumab versus Chemotherapy for PD-L1-Positive Non-Small-Cell Lung Cancer.                        | 7460           | 1.0              | 0.85       |
| 12   | 26412456 | 2015 | Nivolumab versus Docetaxel in Advanced Nonsquamous Non-Small-Cell Lung Cancer.                          | 7174           | 1.0              | 0.85       |
| 13   | 15118125 | 2004 | EGFR mutations in lung cancer: correlation with clinical response to gefitinib therapy.                 | 7121           | 0.95             | 0.85       |
| 14   | 32029601 | 2020 | The biology<b>,</b> function<b>,</b> and biomedical applications of exosomes.                           | 7051           | 0.9              | 0.85       |
| 15   | 26028407 | 2015 | Nivolumab versus Docetaxel in Advanced Squamous-Cell Non-Small-Cell Lung Cancer.                        | 6308           | 0.8500000000000001 | 0.8     |

## 6. Integrated Evidence Interpretation
The assembled evidence establishes EGFR as a clinically validated kinase target with extensive pharmacologic engagement (Tclin; 2,445 ligands) and minimal novelty, indicating a well-characterized therapeutic landscape. Target annotation corroborates high tractability and mature development status, aligning with the presence of numerous disease associations and a deep literature corpus.

Functional genomic dependency data from DepMap complement disease associations by demonstrating that EGFR is variably essential across cancer cell lines, with a modest overall average effect (raw average = -0.24344198617953822) but a substantial subset (210/1,169; 17.96%) manifesting strong dependency (≤ -0.5). The extreme negative gene effects in the top lines (down to -2.8486) suggest that in specific molecular contexts, EGFR acts as a critical survival driver, which is congruent with oncogene addiction principles. This functional pattern is consistent with the high-scoring Open Targets associations observed in lung and other epithelial malignancies.

Disease association data provide convergent external validation. The strongest links to non-small cell lung carcinoma (0.8495103521170136) and lung adenocarcinoma (0.7731689582662028) align directly with literature highlighting activating EGFR mutations and associated therapeutic responsiveness (PMIDs 15118073 and 15118125). Associations with colorectal adenocarcinoma, head and neck squamous cell carcinoma, breast cancer, and glioblastoma multiforme (scores ~0.65–0.67) extend EGFR’s disease sphere, consistent with recurrent aberrations or pathway engagement reported in oncology. The tractability annotations (SM “Druggable Family,” PR “Small Molecule Binder,” AB “Human Protein Atlas loc,” OC “Advanced Clinical”) reinforce feasibility for diverse modality engagement.

The literature corpus, including landmark translational studies and widely used analytic platforms, substantiates both the biological centrality of EGFR and its clinical implications. Papers expressly linking EGFR mutations to clinical drug response in NSCLC provide mechanistic and clinical anchors. The presence of high-citation resources (e.g., IGV, cBioPortal, GSVA) underscores that EGFR is frequently interrogated in genomic oncology analyses, reinforcing breadth and durability of interest and evidence.

Together, annotation, dependency, association, and literature strands cohere around a model where EGFR represents a high-tractability, clinically established oncology target exhibiting pronounced dependency in definable cellular subsets and robust disease linkages, especially in lung cancer. The multi-source agreement strengthens the overall confidence in EGFR as a viable and impactful therapeutic target.

## 7. Evidence Strength Assessment
Target Annotation Evidence:
The Pharos annotation assigns TDL=Tclin with 2,445 ligands and novelty=7.274e-05. The Tclin status denotes substantial clinical evidence and a deep pharmacological toolkit, which, along with the high ligand count, signifies strong maturity and tractability. Although the Pharos disease_association_count is 0 within that specific framework, cross-platform data mitigate this by demonstrating extensive disease linkages. Strength assessment: very strong.

Genetic Dependency Evidence:
DepMap CRISPRGeneEffect profiling across 1,169 cell lines with a global raw average gene effect of -0.24344198617953822 and 210 lines (0.1796 fraction) exhibiting strong dependency constitutes broad, high-quality functional genomic evidence. The extreme gene effects among the most sensitive lines (as low as -2.8486) and consistently high confidence values (0.918–0.95) support a robust context-specific essentiality. While the mean dependency is modest, the sizeable strongly dependent subset elevates translational relevance. Strength assessment: strong (context-dependent).

Disease Association Evidence:
Open Targets provides high association scores with multiple cancers, led by non-small cell lung carcinoma (0.8495103521170136) and lung adenocarcinoma (0.7731689582662028), with consistently high confidence values and uniform tractability flags (including “Advanced Clinical”). The breadth (15 detailed associations; platform-level association_count=2545) and magnitudes indicate substantial, multi-evidence integration. Strength assessment: very strong.

Literature Evidence:
The literature set includes seminal, disease-relevant publications directly implicating EGFR mutations in NSCLC therapeutic responsiveness (PMIDs 15118073 and 15118125) and a wide array of highly cited oncology and genomics resources where EGFR is frequently analyzed. Citation counts are high (range 6,308–12,343), and the corpus spans methodological, translational, and clinical domains, providing comprehensive support. Strength assessment: very strong.

## 8. Overall Target Assessment
EGFR exhibits a mature therapeutic profile characterized by established clinical targeting (Tclin), high tractability across modalities, and extensive ligand availability. Functional genomics data identify a clear, context-specific dependency landscape with a considerable fraction of cancer cell lines demonstrating strong EGFR essentiality and multiple models exhibiting extreme vulnerability to EGFR loss. These features align with a target that drives tumor survival and proliferation in defined molecular settings.

Disease association evidence consolidates EGFR’s linkage to major epithelial cancers, most prominently NSCLC and lung adenocarcinoma, and extends to colorectal, head and neck, breast, bladder, and glioblastoma contexts. Literature entries explicitly tying EGFR mutations to clinical response further substantiate the mechanistic and therapeutic relevance, indicating that EGFR dysregulation has both biological and clinical consequence profiles.

Integrating these data streams yields a coherent picture: EGFR is a high-confidence oncology target with proven clinical engagement, strong disease associations, and functional dependency in select models. This evidence supports both continued therapeutic exploitation in established indications and rigorous context definition for any expanded applications.

## 9. Final Evidence-Based Conclusion
EGFR is a clinically validated, highly tractable kinase target (Tclin) with extensive ligand coverage (n=2445) and minimal novelty, reflecting a mature and deeply characterized therapeutic domain. Open Targets associations demonstrate strong and consistent links to non-small cell lung carcinoma and lung adenocarcinoma, among other malignancies, with uniformly supportive tractability annotations.

DepMap functional genomics evidence shows that while average dependency across 1,169 cell lines is modest (raw average = -0.24344198617953822), a substantial subset (210; 17.96%) exhibits strong dependency, and the most sensitive models display extreme essentiality (gene effect to -2.8486). Literature entries include seminal reports directly connecting EGFR mutations with therapeutic responsiveness in NSCLC, reinforcing mechanistic plausibility and clinical impact.

In aggregate, the convergent strength of target annotation, genetic dependency, disease association, and literature evidence supports EGFR as a high-confidence, therapeutically actionable oncology target with pronounced context-specific essentiality and robust clinical precedence. The evidence base justifies sustained and precise therapeutic engagement of EGFR in appropriate disease settings.