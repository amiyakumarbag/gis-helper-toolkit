"""
Script: remove_domains.py
Purpose: Remove coded value domains from fields
Author: Amiya Kumar

Usage:
1. Update feature_class path
2. Run script in ArcGIS Pro Python environment
"""
"""
Remove domains from multiple fields in a feature class
Useful when field values do not update due to domains
Author: Amiya Kumar
"""

import arcpy

# Path to feature class
feature_class = r"Path\\to\\your\\featureclass"

# List of fields from which domain will be removed
fields = ["STATUS", "TYPE", "CATEGORY"]

for field in fields:
    try:
        arcpy.management.AssignDomainToField(
            in_table=feature_class,
            field_name=field,
            domain_name=""
        )
        print(f"Domain removed from field: {field}")
    except Exception as e:
        print(f"Failed to remove domain from {field}: {e}")
