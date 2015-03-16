#!/usr/bin/python3 -O
"""
Created on May 6, 2014

Model created for geometric figure recognition. Dataset was synthetically
generated by VELES. Self-constructing Model. It means that Model can change
for any Model (Convolutional, Fully connected, different parameters) in
configuration file.

A workflow to test first layer in simple line detection.
"""


from veles.config import root
from veles.znicz.standard_workflow import StandardWorkflow


class LinesWorkflow(StandardWorkflow):
    """Workflow for Lines dataset.
    """
    def create_workflow(self):
        self.link_repeater(self.start_point)

        self.link_loader(self.repeater)

        self.link_forwards(("input", "minibatch_data"), self.loader)

        self.link_evaluator(self.forwards[-1])

        self.link_decision(self.evaluator)

        end_units = [link(self.decision) for link in (self.link_snapshotter,
                                                      self.link_image_saver,
                                                      self.link_error_plotter)]
        gd = self.link_gds(*end_units)
        self.repeater.link_from(
            self.link_weights_plotter(
                root.lines.layers, root.lines.weights_plotter.limit,
                "gradient_weights",
                self.link_table_plotter(root.lines.layers, gd)))

        self.link_end_point(*end_units)


def run(load, main):
    load(LinesWorkflow,
         decision_config=root.lines.decision,
         snapshotter_config=root.lines.snapshotter,
         image_saver_config=root.lines.image_saver,
         loader_config=root.lines.loader,
         layers=root.lines.layers,
         loader_name=root.lines.loader_name,
         loss_function=root.lines.loss_function)
    main()
