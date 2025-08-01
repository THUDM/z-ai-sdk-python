from typing import Union

from typing_extensions import Annotated, TypeAlias

from zai.core._utils import PropertyInfo

from .code_interpreter_delta_block import CodeInterpreterToolBlock
from .drawing_tool_delta_block import DrawingToolBlock
from .function_delta_block import FunctionToolBlock
from .retrieval_delta_black import RetrievalToolBlock
from .web_browser_delta_block import WebBrowserToolBlock

ToolsType: TypeAlias = Annotated[
	Union[
		DrawingToolBlock,
		CodeInterpreterToolBlock,
		WebBrowserToolBlock,
		RetrievalToolBlock,
		FunctionToolBlock,
	],
	PropertyInfo(discriminator='type'),
]
