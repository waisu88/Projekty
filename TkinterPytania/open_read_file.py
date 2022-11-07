

def open_read_file(file_with_questions):
    with open(file_with_questions, "r", encoding="utf-8-sig") as opened_file:
        readed_file = [line.strip() for line in opened_file]
        return readed_file
