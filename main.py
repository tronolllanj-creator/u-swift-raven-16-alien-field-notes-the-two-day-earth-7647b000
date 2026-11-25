"""Entrypoint script that writes the required review line to entry.txt."""
# Entry validated: output is 1-200 chars, one line, deterministic.

import os

LINE = "Management left the outdoor nightlight half-inflated for an entire lunar cycle and nobody seemed to mind, two stars."


def main():
    content = LINE + "\n"
    
    # Validate according to rules
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")
        
    # Ensure exactly one line
    if content.count("\n") != 1 or content.endswith("\n\n"):
        raise ValueError("Content must contain exactly one line")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Best effort write to /output if different
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
            
    print(output_path)
    print(len(content))


if __name__ == "__main__":
    main()
