class Computer:
    def __init__(self, processor, ram, ramFreq, gpu, gpuRamSize, mobo):
        print('New Computer Initialized')
        self.processor = processor
        self.ram = ram
        self.ramFreq = ramFreq
        self.gpu = gpu
        self.gpuRamSize = gpuRamSize
        self.mobo = mobo

    def get_info(self):
        print('**************************************************************')
        print('Processor\t:\t ', self.processor)
        print('RAM \t\t:\t ', self.ram, 'with Frequency of ', self.ramFreq)
        print('Motherboard \t:\t ', self.mobo)
        print('GPU \t\t:\t ', self.gpu, 'with', self.gpuRamSize, ' VRAM')
        print('**************************************************************')


comp1 = Computer('Ryzen 7 2700X', '16GB', '3200Mhz',
                 'RTX 2060', '6 GB', 'X70 Chipset')

comp2 = Computer('i5 8th Generation', '16GB', '3000Mhz',
                 'GTX 1070', '6 GB', 'B450 Chipset')


comp1.get_info()
comp2.get_info()
