# Biblioteca Apostolica Vaticana, gr. 2228: Transcription of ff. 194–313

## Description

This repository contains a digital transcription of John Doxapatres's commentary on Hermogenes of Tarsus, *On Invention*, as preserved in the manuscript Vat. gr. 2228.

The transcription was produced from manuscript images through a hybrid approach combining handwritten-text recognition and transcription using Transkribus with subsequent validation by expert researchers.

The transcription covers 239 manuscript pages, corresponding to folios 194–313.

This project is a work in progress. The files may be revised, corrected, and expanded in subsequent versions.

## Source

**Manuscript:** Biblioteca Apostolica Vaticana, Vat. gr. 2228

**Catalogue:** S. Lilla, *Bibliothecae Apostolicae Vaticanae Codices Manuscripti Recensiti. Codices Vaticani graeci. Codices 2162–2254 (Codices Columnenses)*, Vaticano, 1985, pp. 307–313.

Catalogue record:  
https://archive.org/details/01-giovanni-mercati-ed.-codices-vaticani-graeci-1-329/Salvador%20Lilla%20%28ed.%29%20-%20Codices%20Vaticani%20Graeci.%20Codices%202162-2254%20%28Codices%20Columnenses%29/page/n195/mode/2up

**Digital manuscript:**  
https://digi.vatlib.it/view/MSS_Vat.gr.2228.pt.1  
https://digi.vatlib.it/view/MSS_Vat.gr.2228.pt.2

**Transkribus document ID:** 12866292

## Contents

The repository contains the following materials:

* `transcription_with_folia.txt` — plain-text transcription with manuscript folio headings.
* `metadata.csv` — metadata linking Transkribus page numbers, page IDs, folio numbers, image filenames, and XML files.
* `xml/` — Transkribus PAGE XML files containing the transcription and page-level information.
* `convert.py` — Python script used to generate the TXT and CSV files from the PAGE XML.

## Transcription

The transcription was produced using Transkribus and subsequently exported as PAGE XML.

The plain-text transcription was generated from the PAGE XML and organized according to manuscript folio numbers extracted from the image filenames.

Folio headings in the TXT file use the following format:

    ===== fol. 194r =====

## Data format

The XML files use the **PAGE XML** format.

The CSV file provides a tabular overview of the manuscript pages and includes, where available:

* Transkribus page number
* Transkribus page ID
* manuscript folio
* image filename
* XML filename
* document ID
* image dimensions
* transcription status
* number of transcription lines

The XML files should be regarded as the primary exported transcription data. The TXT and CSV files are derived from the XML.

## Notes

The transcription may contain errors introduced during automatic handwritten-text recognition, transcription, or subsequent correction. It should therefore be considered a work in progress.

Further corrections and updated versions may be uploaded to this repository over time.

## Software

Transkribus was used for handwritten-text recognition and transcription.

The accompanying Python script uses only the Python standard library.

## Funding

This project was developed as part of the **Digital Infrastructure project E-Rhetoric** and the **Semper Ardens Accelerate grant “A Rhetoric for the Empire” (2023–2026)** supported by the **Carlsberg Foundation**.

## Citation and Attribution

If you use, reproduce, adapt, or redistribute material from this repository, **appropriate attribution is required** under the terms of the license specified below.

Please cite the project and provide a link to this repository. When possible, please use the following citation:

> Aglae Pizzone, Nicklas Sindlev, Byron MacDougall, and Ugo Valori, *A Transcription of Vat. gr. 2228*, https://github.com/ByzHerm.

For academic publications, presentations, editions, datasets, or other scholarly work, please retain the project attribution and repository reference wherever the transcription, XML, metadata, or material derived from this repository is used.

When citing a specific version of the transcription, it is recommended to include the relevant GitHub release, version, or commit where available.

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**.

Under this license, you may:

* share and redistribute the material in any medium or format;
* adapt, remix, translate, and build upon the material;

provided that:

* the use is **non-commercial**;
* appropriate attribution is given to the project and its contributors;
* a link to this repository is provided;
* the **CC BY-NC 4.0** license is identified; and
* any modifications to the material are clearly indicated.

The full license is available at:

https://creativecommons.org/licenses/by-nc/4.0/

### Attribution notice

When using material from this repository, please provide appropriate credit to the project and its contributors and retain the project citation and repository reference in subsequent scholarly or other public uses of the material.

## License scope

Unless otherwise stated, this license applies to the transcription, metadata, XML-derived data, Python script, and other original materials contained in this repository.

**Third-party materials**, including manuscript images and materials originating from libraries, archives, repositories, or other institutions, may be subject to separate copyright, licensing, or access conditions. This repository does not necessarily grant rights to such third-party materials.

If you are unsure whether a particular material may be reused, please consult the rights information provided by the original holding institution.
