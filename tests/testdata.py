"""Expected test results for the testdata.* documents.
"""

DOCX_CONTENT_TYPES = {
    "rels": "application/vnd.openxmlformats-package.relationships+xml",
    "xml": "application/xml",
    "/word/document.xml": "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml",
    "/word/styles.xml": "application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml",
    "/word/settings.xml": "application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml",
    "/word/webSettings.xml": "application/vnd.openxmlformats-officedocument.wordprocessingml.webSettings+xml",
    "/word/fontTable.xml": "application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml",
    "/word/theme/theme1.xml": "application/vnd.openxmlformats-officedocument.theme+xml",
    "/docProps/core.xml": "application/vnd.openxmlformats-package.core-properties+xml",
    "/docProps/app.xml": "application/vnd.openxmlformats-officedocument.extended-properties+xml",
    "/docProps/custom.xml": "application/vnd.openxmlformats-officedocument.custom-properties+xml",
}

DOCX_PARTS = [
    "[Content_Types].xml",
    "_rels/.rels",
    "docProps/app.xml",
    "docProps/core.xml",
    "docProps/custom.xml",
    "word/_rels/document.xml.rels",
    "word/document.xml",
    "word/fontTable.xml",
    "word/settings.xml",
    "word/styles.xml",
    "word/theme/theme1.xml",
    "word/webSettings.xml",
]

DOCX_RELATIONSHIPS = {
    "rId3": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties",
    "rId2": "http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties",
    "rId1": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument",
    "rId4": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/custom-properties",
}

PPTX_CONTENT_TYPES = {
    "jpeg": "image/jpeg",
    "rels": "application/vnd.openxmlformats-package.relationships+xml",
    "xml": "application/xml",
    "/ppt/presentation.xml": "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml",
    "/ppt/slideMasters/slideMaster1.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml",
    "/ppt/slides/slide1.xml": "application/vnd.openxmlformats-officedocument.presentationml.slide+xml",
    "/ppt/presProps.xml": "application/vnd.openxmlformats-officedocument.presentationml.presProps+xml",
    "/ppt/viewProps.xml": "application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml",
    "/ppt/theme/theme1.xml": "application/vnd.openxmlformats-officedocument.theme+xml",
    "/ppt/tableStyles.xml": "application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml",
    "/ppt/slideLayouts/slideLayout1.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
    "/ppt/slideLayouts/slideLayout2.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
    "/ppt/slideLayouts/slideLayout3.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
    "/ppt/slideLayouts/slideLayout4.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
    "/ppt/slideLayouts/slideLayout5.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
    "/ppt/slideLayouts/slideLayout6.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
    "/ppt/slideLayouts/slideLayout7.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
    "/ppt/slideLayouts/slideLayout8.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
    "/ppt/slideLayouts/slideLayout9.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
    "/ppt/slideLayouts/slideLayout10.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
    "/ppt/slideLayouts/slideLayout11.xml": "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
    "/docProps/core.xml": "application/vnd.openxmlformats-package.core-properties+xml",
    "/docProps/app.xml": "application/vnd.openxmlformats-officedocument.extended-properties+xml",
    "/docProps/custom.xml": "application/vnd.openxmlformats-officedocument.custom-properties+xml",
}

PPTX_PARTS = [
    "[Content_Types].xml",
    "_rels/.rels",
    "docProps/app.xml",
    "docProps/core.xml",
    "docProps/custom.xml",
    "docProps/thumbnail.jpeg",
    "ppt/_rels/presentation.xml.rels",
    "ppt/presProps.xml",
    "ppt/presentation.xml",
    "ppt/slideLayouts/_rels/slideLayout1.xml.rels",
    "ppt/slideLayouts/_rels/slideLayout10.xml.rels",
    "ppt/slideLayouts/_rels/slideLayout11.xml.rels",
    "ppt/slideLayouts/_rels/slideLayout2.xml.rels",
    "ppt/slideLayouts/_rels/slideLayout3.xml.rels",
    "ppt/slideLayouts/_rels/slideLayout4.xml.rels",
    "ppt/slideLayouts/_rels/slideLayout5.xml.rels",
    "ppt/slideLayouts/_rels/slideLayout6.xml.rels",
    "ppt/slideLayouts/_rels/slideLayout7.xml.rels",
    "ppt/slideLayouts/_rels/slideLayout8.xml.rels",
    "ppt/slideLayouts/_rels/slideLayout9.xml.rels",
    "ppt/slideLayouts/slideLayout1.xml",
    "ppt/slideLayouts/slideLayout10.xml",
    "ppt/slideLayouts/slideLayout11.xml",
    "ppt/slideLayouts/slideLayout2.xml",
    "ppt/slideLayouts/slideLayout3.xml",
    "ppt/slideLayouts/slideLayout4.xml",
    "ppt/slideLayouts/slideLayout5.xml",
    "ppt/slideLayouts/slideLayout6.xml",
    "ppt/slideLayouts/slideLayout7.xml",
    "ppt/slideLayouts/slideLayout8.xml",
    "ppt/slideLayouts/slideLayout9.xml",
    "ppt/slideMasters/_rels/slideMaster1.xml.rels",
    "ppt/slideMasters/slideMaster1.xml",
    "ppt/slides/_rels/slide1.xml.rels",
    "ppt/slides/slide1.xml",
    "ppt/tableStyles.xml",
    "ppt/theme/theme1.xml",
    "ppt/viewProps.xml",
]

PPTX_RELATIONSHIPS = {
    "rId3": "http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties",
    "rId2": "http://schemas.openxmlformats.org/package/2006/relationships/metadata/thumbnail",
    "rId1": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument",
    "rId5": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/custom-properties",
    "rId4": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties",
}

XLSX_CONTENT_TYPES = {
    "rels": "application/vnd.openxmlformats-package.relationships+xml",
    "xml": "application/xml",
    "/xl/workbook.xml": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml",
    "/xl/worksheets/sheet1.xml": "application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml",
    "/xl/theme/theme1.xml": "application/vnd.openxmlformats-officedocument.theme+xml",
    "/xl/styles.xml": "application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml",
    "/xl/sharedStrings.xml": "application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml",
    "/docProps/core.xml": "application/vnd.openxmlformats-package.core-properties+xml",
    "/docProps/app.xml": "application/vnd.openxmlformats-officedocument.extended-properties+xml",
    "/docProps/custom.xml": "application/vnd.openxmlformats-officedocument.custom-properties+xml",
}

XLSX_PARTS = [
    "[Content_Types].xml",
    "_rels/.rels",
    "docProps/app.xml",
    "docProps/core.xml",
    "docProps/custom.xml",
    "xl/_rels/workbook.xml.rels",
    "xl/sharedStrings.xml",
    "xl/styles.xml",
    "xl/theme/theme1.xml",
    "xl/workbook.xml",
    "xl/worksheets/sheet1.xml",
]

XLSX_RELATIONSHIPS = {
    "rId3": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties",
    "rId2": "http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties",
    "rId1": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument",
    "rId4": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/custom-properties",
}
