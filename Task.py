from datetime import *
import os 

class Task():
    def __init__(self, description):
        self.description = description
        self.status = False
        self.date = datetime.now()
    
    def create(self):
        with open("database.txt", 'a+', encoding="utf-8", newline="") as file:
            new_task = f"{self.get_sequence()} - {self.description} criada/atualizada em {datetime.strptime(str(self.date).split(' ')[0], "%Y-%m-%d").strftime("%d/%m/%Y")} - {self.get_status()}"
            file.write(new_task + os.linesep)
        self.set_sequence()

    def edit(self, id):
        date = f"{datetime.strptime(str(self.date).split(' ')[0], "%Y-%m-%d").strftime("%d/%m/%Y")}"
        lines = []
        new = ''
        with open("database.txt", 'r', encoding="utf-8") as file:
            for i, line in enumerate(file):
                id_line = line.split(' ')[0]
                if id_line == str(id):
                    print(line)
                    edited = input('Digite a nova descrição: ')
                    new = f"\n{id_line} - {edited} criada/atualizada em {date}  - {self.get_status()}\n"
                    lines.append(new)
                else:
                    lines.append(line)

        with open("database.txt", 'w', encoding="utf-8", newline='') as new:
            new.write('')    

        with open("database.txt", 'a+', encoding="utf-8", newline='') as new:
            for i,line in enumerate(lines):
                if i == 0:
                    line.replace('\n','')
                    line + '\n'
                new.write(line)            

    def list_all(self):
        with open("database.txt", 'r', encoding="utf-8") as file:
            for line in file:
                if len(line) > 2:
                    print(line.replace('\n',''))
    
    def list_one(self, id):
        with open("database.txt", 'r', encoding="utf-8") as file:
            for line in file:
                id_line = line.split(' ')[0]
                if id_line == str(id):
                    print(f"Tarefa específica: {line}")

    def delete(self, id):
        lines = []
        line_to_remove = None
        with open("database.txt", 'r', encoding="utf-8") as file:
            for i, line in enumerate(file):
                id_line = line.split(' ')[0]
                if id_line == str(id):
                    if 'concluída' in line:
                        print("Não é possível deletar esta tarefa pois esta finalizada")
                        return
                    line_to_remove = i
                lines.append(line)

        if line_to_remove is not None:
            del lines[line_to_remove]

            with open("database.txt", 'w', encoding="utf-8", newline='') as new:
                new.write('')

            with open("database.txt", 'a+', encoding="utf-8", newline='') as new:
                for line in lines:
                    new.write(line)
    
    def to_finish(self, id):
        lines = []
        with open("database.txt", 'r', encoding="utf-8") as file:
            for line in file:
                id_line = line.replace('\n', '').split(' ')[0]
                if id_line == str(id):
                    new = line.replace('pendente', 'concluída')
                    lines.append(new)
                else:
                    lines.append(line)   

        with open("database.txt", 'w', encoding="utf-8", newline='') as new:
            new.write('')    

        with open("database.txt", 'a+', encoding="utf-8", newline='') as new:
            for i,line in enumerate(lines):
                new.write(line)     

    def get_sequence(self):
        with open("sequence.txt", 'r', encoding='utf-8') as file:
            return file.read()

    def set_sequence(self):
        value = None
        with open("sequence.txt", 'r', encoding='utf-8') as file:
            value = int(file.read()) + 1
        with open("sequence.txt", 'w', encoding='utf-8') as file:    
            converted = f"{value}"
            file.write(converted)
        
    def get_status(self):
        return "concluída" if self.status else "pendente"   