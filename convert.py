import xml.etree.ElementTree as ET
import csv
import re
from pathlib import Path

# ------------------------------------------------------------
# SETTINGS
# ------------------------------------------------------------

# Folder containing your Transkribus XML files
INPUT_FOLDER = Path("xml")

# Files that will be created
TXT_OUTPUT = Path("transcription_with_folia.txt")
CSV_OUTPUT = Path("metadata.csv")

# ------------------------------------------------------------
# PAGE XML NAMESPACE
# ------------------------------------------------------------

NAMESPACE = {
    "page": "http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15"
}

# ------------------------------------------------------------
# FIND XML FILES
# ------------------------------------------------------------

xml_files = sorted(INPUT_FOLDER.glob("*.xml"))

if not xml_files:
    print("No XML files found.")
    print("Make sure the XML files are in the same folder as this script.")
    raise SystemExit

print(f"Found {len(xml_files)} XML files.")

# ------------------------------------------------------------
# STORAGE
# ------------------------------------------------------------

all_pages = []

# ------------------------------------------------------------
# PROCESS EACH XML FILE
# ------------------------------------------------------------

for xml_file in xml_files:

    print(f"Processing: {xml_file.name}")

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

    except Exception as e:
        print(f"ERROR reading {xml_file.name}: {e}")
        continue

    # --------------------------------------------------------
    # PAGE INFORMATION
    # --------------------------------------------------------

    page = root.find("page:Page", NAMESPACE)

    if page is None:
        print(f"  WARNING: No <Page> element found.")
        continue

    image_filename = page.get("imageFilename", "")
    image_width = page.get("imageWidth", "")
    image_height = page.get("imageHeight", "")

    # --------------------------------------------------------
    # TRANSKRIBUS METADATA
    # --------------------------------------------------------

    transkribus_metadata = root.find(
        ".//page:TranskribusMetadata",
        NAMESPACE
    )

    doc_id = ""
    page_id = ""
    page_number = ""
    status = ""

    if transkribus_metadata is not None:
        doc_id = transkribus_metadata.get("docId", "")
        page_id = transkribus_metadata.get("pageId", "")
        page_number = transkribus_metadata.get("pageNr", "")
        status = transkribus_metadata.get("status", "")

    # --------------------------------------------------------
    # EXTRACT FOLIO FROM IMAGE FILENAME
    # --------------------------------------------------------
    #
    # Example:
    # 0001_Vat.gr.2228.pt.1_0393_fa_0194r.tif
    #
    # The regular expression finds:
    # 0194r
    #
    # and returns:
    # 194r
    # --------------------------------------------------------

    folio = ""

    match = re.search(r"_(\d+)([rv])\.(?:tif|tiff|jpg|jpeg|png)$",
                      image_filename,
                      re.IGNORECASE)

    if match:
        folio_number = int(match.group(1))
        side = match.group(2).lower()
        folio = f"{folio_number}{side}"

    else:
        print(
            f"  WARNING: Could not determine folio "
            f"from filename: {image_filename}"
        )

    # --------------------------------------------------------
    # EXTRACT ALL UNICODE TEXT
    # --------------------------------------------------------
    #
    # Because the Page XML contains the text in reading order,
    # finding all Unicode elements gives us the transcription
    # line by line.
    # --------------------------------------------------------

    unicode_elements = root.findall(
        ".//page:TextEquiv/page:Unicode",
        NAMESPACE
    )

    lines = []

    for element in unicode_elements:
        if element.text:
            lines.append(element.text.strip())

    text = "\n".join(lines)

    # --------------------------------------------------------
    # STORE PAGE
    # --------------------------------------------------------

    all_pages.append({
        "xml_file": xml_file.name,
        "doc_id": doc_id,
        "page_id": page_id,
        "page_number": page_number,
        "folio": folio,
        "image_filename": image_filename,
        "image_width": image_width,
        "image_height": image_height,
        "status": status,
        "text": text,
        "number_of_lines": len(lines)
    })

# ------------------------------------------------------------
# SORT PAGES
# ------------------------------------------------------------
#
# Transkribus pageNr is used where available.
# This prevents alphabetical filename ordering from causing
# problems (e.g. page 10 appearing before page 2).
# ------------------------------------------------------------

def page_sort_key(page):

    try:
        return int(page["page_number"])
    except (ValueError, TypeError):
        return 999999


all_pages.sort(key=page_sort_key)

# ------------------------------------------------------------
# CREATE TXT
# ------------------------------------------------------------

with open(TXT_OUTPUT, "w", encoding="utf-8") as f:

    for i, page in enumerate(all_pages):

        folio = page["folio"]
        text = page["text"]

        # Folio heading
        if folio:
            f.write(f"===== fol. {folio} =====\n\n")
        else:
            f.write(
                f"===== Transkribus page "
                f"{page['page_number']} =====\n\n"
            )

        # Greek transcription
        f.write(text)

        # Blank lines between folia
        f.write("\n\n")

print()
print(f"Created: {TXT_OUTPUT}")

# ------------------------------------------------------------
# CREATE CSV
# ------------------------------------------------------------

csv_fields = [
    "transkribus_page",
    "page_id",
    "folio",
    "image_filename",
    "xml_file",
    "doc_id",
    "image_width",
    "image_height",
    "status",
    "number_of_lines"
]

with open(
    CSV_OUTPUT,
    "w",
    encoding="utf-8-sig",
    newline=""
) as f:

    writer = csv.DictWriter(
        f,
        fieldnames=csv_fields
    )

    writer.writeheader()

    for page in all_pages:

        writer.writerow({
            "transkribus_page": page["page_number"],
            "page_id": page["page_id"],
            "folio": page["folio"],
            "image_filename": page["image_filename"],
            "xml_file": page["xml_file"],
            "doc_id": page["doc_id"],
            "image_width": page["image_width"],
            "image_height": page["image_height"],
            "status": page["status"],
            "number_of_lines": page["number_of_lines"]
        })

print(f"Created: {CSV_OUTPUT}")

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

print()
print("Finished!")
print(f"Pages processed: {len(all_pages)}")
print(f"TXT file: {TXT_OUTPUT}")
print(f"CSV file: {CSV_OUTPUT}")