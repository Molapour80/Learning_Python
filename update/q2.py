import os
def  count_file(exsation):

    path =os.path.join(os.path.expanduser("~"), "Desktop")
    file_count = 0
    for root , dirs , files in os.walk(path):
        for file in files:
                if file.endswith(exsation):
                    file_count += 1
    
    return file_count




def main():
    exsation =input("Enter your paswand file:").strip()
    if not exsation.startswith("."):
        exsation += "."

    count =count_file(exsation)
    print(f"{exsation}:{count}")

main()