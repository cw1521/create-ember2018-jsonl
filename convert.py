import jsonlines
import json
import os



def convert_label_str(file_dir, file_name, div):
    for i in range(div):
        new_file_name = f"{file_name}_{i+1}.jsonl"
        file_path = os.path.join(file_dir, new_file_name)
        ds_list = []
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    temp = json.loads(line)
                    temp["label"] = str(temp["label"] )
                    ds_list.append(temp)
            os.remove(file_path)
            file_path = file_path.replace("-", "_")
            with jsonlines.open(file_path, "w") as writer:
                writer.write_all(ds_list)
            print(f"Wrote to disk: {new_file_name}")


if __name__ == "__main__":
    train_div = 400
    test_div = 100

    train_file_name = "ember2018-train"
    test_file_name = "ember2018-test"
    file_dir = "./data"

    convert_label_str(file_dir, train_file_name, train_div)
    convert_label_str(file_dir, test_file_name, test_div)