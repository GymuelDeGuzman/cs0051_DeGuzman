import random

NUM_INSTRUCTIONS = 1000
NUM_DATA_ELEMENTS = 100

INSTRUCTION_SET = ["LOAD", "ADD", "STORE"]

DATA_SET = [3, 5, 7, 8]

class Processor:
    def __init__(self, instruction_set, data_set):
        self.instruction_set = instruction_set
        self.data_set = data_set
        self.registers = [0] * 4

    def execute(self):
        instruction = self.instruction_set[random.randint(0, 2)]
        operand1 = random.randint(0, len(self.registers) - 1)
        operand2 = random.choice([random.randint(0, len(self.registers) - 1), random.randint(0, len(self.data_set) - 1)])
        if instruction == "LOAD":
        	self.registers[operand1] = operand2
        elif instruction == "ADD":
            self.registers[operand1] += operand2
        elif instruction == "STORE":
        	self.data_set[operand2] = self.registers[operand1]

        print(instruction)
        print(self.data_set)


def main():
    processors = [Processor(INSTRUCTION_SET, DATA_SET) for i in range(4)]
    for i in range(NUM_INSTRUCTIONS):
        for processor in processors:
            processor.execute()
    print (processor.data_set)

if __name__ == "__main__":
    main()