import argparse
import pandas as pd
from pathlib import Path

def sort_tsv_by_column_name(tsv_file: str, column_name: str, delimiter: str = '\t'):
    # Create a Path object from the file path
    tsv_path = Path(tsv_file)

    # Read the TSV file using pandas with the specified delimiter
    data = pd.read_csv(tsv_path, sep=delimiter)

    # Check if FDR is present
    if "FDR" not in data.columns:
        raise ValueError(f"Invalid column name 'FDR' - could not filter.")

    # Check if the column name is valid
    if column_name not in data.columns:
        raise ValueError(f"Invalid column name '{column_name}'. Please provide a valid column name.")

    # Drop rows where "FDR" column values are <= 0.05
    data = data[data["FDR"] <= 0.05]

    # Sort the dataframe by the absolute values of the specified column
    sorted_data = data.reindex(data[column_name].abs().sort_values().index)

    # Generate the new filename with '-sorted' appended
    sorted_filename = tsv_path.stem + '-sorted' + tsv_path.suffix

    # Write the sorted data to a new TSV file
    sorted_data.to_csv(tsv_path.parent / sorted_filename, sep=delimiter, index=False)

    return tsv_path.parent / sorted_filename

def main():
    parser = argparse.ArgumentParser(description='Sort a CSV file.')
    parser.add_argument('filename', type=str, help='The path of the CSV file.')
    parser.add_argument('delimiter', type=str, help='The delimiter used in the CSV file.')
    parser.add_argument('column', type=str, help='The column name to sort by.')

    args = parser.parse_args()

    sort_tsv_by_column_name(args.filename, args.column, delimiter="\t" if args.delimiter=="tab" else args.delimiter)

if __name__ == "__main__":
    main()