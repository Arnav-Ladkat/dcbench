"""The dcbench module is a collection for benchmarks that test various apsects
of data preparation and handling in the context of AI workflows."""
# flake8: noqa

from .__main__ import main
from .common import Artifact, Problem, Solution, Task
from .common.artifact import (
    CSVArtifact,
    DataPanelArtifact,
    ModelArtifact,
    VisionDatasetArtifact,
    YAMLArtifact,
)
from .config import config
from .tasks.budgetclean import BudgetcleanProblem
from .tasks.budgetclean import task as budgetclean
from .tasks.minidata import MiniDataProblem
from .tasks.minidata import task as minidata
from .tasks.slice_discovery import SliceDiscoveryProblem
from .tasks.slice_discovery import task as slice_discovery
from .version import __version__

__all__ = [
    "minidata",
    "budgetclean",
    "slice_discovery",
    "Artifact",
    "Problem",
    "Solution",
    "BudgetcleanProblem",
    "MiniDataProblem",
    "SliceDiscoveryProblem",
    "Task",
    "ModelArtifact",
    "YAMLArtifact",
    "DataPanelArtifact",
    "VisionDatasetArtifact",
    "CSVArtifact",
    "config",
]

from .common import tasks
