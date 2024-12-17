import datetime
import os
import csv


now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
_file_path = "pishgu_data.csv"
log_path = "./log.csv"
file_path = os.path.splitext(os.path.basename(_file_path))[0] + f"_{now}.csv" # comment this for if you want to test the code


def process_data(input_file, output_file):
    # 读取文件并处理每一行
    with open(input_file, 'r') as infile:
        # 使用csv模块读取
        reader = csv.reader(infile)
        # 初始化变量存储表头和数据行
        headers = []
        data_rows = []
        for row in reader:
            # 初始化存储每行的处理后的数据
            processed_row = []
            for item in row:
                # 分割每个项名称和值
                key, value = item.split(':', 1)
                key = key.strip()
                value = value.strip()
                # 将处理后的值添加到当前行
                processed_row.append(value)
                # 添加表头
                if key not in headers:
                    headers.append(key)
            # 将处理后的行添加到数据行
            data_rows.append(processed_row)
    # 写入到新的CSV文件
    with open(output_file, 'w', newline='') as outfile:
        # 使用csv模块写入
        writer = csv.writer(outfile)
        # 写入表头
        writer.writerow(headers)
        # 写入数据行
        writer.writerows(data_rows)
        print(f"CSV file processing completed. Output file saved to {output_file}")


process_data(log_path, file_path)