import numpy as np
from PIL import Image
from cell_evol import new_grid
from cell_evol import draw_grid

def main():

    dim = 200
    scale_factor = 6
    num_iterations = 1000

    twenty_percent = round(0.20*dim)
    eighty_percent = round(0.80*dim)

    gridarray = np.zeros((dim, dim), dtype=int)
    gridarray[twenty_percent:eighty_percent, twenty_percent:eighty_percent] = np.random.randint(2, size=(eighty_percent-twenty_percent, eighty_percent-twenty_percent))  # Fill the center

    pillow_frames = []

    for _ in range(num_iterations):
        gridarray = new_grid(gridarray)
            
        central_frame = gridarray[twenty_percent:eighty_percent, twenty_percent:eighty_percent]

        frame = np.zeros((central_frame.shape[0], central_frame.shape[1], 3), dtype=np.uint8)
        frame[central_frame == 1] = [255, 255, 255]  # white for live cells
        frame[central_frame == 0] = [0, 0, 0]  # black for dead cells

        img = Image.fromarray(frame)
        img = img.resize(((eighty_percent - twenty_percent) * scale_factor, (eighty_percent - twenty_percent) * scale_factor), Image.NEAREST)
        pillow_frames.append(img)

    pillow_frames[0].save('simulation_high_quality.gif',
                           save_all=True,
                           append_images=pillow_frames[1:],
                           duration=100, 
                           loop=0,
                           dpi=(300, 300))

if __name__ == "__main__":
    main()
