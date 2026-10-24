# Cleaning Steps and Rationale

| Issue | Action | Reason |
|---|---|---|
| Exact duplicate row | Remove duplicate | Avoid double-counting |
| Extra spaces and inconsistent capitalization | Trim spaces; title-case names/cities; lowercase emails | Improve consistency |
| Numeric values stored inconsistently | Convert Age and Purchase_Amount to numeric | Enable calculations |
| Missing Age | Fill with median age | Simple demonstration strategy |
| Missing City | Use `Unknown` | Avoid inventing a value |
| Missing Email | Use `Not Provided` | Clearly flag unavailable information |
| Missing purchase amount | Fill with median amount | Keeps sample numeric |
| Mixed/invalid dates | Normalize to YYYY-MM-DD; invalid -> `Unknown` | Consistent date format |
| Final validation | Count remaining missing cells | Verify output quality |

The original file is preserved. Zero purchase amount is retained because it may be valid. Confirm all rules with the data owner when working with real datasets.
