import typing as t

from composio.core.local import Action, Tool
from composio.local_tools.local_workspace.commons import HistoryProcessor
from composio.local_tools.local_workspace.workspace.actions import WorkspaceStatusAction


class LocalWorkspace(Tool):
    """
    Use this action to create a workspace and get workspace ID in return.
    this is a tool for creating local workspace
    """

    history_processor: t.Optional[HistoryProcessor] = None

    def actions(self) -> list[t.Type[Action]]:
        return [WorkspaceStatusAction]

    def triggers(self) -> list:
        return []

    def set_history_processor(self, history_processor: HistoryProcessor):
        self.history_processor = history_processor

    def get_history_processor(self) -> t.Optional[HistoryProcessor]:
        return self.history_processor
