from openpyxl import load_workbook

def analyze(filename):
    metadata = {}
    try:
        wb = load_workbook(filename)
        print(wb.properties)
        metadata["author"] = wb.properties.creator
        metadata["category"] = wb.properties.category
        metadata["content_status"] = wb.properties.contentStatus
        metadata["identifier"] = wb.properties.identifier
        metadata["keywords"] = wb.properties.keywords
        metadata["last_modified_by"] = wb.properties.lastModifiedBy
        metadata["language"] = wb.properties.language
        metadata["modified"] = wb.properties.modified
        metadata["subject"] = wb.properties.subject
        metadata["title"] = wb.properties.title
        metadata["version"] = wb.properties.version
    except:
        metadata = {}
    return metadata