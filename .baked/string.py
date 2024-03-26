import os
import json


def sort_json(json_obj):
    if isinstance(json_obj, dict):
        return {key: sort_json(value) for key, value in json_obj.items()}
    elif isinstance(json_obj, list):
        return sorted(json_obj, key=lambda x: (x.lower(), x.swapcase())) if all(isinstance(item, str) for item in json_obj) else json_obj
    else:
        return json_obj


def main():
    global_files = [f for f in os.listdir('./string-core') if f.endswith('.json')]

    global_json = {}

    # Iterate the global data.
    for file in global_files:
        with open(f'./string-core/{file}', 'r') as f:
            global_json[os.path.splitext(file)[0]] = sort_json(json.load(f))

    output_file = './.baked/string/global.json'
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump(global_json, f, separators=(',', ':'), ensure_ascii=False)

    sub_module_files = [f for f in os.listdir('./string-core/sub-modules') if f.endswith('.json')]

    # Iterate the submodules.
    for file in sub_module_files:
        sub_json = dict(global_json)
        file_name = os.path.splitext(file)[0]

        with open(f'./string-core/sub-modules/{file}', 'r') as f:
            sub_json[file_name] = json.load(f)

        output_file = f'./.baked/string/sub-modules/{file_name}.json'
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w') as f:
            json.dump(sub_json, f, separators=(',', ':'), ensure_ascii=False)


if __name__ == "__main__":
    main()
