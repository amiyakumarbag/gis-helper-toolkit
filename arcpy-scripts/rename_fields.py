"""
Rename multiple fields in a feature class
Useful for data cleaning and schema standardization
Author: Amiya Kumar
"""

import arcpy

feature_class = r"Path\\to\\your\\featureclass"

fields_to_rename = {
    "ADDRESS_1": "ADDRESS1",
    "ADDRESS_2": "ADDRESS2",
    "ADDRESS_3": "ADDRESS3"
}

for old_name, new_name in fields_to_rename.items():
    try:
        arcpy.management.AlterField(feature_class, old_name, new_name)
        print(f"{old_name} renamed to {new_name}")
    except Exception as e:
        print(f"Failed to rename {old_name}: {e}")
