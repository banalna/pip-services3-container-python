# -*- coding: utf-8 -*-
"""
    test.DummyProcess
    ~~~~~~~~~~~~~~~~~
    
    Dummy process implementation
    
    :copyright: Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

from pip_services_container.ProcessContainer import ProcessContainer
from .DummyFactory import DummyFactory

class DummyProcess(ProcessContainer):

    def __init__(self):
        super(DummyProcess, self).__init__("dummy", "Sample dummy container")
        self._config_path = './config/dummy.yaml'
        self._factories.add(DummyFactory())
