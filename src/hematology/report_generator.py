def generate_report(analysis, output_path):
    with open(output_path, "w") as f:
        for i, result in enumerate(analysis, 1):
            f.write(f"Patient {i} Report:\n")
            for key, value in result.items():
                f.write(f"  {key}: {value}\n")
            f.write("\n")
