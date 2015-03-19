#!/usr/bin/python3 -O
"""
Created on April 2, 2014

Copyright (c) 2013 Samsung Electronics Co., Ltd.
"""


from veles.config import root
from veles.tests import timeout, multi_device
from veles.znicz.tests.functional import StandardTest
import veles.znicz.tests.research.WineRelu.wine_relu as wine_relu
import veles.dummy as dummy_workflow


class TestWineRelu(StandardTest):
    @classmethod
    def setUpClass(cls):
        root.wine_relu.update({
            "decision": {"fail_iterations": 250},
            "snapshotter": {"prefix": "wine_relu"},
            "loader": {"minibatch_size": 10},
            "learning_rate": 0.03,
            "weights_decay": 0.0,
            "layers": [10, 3]})

    @timeout(300)
    @multi_device
    def test_wine_relu(self):
        self.info("Will test wine relu workflow")

        self.w = wine_relu.WineReluWorkflow(dummy_workflow.DummyLauncher(),
                                            layers=root.wine_relu.layers)

        self.assertEqual(self.w.evaluator.labels,
                         self.w.loader.minibatch_labels)
        self.w.initialize(learning_rate=root.wine_relu.learning_rate,
                          weights_decay=root.wine_relu.weights_decay,
                          device=self.device, snapshot=False)
        self.w.run()

        epoch = self.w.decision.epoch_number
        self.info("Converged in %d epochs", epoch)
        self.assertEqual(epoch, 161)
        self.info("All Ok")


if __name__ == "__main__":
    StandardTest.main()
