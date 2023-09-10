import pandas as pd
import numpy as np

x, y, z = np.meshgrid([0, 1, 2], [0, 1, 2], [0, 1, 2])

class Block:
    def __init__(self):
        self.ley = np.random.uniform(1, 3.5)

class BlockModel:
    def __init__(self, x, y, z, cell_size):
        self.nx = x.shape[0]
        self.ny = y.shape[0]
        self.nz = z.shape[0]
        self.cell_size = cell_size

        self.blocks = self.generate_blocks()

    def generate_blocks(self):
        blocks = []
        for _ in range(self.nx * self.ny * self.nz):
            block = Block()
            blocks.append(block)

        return blocks

# Crear un modelo de bloques
cell_size = 1.0  # Tamaño de la celda

block_model = BlockModel(x, y, z, cell_size)

# Crear el DataFrame
data = {
    'X': x.flatten(),
    'Y': y.flatten(),
    'Z': z.flatten(),
    'Ley': [block.ley for block in block_model.blocks],
    'Cell Size': [block_model.cell_size] * (block_model.nx * block_model.ny * block_model.nz)
}

df = pd.DataFrame(data)
