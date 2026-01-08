"""
Script: bulk_null_cleaner.py
Purpose: Replace NULL values in multiple fields
Author: Amiya Kumar

Usage:
1. Update feature_class path
2. Update fields_default dictionary
3. Run in ArcGIS Pro Python environment
"""

import arcpy

feature_class = r"Path\to\your\featureclass"

fields_default = {
    "STATUS": "UNKNOWN",
    "TYPE": "NA",
    "DEPTH": 0
}

with arcpy.da.UpdateCursor(feature_class, fields_default.keys()) as cursor:
    for row in cursor:
        updated = False
        for i, field in enumerate(fields_default):
            if row[i] in (None, "", " "):
                row[i] = fields_default[field]
                updated = True
        if updated:
            cursor.updateRow(row)

print("NULL value cleanup completed")
