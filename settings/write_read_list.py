import json

def write_data_(chennel_name, chennel_id):
    if isinstance(chennel_id,int):

        results = {
        "id": chennel_id,
        "name": chennel_name
        }
        with open("way", "r", encoding="utf-8") as f:
            data = json.load(f)
        data.append(results)

        with open("way", "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=2, ensure_ascii=False)
        
        return "Данные записаны!"
    else:
        return "ID канала/группы не может быть не целым."

def read_data_():
    with open("way", "r", encoding="utf-8") as f:
        data = json.load(f)

    text = ""
    for i, item in enumerate(data, 1):
        text += f"{i}. Name: {item['name']} | ID: {item['id']}"
        text += "\n"

    return text

def del_data_(del_id):
    with open("way", "r", encoding="utf-8") as f:
        data = json.load(f)

    index_to_remove = del_id-1

    if 0 <= index_to_remove < len(data):
        data.pop(index_to_remove)
    else:
        return (f"Индекс {index_to_remove} выходит за пределы списка.")
    
    with open("way", "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=2, ensure_ascii=False)
    
    return "Запись удалена!"
        
def get_ids_():
    with open("way", "r", encoding="utf-8") as f:
        data = json.load(f)
    return [item["id"] for item in data]