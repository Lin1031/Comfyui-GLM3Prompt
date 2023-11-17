import json
from transformers import AutoTokenizer, AutoModel


class GLM3Prompt:
    """
    ChatGLM3接口调用
    """

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("/root/ComfyUI/models/chatglm3-6b", trust_remote_code=True)
        self.model = AutoModel.from_pretrained("/root/ComfyUI/models/chatglm3-6b", trust_remote_code=True).quantize(4).cuda()
        self.model = self.model.eval()
        self.history = []

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True})
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("提示词",)

    FUNCTION = "translate"

    # OUTPUT_NODE = False

    CATEGORY = "lam"

    def translate(self, text):
        reply, self.history = self.model.chat(self.tokenizer, text, history=self.history)
        return (reply,)

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "GLM3Prompt": GLM3Prompt
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "GLM3Prompt": "ChatGLM3提示词生成工具"
}
