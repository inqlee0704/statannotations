import numpy as np


class _XPositions:
    def __init__(self, plotter, box_names):
        self.plotter = plotter
        self.xpositions = {
            np.round(self.get_box_x_position(box_name), 1): box_name
            for box_name in box_names
        }

        self.xunits = \
            (max(list(self.xpositions.keys())) + 1) / len(self.xpositions)

        self.xranges = {
            (pos - self.xunits / 2, pos + self.xunits / 2, pos): box_name
            for pos, box_name in self.xpositions.items()}

    def get_xpos_location(self, pos):
        """
        Finds the x-axis location of a categorical variable
        """
        for xrange in self.xranges:
            if (pos >= xrange[0]) & (pos <= xrange[1]):
                return xrange[2]

    def get_box_x_position(self, box_name):
        """
        box_name can be either a name "cat" or a tuple ("cat", "hue")
        """
        if self.plotter.plot_hues is None:
            cat = box_name
            hue_offset = 0
        else:
            cat = box_name[0]
            hue_level = box_name[1]
            hue_offset = self.plotter.hue_offsets[
                self.plotter.hue_names.index(hue_level)]

        group_pos = self.plotter.group_names.index(cat)
        box_pos = group_pos + hue_offset
        return box_pos
