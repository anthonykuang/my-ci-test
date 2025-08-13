# python_app/src/generator.py
import os
from datetime import datetime

def generate_html_report(output_dir):
    """
    生成一個簡單的 HTML 報告，包含當前時間和計算器結果。
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 假設我們用 calculator 的功能
    from calculator import add, subtract
    result_add = add(10, 5)
    result_subtract = subtract(10, 5)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python CI/CD Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; }}
            .report-section {{ margin-bottom: 15px; padding: 10px; border: 1px solid #eee; border-radius: 5px; background-color: #f9f9f9; }}
            .highlight {{ color: #007bff; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>CI/CD 自動部署報告</h1>
        <div class="report-section">
            <p>部署時間: <span class="highlight">{current_time}</span></p>
        </div>
        <div class="report-section">
            <h2>計算器範例結果:</h2>
            <p>10 + 5 = <span class="highlight">{result_add}</span></p>
            <p>10 - 5 = <span class="highlight">{result_subtract}</span></p>
        </div>
        <p>這是一個由 GitHub Actions 自動生成的報告。</p>
    </body>
    </html>
    """

    output_path = os.path.join(output_dir, "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"HTML report generated at: {output_path}")

if __name__ == '__main__':
    # 這裡的 'output' 是相對於執行 generator.py 的工作目錄
    # 在 GitHub Actions 中，我們將工作目錄設定為 python_app
    # 所以 output_dir 會變成 python_app/output
    generate_html_report('output')