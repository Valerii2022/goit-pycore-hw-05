import sys

def parse_log_line(line: str) -> dict:
    parts = line.split(" ", 3)
    
    if len(parts) != 4:
        raise ValueError("Неправильний формат рядка лог-файлу.")

    date, time, level, message = parts

    return {
        "date": date,
        "time": time,
        "level": level.upper(),  
        "message": message.strip()  
    }

def load_logs(file_path: str) -> list:
    logs = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line) 
                logs.append(parsed_line) 
             
    except FileNotFoundError:
        return "Файл не знайдено"
    
    except Exception:
        return "Помилка при завантаженні лог-файлу."

    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level.upper()]  

def count_logs_by_level(logs: list) -> dict:
    counts = {} 

    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1

    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до лог-файлу як аргумент командного рядка.")
        return
    
    try:
        file_path = sys.argv[1]
        logs = load_logs(file_path)  
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
    except Exception:
        print("Файл не знайдено.")
        return
    
    if len(sys.argv) > 2:
        level = sys.argv[2].upper()  
        filtered_logs = filter_logs_by_level(logs, level)

        if len(filtered_logs) == 0:
            print(f"\nДеталей логів для рівня '{level}' не знайдено")
        else:
            print(f"\nДеталі логів для рівня '{level}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()
