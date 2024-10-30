import json

# 读取jsonl文件
file_path = "auxiliary_train_rewrite.jsonl"
with open(file_path, "r") as file:
    data = [json.loads(line) for line in file]

# 按照original_idx进行排序
sorted_data = sorted(data, key=lambda x: x["original_idx"])

# 写出新文件
new_file_path = file_path.replace(".jsonl", "_rearrange.jsonl")
with open(new_file_path, "w") as new_file:
    for item in sorted_data:
        json.dump(item, new_file)
        new_file.write("\n")

print(f"文件已按 original_idx 排序，并保存为: {new_file_path}")
