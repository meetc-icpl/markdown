import os
import subprocess

def convert_docx_to_md(folder_path):
    # Ensure the path exists
    if not os.path.isdir(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".docx"):
            docx_path = os.path.join(folder_path, filename)
            md_filename = filename.replace(".docx", ".md")
            md_path = os.path.join(folder_path, md_filename)

            print(f"🔄 Converting: {filename} → {md_filename}")
            
            try:
                # Run markitdown command
                with open(md_path, 'w') as output_file:
                    subprocess.run(
                        ["markitdown", docx_path],
                        stdout=output_file,
                        stderr=subprocess.PIPE,
                        check=True
                    )
                print(f"✅ Saved: {md_filename}")
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to convert {filename}: {e.stderr.decode().strip()}")

if __name__ == "__main__":
    # Change this to your desired folder path
    folder = "/home/meet/Documents/XDR Jenil document"
    convert_docx_to_md(folder)
