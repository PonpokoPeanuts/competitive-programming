import os
print("Current working directory:", os.getcwd())
def create_contest_structure(platform, contest_name, problems, language):
        # ベースディレクトリの作成
    base_dir = os.path.join("C:\\Users\\Owner\\Desktop\\competitive-programming\\contests", platform, contest_name)
    os.makedirs(base_dir, exist_ok=True)

    # 言語に対応する拡張子の設定
    extensions = {
        "python": ".py",
        "cpp": ".cpp",
        "java": ".java",
        "c#": ".cs"
    }
    ext = extensions.get(language.lower(), ".txt")  # デフォルトはテキストファイル

    # 問題ファイルの作成
    for i in range(1, problems + 1):
        problem_letter = chr(64 + i)  # A, B, C, ...
        file_path = os.path.join(base_dir, f"{problem_letter}_problem{ext}")
        with open(file_path, 'w') as f:
            f.write(f"// {problem_letter} problem for {contest_name}\n\n")

    print(f"Created {problems} problems for {contest_name} in {platform} using {language}.")

if __name__=="__main__":
    print("This script is run directly.")
    platform=input("Enter the platform (e.g., atcoder, codeforces): ")
    contest_name=input("Enter the contest name (e.g., abc001): ")
    problems=int(input("Enter the number of problems: "))
    language=input("Enter the programming language (e.g., python, cpp, c#): ")

    create_contest_structure(platform, contest_name, problems, language)
else :
    print("This script is imported as a module.")
