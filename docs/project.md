# Project context and contributions

## Problem

Urinary crystal images may contain several species and multiple instances of each species. Folder names alone cannot describe their contents reliably. The project investigates instance segmentation as a way to locate crystals and assign a species label to each predicted instance.

The input collection combines different lighting conditions, resolutions, magnifications and crystal morphologies. Preparing the data and interpreting its labels are substantial parts of the work.

## Academic context

The original report is titled **Detection of crystals in medical images — Research and Innovation Project**. It names Petar Majić as its author, Gilles Venturini and Barthélémy Serres as supervisors, and CHU Orléans as the hospital partner. The report is dated **February 2026**. The poster carries the academic year **2025–2026**. These document dates are retained without inferring exact project start or end dates.

The project was part of Petar's Erasmus work at Polytech Tours, Université de Tours. The source specification uses the title *Classification of Urinary Crystal Images with Deep Learning Models*. The delivered notebook implements YOLO instance segmentation, so the repository title describes that implementation.

## Contribution and collaboration

Petar's report and code document the review and normalisation of the image collection, metadata extraction, preparation of the YOLO dataset, class filtering, training and evaluation. The report, poster, slides and recorded presentation communicate this work.

The **hospital's medical engineers performed the manual CVAT annotation**, according to Chapter 5 of the report. This repository uses their polygon labels for training and validation. The coding guide and initial dataset review provide domain knowledge from the collaboration. They should not be described as a medical ontology or annotation system independently authored by Petar.

| Work | Evidence |
| --- | --- |
| Review of ambiguous folders, mixtures and acquisition conditions | Report Chapter 3; [domain notes](domain-notes/README.md) |
| Structured metadata extraction | [Script](../scripts/preprocessing/data_preprocessing_image_metadata.py), [mappings](../metadata/README.md), report §3.5 |
| Preparation and filtering of annotation classes | Notebook zero-based cells 6–16 and 29–36 |
| YOLO fine-tuning and validation summaries | Notebook cells 24, 26–27 and 37–38; report Chapter 6 |
| Technical explanation | [Report](reports/project-report.pdf), [poster](reports/project-poster.pdf), [slides and recording](media-guide.md) |

## Scope of the result

This is an experimental research project. The repository documents saved training and validation results. It does not establish diagnostic reliability, external clinical validation or deployment in hospital practice. The intended application is support for expert analysis; the evidence here concerns dataset preparation and model experiments.

## Original sources

- [Project specification](reports/project-specification.pdf): goals and proposed activities. Its proposed tools and methods are not all implemented.
- [Final report](reports/project-report.pdf): 24 PDF pages, including cover and contents. Chapter 5 attributes annotation work; Chapter 6 describes the experiments.
- [Material guide](media-guide.md): explains the role and version of each visual deliverable.
