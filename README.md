# Auth0 JSON Utilities

This repository contains two Python scripts designed to process JSON data for use with Auth0. These scripts are particularly useful for fixing and preparing JSON files generated by the Auth0 Import/Export extension, making them suitable for import into a different Auth0 tenant.

## Scripts Overview

### 1. `convert_flat_to_nested.py`

#### Description:
This script converts a flat JSON structure with dot-separated keys into a nested JSON object. It's especially useful when you need to restructure JSON data to match specific requirements, such as those needed for SAML assertions or other hierarchical data formats.

#### How It Works:
- Reads a JSON file containing flat objects with dot-separated keys.
- Converts each flat object into a nested structure by splitting the keys at the dots and creating the appropriate nested dictionaries.
- Outputs the nested objects into a new JSON file.

#### Usage:
```bash
python3 convert_flat_to_nested.py
```
- Ensure that `input.json` is present in the same directory. The output will be written to `output.json`.

### 2. `split_json_file.py`

#### Description:
This script splits a large JSON file into smaller files, each with a maximum size of 500 KB. This is particularly helpful when dealing with large datasets that need to be imported into systems with file size limitations, such as Auth0.

#### How It Works:
- Reads the entire JSON file into memory.
- Iterates through the JSON objects, accumulating them into a batch until the batch size reaches the specified limit (500 KB by default).
- Writes each batch to a separate file.

#### Usage:
```bash
python3 split_json_file.py
```
- Ensure that `input.json` is present in the same directory. The output files will be named `input_part1.json`, `input_part2.json`, etc.

## Use Case

These scripts are designed to assist in manipulating files generated by the Auth0 Import/Export extension. They address common issues when preparing these files for import into a different Auth0 tenant, such as converting flat JSON structures to nested ones and splitting large files into smaller, manageable sizes.

## Repository Structure

```
/auth0
├── convert_flat_to_nested.py  # Script to convert flat JSON to nested JSON
├── split_json_file.py         # Script to split large JSON files into smaller chunks
└── README.md                  # This file
```

## Prerequisites

- Python 3.x
- `jq` (if you are running the `jq` command for preprocessing)

## How to Clone and Use

1. Clone the repository:
   ```bash
   git clone https://github.com/anderri/auth0.git
   ```
2. Navigate to the repository directory:
   ```bash
   cd auth0
   ```
3. Run the scripts as described in the sections above.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue in this repository or contact [Anderri](https://github.com/anderri).

---

This updated `README.md` now includes a section that explains the purpose of the scripts in the context of fixing and preparing JSON files for import into a different Auth0 tenant, addressing common challenges faced when working with files generated by the Auth0 Import/Export extension.
